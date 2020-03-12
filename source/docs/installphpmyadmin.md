---
title: phpMyAdmin Installation & Configuration
---

<div class="docnote">
phpMyAdmin is a free and optional tool which allows MySQL to be administered using a web 
browser. It makes administering the VCL database easier. This tool can be installed on 
the VCL web server.
</div>

1. phpmyadmin recommends performing installation using packages available from you Linux 
distribution

    For CentOS, the EPEL yum repository needs to have been added (which is done for installing
the VCL management node code; use **yum install -y epel-release** in not already installed). Use the 
following to install phpMyAdmin from EPEL:

    ```bash
    yum install -y phpMyAdmin
    ```

1. By default phpMyAdmin on Red Hat based distros restrict access to localhost only. Modify
**/etc/httpd/conf.d/phpMyAdmin.conf** to change that.  It is advisable to only allow access from some
specific IP addresses or IP ranges so that phpMyAdmin is not open to everyone to try to access.
    * In the `<Directory /usr/share/phpMyAdmin/>` section, add
      
        ```text
        Require ip x.x.x.x/y
        ```

        Where x.x.x.x/y represents an IP range such as 192.168.100.1/24. Multiple lines can be added
        to match multiple ranges.

    * restart httpd to active the changes

        ```bash
        systemctl restart httpd
        ```

1. A special database needs to be created to enable some of the more helpful phpMyAdmin functionality.
phpMyAdmin provides a script for creating the database. Look for create_tables.sql (for v4.4.15.10,
it was at /usr/share/phpMyAdmin/sql/create_tables.sql). Create the database using

    ```bash
    mysql < /usr/share/phpMyAdmin/sql/create_tables.sql
    ```

1. A control user must be created in mysql/mariadb for phpMyAdmin to use (we'll use pmacontrol, 
**replace mypassword with your own password!**):

    ```bash
    mysql -e "CREATE USER 'pmacontrol'@'localhost' IDENTIFIED BY 'mypassword';"
    ```

    Save the following in a file named **pmaprivs.sql** to grant the pmacontrol user access to various parts tables:

    ```sql
    GRANT USAGE ON mysql.&ast; TO 'pmacontrol'@'localhost';
    GRANT SELECT (
    Host, User, Select_priv, Insert_priv, Update_priv, Delete_priv,
    Create_priv, Drop_priv, Reload_priv, Shutdown_priv, Process_priv,
    File_priv, Grant_priv, References_priv, Index_priv, Alter_priv,
    Show_db_priv, Super_priv, Create_tmp_table_priv, Lock_tables_priv,
    Execute_priv, Repl_slave_priv, Repl_client_priv
    ) ON mysql.user TO 'pmacontrol'@'localhost';
    GRANT SELECT ON mysql.db TO 'pmacontrol'@'localhost';
    GRANT SELECT ON mysql.host TO 'pmacontrol'@'localhost';
    GRANT SELECT (Host, Db, User, Table_name, Table_priv, Column_priv)
    ON mysql.tables_priv TO 'pmacontrol'@'localhost';
    GRANT SELECT, INSERT, UPDATE, DELETE ON phpmyadmin.&ast; TO 'pmacontrol'@'localhost';
    ```

    ```bash
    mysql < pmaprivs.sql
    ```

1. Configure the phpMyAdmin-VCL Table relationships:

    A file named phpmyadmin.sql file is provided in the mysql directory in the Apache VCL source 
    code. It will add entries to the pma_table_info table in the phpmyadmin database. These entries 
    cause useful information to be displayed when you hover over values in the VCL database.

    Import the SQL file into the phpmyadmin database:

    ```bash
    mysql phpmyadmin < apache-VCL-2.5.1/mysql/phpmyadmin.sql
    ```

1. You should now be able to log in to phpMyAdmin using the account set up for VCL to access the
database (can be referenced in /etc/vcl/vcld.conf or /var/www/html/vcl/.ht-inc/secrets.php).


[1]: VCL251InstallGuide.html
[2]: http://www.phpmyadmin.net/home_page/downloads.php
[3]: http://sourceforge.net/projects/phpmyadmin/files/phpMyAdmin/
