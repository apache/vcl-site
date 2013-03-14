#!/usr/local/bin/python2.7
# -*- python -*-
#
# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.
#
#
# This is a Python CGI script that uses EZT to produce templated
# mirror content and GeoIP to choose the appropriate mirror
#

import sys
import os
import cgi
import stat
import random
import time
import traceback
import cStringIO

# Should be installed in the main system library
import GeoIP

# Insert this directory into PATH so that we can import ezt
this_dir = os.path.dirname(__file__) or '.'
sys.path.insert(0, this_dir)

import ezt


# Configurable stuff
MIRRORS_LIST = "/x1/www/www.apache.org/mirrors/mirrors.list"
DEFAULT_REGION = "us"
DEFAULT_TEMPLATE = "/x1/www/www.apache.org/dyn/closer.html"
DEFAULT_LOCATION = "http://www.apache.org/dyn/closer.cgi"


def get_region(environ):
  """Use GeoIP to find the client's country, falling back to
     DEFAULT_REGION on failure."""
  try:
    remote_ip = environ['REMOTE_ADDR'];
    gi = GeoIP.new(GeoIP.GEOIP_STANDARD)
    region = gi.country_code_by_addr(remote_ip).lower().strip()
    if region == 'gb':
      return 'uk'
    else:
      return region
  except:
    ### should we log an error here? absorbing without reporting is
    ### generally bad form.
    return DEFAULT_REGION


def parse_mirrors(filename, country, preferred, mingood):
  """Parse the mirror database to find the best mirrors for a client.

  The Format of the mirror database is (last two fields are optional):
  ftp au  ftp://ftp.planetmirror.com/pub/apache/dist/ 1117724635 http://example.com/logo.gif http://example.com/ """

  output = { 'http'   : [ ],
             'ftp'    : [ ],
             'backup' : [ ],
             'preferred' : None,
             'logo' : None,
             'link' : None,
             }

  # Read the mirror database and put it in a list of lists
  # skip empty lines and comment
  mirrors = [line.split() for line in open(filename).readlines()
             if line.strip() and not line.startswith('#')]

  mirrors.append(['http', 'us', 'http://archive.apache.org/dist/', '9999999999'])

  # Add trailing slashes where missing.  Otherwise,
  # strcat("http://www.mirror.org", pathinfo=".foo.evil") would link to
  # http://www.mirror.org.foo.evil
  for mir in mirrors:
    if not mir[2].endswith('/'):
      mir[2] += '/'

  # grab the backup mirrors
  backupmirrors = [mir for mir in mirrors if mir[1] == 'Backup']

  # Grab the mirrors for the requested country or, failing that,
  # from the default region (us)
  for region in (country, DEFAULT_REGION):
    countrymirrors = [mir for mir in mirrors if mir[1] == region]
    random.shuffle(countrymirrors)
    goodmirror = None
    for mir in countrymirrors:
      if mir[0] == 'http' and int(mir[3]) > mingood:
        goodmirror = mir
        break
    if goodmirror:
      break

  # Check if the requested Preferred mirror is in the list
  # Note the user-requested mirror doesn't have a trailing-slash
  prefmir = None
  if preferred:
    for mir in mirrors:
      if mir[2] == preferred:
        prefmir = mir
        break
  # Otherwise pick a preferred mirror from our country
  if not prefmir and goodmirror:
    prefmir = goodmirror
  if not prefmir:  # In the worst case, choose a backup
    prefmir = random.choice(backupmirrors)

  # Record the preferred mirror and, if available, its logo and link
  # Keep the trailing-slash on the URL (it is later joined to the path_info)
  output['preferred'] = prefmir[2]
  if len(prefmir) > 5:
    output['logo'] = prefmir[4]
    output['link'] = prefmir[5]

  # Now assemble a list of all the other mirrors.
  # Keep the trailing-slash on the URL (it is later joined to the path_info)
  output['http'] = [mir[2] for mir in countrymirrors if mir[0] == 'http']
  output['ftp'] = [mir[2] for mir in countrymirrors if mir[0] == 'ftp']
  output['backup'] = [mir[2] for mir in backupmirrors]

  return output


def mirrorwrap(environ, start_response):
  try:
    return mirrorsapp(environ, start_response)
  except:
    status = "500 Oops"
    response_headers = [("content-type","text/plain")]
    start_response(status, response_headers, sys.exc_info())
    return ["Problem running mirror.cgi, contact <infrastructure@apache.org> "
            "if it persists.\n\n"
            + traceback.format_exc() ]


