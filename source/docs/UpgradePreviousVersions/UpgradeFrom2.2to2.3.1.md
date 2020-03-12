---
title: Upgrade From 2.2 to 2.3.1
---

This page provides information on how to upgrade from VCL 2.2 to VCL 2.3.1. Please note it only applies for the upgrade from 2.2 to 2.3.1, 
this may or may not work for other versions.

**The basic steps that will be performed**

 - Download and Extract 2.3.1 code
 - Shutdown httpd and vcld services
 - Create backup of vcl database
 - Update mysql schema
 - Update Web code, create a backup, copy in new, make changes
 - Restart httpd service
 - Update Management node vcl code, create a backup, copy in new, make changes
 - Restart vcld service
 
# Detailed steps for upgrade from 2.2 to 2.3.1 #

1. follow instructions on VCL 2.3.1 Release page to download and verify apache-VCL-2.3.1.tar.bz2 and put in in /root
1. **extract VCL 2.3.1 code**
    
    ```bash
    tar xjf apache-VCL-2.3.1.tar.bz2
    ```

1. **Shutdown** the httpd and vcld services
           
    ```bash
    service httpd stop or /etc/init.d/httpd stop
    service vcld stop or /etc/init.d/vcld stop
    ```

1. We will **create a backup of the vcl database**. This will provide a restore point if necessary.

    ```bash
    mysqldump vcl > ~/vcl-pre2.3.1-upgrade.sql
    ```

1. This step **updates the mysql schema**. *Note*: A new resource group is added in update-vcl.sql - **all profiles**. 
Access to manage the group is added to the VCL->admin node in the privilege tree if that node exists. If not, you will 
need to add it manually after starting httpd again. To add it manually, pick a node in the privilege tree, scroll to 
Resources, click Add Resource Group, select serverprofile/all profiles from the drop-down box, check available, 
administer, manageGroup, and manageMapping, and click Submit New Resource Group.

    ```bash
    cd /root/apache-VCL-2.3.1
    mysql vcl < mysql/update-vcl.sql
    ```

1. Grant CREATE TEMPORARY TABLES to mysql user
The web code now requires access to create temporary tables in mysql. You need to grant the user your web code uses 
to access mysql the "CREATE TEMPORARY TABLES" permission. Look at the secrets.php file in your web code for the user 
and hostname. For example, if your web code is installed at /var/www/html/vcl, your secrets.php file would be 
/var/www/html/vcl/.ht-inc/secrets.php. Look for $vclhost and $vclusername. The secrets.php file might have something like:

    ```php
    $vclhost = 'localhost';
    $vcluser = 'vcluser';
    ```

1. Then, you need to issue the grant command to mysql. Using the values from above as examples, connect to mysql and then issue the grant command:

    ```bash
    mysql
    GRANT CREATE TEMPORARY TABLES ON `vcl`.* TO 'vcluser'@'localhost';
    exit
    ```

1. **Update the web code**. This step we will move the 2.2 web directory out of the way, so we can copy in the new 
web code base. After copying in the new code, we will migrate your configuration changes. These instructions assume 
that you installed the vcl web code at /var/www/html/vcl. If you installed it elsewhere, replace /var/www/html/vcl 
with your vcl web root.

    ```bash
    cd /var/www/html
    mv vcl ~/vcl_2.2_web
    ```

1. **Copy the new code** in place
	
    ```bash
    cd /root/apache-VCL-2.3.1
    cp -r web /var/www/html/vcl
    ```

1. **Copy your 2.2 config files**
	
    ```bash
    cd ~/vcl_2.2_web/.ht-inc
    cp conf.php secrets.php pubkey.pem keys.pem /var/www/html/vcl/.ht-inc
    ```

1. **Make the maintenance directory writable by the web server user**. Normally this is the apache user,  if using a 
different user change below cmd accordingly.
	
    ```bash
    chown apache /var/www/html/vcl/.ht-inc/maintenance
    ```

1. **Make changes to conf.php**:

    1. A new user group permission that controls who can manage block allocations globally or for a specific affiliation 
    has been added. It can be granted to any user group under Privileges->Additional User Permissions->Manage Block Allocations. 
    Users with this permission are notified of new block allocation requests. **Remove the following from conf.php**.
	
        ```php
        $blockNotifyUsers
        ```

    1. A new user group permission that controls who can look up users globally or for a specific affiliation has been 
