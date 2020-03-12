---
title: phpMyAdmin Installation & Configuration
---

<br>
<div class="docnote">
phpMyAdmin is a free and optional tool which allows MySQL or MariaDB to be administered using a web 
browser. It makes administering the VCL database easier. This tool can be installed on 
the VCL web server.
</div>

1. Install phpMyAdmin via the yum package manager. Tested on clean installs of CentOS, Red Hat versions 6 and 7

    1. phpMyAdmin is in the extras repository, use epel-release package to add this repo

        ```bash
        yum -y install epel-release 
        ```

    1. Install phpMyAdmin

        ```bash
        yum -y install phpMyAdmin
        ```

    1. Move the phpMyAdmin directory to the web server directory:

        ```bash
    	mv /usr/share/phpMyAdmin /var/www/html/phpMyAdmin
        ```

    1. Edit /etc/httpd/conf.d/phpMyAdmin.conf with your favorite editor.
        Replace the paths created by the yum install, change each 
        "**/usr/share/phpMyAdmin**" with **/var/www/html/phpMyAdmin** 
        or use this sed command

        ```bash
        sed -i "s|/usr/share/|/var/www/html/|g" /etc/httpd/conf.d/phpMyAdmin.conf
        ```

* Follow the latest setup instructions at [http://docs.phpmyadmin.net][1]
    <pre class="docnote">

    The "Securing your phpMyAdmin installation" instructions can be followed 
    to secure phpMyAdmin. At a minimum set the MySQL user and password 
    in the config.inc.php file
    Edit /etc/phpMyAdmin/config.inc.php and set the user and password variables to match 
    the LockerWrtUser(typically vcluser) and wrtPass from /etc/vcl/vcld.conf

    $cfg['Servers'][$i]['user']          = 'vcluser';  
    $cfg['Servers'][$i]['password']      = '';  //Use wrtPass from /etc/vcl/vcld.conf
    </pre>

* How to allow access to phpMyAdmin from other machines. The default server configuration limits 
access only to localhost (127.0.0.1). If desired to access from other machines, edit the 
server config file to allow other machines, change any lines with 127.0.0.1 to your workstation IP or 
a set of known IP addresses. 

    In your editor, open /etc/httpd/conf.d/phpMyAdmin.conf 
    Edit the first section, there are two locations that need to change

    <pre class="docnote">
    Under the section labeled:  Directory /var/www/html/phpMyAdmin/
    . . .
    Require ip your_workstation_IP_address
    . . .
    Allow from your_workstation_IP_address
    . . .
    </pre>

* Restart httpd service and test

    ```bash
    service httpd restart
    ```

    If you receive 403-Forbidden errors after installing phpMyAdmin, the problem is likely caused by SELinux. Run the following command to correct the problem:
    <pre class="docnote">
    chcon -R -t httpd_sys_content_t /var/www/html/phpMyAdmin
    </pre>

* Optional, Configure the phpMyAdmin-VCL Table relationships:

    After following the documentation on creating the phpMyAdmin Linked-tables 
    infrastructure, you can set up the VCL table relationships. The phpmyadmin.sql file is 
    provided in the mysql directory in the Apache VCL source code. It will add entries to the 
    pma_table_info table in the phpmyadmin database. These entries cause corresponding 
    information to be displayed when you hover over a value in the VCL database.

    Import the SQL file into the phpmyadmin database:

    ```bash
    mysql phpmyadmin < apache-VCL-2.4/mysql/phpmyadmin.sql
    ```

[1]: http://docs.phpmyadmin.net
