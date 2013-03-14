#!/bin/sh
# Wrapper script around mirrors.cgi script
# (we must change to that directory in order for python to pick up the
#  python includes correctly)

echo Content-type: text/plain
echo ""

echo "|${HTTP_HOST}|"

if [ "${HTTP_HOST}" = "vcl.staging.apache.org" ]; then
	echo staging
else
	echo "not staging"
fi

#cd /www/vcl.apache.org/content/downloads
#/www/vcl.apache.org/content/downloads/test2.cgi $*
