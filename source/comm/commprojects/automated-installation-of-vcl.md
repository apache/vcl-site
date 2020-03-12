---
title: Automated Installation of VCL
---

I developed a set of scripts to automate the installation of VCL for my own
purposes. I used the scripts in an advanced Linux class I taught at NCA&T
as an example of scripting. Several student teams installed VCL on their
individual servers, and the installation had to be repeated after the
students experimented with the setup. The script made installation
relatively quick and always consistent. The installation is basically one
click.

The starting point of the installation is a configured Scientific Linux 6.2
operating system. This installation also uses scripting and a custom local
repository I developed. The installation is either PXE or iPXE based. The
student's starting point is an _ether-wake_ command to the target server,
and installation is automatic from that point on. My home repository
contains a database of configuration data for various computers of friends
at several different geographical locations who use my repository to
perform automated installation and configuration of LAMP servers, directory
servers, repository servers, Plandora, Moodle, and so forth. I mirrored my
home site at NC A&T, and added customization for some NC A&T hosts.

Each student team adds their customization data, for example, host name,
partitioning information, and application customization data. Each team
also makes an entry in the local dnsmasq TFTP/DNS/DHCP configuration.
These one-time tasks are completed early in the semester during the study
of enterprise configuration. This background is of interest only because my
VCL scripts assume certain things, such as, the web directory roots for all
named virtual hosts are in **/var/www/web_servers/** and configuration
snippets are in **/etc/httpd/virtual_hosts/**.

Once the LAMP server is loaded, a team member opens Firefox and downloads
**vcl_pre_commands_nn.sh** from the repo web server. The “nn” is
anything, but usually a “1”, or a “2”, and forth, to access a
unique parameters file for each unique VCL installation. If you look in the
pre_commands script, you will notice the number is just used to append to
the filename **vcl_parameters_nn.sh**. In the scripts below, I used "13",
since the particular target host name was "burton-research-13". Before
starting installation, the students make a one-time instance of both the
vcl_pre_commands file and the vcl_parameters file customized for their
team. That is, each team could represent a different institution seeking to
create a VCL cloud. If you look in these files, you will see the only real
task is to set the host name of the target server to agree with the DHCP
hostname assignment. Of course, you can vary every parameter, but since
this is a student lab, all teams used my default settings for digital
certificates and so forth. If you use the scripts for your own institution,
you will wish to change additional settings to reflect your institution's
name and login credentials. The parameters.sh file is -- at least to me
-- documented and straightforward. I kept the students confined to a
private LAN without outside access, so **we used weak
passwords**. Please, use a strong password for any system with access
from the Internet. Once the pre-commands file is downloaded, the students
make the file executable, the run the script. About 30 minutes later, VCL
installation is complete. Packages are installed using _yum_ (see
**vcl_packages.sh**), and all source tarballs are downloaded directly from
the VCL site. The main script, **install_vcl.sh**, incorporates several
modifications to the current VCL installation instructions. Notable areas
are sourcing the MySQL database structure, dynamically modifying the VCL
perl script to remove Linux package installation and perl interaction, use
of SL 6.2, and rearranging the order of installation to complete all
package installation in one place. The use of explicit yum package
installation will allow me to copy **vcl_packages.sh** almost directly into
RPM requires statements. I did not use an RPM for my students because I
wanted the students to explore and experiment with the scripts.

## So what is a “complete” VCL installation?

In this case, it means everything required to install and configure the VCL
web front end and the VCL management node is completed automatically. The
script automatically launches Firefox to the VCL web interface and lists
the few steps that must be completed through the web interface (admin
password, initial specification of management node).

What is not done (at this time) is the automated installation of VMware
ESXi on the service nodes, nor the installation and configuration of XCAT.
I expect I will just automate the XCAT installation and configuration, and
let XCAT take care of the service node installation and management, since
this will provide an arbitrarily large cloud. For my class, we just
installed VMware ESXi manually on a service node.

Images can be&nbsp; copied manually, of course, but in my scheme of
infrastructure, booting a bare metal image with a PXE boot to my repository
automatically builds Linux images. I expect XCAT can be persuaded to do the
same.

## How could these scripts help the VCL project?

I mentioned the automated installation in a poster session at the first ICA-CON 
conference hosted by IBM in April, 2012 ([ICA-CON](http://www.ibm.com/solutions/education/cloudacademy/us/en/cloud_academy_conference.html)). Several people expressed an interest in access to the scripts, and I
agreed to post the scripts in support of the Apache VCL project. I suppose
with a few tweaks the script could be embedded in a no-arch RPM (or at
least a self-determining arch) so that those who are interested in using
VCL, but might not have the skills or patience to wade through the
installation, could go immediately to their own VCL cloud with a click or
two. This could lower the barrier to entry of cloud computing, and let more
folks get on with exploring new ways to actually **use** a vcl cloud.

## The scripts follow:

### vcl_pre_commands_13.sh

```bash
 # Make sure time is correct, otherwise certificates will fail
ntpd -gq
service ntpd start
cd /root
wget http://linuxlab.ncat.edu/inet_boot/install_vcl.sh
chmod +x install_vcl.sh
./install_vcl.sh "http://linuxlab.ncat.edu/inet_boot" "13"
```

### vcl_parameters_13.sh

```bash
# + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + +
# + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + +
# + +                                                                      
# + +                                                                      
# + + Filename:     vcl_parameters.sh
# + + Author:       Larry Burton
# + + Copyright:    Copyright 2012 Larry Burton All rights reserved.
# + + Revision:     20120324
# + + Description:                                                        
# + + A script to define paramters used to install Apache VCL
# + + Usage:        sourced in other files
# + +                                                  
# + +                                                                     
# + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + +
# + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + +
#
this_host="burton-research-13"
this_domain="ncat.edu"
#  + + + + + + + + VCL Installation paramters + + + + + + + + + + + +
#
# Logging file
export log_file="/tmp/vcllog.log"
# Logging device
export logging="| tee $log_file"
# Location of the VCL source tarball
export source_url="http://www.apache.org/dist/incubator/vcl"
# VCL version
export vcl_version="2.2.1-incubating"
# tarball directory
export vcl_source_directory="/opt/vcl"
# The FQDN of the VCL Management Node (Must have valid DNS entry)
export vcl_management_node_name="$this_host.$this_domain"
# The FQDN of the VCL Management Node (Must have valid DNS entry)
export vcl_FQDN="$this_host.$this_domain"
#
# The architecture of this machine (for Perl download)
export arch='i386'
#
#
#  + + + + + + + + MySQL parameters + + + + + + + + + + + +
#
# The MySQL root password
export mysql_password='useyourownpassword'
# VCL database user name
export vcl_mysql_user_name="vcluser"
# VCL database user password
export vcl_mysql_user_password="vcluserpassword"
# VCL database name
export vcl_database_name="vcl"
# $mcryptkey
export vcl_mcryptkey="alongpassword"
#vcl_pemkey
export vcl_pemkey="alongkey"
# FQDN of database server (Must have valid DNS entry)
export vcl_database_server_name="$this_host.$this_domain"
#LockerWrtUser
export vcl_lockerwrite_user="vcluser"
# LockerWrtUser password
export vcl_lockerwrite_user_password="vcluserpassword"
# MySQL server name (The name used to connect, which must match the
# MySQL database username. Typically, localhost unless you explicitly
# allow external connections to the database.
export vcl_mysql_server_name="localhost"
#
#  + + + + + + + + HTTP parameters + + + + + + + + + + + +
#
export host_name="$this_host.$this_domain"
export search_path="$this_domain"
export web_virtual_hosts_directory='/etc/httpd/virtual_hosts'
export web_content_base='/var/www/web_servers'
# The VCL document root for the web server
export vcl_web_document_root="$web_content_base/$host_name"
#
#  + + + + + + + + CA Certificate Parameters + + + + + + + + + + + +
#
export ca_passphrase="password"
#
export ca_starting_serial_number="100"
export ca_country="US"
export ca_state='NorthCarolina'
export ca_city="Greensboro"
export ca_org="LinuxLab"
export ca_ou="VirtualComputingLab"
export ca_common_name="$this_host.$this_domain"
export ca_email="super@ncat.edu"
# File to contain the self-signed CA certificate (which contains the public key)
export ca_certificate_file_name="$ca_common_name.cer"
# File to contain the unencrypted, base-64 encoded, private key
export ca_certificate_private_unencrypted_key_file_name="$ca_common_name.key"
# The directory in which to copy the digital certificates
export ca_path_to_local_certs_files="/etc/pki/tls/certs"
# The directory in which to copy the unencrypted private certificate key
export ca_path_to_local_key_files="/etc/pki/tls/private"
#
#  + + + + + + + + xmlrpc Parameters + + + + + + + + + + + +
#
# The VCL daemon uses xmlrpc (remote procedure call) to connect to the
# MySQL database for doing things such as creating block reservations.
# A user must exist in the vcl MySQL database with privileges suitable for
# acccomplishing the database queries. You may use the MySQL GRANT command
# to create a distinct user, or you may use the default vcl user.
export vcl_xmlrpc_username=$vcl_mysql_user_name
export vcl_xmlrpc_pass=$vcl_mysql_user_password
```

## https_setup.sh

```bash
#!/bin/bash
#
# + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + +
# + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + +
# + +                                                                      
# + +                                                                      
# + + Filename:     https_setup.sh
# + + Author:       Larry Burton
# + + Copyright:    Copyright 2012 Larry Burton All rights reserved.
# + + Revision:     20120324
# + + Description:                                                        
# + + A script to configure httpd for https
# + + Usage:        https_setup.sh
# + +               Must be run as root                                    
# + +                                                                     
# + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + +
# + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + +
#
#  + + + + + + + + HTTP parameters + + + + + + + + + + + +
#

# Note: This script assumes httpd is already setup with Larry Burton's LAMP
#       RPMs. This means the virtual_hosts directory and the web_servers
#       directories are in place and the http access on port 80 is already
#       in place.
#
#       This script forces ALL HTTP access to rewrite to HTTPS. If you wish to
#       keep some HTTP access, you will have to edit the reqrite section to
#       only rewrite selected locations, eg /location, rather than /.
#
#
#  + + + + + + + + Add the https rewrite directives + + + + + + + + + + + +
#
# ************ check for existence of cert files ***********************
# The line with CustomLog appears in Larry Burton's default HTTP access.
# Add the new location to httpd virtual host
#
sed -i -e '/CustomLog/a\ \n\
 \
# \ 
<Location "/"> \
# Set the content to ALLOW Indexex to be displayed and to FOLLOW \
# symbolic links \
Options FollowSymLinks Indexes \
# \
# \
RewriteEngine On \
# This will enable the Rewrite capabilities \
# \
RewriteCond %{HTTPS} !=on \
# This checks to make sure the connection is not already HTTPS \
# \
RewriteRule (.*) https://%{HTTP_HOST}%{REQUEST_URI} \
# \
# This takes http request and changes hhtp to https \
# \
# \
</Location> \
 \
' $web_virtual_hosts_directory/$host_name.conf
#
#
#
#  + + + + + + + + Add the https access directives + + + + + + + + + + + +
#
# The </VirtualHost> tag will be the last line of some HTTP virtual host,
# so we may insert the https virtual host immediately afterwards.
# Note the escaping of the forward slash.
#
sed -i -e '/<\/VirtualHost>/a\ \n\
 \
# \
# Make sure httpd listens to port 443 \
# \
NameVirtualHost *:443 \
# \
# Add an HTTPS virtual host \
# \
<VirtualHost *:443> \
 \
DirectoryIndex home.php \
 \
 \
 \
 \
     ServerAdmin webmaster@'"$host_name"' \
     DocumentRoot '"$web_content_base/$host_name"' \
 \
     ServerName '"$host_name"' \
     ErrorLog logs/'"$host_name"'-error_log \
     CustomLog logs/'"$host_name"'-access_log common \
 \
        SSLEngine on \
        SSLCertificateFile '"$ca_path_to_local_certs_files/$ca_certificate_file_name"' \
        SSLCertificateKeyFile '"$ca_path_to_local_key_files/$ca_certificate_private_unencrypted_key_file_name"' \
 \
        <Directory /'"$web_content_base/$host_name"'> \
        AllowOverride All \
        </Directory> \
  \
 \
<Location \/> \
Options FollowSymLinks Indexes \
</Location> \
# \
</VirtualHost> \
# This ends an HTTPS virtual host definition. \
# \
 \
' $web_virtual_hosts_directory/$host_name.conf
#
#
#  + + + + + + + + Restart -- not reload -- the httpd server + + + + + + + + +
#
# Retart the web server daemon:
/etc/init.d/httpd restart
#
# End of script
```

## vcl_packages.sh

I placed the installation of required packages in a separate file to ease
the transition of the script into an RPM.

```bash
#
# + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + +
# + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + +
# + +                                                                      
# + +                                                                      
# + + Filename:     vcl_packages.sh
# + + Author:       Larry Burton
# + + Copyright:    Copyright 2012 Larry Burton All rights reserved.
# + + Revision:     20120324
# + + Description:                                                        
# + + A script to define paramters used to install packages used by Apache VCL
# + + Usage:        sourced in other files
# + +                                                  
# + +                                                                     
# + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + +
# + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + +
#
#  + + + + + + + + VCL Installation paramters + + + + + + + + + + + +
#
/bin/echo "Installing packages used by VCL" $logging
/bin/echo "" $logging
/bin/echo "Some of these packages may already be installed, but we" $logging
/bin/echo "check them anyway to see if they need updating." $logging
/bin/echo "" $logging
#
# Install these packages
#
/bin/echo "httpd - Apache HTTP Server" $logging
yum -y install httpd
#
#
/bin/echo "mod_ssl - SSL/TLS module for the Apache HTTP server" $logging
yum -y install mod_ssl
#
#
/bin/echo "php - The PHP HTML-embedded scripting language" $logging
yum -y install php
#
#
/bin/echo "We will not use libmcrypt - Encryption algorithms library" $logging
#yum -y install libmcrypt
#
# Required PHP Modules:
#
/bin/echo "" $logging
/bin/echo "We need the following PHP modules." $logging
/bin/echo "" $logging
#
/bin/echo "php-gd" $logging
yum -y install php-gd
#
#
/bin/echo "php-json (required if your PHP version is 5.2 or later)" $logging
yum -y install php-json
#
#
/bin/echo "We will not use php-mcrypt" $logging
#yum -y install php-mcrypt
#
#
/bin/echo "php-mysql" $logging
yum -y install php-mysql
#
#
/bin/echo "php-openssl" $logging
yum -y install php-openssl
#
#
/bin/echo "php-sysvsem" $logging
yum -y install php-sysvsem
#
#
/bin/echo "php-xml" $logging
yum -y install php-xml
#
#
/bin/echo "php-xmlrpc" $logging
yum -y install php-xmlrpc
#
#
/bin/echo "php-ldap" $logging
yum -y install php-ldap
#
#
# Management Node packages
#Required Linux Packages:

# The VCL management node daemon (vcld) requires the following Linux packages and 
# Perl modules in order to run (see step 2 below for installation instructions):

#
/bin/echo "expat - A library for parsing XML" $logging
yum -y install expat
#
/bin/echo "expat-devel - Libraries and include files to develop XML applications with expat" $logging
yum -y install expat-devel
#
/bin/echo "gcc - Various compilers C, C++, Objective-C, Java, ..." $logging
yum -y install gcc
#
/bin/echo "krb5-libs - The shared libraries used by Kerberos 5" $logging
yum -y install krb5-libs
#
/bin/echo "krb5-devel - Development files needed to compile Kerberos 5 programs" $logging
yum -y install krb5-devel
#
/bin/echo "libxml2 - Library providing XML and HTML support" $logging
yum -y install libxml2
#
/bin/echo "libxml2-devel - Libraries, includes, etc. to develop XML and HTML applications" $logging
yum -y install libxml2-devel
#
/bin/echo "mysql - MySQL client programs and shared libraries" $logging
yum -y install mysql
#
/bin/echo "nmap - Network exploration tool and security scanner" $logging
yum -y install nmap
#
/bin/echo "openssh - The OpenSSH implementation of SSH protocol versions 1 and 2" $logging
yum -y install openssh
#
/bin/echo "openssl - The OpenSSL toolkit" $logging
yum -y install openssl
#
/bin/echo "openssl-devel - Files for development of applications which will use OpenSSL" $logging
yum -y install openssl-devel
#
/bin/echo "perl - The Perl programming language" $logging
yum -y install perl
#
/bin/echo "perl-DBD-MySQL - A MySQL interface for perl" $logging
yum -y install perl-DBD-MySQL
#
#          ------------------------- /bin/echo "xmlsec1-openssl - OpenSSL crypto plugin for XML Security Library" $logging
#          ------------------------- yum -y install xmlsec1-openssl
#
#
#
if [ $arch == "i386" ]
then
perlarch="i686"
else
perlarch="x86_64"
fi
/bin/echo "Perl Architecture for download is $perlarch" $logging
wget ftp://rpmfind.net/linux/epel/beta/6/$arch/xmlsec1-1.2.16-2.el6.$perlarch.rpm
yum -y install xmlsec1-1.2.16-2.el6.$perlarch.rpm
#
#
#wget ftp://rpmfind.net/linux/epel/beta/6/x86_64/xmlsec1-1.2.16-2.el6.x86_64.rpm
#yum -y install xmlsec1-1.2.16-2.el6.x86_64.rpm
#
#wget http://rpmfind.net/linux/epel/beta/6/i386/xmlsec1-1.2.16-2.el6.i686.rpm
#yum -y install xmlsec1-1.2.16-2.el6.i686.rpm
```

## create_a_new_self_signed_certificate.sh

```bash
#!/bin/bash
#
# + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + +
# + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + +
# + +
# + +                                                                      
# + + Filename:     create_new_self-signed_ca.sh
# + + Author:       Larry Burton
# + + Copyright:    Copyright 2012 Larry Burton All rights reserved.
# + + Revision:     20120324
# + + Description:                                                        
# + + A script to create a new self-signed digital certificate
# + + Usage:        create_new_self-signed_ca.sh
# + +                                  
# + +                                                                     
# + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + +
# + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + +
#
#
# This script will create a new self-signed Certificate Authority (CA)
# digital certificate. The CA certificate can be posted on a web server for
# the public to download in order to verify digital certificates signed by
# this CA certificate.
#
# When creating the CA, we will NOT ENCRYPT the private key because we wish
# to store the unencrypted private key on a server for access by software
# such as httpd. If we encrypted the private key, we would have to type in the
# passphrase every time the software needed to use the key. The "-nodes"
# option specifies no encryption.

# Prepare subject text
# If you have a problem
ca_subj=/C=$ca_country/ST=$ca_state/O=$ca_org/localityName=$ca_city/commonName=$ca_common_name/organizationalUnitName=$ca_ou/emailAddress=$ca_email
#
echo "The subject text is:"
echo "$ca_subj"
#
# Create the self-signed certificate
#    PEM format is default, but specify it to make sure we do not have DER format
openssl req -x509 \
    -nodes \
    -keyform PEM \
    -inform PEM \
    -outform PEM \
    -days 3650 \
    -newkey rsa:2048 \
    -set_serial $ca_starting_serial_number \
    -batch \
    -subj "$ca_subj" \
    -keyout $ca_certificate_private_unencrypted_key_file_name \
    -out $ca_certificate_file_name \
    -passin pass:$ca_passphrase
#
# Self-signed certificate is complete
/bin/echo "Here is the unencrypted private key stored in $ca_certificate_private_unencrypted_key_file_name:"
cat $ca_certificate_private_unencrypted_key_file_name
/bin/echo "Here is the self-signed Certificate Authority certificate stored in $ca_certificate_file_name:"
cat $ca_certificate_file_name
#
/bin/echo "Here is the information contained in the self-signed CA certificate:"
openssl x509 -text -in $ca_certificate_file_name
#
#  + + + + + + + + Copy Cert and Key to local directory + + + + + + + + + + + +
#
mkdir -p $ca_path_to_local_certs_files
mkdir -p $ca_path_to_local_key_files
cp $ca_certificate_file_name $ca_path_to_local_certs_files/$ca_certificate_file_name
cp $ca_certificate_private_unencrypted_key_file_name $ca_path_to_local_key_files/$ca_certificate_private_unencrypted_key_file_name
#
/bin/echo "The CA certificate has been copied to $ca_path_to_local_certs_files"
/bin/echo "The CA unecrypted private key has been copied to $ca_path_to_local_key_files"
# end of script
```

## install_vcl.sh

```bash
#!/bin/bash
#
# + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + +
# + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + +
# + +                                                                      
# + +                                                                      
# + + Filename:     install_vcl.sh
# + + Author:       Larry Burton
# + + Copyright:    Copyright 2012 Larry Burton All rights reserved.
# + + Revision:     20120324
# + + Description:                                                        
# + + A script to install Apache VCL on a LAMP server
# + + Usage:        install_vcl.sh repo_url host
# + + Example:      install_vcl.sh "http://linuxlab.ncat.edu/inet_boot" "1"
# + +               Must be run as root    
# + +               The second paraeter is appended to the parameters filename
# + +                  to allow multiple different VCL installations to use the same script
# + +               The target server, which is the computer upon which this
# + +               script is executing, must have:
# + +                  Internet access and must
# + +                  A valid forward and reverse DNS entry
# + +                  Access to a valid DS server
# + +                  Access to a valid DHCP server                                  
# + +                                                                     
# + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + +
# + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + +
#
repo_url=$1
target_host=$2
#
mkdir -p /tmp/install
#
# Get installation parameters
wget --no-host-directories --output-document="/tmp/install/vcl_parameters" $repo_url/vcl_parameters_$target_host.sh
#
# All the host paramters are now in /tmp/install/host_parameters
#
# Source the customization variables
. /tmp/install/vcl_parameters
/bin/echo "Following are the VCL installation parameters" $logging
cat /tmp/install/vcl_parameters
#
#
# Use yum to install the necessary repository packages
wget --no-host-directories --output-document="/tmp/install/vcl_packages" $repo_url/vcl_packages.sh
. /tmp/install/vcl_packages
#
#  + + + + + + + + Start the VCL Installation + + + + + + + + + + + +
#
# The starting point is an installed and hardened LAMP server created by
# Larry Burton's RPMs
#
# Create the VCL source code directory
/bin/echo "Creating VCL source code directory as $vcl_source_directory" $logging
mkdir -p $vcl_source_directory
# Change the working directory to the source code directory
/bin/echo "Changing working directory to source code directory" $logging
pushd $vcl_source_directory
# Download & Extract the Apache VCL Source
/bin/echo "Downloading the VCL source tarball from $source_url" $logging
wget $source_url/apache-VCL-$vcl_version.tar.bz2
# Extract the files
/bin/echo "Extracting the VCL source tarball" $logging
tar -jxvf apache-VCL-2.2.1-incubating.tar.bz2
#
# Configure MySQL for VCL (MySQL is already installed and configured by LAMP)
#
# Make sure the firewall on the database server is configured to allow
# traffic from the web server and management node servers to connect to
# the MySQL daemon TCP port: 3306.  See the firewall documentation for
# more information.
#
# Create a VCL database
/bin/echo "Creating VCL database" $logging

#mysql --user=root --password=$mysql_password -e 'DROP DATABASE vcl;'
mysql --user=root --password=$mysql_password -e 'CREATE DATABASE vcl; USE vcl; source apache-VCL-2.2.1-incubating/mysql/vcl.sql; SHOW TABLES;'

mysql --user=root --password=$mysql_password -e "GRANT SELECT,INSERT,UPDATE,DELETE,CREATE TEMPORARY TABLES ON vcl.* TO '$vcl_mysql_user_name'@'localhost' IDENTIFIED BY '$vcl_mysql_user_password';"

mysql --user=root --password=$mysql_password -e "USE mysql; SELECT * FROM user WHERE User='vcluser';"

# Create the VCL user for the MySQL database
# Note this user is created with access from the localhost only since the
# database server is assumed to be on the same physical machine as the vcl daemon

/bin/echo "These are the tables in the VCL database:" $logging
mysql --user=root --password=$mysql_password -e "USE vcl;SHOW TABLES;"
#
# At this point, VCL support in MySQL is complete
/bin/echo "" $logging
#
/bin/echo "MySQL configuration for VCL complete" $logging
/bin/echo "" $logging
#
#  NOTE ----------- Change http.conf document root to correct document root
sed -i -e "s:DocumentRoot \"/var/www/html\":DocumentRoot \"$web_content_base/$vcl_FQDN\":g" /etc/httpd/conf/httpd.conf
#
#  + + + + + + + + Set up Apache httpd for https + + + + + + + + + + + +
#
/bin/echo "Creating digital certificates for web server" $logging
# Download and run the https configuration script
wget --no-host-directories --output-document="/tmp/install/create_new_self-signed_ca.sh" $repo_url/create_new_self-signed_ca.sh
sh /tmp/install/create_new_self-signed_ca.sh

#
# Note: The certificates must be in place before trying to start https
#
/bin/echo "Beginning httpd configuration for VCL" $logging
# Download and run the https configuration script
wget --no-host-directories --output-document="/tmp/install/https_setup.sh" $repo_url/https_setup.sh
sh /tmp/install/https_setup.sh
#
# At this point, VCL support in httpd is complete
/bin/echo "" $logging
/bin/echo "httpd configuration for VCL complete" $logging
/bin/echo "" $logging
#

#4. If SELinux is enabled, run the following command to allow the web server to connect to the database:
#/usr/sbin/setsebool -P httpd_can_network_connect=1
#5. If the iptables firewall is being used, port 80 and 443 should be opened up:
#vi /etc/sysconfig/iptables
#
#-A RH-Firewall-1-INPUT -m state --state NEW -p tcp --dport 80 -j ACCEPT
#-A RH-Firewall-1-INPUT -m state --state NEW -p tcp --dport 443 -j ACCEPT
#service iptables restart
#
#
#
#  + + + + + + + + Install the VCL Frontend Web Code + + + + + + + + + + + +
#
#
/bin/echo "Beginning VCL Frontend Web Code Installation" $logging
#
# Copy the web directory to a location under the web root of your web server
# and navigate to the destination .ht-inc subdirectory
# Create the VCL web server document root directory
mkdir -p $vcl_web_document_root
# Copy the VCL web documents to the VCL web server document root
cp -r apache-VCL-$vcl_version/web/ $vcl_web_document_root/vcl
# Change the working directory to the web server document root patch file directory
pushd $vcl_web_document_root/vcl/.ht-inc
# Apply patch to fix editing reservations
wget https://issues.apache.org/jira/secure/attachment/12477101/utils_virtual_undefined.patch
patch < utils_virtual_undefined.patch
# Apply patch to fix processing of block allocations
wget https://issues.apache.org/jira/secure/attachment/12485328/vmhostcheck_fix.patch
patch < vmhostcheck_fix.patch
#
# Configure the PHP secrets file
#

# Copy secrets-default.php to secrets.php:
cp secrets-default.php secrets.php
# Edit the secrets.php file
/bin/echo "Editing the PHP secrets.php file" $logging
# Set the VCL hostname
####### default is ok sed -i -e "s/\$vclhost = 'localhost'; # name of mysql server/###\$vclhost = 'localhost'; # name of mysql server/g" \
####### default is ok        -e "/\$vclhost = 'localhost'; # name of mysql server/a\ \n\
####### default is ok ####### default is ok \$vclhost = '$host_name'; # name of mysql server/
####### default is ok  \
####### default is ok " \
####### default is ok secrets.php
#
# Set the VCL database name
####### default is ok sed -i -e "s/\$vcldb = 'vcl';         # name of mysql database/###\$vcldb = 'vcl';         # name of mysql database/g" \
####### default is ok        -e "/\$vcldb = 'vcl';         # name of mysql database/a\ \n\
####### default is ok \$vcldb = '$vcl_database_name';         # name of mysql database/
####### default is ok  \
####### default is ok " \
####### default is ok secrets.php
#
# Set the VCL user name
sed -i -e "s/\$vclusername = '';      # username to access database/###\$vclusername = '';      # username to access database/g" \
       -e "/\$vclusername = '';      # username to access database/a\ \n\
\$vclusername = '$vcl_mysql_user_name';      # username to access database/
 \
" \
secrets.php
#
# Set the VCL password
sed -i -e "s/\$vclpassword = '';      # password to access database/###\$vclpassword = '';      # password to access database/g" \
       -e "/\$vclpassword = '';      # password to access database/a\ \n\
\$vclpassword = '$vcl_mysql_user_password';      # password to access database/
 \
" \
secrets.php
#
# Set the VCL password
sed -i -e "s/\$mcryptkey = '';  # random password - won't ever have to type it so make it long/###\$mcryptkey = '';  # random password - won't ever have to type it so make it long/g" \
       -e "/\$mcryptkey = '';  # random password - won't ever have to type it so make it long/a\ \n\
\$mcryptkey = '$vcl_mcryptkey';  # random password - won't ever have to type it so make it long/
 \
" \
secrets.php
#
# $mcryptiv = '12345678'; // must be 8 hex chars
#
# Set the VCL passphrase
sed -i -e "s/\$pemkey = ''; # random passphrase - same as given to genkeys.sh - should be long/###\$pemkey = ''; # random passphrase - same as given to genkeys.sh - should be long/g" \
       -e "/\$pemkey = ''; # random passphrase - same as given to genkeys.sh - should be long/a\ \n\
\$pemkey = '$vcl_pemkey'; # random passphrase - same as given to genkeys.sh - should be long/
 \
" \
secrets.php
#

#
#  + + Create the public and private keys for the vcl user + + + + + + + + +
#
/bin/echo "Creating the public and private keys for the vcl user" $logging
# The 2048 MUST come after the passphrase

echo "openssl genrsa -aes256 -out keys.pem -passout pass:$vcl_pemkey 2048"
openssl genrsa -aes256 -out keys.pem -passout pass:$vcl_pemkey 2048
echo "openssl rsa -pubout -in keys.pem -out pubkey.pem -passin pass:$vcl_pemkey"
openssl rsa -pubout -in keys.pem -out pubkey.pem -passin pass:$vcl_pemkey
#
#
#
#  + + Configure the PHP conf.php + + + + + + + + +
#
/bin/echo "Configuring the PHP conf.php" $logging
#

# Copy conf-default.php to conf.php:
cp conf-default.php conf.php
#
# Modify conf.php to match your site
# Basically this consists of specifying the FQDN and domain name of the server.
# NOTE: use = as delimiter instead of slash to avoid escaping slashes
sed -i -e "s:define(\"COOKIEDOMAIN\", \".example.org\");       // domain in which cookies are set:define(\"COOKIEDOMAIN\", \"$vcl_FQDN\");       // domain in which cookies are set:g" conf.php
sed -i -e "s=define(\"BASEURL\", \"https:\/\/vcl.example.org\");=define(\"BASEURL\", \"https:\/\/$vcl_FQDN/vcl\");=g" conf.php
sed -i -e "s=define(\"HOMEURL\", \"http:\/\/vcl.example.org\/\");=define(\"HOMEURL\", \"http:\/\/$vcl_FQDN\/vcl\/\");=g" conf.php
sed -i -e "s=vcl.example.org=$vcl_FQDN=g" conf.php
sed -i -e "s=example.org=$search_path=g" conf.php
# Did not set timezone
#
#  
#
#
# Set the owner of the .ht-inc/maintenance directory to the web server user (normally 'apache'):
chown apache maintenance
#
#
#
#  + + Install phpseclib and apply a patch to remove the requirement of having mcrypt installed + + + + + + + + +
#
# Optionally, you can install phpseclib and apply a patch to remove the requirement of having mcrypt installed
/bin/echo "Patching to remove the mcrypt dependency" $logging
#Here are the steps to remove the dependency:
#Download phpseclib to /tmp (version 0.2.2 was used for testing)
pushd /tmp
wget http://downloads.sourceforge.net/project/phpseclib/phpseclib0.2.2.zip
#Create a directory named phpseclib in your .ht-inc directory
mkdir $vcl_web_document_root/vcl/.ht-inc/phpseclib
#unzip phpseclib in the phpseclib directory
pushd $vcl_web_document_root/vcl/.ht-inc/phpseclib
unzip /tmp/phpseclib0.2.2.zip
#Download no_mcrypt.patch to your .ht-inc directory
pushd $vcl_web_document_root/vcl/.ht-inc
wget http://people.apache.org/~jfthomps/no_mcrypt.patch
#Apply the patch
patch < no_mcrypt.patch
#
/bin/echo "The VCL web server is now set up" $logging
#
#
#
# Test the webserver
# Open the testsetup.php page in a web browser
firefox https://$host_name/vcl/testsetup.php &

# ---------------------------- Must manually use web interface to setup management node !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# Right now, before completing remaining steps
# It is easier to just let the script run, then use the web interface, and then restart vcld

pushd $vcl_web_document_root/vcl/.ht-inc


#
# At this point, the VCL webserver is configured
#
#
#
#
#  + + Install the Management Node + + + + + + + + +
#
/bin/echo "Installing VCL Management Node" $logging
popd
popd
popd
cd
# Change the working directory to the source code directory
/bin/echo "Changing working directory to source code directory" $logging
pushd $vcl_source_directory
#
cp -r apache-VCL-2.2.1-incubating/managementnode /usr/local/vcl
#
/bin/echo "Installing perl modules" $logging
# Skip the Linux package installation in the perl script and say YES
sed -i -e "s=install_linux_packages();=###install_linux_packages()=g" /usr/local/vcl/bin/install_perl_libs.pl
sed -i -e "s:my \$input = <>;:my \$input = 'YES';:g" /usr/local/vcl/bin/install_perl_libs.pl
#sed -i -e "s=my @ERRORS;=###my @ERRORS;=g" /usr/local/vcl/bin/install_perl_libs.pl


# Now install the perl modules
perl /usr/local/vcl/bin/install_perl_libs.pl
#
#  + + Configure vcld.conf + + + + + + + + +
#
/bin/echo "Configuring /etc/vcld.conf" $logging
#Create the */etc/vcl* directory:
mkdir /etc/vcl
#Copy the stock *vcld.conf* file to */etc/vcl*:
cp /usr/local/vcl/etc/vcl/vcld.conf /etc/vcl
#Edit */etc/vcl/vcld.conf*:
#
vcl_conf_file="/etc/vcl/vcld.conf"
#
echo $vcl_management_node_name
# You can use any delimiter you like in an address by prepending a \ i.e. \|...| for the substitute command the \ is not necessary.
#
# Set the FQDN for the management server (vcld)
sed -i -e "s/FQDN=/###FQDN=/g" \
       -e "/###FQDN=/a \
FQDN=$vcl_management_node_name
 \
