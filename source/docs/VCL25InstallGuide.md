---
title: VCL 2.5 Installation Guide
---

# Scripted Installation
VCL 2.5 is the first release to include an installation script.  All you need to install
VCL is the script. It will download and validate the VCL software and then install it.
The script can be used to install all three parts of VCL (database, web portal, and 
management node) or to install each part individually.

[Download Install Script (vcl-install.sh)][4]

Validate script:

```bash
wget https://www.apache.org/dist/vcl/2.5/vcl-install.sh.sha1
sha1sum -c vcl-install.sh.sha1
wget https://www.apache.org/dist/vcl/KEYS
gpg --import KEYS
wget https://www.apache.org/dist/vcl/2.5/vcl-install.sh.asc
gpg --verify vcl-install.sh.asc
```

Running the installation script with no arguments will step you through installing all
three parts of VCL.  Alternatively, the following explains optional arguments.  If
installing the management node part of VCL, it will also prompt you to agree to the 
installation of various system level requirements needed for the code to run.

```bash
vcl-install.sh [-h|--help] [-d|--database] [-w|--web] [-m|--managementnode]
        [--dbhost <hostname> --dbpass <password>] 
        [--mnhost <hostname>] [--webhost <hostname>]

-d|--database - install database server components
        --dbpass, --mnhost, --mnip, --webhost, and --adminpass must also be specified

-w|--web - install web server components
        --dbhost and --dbpass must also be specified

-m|--managementnode - install management node (vcld) components
        --dbhost, --dbpass, and --adminpass must also be specified

--dbhost <hostname> - hostname of database server (default=localhost)

--dbpass <password> - password VCL will use for accessing
        database (default=random)

--mnhost <hostname> - hostname of management node (default=localhost)

--webhost <hostname> - hostname of web server (default=localhost)

--adminpass <password> - password for VCL admin user
```

# Manual Installation 

This section provides a list of commands for installing VCL if you prefer to manually 
install it.

