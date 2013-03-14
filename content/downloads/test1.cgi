#!/bin/sh
# Wrapper script around mirrors.cgi script
# (we must change to that directory in order for python to pick up the
#  python includes correctly)
cd /www/vcl.apache.org/content/downloads
/www/vcl.apache.org/content/downloads/test2.cgi $*
