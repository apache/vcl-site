---
title: Upgrade From Previous Version
---

This file provides information on how to upgrade from VCL 2.1 to VCL 2.2.
Please note it only applies for the upgrade from 2.1 to 2.2, this may or
may not work for other versions.

<a name="UpgradeFromPreviousVersion-*Thebasicstepsthatwillbeperformed*"></a>
## The basic steps that will be performed

* Download and Extract 2.2 code
* Shutdown httpd and vcld services
* Create backup of vcl database
* Update mysql schema
* Update Web code, create a backup, copy in new, make changes
* Restart httpd service
* Update Management node vcl code, create a backup, copy in new, make
changes
* Restart vcld service

<a name="UpgradeFromPreviousVersion-*DownloadandExtract2.2code*"></a>
## Download and Extract 2.2 code

1. follow instructions on [VCL 2.2](vcl-2.2.html)
 Release page to download and verify apache-VCL-2.2-incubating.tar.bz2 and
put in in /root
1. extract VCL 2.2 code

        tar xjf apache-VCL-2.2-incubating.tar.bz2



<a name="UpgradeFromPreviousVersion-*Shutdownservices*"></a>
## Shutdown services

Shutdown the httpd and vcld services

        service httpd stop or /etc/init.d/httpd stop
        service vcld stop or /etc/init.d/vcld stop


<a name="UpgradeFromPreviousVersion-*Createabackupofvcldatabase*"></a>
## Create a backup of vcl database

We will create a backup of the vcl database. This will provide a restore
point if necessary.


        mysqldump vcl > ~/vcl-pre2.2-upgrade.sql


<a name="UpgradeFromPreviousVersion-*Updatemysqlschema*"></a>
## Update mysql schema

This step updates the mysql schema.


        cd /root/apache-VCL-2.2-incubating
        mysql vcl < mysql/update-2.2.sql


<a name="UpgradeFromPreviousVersion-*Updatewebcode*"></a>
## Update web code

This step we will move the 2.1 web directory out of the way, so we can copy
in the new web code base. After copying in the new code, we will migrate
your configuration changes. These instructions assume that you installed
the vcl web code at /var/www/html/vcl. If you installed it elsewhere,
replace /var/www/html/vcl with your vcl web root.

1. copy your old code out of the way

        cd /var/www/html
        mv vcl ~/vcl_2.1_web

1. copy the new code in place

        cd /root/apache-VCL-2.2-incubating
        cp -r web /var/www/html/vcl

1. copy your 2.1 config files

        cd ~/vcl_2.1_web/.ht-inc
        cp conf.php secrets.php pubkey.pem keys.pem /var/www/html/vcl/.ht-inc

1. make /var/www/html/vcl/.ht-inc/maintenance writable by the web server -
if httpd on your server is running as the user apache:

        chown apache /var/www/html/vcl/.ht-inc/maintenance

1. add the following new entries to conf.php - You can copy them in from
.ht-inc/conf-default.php. Descriptions of each item can also be found in
conf-default.php
 * date_default_timezone_set('America/New_York');
 * $blockNotifyUsers = "adminuser@example.org";
 * define("SCHEDULER_ALLOCATE_RANDOM_COMPUTER", 0);
 * define("DOCUMENTATIONURL", "https://cwiki.apache.org/VCLDOCS/");
 * define("USEFILTERINGSELECT", 1);
 * define("FILTERINGSELECTTHRESHOLD", 1000);
 * define("DEFAULTTHEME", 'default');

<a name="UpgradeFromPreviousVersion-Restarthttpdservice"></a>
## Restart httpd service

    service httpd start or /etc/init.d/httpd start


<a name="UpgradeFromPreviousVersion-*Updatemanagementnodecode*"></a>
## Update management node code

This step will move the 2.1 vcl code base out of the way, so we can cleanly
copy in the new management node(MN) code.

1. Copy 2.1 code base to a backup location

        cd <your vcl MN code root path>
        ie. cd /usr/local/
        cp -r vcl ~/vcl_2.1_managementnode

1. Copy in the 2.2 code base to /usr/local, copying in should preserve any
drivers or other files you've added.

        /bin/cp -r /root/apache-VCL-2.2-incubating/managementnode/* /usr/local/vcl

1. Make changes related to vcld.conf settings
 * Open VCL web interface
 * Go to Management Nodes
 * Select Edit Management Node Information
 * Select Edit.
 * Set any relevant fields:
 * SysAdmin Email Address(es) - comma delimited list of vcl admin email
addresses
 * Address for Shadow Emails - a shared mail box, optional it receives
email of all notifications
 * Public NIC configuration method - Defines what type of NIC configuration
is used, options are dynamic DHCP, Manual DHCP, or static
 * End Node SSH Identity Key Files

<a name="UpgradeFromPreviousVersion-Restartvcldservice"></a>
## Restart vcld service

        service vcld start or /etc/init.d/vcld start