" \
$vcl_conf_file
#
#
# Set the MySQL database name for the management server (vcld)
sed -i -e "s/database=vcl/###database=vcl/g" \
       -e "/##database=vcl/a \
database=$vcl_database_name
 \
" \
$vcl_conf_file
#
# Set the MySQL database name for the management server (vcld)
sed -i -e "s/server=/###server=/g" \
       -e "/###server=/a \
server=$vcl_mysql_server_name
 \
" \
$vcl_conf_file
#
# Set the MySQL database name for the management server (vcld)
sed -i -e "s/LockerWrtUser=vcl-wr/###LockerWrtUser=vcl-wr/g" \
       -e "/###LockerWrtUser=vcl-wr/a \
LockerWrtUser=$vcl_mysql_user_name
 \
" \
$vcl_conf_file
#
# Set the MySQL database name for the management server (vcld)
sed -i -e "s/wrtPass=/###wrtPass=/g" \
       -e "/###wrtPass=/a \
wrtPass=$vcl_mysql_user_password
 \
" \
$vcl_conf_file
#
#
# Set the MySQL database name for the management server (vcld)
sed -i -e "s/xmlrpc_username=vclsystem/###xmlrpc_username=vclsystem/g" \
       -e "/###xmlrpc_username=vclsystem/a \
xmlrpc_username=$vcl_mysql_user_name
 \
