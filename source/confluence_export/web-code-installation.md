---
title: Web Code Installation
---

{excerpt}This page describes how to install and configure the frontend VCL
web code components including the web server prerequisites and frontend VCL
web code. It also describes how to add local web accounts, configure LDAP
authentication, and set the timezone correctly.{excerpt}


<a name="WebCodeInstallation-*Prerequisites*"></a>
## *Prerequisites*

Your web server should meet the following criteria before installing the
frontend VCL code:
* Apache HTTP Server v1.3 or v2.x with SSL enabled - while VCL may run
under another webserver capable of running PHP code, it has only been
tested to work with Apache HTTP Server
* PHP 5
* php modules that should be installed (depending on your Linux distro,
some of these may be compiled in to php instead of being a separate
module):
** php-gd
** php-json (if your PHP version is < 5.2, this is not required)
** php-mcrypt
** php-mysql
** php-openssl
** php-sysvsem
** php-xml
** php-xmlrpc
* useful to have the server set up to be able to send debugging emails
* php-mcrypt requires libmcrypt and mcrypt libraries as dependencies. 
These may need to be installed first.

<a name="WebCodeInstallation-*InstallingVCLFrontendWebCode*"></a>
## *Installing VCL Frontend Web Code*

1. If you haven't already done so, download and extract a copy of the latest
release. There is a link to it under the Project Resources section on our
wiki [home page](apache-vcl.html)
. Look for "Current version".
1. copy the "web" directory to a location somewhere under the web root of
your web server:

    cp -r web/ /var/www/html/vcl

1. modify vcl/.ht-inc/secrets.php
1. * set $vclhost, $vcldb, $vclusername, and $vclpassword to match your
database setup
1. * create random passwords for $mcryptkey, $mcryptiv, and $pemkey -
$mcryptiv must be 8 hex characters
1. run the genkeys.sh script from within vcl/.ht-inc and give it $pemkey
from secrets.php as the passphrase (3 times, copy/paste is a good idea
here)
1. modify vcl/.ht-inc/conf.php to match your site - COOKIEDOMAIN needs to be
the domain name your web server is using, or left blank if you are
accessing it by IP only.
*NOTE:* There is a misconfiguration in conf.php in VCL 2.1.  To correct it,
change affiliationid for "Local Account" in the $authMechs array from 4 to
1.
1. \**NOTICE*\* JpGraph 2.x is no longer available.  JpGraph 3.x is released
under a dual license. QPL 1.0 (Qt Free Licensee).  Free for non-commercial,
open-source or educational use (JpGraph Professional License for commercial
use).  If you are planning to use this for commercial use and don't want to
pay for JpGraph, you can safely skip this step with the only side effect of
not being able to display a few graphs on the statistics page.
Download JpGraph from [http://www.aditus.nu/jpgraph/jpdownload.php](http://www.aditus.nu/jpgraph/jpdownload.php)
1. * For PHP5, download the 3.x series, extract it, and copy the src
directory from it to vcl/.ht-inc/jpgraph
1. download version 0.4.0 of Dojo Toolkit: [http://download.dojotoolkit.org/release-0.4.0/dojo-0.4.0-ajax.tar.gz](http://download.dojotoolkit.org/release-0.4.0/dojo-0.4.0-ajax.tar.gz)
1. * extract it under the vcl directory and rename "dojo-0.4.0-ajax" to
"dojoAjax"
1. download version 1.1.0 of Dojo Toolkit: [http://download.dojotoolkit.org/release-1.1.0/dojo-release-1.1.0.tar.gz](http://download.dojotoolkit.org/release-1.1.0/dojo-release-1.1.0.tar.gz)
1. * extract it under the vcl directory and rename "dojo-release-1.1.0" to
"dojo"
1. go into the themes directory (vcl/themes) and run "./copydojocss.sh
default" to copy parts of dojo's css into the "default" theme
1. if you want to be able to edit any of the documentation that comes
bundled with the vcl web code, download fckeditor from [http://www.fckeditor.net/download](http://www.fckeditor.net/download)
 (most people can skip this step)
1. * extract it under the vcl directory
1. open a browser and open the testsetup.php page
1. * i.e. if you set up your site to be [https://my.server.org/vcl/](https://my.server.org/vcl/)
 open [https://my.server.org/vcl/testsetup.php]
1. debug any issues reported by testsetup.php
1. now, open the index.php page in your browser
1. select Local Account and use 'admin' as the user and 'adminVc1passw0rd'
as the password
1. click the "Management Nodes" link
1. enter the hostname and IP of your management node
1. click Add
1. fill in "Install Path" - this is parent directory under which image files
will be stored
1. enter "/etc/vcl/vcl.key" for "End Node SSH Identity Key Files"
1. click "Confirm Management Node"
1. click Submit
1. click the "Management Nodes" link
1. select "Edit Management Node Grouping"
1. click Submit
1. select the checkbox for your management node
1. click Submit
1. click "Manage Computers"
1. select the "Add Single Computer" radio button
1. click the Submit
1. fill in Hostname, IP Address, owner (admin@Local), RAM, Proc Speed,
Network Speed, select "blade" for Type, select "xCAT 1.x Provisioning" for
"Provisioning Engine", and click the checkbox under "allcomputers", and
"newimages"
&nbsp;&nbsp; &nbsp;Note: if using using vmware, select "virtualmachine" for
Type and "VMWare Server Provisioning" for "Provisioning Engine"
1. click Confirm Computer
1. click Submit (don't worry about the fact that the computer you just added
isn't listed after clicking Submit)
1. after you've configured your image library and your management node has
started checking in, you should be able to make a reservation

<a name="WebCodeInstallation-*Addingextralocalaccounts*"></a>
## *Adding extra local accounts*

There's not currently a tool for this.	You will need to add entries
directly to the database.
1. add entry to user table

    INSERT INTO user (unityid, firstname, lastname, email, lastupdated) VALUES
('myusername', 'myfirstname', 'mylastname', 'myemailaddr', NOW());

1. find out the id generated for that user

    SELECT id, unityid FROM user WHERE unityid = 'myusername';

1. add entry to the localauth table

    INSERT INTO localauth (userid, salt, passhash, lastupdated) VALUES
('place1', 'place2', 'place3', NOW())

with place1 = id from step 2
place2 = an 8 char random string
place3 = sha1sum( desired password with place2 stuck on the end )
this can be generated under linux like this (using 'thedog' as the password
and 11111111 as place2):
echo \-n 'thedog11111111' \| sha1sum
Once a user has been added, the user can go to User Preferences to change
his/her password

<a name="WebCodeInstallation-*AddingLDAPauthentication*"></a>
## *Adding LDAP authentication*

1. fill in the necessary information in vcl/.ht-inc/conf.php
1. add an entry to the affiliation table and use the id for that entry as
'affiliationid' for your new entry in vcl/.ht-inc/conf.php
1. uncomment the 'require_once(".ht-inc/authmethods/ldapauth.php");' line in
in vcl/.ht-inc/conf.php

<a name="WebCodeInstallation-*SettingTimeZone*"></a>
## *Setting Time Zone*

1. Edit /var/www/html/vcl/.ht-inc/php5extras.php to indicate the correct
time zone:
date_default_timezone_set('America/Los_Angeles');
1. Edit /var/www/html/vcl/.ht-inc/requests.php (line 3301 currently) to
indicate the correct time zone (purely cosmetic):
print "<small>(Pacific Time Zone)</small>";
