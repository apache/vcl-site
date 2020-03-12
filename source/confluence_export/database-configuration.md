---
title: Database Configuration
---

{excerpt}This page describes how to create the VCL MySQL database and
import the VCL database schema.{excerpt}


<a name="DatabaseConfiguration-*Prerequisites*"></a>
## *Prerequisites*

1. You should have mysql server 5.x installed.&nbsp;If mysql server is not
installed:

    yum install mysql-server -y
    /sbin/chkconfig --level 345 mysqld on
    /sbin/service mysqld start

1. Your host based firewall (IPTables) should be configured to allow traffic
from the web server and management server to connect to TCP port 3306
(mysqld).


<a name="DatabaseConfiguration-*SettingUptheDatabaseforVCL*"></a>
## *Setting Up the Database for VCL*

1. create a database in mysql named for use with VCL

    CREATE DATABASE vcl;

1. create a user with SELECT, INSERT, UPDATE, and DELETE privileges on the
database you just created
*NOTE*: Replace vcluserpassword with your own password\!

    GRANT SELECT,INSERT,UPDATE,DELETE ON vcl.* TO 'vcluser'@'localhost'
IDENTIFIED BY 'vcluserpassword';

1. locate vcl.sql file
The vcl.sql file should be contained in the release artifact you should
have downloaded already. After extracting it, look in the mysql directory.
1. import vcl.sql file into database

    mysql vcl < vcl.sql

