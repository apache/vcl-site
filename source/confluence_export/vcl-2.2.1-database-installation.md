---
title: VCL 2.2.1 Database Installation
---

{excerpt:hidden=true}How to install MySQL Server, create the VCL database,
and import the VCL database schema{excerpt}

<a name="VCL2.2.1DatabaseInstallation-Install&ConfiguretheDatabase"></a>
# Install & Configure the Database

1. h2. Download & Extract the Apache VCL Source
1. # If you have not already done so, download and the Apache VCL source to
the database server:
{tip}wget
{nolink:http://www.apache.org/dist/incubator/vcl/apache-VCL-2.2.1-incubating.tar.bz2}{tip}
1. # Extract the files:
{tip}tar \-jxvf apache-VCL-2.2.1-incubating.tar.bz2{tip}
1. h2. Install MySQL Server
1. # Install MySQL Server 5.x: {tip}yum install mysql-server \-y{tip}
1. # Configure the MySQL daemon (mysqld) to start automatically:
{tip}/sbin/chkconfig \--level 345 mysqld on{tip}
1. # Start the MySQL daemon:
{tip}/sbin/service mysqld start{tip}
1. # Make sure&nbsp;the&nbsp;firewall&nbsp;on the database server is
configured to allow traffic from the web server and management node servers
to connect to the MySQL&nbsp;daemon TCP port: *3306*.&nbsp; See the
firewall documentation for more information. {info}man iptables{info}
1. h2. Create&nbsp;the VCL Database
1. # Run the MySQL command-line client: {tip}mysql{tip}
1. # Create a database:
{tip}CREATE DATABASE vcl;{tip}
1. # Create a user with SELECT, INSERT, UPDATE, DELETE, and CREATE TEMPORARY
TABLES privileges on the database you just created:
{tip}GRANT SELECT,INSERT,UPDATE,DELETE,CREATE TEMPORARY TABLES ON vcl.\* TO
'*vcluser*'@'localhost' IDENTIFIED BY '*vcluserpassword*';{tip}
{note}Replace *vcluser* and *vcluserpassword* with that of the user you
want to use to connect to the database{note}
{info}The GRANT command will automatically create the user if it doesn't
already exist{info}
1. # Exit the MySQL command-line client: {tip}exit{tip}
1. # Import the vcl.sql file into the database:
{tip}mysql vcl < apache-VCL-2.2.1-incubating/mysql/vcl.sql{tip}
{info}The *vcl.sql* file is included in the *mysql* directory within the
Apache VCL&nbsp;source code{info}
1. h2. Install & Configure phpMyAdmin (Optional):
{excerpt-include:VCL 2.2.1 phpMyAdmin Installation &
Configuration|nopanel=true}
To install phpMyAdmin, follow the instructions on: [VCL:VCL 2.2.1 phpMyAdmin Installation & Configuration](vcl:vcl-2.2.1-phpmyadmin-installation-&-configuration.html)

----
Next step: [VCL:VCL 2.2.1 Web Code Installation](vcl:vcl-2.2.1-web-code-installation.html)
