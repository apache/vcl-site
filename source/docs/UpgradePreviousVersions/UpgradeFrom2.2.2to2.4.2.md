---
title: Upgrade From 2.2.2 to 2.4.2
---

# Scripted Upgrade

VCL 2.4.2 is the first release to include an upgrade script. All you need to
upgrade VCL is the script. It will download and validate the VCL software and
then upgrade your system. The script can be used to upgrade all three parts of
VCL (database, web portal, and management node) or to upgrade each part
individually. It works for upgrading from any previous version of Apache VCL.

[Download Upgrade Script (vcl-upgrade.sh)](https://www.apache.org/dist/vcl/2.4.2/vcl-upgrade.sh)

```bash
wget https://www.apache.org/dist/vcl/2.4.2/vcl-upgrade.sh.sha1
sha1sum -c vcl-upgrade.sh.sha1
wget https://www.apache.org/dist/vcl/KEYS
gpg --import KEYS
wget https://www.apache.org/dist/vcl/2.4.2/vcl-upgrade.sh.asc
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

These instructions explain how to upgrade from VCL 2.2.2 to VCL 2.4.2. Please note 
it only applies for the upgrade from 2.2.2 to 2.4.2, this may or may not work for other 
versions.

**The basic steps that will be performed**

  - Download and Extract 2.4.2 code 
  - Shutdown httpd and vcld services
  - Create backup of vcl database 
  - Update mysql schema
  - Update web code, create a backup, copy in new, make changes 
  - Restart httpd service
  - Update management node vcl code, create a backup, copy in new, make changes 
  - Restart vcld service

### Upgrade steps

1. follow instructions on the [VCL download](http://vcl.apache.org/downloads/download.cgi) 
page to download and verify apache-VCL-2.4.2.tar.bz2 and put in in /root
2. **extract VCL 2.4.2 code**
    
    ```bash
    tar xf apache-VCL-2.4.2.tar.bz2
    ```

3. **Shutdown** the httpd and vcld services
           
    ```bash
    service httpd stop
    service vcld stop
    ```

4. create a **backup** of the VCL database. This will provide a restore point if 
necessary.

    ```bash
    mysqldump vcl > ~/vcl-pre2.4.2-upgrade.sql
    ```

5. This step **updates the database** schema.

    ```bash
    mysql vcl < /root/apache-VCL-2.4.2/mysql/update-vcl.sql
    ```

6. **Update the web code**. This step we will move the 2.2.2 web directory out of the 
way, so we can copy in the new web code base. After copying in the new code, we will 
migrate your configuration changes. These instructions assume that you installed the 
VCL web code at /var/www/html/vcl. If you installed it elsewhere, replace 
/var/www/html/vcl with your vcl web root.

    ```bash
    mv /var/www/html/vcl /var/www/html/vcl-2.2.2
    ```

7. **Disable access** to the old web code

    ```bash
    echo "Deny from all" > /var/www/html/vcl-2.2.2/.htaccess
    ```

7. **Copy the new code** in place
	
    ```bash
    cp -r /root/apache-VCL-2.4.2/web /var/www/html/vcl-2.4.2
    ln -s /var/www/html/vcl-2.4.2 /var/www/html/vcl
    ```

8. **Copy your 2.2.2 config files**
	
    ```bash
    cd /var/www/html/vcl-2.2.2/.ht-inc
    cp conf.php secrets.php pubkey.pem keys.pem /var/www/html/vcl/.ht-inc
    ```

9. **Add new items to conf.php**. The following items need to be added to the conf.php
file (they can be added anywhere as long as it is not inside an 
array() definition):

    ```bash
    (don't forget to edit conf.php in the **new** location)
    vim /var/www/html/vcl/.ht-inc/conf.php
    ```

    ```php
    define("DEFAULTLOCALE", "en_US");              // default locale for the site

    define("SEMTIMEOUT", "45");

    define("ALLOWADDSHIBUSERS", 0); // this is only related to using Shibboleth authentication for an affiliation that does not
                                    // also have LDAP set up (i.e. affiliation.shibonly = 1)
                                    // set this to 1 to allow users be manually added to VCL before they have ever logged in
                                    // through things such as adding a user to a user group or directly granting a user a
                                    // privilege somewhere in the privilege tree. Note that if you enable this and typo
                                    // a userid, there is no way to verify that it was entered incorrectly so the user
                                    // will be added to the database with the typoed userid

    define("MAXINITIALIMAGINGTIME", 720); // for imaging reservations, users will have at least this long as the max selectable duration

    define("MAXSUBIMAGES", 5000);  // maximum allowed number for subimages in a config

    # boolean value of 0 or 1 to enable documentation links on login page and page
    #   where authentication method is selected
    # 0 = disables; 1 = enabled
    define("NOAUTH_HOMENAV", 0);

    # boolean value of 0 or 1 to control logging of non SELECT database queries for auditing or debugging purposes; queries are logged to the querylog table
    define("QUERYLOGGING", 1);

    # boolean value of 0 or 1 to control logging of XMLRPC calls for auditing or debugging purposes; queries are logged to the xmlrpcLog table
    define("XMLRPCLOGGING", 1);

    # documentation links to display on login page and page
    #   where authentication method is selected when NOAUTH_HOMENAV is set to 1
    $NOAUTH_HOMENAV = array (
        "What is VCL" => "http://vcl.apache.org/",
        "How to use VCL" => "https://cwiki.apache.org/confluence/display/VCL/Using+VCL",
        "Report a Problem" => "mailto:" . HELPEMAIL,
    );
    ```

9. **Modify existing items in conf.php**. The following items in conf.php need to be 
modified. Change:

    * OLD
	
        ```php
        $addUserFunc[$item['affiliationid']] = create_function('', 'return 0;');
        $updateUserFunc[$item['affiliationid']] = create_function('', 'return 0;');
        ```

    * NEW

        ```php
        $addUserFunc[$item['affiliationid']] = create_function('', 'return NULL;');
        $updateUserFunc[$item['affiliationid']] = create_function('', 'return NULL;');
        ```

9. **Make the maintenance directory writable** by the web server user. Normally this is
the apache user, if using a different user change below cmd accordingly.
	
    ```bash
    chown apache /var/www/html/vcl/.ht-inc/maintenance
    ```

11. **Start httpd service**

    ```bash
    service httpd start
    ```

12. **Backup management node code**. This step will make a backup copy of the 2.2.2  
management node code. These instructions assume that you installed the 
VCL management node code at /usr/local/vcl. If you installed it elsewhere, replace 
/usr/local with your management node path.
	
    ```bash
    cp -r /usr/local/vcl /usr/local/vcl-2.2.2
    ```

13. **Copy in the 2.4.2 management node code** to /usr/local. First, rename the existing
management node code directory to vcl-2.4.2 so that any drivers or other files you've 
added are preserved. Then, create a symlink for /usr/local/vcl and copy the new 
management code over top of it.
	
    ```bash
    mv /usr/local/vcl /usr/local/vcl-2.4.2
    ln -s /usr/local/vcl-2.4.2 /usr/local/vcl
    /bin/cp -r /root/apache-VCL-2.4.2/managementnode/* /usr/local/vcl
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
