---
title: Upgrade From 2.2.1 to 2.2.2
---

This page provides information on how to upgrade from VCL 2.2.1 to VCL 2.2.2. Please 
note it only applies for the upgrade from 2.2.1 to 2.2.2, this may or may not work for 
other versions.


**The basic steps that will be performed**

  - Download and Extract 2.2.2 code 
  - Shutdown httpd service
  - Create backup of vcl database 
  - Create backup of web code
  - Upgrade web code
  - Restart httpd service

# Detailed steps for upgrade from 2.2.1 to 2.2.2

1. follow instructions on the [VCL download](http://vcl.apache.org/downloads/download.cgi) 
page to download and verify apache-VCL-2.2.2.tar.bz2 and put in in /root
1. **extract VCL 2.2.2 code**
    
    ```bash
    tar xjf apache-VCL-2.2.2.tar.bz2
    ```

1. **Shutdown** the httpd service
           
    ```bash
    service httpd stop or /etc/init.d/httpd stop
    ```

1. We will **create a backup of the vcl database**. This will provide a restore point 
if necessary. There are no updates to the database in this upgrade, but it is still a
good idea to have a backup.

    ```bash
    mysqldump vcl > ~/vcl-pre2.2.2-upgrade.sql
    ```

1. **Backup the web code**. This step will move the 2.2.1 web directory out of the 
way so we can copy in the new web code base. These instructions assume that you installed the 
vcl web code at /var/www/html/vcl. If you installed it elsewhere, replace 
/var/www/html/vcl with your vcl web root.

    ```bash
    cd /var/www/html
    mv vcl ~/vcl_2.2.1_web
    ```

1. **Copy the new code** in place
	
    ```bash
    cd /root/apache-VCL-2.2.2
    cp -r web /var/www/html/vcl
    ```

1. **Copy your 2.2.1 config files**
	
    ```bash
    cd ~/vcl_2.2.1_web/.ht-inc
    cp conf.php secrets.php pubkey.pem keys.pem /var/www/html/vcl/.ht-inc
    ```

1. **Make the maintenance directory writable by the web server user**. Normally this is 
the apache user. If using a different user, change the below command accordingly.
	
    ```bash
    chown apache /var/www/html/vcl/.ht-inc/maintenance
    ```

1. **Restart httpd service**

    ```bash
    service httpd start or /etc/init.d/httpd start
    ```

1. Make some test reservations and watch the vcld.log to verify everything is working 
correctly.

    ```bash
    tail -f /var/log/vcld.log
    ```