" \
$vcl_conf_file
#
# Set the MySQL database name for the management server (vcld)
sed -i -e "s/xmlrpc_pass=insecureDefault/###xmlrpc_pass=insecureDefault/g" \
       -e "/###xmlrpc_pass=insecureDefault/a \
xmlrpc_pass=$vcl_mysql_user_password
 \
" \
$vcl_conf_file
#
#
# Set the MySQL database name for the management server (vcld)
sed -i -e "s/xmlrpc_url=/###xmlrpc_url=/g" \
       -e "/###xmlrpc_url=/a \
xmlrpc_url=https:\/\/$vcl_management_node_name\/vcl\/index.php\?mode=xmlrpccall
 \
" \
$vcl_conf_file
#
#
#  + + Configure the SSH Client + + + + + + + + +
#
/bin/echo "Configuring SSH Client" $logging
#
# Locate the UserKnownHostsFile and StrictHostKeyChecking lines and change them to the following:
# Note: These lines may not exist, so just comment them out if they do exist
#       and add the new lines at the end of the file.
sed -i -e "s/UserKnownHostsFile/###UserKnownHostsFile/g" \
       -e "$ a\ \n\
UserKnownHostsFile \/dev\/null
 \
" \
/etc/ssh/ssh_config
#
sed -i -e "s/StrictHostKeyChecking/###StrictHostKeyChecking/g" \
       -e "$ a\ \n\
StrictHostKeyChecking no
 \
