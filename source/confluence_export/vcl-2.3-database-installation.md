---
title: VCL 2.3 Database Installation
---

{excerpt:hidden=true}How to install MySQL Server, create the VCL database,
and import the VCL database schema{excerpt}

<a name="VCL2.3DatabaseInstallation-Install&ConfiguretheDatabase"></a>
# Install & Configure the Database

1. h2. Download & Extract the Apache VCL Source
1. # If you have not already done so, download and the Apache VCL source to
the database server:
{tip}wget --trust-server-names
'{nolink:http://vcl.apache.org/downloads/download.cgi?action=download&filename=%2Fvcl%2Fapache-VCL-2.3.tar.bz2}'{tip}
1. # Extract the files:
{tip}tar \-jxvf apache-VCL-2.3.tar.bz2{tip}
1. h2. Install MySQL Server
1. # Install MySQL Server 5.x: {tip}yum install mysql-server \-y{tip}
1. # Configure the MySQL daemon (mysqld) to start automatically:
{tip}/sbin/chkconfig \--level 345 mysqld on{tip}
1. # Start the MySQL daemon:
{tip}/sbin/service mysqld start{tip}
1. # If the iptables firewall is being used and the web server and management
nodes will be on different machines, port 3306 should be opend up
{tip}
vi /etc/sysconfig/iptables
{tip}

    -A RH-Firewall-1-INPUT -m state --state NEW -s <web server IP> -p tcp
--dport 3306 -j ACCEPT
    -A RH-Firewall-1-INPUT -m state --state NEW -s <management node IP> -p tcp
--dport 3306 -j ACCEPT
    service iptables restart

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
{tip}mysql vcl < apache-VCL-2.3/mysql/vcl.sql{tip}
{info}The *vcl.sql* file is included in the *mysql* directory within the
Apache VCL&nbsp;source code{info}

----
Next step: [VCL:VCL 2.3 Web Code Installation](vcl:vcl-2.3-web-code-installation.html)
