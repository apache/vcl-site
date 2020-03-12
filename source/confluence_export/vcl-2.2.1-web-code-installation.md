---
title: VCL 2.2.1 Web Code Installation
---

{excerpt:hidden=true}
How to install and configure the frontend VCL web code. It also describes
how to add local accounts to the VCL database, configure LDAP
authentication, and set the timezone correctly.{excerpt}

<a name="VCL2.2.1WebCodeInstallation-Install&ConfiguretheWebComponents"></a>
# Install & Configure the Web Components

<a name="VCL2.2.1WebCodeInstallation-*Prerequisites*"></a>
## *Prerequisites*

The following instructions assume these tasks have previously been
completed:
* [Apache VCL 2.2.1 has been downloaded](download.html)
* [VCL database has been installed and configured](vcl:vcl-2.2.1-database-installation.html)

  
  

<a name="VCL2.2.1WebCodeInstallation-WebServer:"></a>
#### Web Server:

* Apache HTTP Server v1.3 or v2.x with SSL enabled
* PHP 5.0 or later

{info}The VCL web frontend may run under other web server platforms capable
of running PHP code, but has only been tested to work with Apache HTTP
Server.{info}

<a name="VCL2.2.1WebCodeInstallation-RequiredLinuxPackages:"></a>
#### Required Linux Packages:

* *httpd* \- Apache HTTP Server
* *mod_ssl* \- SSL/TLS module for the Apache HTTP server
* *php* \- The PHP HTML-embedded scripting language
* *libmcrypt* \- Encryption algorithms library (this requirement can be
removed with a [patch](vcl:patch-to-remove-mcrypt-dependency.html)
)

<a name="VCL2.2.1WebCodeInstallation-RequiredPHPModules:"></a>
#### Required PHP Modules:

(Some of these may already be included with your PHP distribution)
* *php-gd*
* *php-json* (required if your PHP version is 5.2 or later)
* *php-mcrypt* (this requirement can be removed with a [patch](vcl:patch-to-remove-mcrypt-dependency.html)
)
* *php-mysql*
* *php-openssl*
* *php-sysvsem*
* *php-xml*
* *php-xmlrpc*
* *php-ldap* (if you will be using LDAP authentication)

  
  
1. # If your web server is running a Red Hat-based OS, the required
components&nbsp;can be installed with:
{tip}
yum install httpd mod_ssl php php-gd php-mcrypt php-mysql php-xml
php-xmlrpc php-ldap \-y
{tip}
1. #* If you will be using a self-signed certificate for SSL, [this is a great HOWTO ](http://wiki.centos.org/HowTos/Https)
explaining how to set it up on CentOS
1. #* It is useful to configure the server to be able to send debugging
emails
1. # Configure the web server daemon (httpd) to start automatically:
{tip}
/sbin/chkconfig \--level 345 httpd on
{tip}
1. # Start the web server daemon:
{tip}
/sbin/service httpd start
{tip}
1. # If SELinux is enabled, run the following command to allow the web server
to connect to the database:
{tip}
/usr/sbin/setsebool \-P httpd_can_network_connect=1
{tip}
1. # If the iptables firewall is being used, port 80 and 443 should be opened
up:
{tip}vi /etc/sysconfig/iptables{tip}

    -A RH-Firewall-1-INPUT -m state --state NEW -p tcp --dport 80 -j ACCEPT
    -A RH-Firewall-1-INPUT -m state --state NEW -p tcp --dport 443 -j ACCEPT
    service iptables restart

  
  