" \
/etc/ssh/ssh_config
#
#
#  + + Install and Start the VCL Daemon (vcld) Service + + + + + + + + +
#
/bin/echo "Install and Start the VCL Daemon (vcld) Service" $logging
#
# Copy the vcld service script to /etc/init.d and name it vcld:
cp /usr/local/vcl/bin/S99vcld.linux /etc/init.d/vcld
# Add the vcld service using chkconfig:
/sbin/chkconfig --add vcld
# Configure the vcld service to automatically run at runtime levels 3-5:
/sbin/chkconfig --level 345 vcld on
# Start the vcld service:
/sbin/service vcld start
#
#       You should see output similar to the following:
#
#       Starting vcld daemon:
#       ============================================================================
#       VCL Management Node Daemon (vcld) | 2011-03-15 10:23:04
#       ============================================================================
#       bin path:      /usr/local/vcl/bin
#       config file:   /etc/vcl/vcld.conf
#       log file:      /var/log/vcld.log
#       pid file:      /var/run/vcld.pid
#       daemon mode:   1
#       setup mode:    0
#       verbose mode:  1
#       ============================================================================
#       Created VCL daemon process: 8465
#                                                                  [  OK  ]
#
# The vcld service can also be started by running the service script directly: /etc/init.d/vcld start
# Check the vcld service by monitoring the vcld.log file:
tail -f /var/log/vcld.log
#
# You should see the following being added to the log file every few seconds if
# the management node is checking in with the database:
#
#       2009-06-16 16:57:15|15792|vcld:main(165)|lastcheckin time updated for management node 18: 2009-06-16 16:57:15
#

