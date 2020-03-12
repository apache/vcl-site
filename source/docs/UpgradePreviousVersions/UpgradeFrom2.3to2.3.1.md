---
title: Upgrade From 2.3 to 2.3.1
---

This page provides information on how to upgrade from VCL 2.3 to VCL 2.3.1. Please note it only applies for the upgrade 
from 2.3 to 2.3.1, this may or may not work for other versions.

**The basic steps that will be performed**

  - Download and Extract 2.3.1 code 
  - Shutdown httpd and vcld services
  - Create backup of vcl database 
  - Update mysql schema Update Web code, create a backup, copy in new, make changes 
  - Restart httpd service
  - Update Management node vcl code, create a backup, copy in new, make changes 
  - Restart vcld service

# Detailed steps for upgrade from 2.3 to 2.3.1

1. follow instructions on VCL 2.3.1 Release page to download and verify apache-VCL-2.3.1.tar.bz2 and put in in /root
2. **extract VCL 2.3.1 code**
    
    ```bash
    tar xjf apache-VCL-2.3.1.tar.bz2
    ```

3. **Shutdown** the httpd and vcld services
           
    ```bash
    service httpd stop or /etc/init.d/httpd stop
    service vcld stop or /etc/init.d/vcld stop
    ```

4. We will **create a backup of the vcl database**. This will provide a restore point if necessary.

    ```bash
    mysqldump vcl > ~/vcl-pre2.3.1-upgrade.sql
    ```

5. This step **updates the mysql schema**.

    ```bash
    cd /root/apache-VCL-2.3.1
    mysql vcl < mysql/update-vcl.sql
    ```

6. **Update the web code**. This step we will move the 2.3 web directory out of the way, so we can copy in the new 
web code base. After copying in the new code, we will migrate your configuration changes. These instructions assume 
that you installed the vcl web code at /var/www/html/vcl. If you installed it elsewhere, replace /var/www/html/vcl with your vcl web root.

    ```bash
    cd /var/www/html
    mv vcl ~/vcl_2.3_web
    ```

7. **Copy the new code** in place
	
    ```bash
    cd /root/apache-VCL-2.3.1
    cp -r web /var/www/html/vcl
    ```

8. **Copy your 2.3 config files**
	
    ```bash
    cd ~/vcl_2.3_web/.ht-inc
    cp conf.php secrets.php pubkey.pem keys.pem /var/www/html/vcl/.ht-inc
    ```

9. **Make the maintenance directory writable by the web server user**. Normally this is the apache user,  if using 
a different user change below cmd accordingly.
	
    ```bash
    chown apache /var/www/html/vcl/.ht-inc/maintenance
    ```

11. **Restart httpd service**

    ```bash
    service httpd start or /etc/init.d/httpd start
    ```

12. **Update management node code** This step will make a backup copy of the 2.3 vcl code base and then copy 
the new code over the existing code to preserve any drivers or other files you've added.
	
    ```bash
    cd <your vcl MN code root path>
    ie. cd /usr/local/
    cp -r vcl ~/vcl_2.3_managementnode
    ```

13. **Copy in the 2.3.1 code base to /usr/local**, copying in should preserve any drivers or other files you've added.
	
    ```bash
    /bin/cp -r /root/apache-VCL-2.3.1/managementnode/* /usr/local/vcl
    ```

14. **Run install_perl_libs.pl** to add any new perl library requirements:
	
    ```bash
    /usr/local/vcl/bin/install_perl_libs.pl
    ```

15. **Restart vcld service**
	
    ```bash
    service vcld start or /etc/init.d/vcld start
    ```

16. Make some test reservations and watch the vcld.log to verify everything is working correctly.

    ```bash
    tail -f /var/log/vcld.log
    ```
