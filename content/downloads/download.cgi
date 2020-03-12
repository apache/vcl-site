#!/bin/sh
# Wrapper script around mirrors.cgi script
# (we must change to that directory in order for python to pick up the
#  python includes correctly)

# conditional allows to work from both staging and production sites
if [ "${HTTP_HOST}" = "vcl.staging.apache.org" ]; then
	cd /usr/local/websites/vcl/trunk/content/downloads
	/usr/local/websites/vcl/trunk/content/downloads/mirrors.cgi $*
else
	cd /www/vcl.apache.org/content/downloads
	/www/vcl.apache.org/content/downloads/mirrors.cgi $*
fi