# Print instructions for web setup
#
cat << WEBSETUP

+ + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + +
+ +  
+ +                       VCL Web Set Up Instructions
+ +
+ + All VCL installation is now complete except for a few administrative tasks
+ + you must complete using the VCL web-based administration tools.
+ +
+ + Please use a web browser to complete the following steps.
+ + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + +

Step 1: Log In to the VCL Website with the following URL

        https://$vcl_FQDN/vcl/index.php

        Then select "Local Account"
        The username is:    admin
        The password is:    adminVc1passw0rd

        (Note: You may change the password at this time, but be certain to
               REMEMBER your new password!)

Step 2: Click the Management Nodes link

        Click Add
        Fill in these required fields:
# Owner - admin@Local
             Hostname = $vcl_FQDN
             IP address = $(hostname -i)
             SysAdmin Email Address = sysadmin@$search_path
             Install Path = /var/data
             End Node SSH Identity Key Files = /etc/vcl/vcl.key

        Click Confirm Management Node
        Click Submit

Step 3: Click the Management Nodes link
             ( Note: You must click the anagement Nodes link to get out of
                     of the previous screen state.)
        Select Edit Management Node Grouping
        Click Submit
        Select the checkbox for your management node
        Click Submit Changes

Congratualations! You VCL head node installation is complete!

Now, restart the vcld daemon with the following command:

/sbin/service vcld restart

You may monitor vlcd with this command

tail -f /var/log/vcld.log


WEBSETUP

#
#
#  + + Install and Start the DHCP Service + + + + + + + + +
# Note: We use dnsmasq rather than dhcpd
#
exit
#
# End of script
```

Larry Burton 3 May 2012