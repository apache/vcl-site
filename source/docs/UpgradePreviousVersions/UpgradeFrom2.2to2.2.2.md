---
title: Upgrade From 2.2 to 2.2.2
---

This page provides information on how to upgrade from VCL 2.2 to VCL 2.2.2. Please note 
it only applies for the upgrade from 2.2 to 2.2.2, this may or may not work for other 
versions.
The basic steps that will be performed

**The basic steps that will be performed**

* Download and Extract 2.2.2 code
* Shutdown httpd and vcld services
* Create backup of vcl database
* Update mysql schema
* Grant CREATE TEMPORARY TABLES to mysql user
* Update Web code, create a backup, copy in new, make changes
* Restart httpd service
* Update Management node vcl code, create a backup, copy in new, make changes
* Restart vcld service

# Detailed steps for upgrade from 2.2 to 2.2.2

1. follow instructions on the [VCL download](http://vcl.apache.org/downloads/download.cgi) 
page to download and verify apache-VCL-2.2.2.tar.bz2 and put in in /root

1. extract VCL 2.2.2 code

    ```bash
    tar xjf apache-VCL-2.2.2.tar.bz2
    ```

1. **Shutdown** the httpd service
           
    ```bash
    service httpd stop or /etc/init.d/httpd stop
    service vcld stop or /etc/init.d/vcld stop
    ```

1. We will **create a backup of the vcl database**. This will provide a restore point 
if necessary. There are no updates to the database in this upgrade, but it is still a
good idea to have a backup.

    ```bash
    mysqldump vcl > ~/vcl-pre2.2.2-upgrade.sql
    ```

1. This step **updates the mysql schema**.

    ```bash
    cd /root/apache-VCL-2.2.2
    mysql vcl < mysql/update-vcl.sql
    ```

1. Grant CREATE TEMPORARY TABLES to mysql user

    The web code now requires access to create temporary tables in mysql. You need to 
    grant the user your web code uses to access mysql the "CREATE TEMPORARY TABLES" 
    permission. Look at the secrets.php file in your web code for the user and hostname.
    For example, if your web code is installed at /var/www/html/vcl, your secrets.php 
    file would be /var/www/html/vcl/.ht-inc/secrets.php. Look for $vclhost and 
    $vclusername. The secrets.php file might have something like:

    ```php
    $vclhost = 'localhost';
    $vcluser = 'vcluser';
    ```

    Then, you need to issue the grant command to mysql. Using the values from above 
    as examples, connect to mysql and then issue the grant command:

    ```bash
    mysql
    GRANT CREATE TEMPORARY TABLES ON `vcl`.* TO 'vcluser'@'localhost';
    exit
    ```

1. **Update the web code**. This step will move the 2.2 web directory out 
of the way, so we can copy in the new web code base. After copying in the new 
code, we will migrate your configuration changes. These instructions assume that 
you installed the vcl web code at /var/www/html/vcl. If you installed it 
elsewhere, replace /var/www/html/vcl with your vcl web root.

    ```bash
    cd /var/www/html
    mv vcl ~/vcl_2.2_web
    ```

1. **Copy the new code** in place
	
    ```bash
    cd /root/apache-VCL-2.2.2
    cp -r web /var/www/html/vcl
    ```

1. **Copy your 2.2 config files**
	
    ```bash
    cd ~/vcl_2.2_web/.ht-inc
    cp conf.php secrets.php pubkey.pem keys.pem /var/www/html/vcl/.ht-inc
    ```

1. **Make the maintenance directory writable by the web server user**. Normally 
this is the apache user,  if using a different user change below cmd accordingly.
	
    ```bash
    chown apache /var/www/html/vcl/.ht-inc/maintenance
    ```

1. **Make changes to conf.php**:

    1. A new user group permission that controls who can manage block allocations 
    globally or for a specific affiliation has been added. It can be granted to any 
    user group under Privileges->Additional User Permissions->Manage Block Allocations. 
    Users with this permission are notified of new block allocation requests. 
    **Remove the following from conf.php**.

        ```php
        $blockNotifyUsers
        ```bash

    1. A new user group permission that controls who can look up users globally 
    or for a specific affiliation has been added. It can be granted to any user group 
    under Privileges->Additional User Permissions->User Lookup. Users with this 
    permission can look up information about other users. 
    **Remove the following from conf.php**.

        ```php
        $userlookupUsers
        ```

1. **Restart httpd service**

    ```bash
    service httpd start or /etc/init.d/httpd start
    ```

1. **Update management node code** This step will make a backup copy of the 2.2 vcl code 
base and then copy the new code over the existing code to preserve any drivers or other 
files you've added.
	
    ```bash
    cd <your vcl MN code root path>
    ie. cd /usr/local/
    cp -r vcl ~/vcl_2.2_managementnode
    ```

1. **Copy in the 2.2.2 code base to /usr/local**, copying in should preserve any drivers 
or other files you've added.
	
    ```bash
    /bin/cp -r /root/apache-VCL-2.2.2/managementnode/* /usr/local/vcl
    ```

1. **Run install_perl_libs.pl** to add any new perl library requirements:
	
    ```bash
    /usr/local/vcl/bin/install_perl_libs.pl
    ```

1. **Restart vcld service**
	
    ```bash
    service vcld start or /etc/init.d/vcld start
    ```

1. Make some test reservations and watch the vcld.log to verify everything is working 
correctly.

    ```bash
    tail -f /var/log/vcld.log
    ```