added. It can be granted to any user group under Privileges->Additional User Permissions->User Lookup. Users with this 
permission can look up information about other users. **Remove the following from conf.php** 
	
        ```php
        $userlookupUsers
        ```

    1. **Multilingualization** has been added VCL. So, **DEFAULTLOCALE** has been added to conf.php to set the default 
locale. **Add the following to conf.php**, changing en_US if needed to match your locale. You can look in 
/var/www/html/vcl/locale to see which ones are available.
	
        ```php
        define("DEFAULTLOCALE", "en_US");
        ```

    1. Users authenticated using Shibboleth without also having an LDAP server can now be added before they log in. **Add 
the following to conf.php**  If you are using Shibboleth and would like to be able to add users to groups before the user 
has ever logged in to VCL, you can set this to 1. However, please note that if you typo the userid, there is no way to 
verify it, and the user will be added with the typoed userid.
	
        ```php
        define("ALLOWADDSHIBUSERS", 0);
        ```

    1. LDAP related items have been simplified in the code using additional options in $authMechs. For any LDAP entries, 
add two options. "lookupuserbeforeauth" is used if you need VCL to look up the full DN of a user and use that when doing 
the bind that authenticates the user (if you don't know what this means, leave it set to 0). If you need to set it to 1, 
then you will need to set "lookupuserfield" to what LDAP attribute to use when looking up the user's DN 
(typically either 'cn', 'uid', or 'samaccountname'). In conf.php, **Add the following to each LDAP** array you have in the $authMech array.
	
        ```php
        "lookupuserbeforeauth" => 0,
        "lookupuserfield" => '',
        ```

    1. The way the authentication functions toward the bottom of conf.php are initialized has been simplified. Make the following changes:

        * REMOVE

            ```php
            $affilValFunc
            $affilValFuncArgs 
            $addUserFunc
            $addUserFuncArgs
            $updateUserFunc
            $updateUserFuncArgs
            ```
   
        * ADD

            ```php
            $affilValFunc = array();
            $affilValFuncArgs = array();
            $addUserFunc = array();
            $addUserFuncArgs = array();
            $updateUserFunc = array();
            $updateUserFuncArgs = array();
            foreach($authMechs as $key => $item) {
                 if($item['type'] == 'ldap') {
                    $affilValFunc[$item['affiliationid']] = 'validateLDAPUser';
                    $affilValFuncArgs[$item['affiliationid']] = $key;
                    $addUserFunc[$item['affiliationid']] = 'addLDAPUser';
                    $addUserFuncArgs[$item['affiliationid']] = $key;
                    $updateUserFunc[$item['affiliationid']] = 'updateLDAPUser';
                    $updateUserFuncArgs[$item['affiliationid']] = $key;
                }
                elseif($item['type'] == 'local') {
                    $affilValFunc[$item['affiliationid']] = create_function('', 'return 0;');
                    $addUserFunc[$item['affiliationid']] = create_function('', 'return NULL;');
                    $updateUserFunc[$item['affiliationid']] = create_function('', 'return NULL;');
                }
            }
            ```

1. **Restart httpd service**

    ```bash
    service httpd start or /etc/init.d/httpd start
    ```

1. **Update management node code** This step will make a backup copy of the 2.2 vcl code base and then copy the new code 
over the existing code to preserve any drivers or other files you've added.
	
    ```bash
    cd <your vcl MN code root path>
    ie. cd /usr/local/
    cp -r vcl ~/vcl_2.2_managementnode
    ```

1. **Copy in the 2.3.1 code base to /usr/local**, copying in should preserve any drivers or other files you've added.
	
    ```bash
    /bin/cp -r /root/apache-VCL-2.3.1/managementnode/* /usr/local/vcl
    ```

1. **Run install_perl_libs.pl** to add any new perl library requirements:
	
    ```bash
    /usr/local/vcl/bin/install_perl_libs.pl
    ```

1. **Restart vcld service**
	
    ```bash
    service vcld start or /etc/init.d/vcld start
    ```

1. Make some test reservations and watch the vcld.log to verify everything is working correctly.

    ```bash
    tail -f /var/log/vcld.log
    ```
