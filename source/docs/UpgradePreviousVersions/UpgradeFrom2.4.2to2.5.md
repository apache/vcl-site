---
title: Upgrade From 2.4.2 to 2.5
---

# Scripted Upgrade

VCL 2.5 is the second release to include an upgrade script. All you need to
upgrade VCL is the script. It will download and validate the VCL software and
then upgrade your system. The script can be used to upgrade all three parts of
VCL (database, web portal, and management node) or to upgrade each part
individually. It works for upgrading from any previous version of Apache VCL.

[Download Upgrade Script (vcl-upgrade.sh)](https://www.apache.org/dist/vcl/2.5/vcl-upgrade.sh)

```bash
wget https://www.apache.org/dist/vcl/2.5/vcl-upgrade.sh.sha1
sha1sum -c vcl-upgrade.sh.sha1
wget https://www.apache.org/dist/vcl/KEYS
gpg --import KEYS
wget https://www.apache.org/dist/vcl/2.5/vcl-upgrade.sh.asc
gpg --verify vcl-upgrade.sh.asc
```

Running the upgrade script with no arguments will step you through upgrading
all three parts of VCL. Alternatively, the following explains optional 
arguments. If upgrading the management node part of VCL, it will also prompt 
you to agree to the installation of various system level requirements needed 
for the code to run.

```bash
vcl-upgrade.sh [-h|--help] [-d|--database] [-w|--web] [-m|--managementnode]
        [--dbhost <hostname>] [--dbadminuser <username>]
        [--dbadminpass <password>]

-d|--database - upgrade database components
        --dbhost may optionally be specified if not localhost

-w|--web - upgrade web server components

-m|--managementnode - upgrade management node (vcld) components

--dbhost <hostname> - hostname of database server (default=localhost)

--dbname <name> - name of VCL database on database server (default=vcl)

--dbadminuser <username> - admin username for database; must have access
        to modify database schema and dump data for backup (default=root)

--dbadminpass <password> - password for dbadminuser (default=[no password])
```

---

# Manual Upgrade Instructions

These instructions explain how to upgrade from VCL 2.4.2 to VCL 2.5. Please note 
it only applies for the upgrade from 2.4.2 to 2.5, this may or may not work for other 
versions.

**The basic steps that will be performed**

  - Download and Extract 2.5 code 
  - Shutdown httpd and vcld services
  - Create backup of vcl database 
  - Update mysql schema
  - Update web code, create a backup, copy in new, make changes 
  - Restart httpd service
  - Update management node VCL code, create a backup, copy in new, make changes 
  - Restart vcld service

### Upgrade steps

1. follow instructions on the [VCL download](http://vcl.apache.org/downloads/download.cgi) 
page to download and verify apache-VCL-2.5.tar.bz2 and put in in /root
2. **extract VCL 2.5 code**
    
    ```bash
    tar xf apache-VCL-2.5.tar.bz2
    ```

3. **Shutdown** the httpd and vcld services
           
    ```bash
    service httpd stop
    service vcld stop
    ```

4. create a **backup** of the VCL database. This will provide a restore point if 
necessary.

    ```bash
    mysqldump vcl > ~/vcl-pre2.5-upgrade.sql
    ```

5. This step **updates the database** schema.

    ```bash
    mysql vcl < /root/apache-VCL-2.5/mysql/update-vcl.sql
    ```

6. **Possibly move old web code**. If /var/www/html/vcl **is a directory**, rename it to 
/var/www/html/vcl-2.4.2. These instructions assume that you installed the 
VCL web code at /var/www/html/vcl. If you installed it elsewhere, replace 
/var/www/html/vcl with your vcl web root.

    ```bash
    mv /var/www/html/vcl /var/www/html/vcl-2.4.2
    ```

7. **Disable access** to the old web code

    ```bash
    echo "Require all denied" > /var/www/html/vcl-2.4.2/.htaccess
    ```

7. **Copy the new code** in place
	
    ```bash
    cp -ar /root/apache-VCL-2.5/web /var/www/html/vcl-2.5
    ln -sfn /var/www/html/vcl-2.5 /var/www/html/vcl
    ```

8. **Copy your 2.4.2 config files**
	
    ```bash
    cd /var/www/html/vcl-2.4.2/.ht-inc
    cp conf.php secrets.php pubkey.pem keys.pem /var/www/html/vcl/.ht-inc
    ```

8. **Set SELinux context** If you are using SELinux, set the correct context:

    ```bash
    chcon -R -t httpd_sys_content_t /var/www/html/vcl-2.5
    chcon -t httpd_sys_rw_content_t /var/www/html/vcl-2.5/.ht-inc/maintenance
    chcon -t httpd_sys_rw_content_t /var/www/html/vcl-2.5/.ht-inc/cryptkey
    ```

9. **Update conf.php**. The following item needs to be removed from the conf.php
file:

    ```bash
    # (don't forget to edit conf.php in the **new** location)
    vim /var/www/html/vcl/.ht-inc/conf.php
    ```

    ```php
    define("MAXVMLIMIT", "100");
    ```

9. **Update secrets.php**  $cryptkey in secrets.php needs to be generated
using openssl. Generate the value and set it in secrets.php:

    ```bash
    openssl rand 32 | base64
    vim /var/www/html/vcl/.ht-inc/secrets.php
    ```

    ```php
    $cryptkey = 'xxxxxxxxxxxxxxxxxxxxxxxxx'; # set this to output of "openssl rand 32 | base64"
    ```

9. **Make the maintenance and cryptkey directories writable** by the web server user. Normally this is
the apache user, if using a different user change below command accordingly.
	
    ```bash
    chown apache /var/www/html/vcl/.ht-inc/maintenance
    chown apache /var/www/html/vcl/.ht-inc/cryptkey
    ```

10. **Start httpd service**

    ```bash
    service httpd start
    ```

11. **Check testsetup.php** Check that everything is correct by viewing the testsetup.php
script in your browser. This script is located in the same directory as the index.php script.
I.e.

    ```bash
    https://your.site.url/vcl/testsetup.php
    ```

13. **Copy old management node code** If /usr/local/vcl is a directory, copy it to
/usr/local/vcl-2.4.2, rename /usr/local/vcl to /usr/local/vcl-2.5, and create a symlink.
If /usr/local/vcl is a symlink to vcl-2.4.2, copy /usr/local/vcl-2.4.2 to /usr/local/vcl-2.5
and update the symlink.
	
    ```bash
    # (for directory)
    cp -ar /usr/local/vcl /usr/local/vcl-2.4.2
    mv /usr/local/vcl /usr/local/vcl-2.5
    ln -s /usr/local/vcl-2.5 /usr/local/vcl
    ```

    ```bash
    # (for symlink)
    cp -ar /usr/local/vcl-2.4.2 /usr/local/vcl-2.5
    ln -sfn /usr/local/vcl-2.5 /usr/local/vcl
    ```

13. **Copy new code in place** Copy the new management node code over the old code:

    ```bash
    /bin/cp -ar /root/apache-VCL-2.5/managementnode/* /usr/local/vcl-2.5
    ```

14. **Run install_perl_libs.pl** to add any new perl library requirements:
	
    ```bash
    /usr/local/vcl/bin/install_perl_libs.pl
    ```

15. **Start vcld service**
	
    ```bash
    service vcld start
    ```

16. Make some **test reservations** and watch the vcld.log to verify everything is working 
correctly.

    ```bash
    tail -f /var/log/vcld.log
    ```