[Database Installation](#database)<br>
[Web Portal Installation](#web)<br>
[Management Node Installation](#managementnode)

## Install and Configure Database {#database}

VCL currently supports the use of MySQL or MariaDB as the database.

1. Download and Extract the Apache VCL Source
    * If you have not already done so, follow the instructions on the [download](/downloads/download.cgi)
page to download and verify apache-VCL-2.5.tar.bz2, and put it in /root

    * Extract the files:

        ```bash
        tar -jxvf apache-VCL-2.5.tar.bz2
        ```

2. Install MySQL Server or MariaDB Server

    * Install MySQL or MariaDB Server
        
        ```bash
        yum install mysql-server -y
        ```

        or

        ```bash
        yum install mariadb-server -y
        ```

    * Configure the database daemon to start automatically:

        ```bash
        /sbin/chkconfig --level 345 mysqld on
        ```

        or

        ```bash
        /sbin/chkconfig --level 345 mariadb on
        ```

    *  Start the database daemon:
        
        ```bash
        /sbin/service mysqld start
        ```

        or

        ```bash
        /sbin/service mariadb start
        ```

    *  If the iptables firewall is being used and the web server and management nodes 
will be on different machines, port 3306 should be opened up to each of those nodes. 
Add the following to your iptables config and restart iptables service.

        **Note:** Insert your web server and management node IP address in the right locations.

        ```bash
        vi /etc/sysconfig/iptables
        ```

        * Add these rules:

            ```text
            -A INPUT -m state --state NEW -s <web server IP> -p tcp --dport 3306 -j ACCEPT
            -A INPUT -m state --state NEW -s <management node IP> -p tcp --dport 3306 -j ACCEPT
            ```

        * Restart iptables:

            ```bash
            service iptables restart
            ```

    *  If the firewalld firewall is being used and the web server and management nodes 
will be on different machines, port 3306 should be opened up to each of those nodes. 
Add the following rules and reload the rule set.<br>
**Note:** Insert your web server and management node IP address in the right locations.

        * Add these rules:

            ```bash
            firewall-cmd --zone=public --permanent --add-rich-rule="rule family="ipv4" source address="<web server IP>" service name="mysql" accept"
            firewall-cmd --zone=public --permanent --add-rich-rule="rule family="ipv4" source address="<management node IP>" service name="mysql" accept"
            ```

        * Restart iptables:

            ```bash
            firewall-cmd --reload
            ```

3. Create the VCL Database
   
    * Run the MySQL command-line client:
         
        ```bash
        mysql
        ```

    * Create a database:
         
        ```sql
        CREATE DATABASE vcl;
        ```

    * Create a user with SELECT, INSERT, UPDATE, DELETE, and CREATE TEMPORARY TABLES 
privileges on the database you just created (**NOTE Use your own password**):
        
        ```sql
        GRANT SELECT,INSERT,UPDATE,DELETE,CREATE TEMPORARY TABLES ON vcl.* TO 'vcluser'@'localhost' IDENTIFIED BY 'vcluserpassword';
        ```bash

    * Exit the MySQL command-line client

        ```bash
        exit
        ```

    * Import the vcl.sql file into the database. The **vcl.sql** file is included in the 
**mysql** directory within the Apache VCL source code

        ```bash
        mysql vcl < apache-VCL-2.5/mysql/vcl.sql
        ```

----------

## Install and Configure the Web Components {#web}

**Prerequisites**

  - Apache VCL 2.5 has been downloaded
  - VCL database has been installed and configured

**Web Server:**
 
   - Apache HTTP Server v1.3 or v2.x with SSL enabled
   - PHP 5.0 or later

**Required Linux Packages:**

  - httpd - Apache HTTP Server
  - mod_ssl - SSL/TLS module for the Apache HTTP server
  - php - The PHP HTML-embedded scripting language

**Required PHP Modules:**

  * php
  * php-gettext
  * php-json (required if your PHP version is 5.2 or later)
  * php-ldap (if you will be using LDAP authentication)
  * php-mysql
  * php-openssl
  * php-xml
  * php-xmlrpc


 - - -

1. **Install the Required Linux Packages & PHP Modules**

    * If your web server is running a Red Hat-based OS, the required components can be installed with:
        
        For RHEL / CentOS 6 and 7

        ```bash
        yum install httpd mod_ssl php php-mysql php-xml php-xmlrpc php-ldap -y
        ```

    * Configure the web server daemon (httpd) to start automatically:

        ```bash
        /sbin/chkconfig --level 345 httpd on
        ```

    * Start the web server daemon

        ```bash
        /sbin/service httpd start 
        ```

    * If SELinux is enabled, run the following command to allow the web server to connect to the database:

        ```bash
        /usr/sbin/setsebool -P httpd_can_network_connect=1
        ```

    * If the iptables firewall is being used, port 80 and 443 should be opened up in the iptables
config file:

        ```bash
        vi /etc/sysconfig/iptables
        ```

        * Add these rules:

            ```text
            -A INPUT -m state --state NEW -p tcp --dport 80 -j ACCEPT
            -A INPUT -m state --state NEW -p tcp --dport 443 -j ACCEPT
            ```

        * Restart iptables

            ```bash
            service iptables restart
            ```

    * If the firewalld firewall is being used, port 80 and 443 should be opened up:

        * Add these rules:

            ```bash
            firewall-cmd --zone=public --add-service=http --permanent
            firewall-cmd --zone=public --add-service=https --permanent
            ```

        * Reload firewalld rules

            ```bash
            firewall-cmd --reload
            ```

2. **Install the VCL Frontend Web Code**
    * If you have not already done so, follow the instructions on the [download](/downloads/download.cgi)
page to download and verify apache-VCL-2.5.tar.bz2, and put it in /root

    * Extract the files:

        ```bash
        tar -jxvf apache-VCL-2.5.tar.bz2
        ```

    * Copy the **web** directory to a location under the web root of your web server and 
navigate to the destination **.ht-inc** subdirectory:

        ```bash
        cp -ar apache-VCL-2.5/web/ /var/www/html/vcl-2.5
        ln -s /var/www/html/vcl-2.5 /var/www/html/vcl
        cd /var/www/html/vcl/.ht-inc
        ```

    * If SELinux is enabled, run the following command to set the context of the web code to httpd_sys_content_t
	
        ```bash
        chcon -R -t httpd_sys_content_t /var/www/html/vcl-2.5
        ```

    * Copy secrets-default.php to secrets.php:

        ```bash
        cp secrets-default.php secrets.php
        ```

    * Edit the secrets.php file:

        ```bash
        vi secrets.php
        ```

        * Set the following variables to match your database configuration:
            * $vclhost
            * $vcldb
            * $vclusername
            * $vclpassword
        * Create random passwords for the following variables:
            * $cryptkey (generate with "openssl rand 32 | base64")
            * $pemkey
        * Save the secrets.php file

    * Run the genkeys.sh
	
        ```bash
        ./genkeys.sh
        ```

    * Copy conf-default.php to conf.php:

        ```bash
        cp conf-default.php conf.php
        ```

    * Modify conf.php to match your site

        ```bash
        vi conf.php
        ```

        * Review every entry under "Things in this section must be modified/reviewed". 
        Descriptions and pointers for each value are included within conf.php.
        
    * Set the owner of the .ht-inc/maintenance and .ht-inc/cryptkey directories to the web server user (normally 'apache'):
	
        ```bash
        chown apache maintenance
        chown apache cryptkey
        ```

    * If SELinux is enabled, run the following command to allow the web server to write to maintenance and cryptkey
	
        ```bash
        chcon -t httpd_sys_rw_content_t maintenance
        chcon -t httpd_sys_rw_content_t cryptkey
        ```

    * Open the testsetup.php page in a web browser:
        * If you set up your site to be https://my.server.org/vcl/ open https://my.server.org/vcl/testsetup.php
        * Debug any issues reported by testsetup.php

3. **Log In to the VCL Website**
    * Open the index.php page in your browser (https://my.server.org/vcl/index.php)
        * Select Local Account
        * Username: admin
        * Password: adminVc1passw0rd

    * Set the admin user password (**DO NOT skip this step**):
        * Click User Preferences
        * Enter the current password: adminVc1passw0rd
        * Enter a new password
        * Click Submit Changes

4. **Add a Management Node to the Database**
    * Click the Management Nodes link
        * Select Edit Management Node Profiles
        * Click Submit
        * Click Add New Management Node
        * Fill in these required fields:
            * Hostname - The name of the management node server. This value doesn't 
necessarily need to be a name registered in DNS nor does it need to be the value 
displayed by the Linux hostname command. For example, if you are installing all of the 
VCL components on the same machine you can set this value to localhost.
            * IP address - the public IP address of the management node
            * SysAdmin Email Address - error emails will be sent to this address
            * Install Path - this is the parent directory under which image files will be 
stored - only required if doing bare metal installs or using VMWare with local disks
            * End Node SSH Identity Key Files - enter /etc/vcl/vcl.key unless you know 
you are using a different SSH identity key file
        * Optionally, fill in these fields:
            * Address for Shadow Emails - End users are sent various emails about the 
status of their reservations. If this field is configured, copies of all of those emails 
will be sent to this address.
            * Public NIC configuration method - this defaults to Dynamic DHCP - if DHCP 
is not available for the public interface of your nodes, you can set this to Static. 
Then, the IP configuration on the nodes will be manually set using Public Netmask, 
Public Gateway, Public DNS Server, and the IP address set for the computer under Manage 
Computers       
        * Click Add Management Node
        * A dialog will pop up informing you to add the management node to a group, 
read it and click Close
        * select the allManagementNodes group on the right
        * click <-Add
        * click Close

5. **Install & Configure phpMyAdmin (Optional):**
[phpMyAdmin][1] is a free and optional tool which allows [MySQL][2] to be administered 
using a web browser. It makes administering the VCL database easier. This tool can be 
installed on the VCL web server.
To install phpMyAdmin, follow the instructions on: [phpMyAdmin Installation & 
Configuration][3]

---------


## Install & Configure the Management Node Components {#managementnode}

**Prerequisites**
The following management node installation instructions assume the instructions in these
previous sections have been completed:

* VCL 2.5 Database Installation
* VCL 2.5 Web Code Installation

**Supported Operating Systems:**

The VCL management node daemon (vcld) has been developed to run on an operating system 
based on Red Hat Enterprise Linux (RHEL). It has been tested on the following:

* Red Hat Enterprise Linux 6.x
* Red Hat Enterprise Linux 7.x
* CentOS 6.x
* CentOS 7.x

**Required Linux Packages:**

The VCL management node daemon (vcld) requires the following Linux packages and Perl 
modules in order to run (see step 2 below for installation instructions).

* expat-devel - Libraries and include files to develop XML applications with expat
* gcc - Various compilers (C, C++, Objective-C, Java, ...)
* krb5-devel - Development files needed to compile Kerberos 5 programs
* krb5-libs - The shared libraries used by Kerberos 5
* libxml2-devel - Libraries, includes, etc. to develop XML and HTML applications
* make - GNU make utility to maintain groups of programs
* mysql/mariadb - Includes libraries for connecting to mysql/mariadb
* nmap - Network exploration tool and security scanner
* openssh - The OpenSSH implementation of SSH protocol versions 1 and 2
* openssl-devel - Files for development of applications which will use OpenSSL
* perl - The Perl programming language
* xmlsec1-openssl - OpenSSL crypto plugin for XML Security Library

**Required Perl Modules:**

The VCL management node daemon (vcld) is written in Perl and has been tested on Perl 
5.10 and 5.16. The following Perl modules available from CPAN are also required (see step 2 
below for installation instructions):

* Crypt::CBC - implementation of the cryptographic cipher block chaining mode
* Crypt::OpenSSL::RSA - RSA encoding and decoding, using the openSSL libraries
* Crypt::Rijndael - Crypt::CBC compliant Rijndael encryption module
* DBI - Generic Database Interface
* Digest::SHA1 - NIST SHA message digest algorithm
* Exception::Class::Base - base class for exception objects
* Frontier::Client - issue Frontier XML RPC requests to a server
* HTTP::Headers - class encapsulating HTTP Message headers
* IO::String - emulate file interface for in-core strings
* JSON - JavaScript Object Notation
* LWP::UserAgent - class implementing a web user agent
* Mail::Mailer - Simple mail agent interface
* Net::Jabber - Jabber perl library
* Net::Netmask - parse, manipulate and lookup IP network blocks
* Net::SSH::Expect - a wrapper to the ssh executable that is available in system's PATH
* Object::InsideOut - Comprehensive inside-out object support
* RPC::XML::Client - XML-RPC client class
* Text::CSV_XS - comma-separated values manipulation routines
* XML::Simple - API for simple XML files
* YAML - YAML Ain't Markup Language
<BR>
---

1. **Install the VCL Management Node Code - Perl Daemon**
    * If you have not already done so, follow the instructions on the 
[download](/downloads/download.cgi) page to download and verify 
apache-VCL-2.5.tar.bz2, and put it in /root

    * Extract the files:

        ```bash
        tar -jxvf apache-VCL-2.5.tar.bz2
        ```

    * Copy the managementnode directory to the location where you want it to reside 
(typically /usr/local):

        ```bash
        cp -ar apache-VCL-2.5/managementnode /usr/local/vcl-2.5
        ln -s /usr/local/vcl-2.5 /usr/local/vcl
        ```

2. **Install the Required Linux Packages & Perl Modules**

    * Run the install_perl_libs.pl script located in the bin directory:

        ```bash
        perl /usr/local/vcl/bin/install_perl_libs.pl
        ```

    The last line of the install_perl_libs.pl script output should be:
    
    *COMPLETE: installed all components*
    
    Note: The script will hang or terminate if it encounters a problem. If this occurs, 
you will need to troubleshoot the problem by looking at the output. 

    The install_perl_libs.pl script included in the VCL distribution will attempt to 
download and install the required Linux packages and Perl modules. It uses the yum 
utility to install the required Linux packages. The required Perl modules are available 
from CPAN - The Comprehensive Perl Archive Network. The install_perl_libs.pl script 
attempts to download and install the required Perl modules by using the CPAN.pm module 
which is included with most Perl distributions. 

    The yum utility should exist on any modern Red Hat-based Linux distribution (Red 
Hat, CentOS, Fedora, etc). If yum isn't available on your management node OS, you will 
need to download and install the required Linux packages manually or by using another 
package management utility. After installing the required Linux packages, attempt to 
run the install_perl_libs.pl script again.

3. **Configure vcld.conf**

    * Create the /etc/vcl directory:

        ```bash
        mkdir /etc/vcl
        ```

    * Copy the stock vcld.conf file to /etc/vcl:
	
        ```bash
        cp /usr/local/vcl/etc/vcl/vcld.conf /etc/vcl
        ```

    * Edit /etc/vcl/vcld.conf:
	
        ```bash
        vi /etc/vcl/vcld.conf
        ```

        The following lines must be configured in order to start the VCL daemon (vcld) 
and allow it to check in to the database:

        * FQDN - the fully qualified name of the management node, this should match the 
name that was configured for the management node in the database
        * server - the IP address or FQDN of the database server
        * LockerWrtUser - database user account with write privileges
        * wrtPass - database user password
        * xmlrpc_pass - password for xmlrpc api from vcld to the web interface(can be 
long). This will be used later to sync the database vclsystem user account
        * xmlrpc_url - URL for xmlrpc api 
https://my.server.org/vcl/index.php?mode=xmlrpccall

    * Save the vcld.conf file

4. **Configure the SSH Client**

    The SSH client on the management node should be configured to prevent SSH processes 
spawned by the root user to the computers it controls from hanging because of missing or 
different entries in the known_hosts file. 

    * Edit the ssh_config file:

        ```bash
        vi /etc/ssh/ssh_config
        ```

    * Set the following parameters:
        * UserKnownHostsFile /dev/null
        * StrictHostKeyChecking no

    Note: If you do not want these settings applied universally on the management node 
the SSH configuration can also be configured to only apply these settings to certain 
hosts or only for the root user. Consult the SSH documentation for more information.

5. **Install and Start the VCL Daemon (vcld) Service**

    * **Steps for systemd** - use these steps if your system is using systemd

        * Copy the vcld service script to /usr/lib/systemd/system

            ```bash
            cp /usr/local/vcl/etc/systemd/system/vcld.service /usr/lib/systemd/system
            ```

        * Create a vcld config file in /etc/sysconfig

            ```bash
            echo "OPTIONS='-v -conf=/etc/vcl/vcld.conf'" > /etc/sysconfig/vcld
            ```

        * If using SELinux, set the correct user and context:

            ```bash
            chcon -u system_u -t systemd_unit_file_t /usr/lib/systemd/system/vcld.service
            ```

        * Enable vcld.service

            ```bash
            systemctl enable vcld.service
            ```

        * Start the vcld service:
	
            ```bash
            systemctl start vcld.service
            ```

        * Check the vcld service by monitoring the vcld.log file:

            ```bash
            tail -f /var/log/vcld.log
            ```

    * **Steps for SystemV** - use these steps if your system is using SystemV (scripts located in
/etc/init.d)

        * Copy the vcld service script to /etc/init.d and name it vcld:
	
            ```bash
            cp /usr/local/vcl/bin/S99vcld.linux /etc/init.d/vcld
            ```

        * Add the vcld service using chkconfig:
	
            ```bash
            /sbin/chkconfig --add vcld
            ```

        * Configure the vcld service to automatically run at runtime levels 3-5:
	
            ```bash
            /sbin/chkconfig --level 345 vcld on
            ```

        * Start the vcld service:
	
            ```bash
            /sbin/service vcld start
            ```

        * Check the vcld service by monitoring the vcld.log file:

            ```bash
            tail -f /var/log/vcld.log
            ```

            You should see the following being added to the log file every few seconds if the 
management node is checking in with the database:

            ```text
            2017-07-13 13:23:45|25494|vcld:main(167)|lastcheckin time updated for management node 1: 2017-07-13 13:23:45
            ```

6. **Set the vclsystem account password for xmlrpc api**

    Using the vcld -setup tool, set the vclsystem account. This is needed to properly 
use the block allocation features.
	
    ```bash
    /usr/local/vcl/bin/vcld --setup
    ```

    Select the options listed below to set the password. When prompted paste or type the 
password from xmlrpc_pass variable in the vcld.conf file and hit enter. 

    ```bash
    Select 5. Set Local VCL User Account Password
    Select 2. vclsystem
    Enter the password you set for xmlrpc_pass in /etc/vcl/vcld.conf
    ```

    After setting the password for the vclsystem user, test that RPC-XML Access works correctly
by selecting

    ```bash
    2: Test RPC-XML Access
    ```

    **SUCCESS: RPC-XML access is configured correctly** should be displayed followed by a long list of
available XMLRPC functions

7. **Install & Configure the DHCP Service**
   
    DHCP service is needed for the private network to provide address to provisioned 
machines.

    * Install dhcp if it is not already installed:
	
        ```bash
        yum install dhcp -y
        ```

    * Configure the dhcpd service to automatically start at runlevels 3-5:

        ```bash
        /sbin/chkconfig dhcpd on
        ```

    * Configure the dhcpd.conf file.
	
        ```bash
        vi /etc/dhcpd.conf
        # -or-
        vi /etc/dhcp/dhcpd.conf
        ```

        Configure your dhcpd.conf file according to your network configuration. 
        The contents of the dhcpd.conf file will vary based on how your network is 
        configured. Below is an example of a basic dhcpd.conf file:
  
        ```text
        ddns-update-style none;
        shared-network eth0 {
	        subnet 10.100.0.0 netmask 255.255.255.0 {
	                 ignore unknown-clients;
	        }
        }
        ```

        You will add host definitions to the dhcpd.conf file after you add computers to VCL 
using the website. The website allows you to select a set of computers for which to
generate dhcpd.conf information, which can be copied and pasted into the dhcpd.conf file.

    * Start the dhcpd service:

        ```bash
        /sbin/service dhcpd start
        ```

---------

# Initial Administration Steps After Installing VCL

After you have installed the VCL components, you need to do some initial administration 
of your new VCL install.

1. Add Computers

    * If using **bare-metal** provisioning, follow the instruction
on the [Adding Computers](addcomputers) page, selecting **Bare Metal** 
as the computer Type
    * If using **VM** provisioning:
        * Follow the instruction on the [Adding Computers](addcomputers) 
page, selecting **Bare Metal** as the computer Type to add at least one
VM Host
        * Follow the instruction on the [Adding Computers](addcomputers) 
page, selecting **Virtual Machine** as the computer Type to add some
virtual computers
        * Finally, [Assign the VMs to VM hosts](assignvmtohost)

2. [Create Base Images](image-creation)

3. Configure Authorization (follow links appropriate to your site)
    * [Adding Local Accounts](localaccounts)
    * [Configuring LDAP Authentication](ldapauth)
    * [Configuring Shibboleth Authentication](shibauth)

------

[1]: http://www.phpmyadmin.net/
[2]: http://www.mysql.com/
[3]: installphpmyadmin
[4]: https://www.apache.org/dist/vcl/2.5/vcl-install.sh