1. h2. Install the&nbsp;VCL Frontend Web Code
1. # If you have not already done so, download and extract the source files
on the web server:
{tip}
wget
{nolink:http://www.apache.org/dist/incubator/vcl/apache-VCL-2.2.1-incubating.tar.bz2}
tar \-jxvf apache-VCL-2.2.1-incubating.tar.bz2
{tip}
1. # Copy the *web* directory to a location under the web root of your web
server and navigate to the&nbsp;destination&nbsp;*.ht-inc* subdirectory:
{tip}
cp \-r apache-VCL-2.2.1-incubating/web/ /var/www/html/vcl
cd /var/www/html/vcl/.ht-inc
{tip}
1. # apply patch to fix editing reservations
{tip}
wget [https://issues.apache.org/jira/secure/attachment/12477101/utils_virtual_undefined.patch](https://issues.apache.org/jira/secure/attachment/12477101/utils_virtual_undefined.patch)
patch < utils_virtual_undefined.patch
{tip}
1. # apply patch to fix processing of block allocations
{tip}
wget [https://issues.apache.org/jira/secure/attachment/12485328/vmhostcheck_fix.patch](https://issues.apache.org/jira/secure/attachment/12485328/vmhostcheck_fix.patch)
patch < vmhostcheck_fix.patch
{tip}
1. # Copy *secrets-default.php* to *secrets.php*:
{tip}
cp secrets-default.php secrets.php
{tip}
1. # Edit the *secrets.php* file:
{tip}
vi secrets.php
{tip}
1. #* Set the following variables to match your database configuration:
1. #** *$vclhost*
1. #** *$vcldb*
1. #** *$vclusername*
1. #** *$vclpassword*
1. #* Create random passwords for the following variables:
1. #** *$mcryptkey*
1. #** *$mcryptiv* (must be 8 hex characters)
1. #** *$pemkey*
1. #* Save the secrets.php file
1. # Run the *genkeys.sh*&nbsp;script.&nbsp; Enter the value you set for
*$pemkey* in secrets.php as the passphrase (3 times, copy/paste is a good
idea)
{tip}
./genkeys.sh
{tip}
1. # Copy *conf-default.php* to *conf.php*:
{tip}
cp conf-default.php conf.php
{tip}
1. # Modify *conf.php* to match your site
{tip}vi conf.php{tip}
{info}Modify every entry under *"Things in this section must be modified"*.
Descriptions and pointers for each value are included within
conf.php.{info}
1. #* *COOKIEDOMAIN* \- set this to the domain name your web server is using
or leave it blank if you are only accessing the web server by its IP
address
1. # Set the owner of the *.ht-inc/maintenance* directory to the web server
user (normally 'apache'):
{tip}chown apache maintenance{tip}
1. # Optionally, you can [install phpseclib and apply a patch](vcl:patch-to-remove-mcrypt-dependency.html)
 to remove the requirement of having mcrypt installed
1. # Open the *testsetup.php* page in a web browser:
1. #* If you set up your site to be [https://my.server.org/vcl/](https://my.server.org/vcl/)
 open [https://my.server.org/vcl/testsetup.php]
1. #* Debug any issues reported by testsetup.php
1. h2. Log In to the VCL Website
1. # Open the index.php page in your browser ([https://my.server.org/vcl/index.php](https://my.server.org/vcl/index.php)
)
1. #* Select *Local Account*
1. #* Username: *admin*
1. #* Password: *adminVc1passw0rd*
1. # Set the admin user password (optional):
1. ## Click *User Preferences*
1. ## Enter the current password: *adminVc1passw0rd*
1. ## Enter a new password
1. ## Click *Submit Changes*
1. h2. Add a Management Node to the Database
1. # Click the *Management Nodes* link
1. ## Click *Add*
1. ## Fill in these&nbsp;required fields:
1. ##* *Hostname -* The name of&nbsp;the management node server. This value
doesn't necessarily need to be&nbsp;a name registered in DNS nor does it
need to be the value displayed by the Linux&nbsp;_hostname_ command. For
example, if you are installing all of the VCL components on the same
machine you can set this value to _localhost_.
{info}Take note of the value you enter for Hostname.&nbsp;In a later step performed during the&nbsp;[management node installation](vcl:vcl-2.2.1-management-node-installation.html)
, the value enter for Hostname must match the value you enter&nbsp;for FQDN
in the /etc/vcl/vcld.conf file on the management node.{info}
1. ##* *IP address* \- the public IP address of the management node
1. ##* *SysAdmin Email Address* \- error emails will be sent to this address
1. ##* *Install Path* \- this is parent directory under which image files
will be stored - only required if doing bare metal installs or using VMWare
with local disks
1. ##* *End Node SSH Identity Key Files* \- enter /etc/vcl/vcl.key unless you
know you are using a different SSH identity key file
1. ## Optionally, fill in these fields:
1. ##* *Address for Shadow Emails* \- End users are sent various emails about
the status of their reservations. If this field is configured, copies of
all of those emails will be sent to this address.
1. ##* *Public NIC configuration method* \- this defaults to Dynamic DHCP -
if DHCP is not available for the public interface of your nodes, you can
set this to Static. Then, the IP configuration on the nodes will be
manually set using Public Netmask, Public Gateway, Public DNS Server, and
the IP address set for the computer under Manage Computers
1. # Click *Confirm Management Node*
1. # Click *Submit*
1. # Click the *Management Nodes* link
1. ## Select *Edit Management Node Grouping*
1. ## Click *Submit*
1. ## Select the checkbox for your management node
1. ## Click *Submit Changes*

[Further steps if using only VMWare](vcl-2.2.1---further-steps-if-using-vmware.html)





[Further steps if using xCAT](vcl-2.2.1---further-steps-if-using-xcat.html)






<a name="VCL2.2.1WebCodeInstallation-*Adding&nbsp;LocalVCLAccounts*"></a>
## *Adding&nbsp;Local VCL Accounts*

Local VCL accounts are&nbsp;contained within the VCL database.&nbsp; The
*admin* account&nbsp;is a local VCL account.&nbsp; Additional local
accounts can be added via the backend management node code. After you have
finished the backend management node installation, run:
{tip}
vcld \-setup
{tip}
1. Select *VCL Base Module*
1. Select *Add Local VCL User Account*
1. Enter the requested information

<a name="VCL2.2.1WebCodeInstallation-AddingLDAPAuthentication"></a>
## Adding LDAP Authentication

Follow the instruction on the&nbsp;[Adding LDAP Authentication](vcl-2.2.1---adding-ldap-authentication.html)
 page.

  
  
----
Previous Step: [VCL:VCL 2.2.1 Database Installation](vcl:vcl-2.2.1-database-installation.html)
Next Step: [VCL:VCL 2.2.1 Management Node Installation](vcl:vcl-2.2.1-management-node-installation.html)