def locate_template(environ):
  # Determine the correct template by noting our filesystem location
  if environ.has_key('ASF_MIRROR_FILENAME'):
    template_file = environ['ASF_MIRROR_FILENAME'].replace(".cgi", ".html")
  elif environ.has_key('SCRIPT_FILENAME'):
    template_file = environ['SCRIPT_FILENAME'].replace(".cgi", ".html")
  else:
    template_file = sys.argv[0].replace(".cgi", ".html")

  if not os.path.isfile(template_file):
    # look in docroot instead if this is in a cgi-bin dir
    template_file = template_file.replace("/cgi-bin/", "/content/")
    if not os.path.isfile(template_file):
      template_file = DEFAULT_TEMPLATE

  return template_file


def locate_mirrors(environ):
  # Allow the MIRRORS_LIST environment variable to override the default
  mirrors = environ.get('MIRRORS_LIST')
  if mirrors and os.path.isfile(mirrors):
    return mirrors
  return MIRRORS_LIST  # the default


def mirrorsapp(environ, start_response):
  headers = [ ]
  resp_code = '200 OK'

  # Where is the client coming from
  region = get_region(environ)

  # Was there a preferred mirror or update requirement?
  form = cgi.FieldStorage(fp=environ['wsgi.input'],
                          environ=environ,
                          keep_blank_values=True)
  preferred = form.getfirst("Preferred", "")
  update = form.getfirst("update", "")

  # Get the last update time of the mirror database
  mirrors = locate_mirrors(environ)
  base_time = os.path.getmtime(mirrors)

  # convert from YYYYMMDDhhmm to time-since-unix-epoch
  try:
    mingood = time.mktime(time.strptime(update, "%Y%m%d%H%M"))
    # Never use a mirror more than a week old
    mingood = max(mingood, base_time - 7*24*60*60)
  except:
    # if we didn't get a time, or we can't convert it, then
    # use the time the mirror database was last updated minus 24 hours
    mingood = base_time - 24*60*60

  # Load the mirrors file and parse it out
  data = parse_mirrors(mirrors, region, preferred, mingood)

  # ======== new download tracking code ==========
  action = form.getfirst("action", "")
  filename = form.getfirst("filename", "")
  if action == 'download' and filename != '':
    url = "%s%s" % (data['preferred'][:-1], filename)
    headers.append(('Location', url))
    start_response(resp_code, headers)
    #log_download(url, data['preferred'], environ, region)
    return ''
  # ====== end new download tracking code ========

  # Note location to self
  data['location'] = environ.get('SCRIPT_NAME', DEFAULT_LOCATION)

  path_param = form.getfirst("path", None)
  if path_param:
    path_info = cgi.escape(path_param, 1)
  else:
    # Note any PATH_INFO
    if environ.has_key('PATH_INFO'):
      path_info = cgi.escape(environ['PATH_INFO'], 1)
      if environ.has_key('SCRIPT_NAME'):
        if environ['PATH_INFO'] == environ['SCRIPT_NAME']:
          path_info = ''
    else:
      path_info = ''
  # The mirror URL already has a trailing slash. Avoid doubling it up.
  if path_info.startswith('/'):
    path_info = path_info[1:]
  data['path_info'] = path_info

  template_file = locate_template(environ)

  # Print out the CGI header component
  # using xml if the filename ends with the magic '--xml' string
  if template_file.endswith('--xml.html'):
    headers.append(('Content-type', 'text/xml'))
  else:
    headers.append(('Content-type', 'text/html'))

  start_response(resp_code, headers)

  output = cStringIO.StringIO()
  template = ezt.Template(template_file)
  template.generate(output, data)
  return [ output.getvalue() ]

# ======== new download tracking code ==========
def log_download(url, preferred, environ, region):
  timestamp = int(time.time())
  # format: timestamp,url,mirror,IP,region,"useragent"
  try:
    fh = open('/home/jfthomps/debug', 'a')
    fh.write('%s,%s,%s,%s,%s,"%s"\n' % (timestamp, url, preferred, environ['REMOTE_ADDR'], region, environ['HTTP_USER_AGENT']))
    fh.close
  except:
    pass
# ====== end new download tracking code ========

if __name__ == '__main__':
  #from flup.server.fcgi import WSGIServer
  from flup.server.cgi import WSGIServer
  WSGIServer(mirrorwrap).run()
