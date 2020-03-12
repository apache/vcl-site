---
title: VCL 2.2.1 Management Node Installation
---

{excerpt:hidden=true}
How to install and configure the VCL management node components including
the required Linux packages, Perl modules, VCL daemon (vcld), and Windows
utility dependencies{excerpt}

<a name="VCL2.2.1ManagementNodeInstallation-Install&ConfiguretheManagementNodeComponents"></a>
# Install & Configure the Management Node Components

<a name="VCL2.2.1ManagementNodeInstallation-Prerequisites"></a>
### Prerequisites

The following management node installation instructions assume the
instructions on the following pages have previously been completed:
* [VCL:VCL 2.2.1 Database Installation](vcl:vcl-2.2.1-database-installation.html)
* [VCL:VCL 2.2.1 Web Code Installation](vcl:vcl-2.2.1-web-code-installation.html)

<a name="VCL2.2.1ManagementNodeInstallation-SupportedOperatingSystems:"></a>
##### Supported Operating Systems:

The VCL management node daemon (vcld) has been developed to run on an
operating system based on Red Hat Enterprise Linux (RHEL). It has been
tested on the following:
* Red Hat Enterprise Linux 4.x
* Red Hat Enterprise Linux 5.x
* CentOS 5.x

<a name="VCL2.2.1ManagementNodeInstallation-RequiredLinuxPackages:"></a>
##### Required Linux Packages:

The VCL management node daemon (vcld) requires the following Linux packages
and Perl modules in order to run (see step 2 below for installation
instructions):


* *expat* \- A library for parsing XML
* *expat-devel* \- Libraries and include files to develop XML applications
with expat
* *gcc* \- Various compilers (C, C++, Objective-C, Java, ...)
* *krb5-libs* \- The shared libraries used by Kerberos 5
* *krb5-devel* \- Development files needed to compile Kerberos 5 programs
* *libxml2* \- Library providing XML and HTML support
* *libxml2-devel* \- Libraries, includes, etc. to develop XML and HTML
applications
* *mysql* \- MySQL client programs and shared libraries
* *nmap* \- Network exploration tool and security scanner
* *openssh* \- The OpenSSH implementation of SSH protocol versions 1 and 2
* *openssl* \- The OpenSSL toolkit
* *openssl-devel* \- Files for development of applications which will use
OpenSSL
* *perl* \- The Perl programming language
* *perl-DBD-MySQL* \- A MySQL interface for perl
* *xmlsec1-openssl* \- OpenSSL crypto plugin for XML Security Library

<a name="VCL2.2.1ManagementNodeInstallation-RequiredPerlModules:"></a>
##### Required Perl Modules:

The VCL management node daemon (vcld) is written in Perl and has been
tested on Perl 5.8.x. The following Perl modules available from [CPAN ](http://www.cpan.org)
are also required (see step 2 below for installation instructions):
* *DBI* \- Generic Database Interface
* *Digest::SHA1* \- NIST SHA message digest algorithm
* *Mail::Mailer* \- Simple mail agent interface
* *Object::InsideOut* \- Comprehensive inside-out object support
* *RPC::XML* \- A set of classes for core data, message and XML handling
* *YAML* \- YAML Ain't Markup Language

1. h2. Install the VCL Management Node Code - Perl Daemon
1. # If you have not already done so, download and extract the VCL source
files to the management node:
  
  
tar \-jxvf apache-VCL-2.2.1-incubating.tar.bz2{tip}
1. # Copy the *managementnode* directory to the location where you want it to
reside (typically */usr/local*):
{tip}cp \-r apache-VCL-2.2.1-incubating/managementnode /usr/local/vcl{tip}
1. h2. Install the Required Linux Packages & Perl Modules
*Run the install_perl_libs.pl script:*
{tip}perl /usr/local/vcl/bin/install_perl_libs.pl{tip}
The last line of the install_perl_libs.pl script output should be:

    _Note: The script will hang or terminate if it encounters a problem. If
this occurs, you will need to troubleshoot the problem by looking at the
output._
    \\
    \\
    _Note:_ RPC::XML may not install correctly on CentOS 5.6. The CPAN install
of RPC::XML fails because RPC::XML needs 'XML::LibXML' for it's 'self
tests' - even though - it's _NOT_ configured as a dependency, and the 'self
tests' are suppose to skip tests involving 'XML::LibXML' if it's not
installed. You may need to install the module manually before running the
'install_perl_libs.pl' script.
    (i.e. cpan -i XML::LibXML )
    \\
    \\
    The install_perl_libs.pl script included in the VCL distribution will
attempt to download and install the required Linux packages and Perl
modules. It uses the yum utility to install the required Linux packages.
The required Perl modules are available from [CPAN - The Comprehensive Perl Archive Network|http://www.cpan.org]
. The install_perl_libs.pl script attempts to download and install the
required Perl modules by using the CPAN.pm module which is included with
most Perl distributions.
    \\
    \\
    The yum utility should exist on any modern Red Hat-based Linux distribution
(Red Hat, CentOS, Fedora, etc). If yum isn't available on your management
node OS, you will need to download and install the required Linux packages
manually or by using another package management utility. After installing
the required Linux packages, attempt to run the install_perl_libs.pl script
again.
    # h2. Configure vcld.conf
    ## Create the \*/etc/vcl\* directory: {tip}mkdir /etc/vcl{tip}
    ## Copy the stock \*vcld.conf\* file to \*/etc/vcl*: {tip}cp
/usr/local/vcl/etc/vcl/vcld.conf /etc/vcl{tip}
    ## Edit \*/etc/vcl/vcld.conf*:
    {tip}vi /etc/vcl/vcld.conf{tip}
    The following lines must be configured in order to start the VCL daemon
(vcld) and allow it to check in to the database:
    ##* *FQDN* \- the fully qualified name of the management node, this should
match the name that was configured for the management node in the database
    ##* *server* \- the IP address or FQDN of the database server
    ##* *LockerWrtUser* \- database user account with write privileges
    ##* *wrtPass* \- database user password
    ## Save the vcld.conf file
    # h2. Configure the SSH Client
    The SSH client on the management node should be configured to prevent SSH
processes spawned by the root user to the computers it controls from
hanging because of missing or different entries in the known_hosts file.
    \\
    \\
    Edit the ssh_config file: {tip}vi /etc/ssh/ssh_config{tip}
    Locate the *UserKnownHostsFile* and *StrictHostKeyChecking* lines and
change them to the following:

StrictHostKeyChecking no{noformat}
_Note: If you do not want these settings applied universally on the
management node the SSH configuration can also be configured to only apply
these settings to certain hosts or only for the root user. Consult the SSH
documentation for more information._
1. h2. Install and Start the VCL Daemon (vcld) Service
1. # Copy the vcld service script to /etc/init.d and name it vcld:
{tip}
cp /usr/local/vcl/bin/S99vcld.linux /etc/init.d/vcld
{tip}
1. # Add the vcld service using chkconfig:
{tip}
/sbin/chkconfig \--add vcld
{tip}
1. # Configure the vcld service to automatically run at runtime levels 3-5:
{tip}
/sbin/chkconfig \--level 345 vcld on
{tip}
1. # Start the vcld service:
{tip}
/sbin/service vcld start
{tip}
You should see output similar to the following:

    ============================================================================
    VCL Management Node Daemon (vcld) | 2011-03-15 10:23:04
    ============================================================================
    bin path:����� /usr/local/vcl/bin
    config file:�� /etc/vcl/vcld.conf
    log file:����� /var/log/vcld.log
    pid file:����� /var/run/vcld.pid
    daemon mode:�� 1
    setup mode:��� 0
    verbose mode:� 1
    ============================================================================
    Created VCL daemon process: 8465
    ���������������������������������������������������������� [� OK� ]
{noformat}
    {info}
    The vcld service can also be started by running the service script
directly: */etc/init.d/vcld start{*}{info}
    ## Check the vcld service by monitoring the vcld.log file: {tip}tail \-f
/var/log/vcld.log{tip}
    You should see the following being added to the log file every few seconds
if the management node is checking in with the database:

1. h2. Install & Configure the DHCP Service
1. # Install *dhcp* if it is not already installed:
{tip}
yum install dhcp \-y
{tip}
1. # The DHCP daemon should only listen on the virtual private network (eth0)
to avoid conflicts with other networks. Configure the dhcpd service startup
script to only listen on the private interface:
{tip}
vi /etc/sysconfig/dhcpd
{tip}
Add *eth0* the to the *DHCPDARGS* line:

    # Command line options here
    DHCPDARGS=eth0

1. # Configure the dhcpd service to automatically start at runlevels 3-5:
{tip}
/sbin/chkconfig \--level 345 dhcpd on
{tip}
1. # Configure the dhcpd.conf file.
{tip}
vi /etc/dhcpd.conf
{tip}
{info}Configure your dhcpd.conf file according to your network
configuration. The contents of the dhcpd.conf file will vary based on how
your network is configured. Below is an example of a basic dhcpd.conf
file:{info}

    ddns-update-style none;
    	 shared-network eth0 {
    	subnet 10.100.0.0 netmask 255.255.255.0 {
    		ignore unknown-clients;
    	  }
    }

You will add host definitions to the dhcpd.conf file after you add
computers to VCL using the website. The website will display the dhcpd.conf
host definitions after the computers have been added to VCL, which can be
copied and pasted into the dhcpd.conf file.
1. # Start the dhcpd service:
{tip}/sbin/service dhcpd start{tip}
1. h2. Configure Windows Product Keys and/or KMS Server Addresses (Optional)
If you will be deploying Windows environments your institution's Windows
product key and/or KMS server addresses must be entered into the VCL
database. This can be done by running the following command:
{tip}/usr/local/vcl/bin/vcld \-setup{tip}
Select "*Windows OS Module*" and follow the prompts.
1. h2. Download Windows Sysprep Utility (Optional)
If you will be using VCL to deploy bare-metal Windows XP or Windows Server
2003 environments via xCAT, the appropriate versions of the Microsoft
Sysprep utility must be downloaded to the management node. The following
steps do not need to be completed if you only intend to deploy VMware
virtual machines.
  
  
  
  
The Sysprep utility is included in the Deployment Tools available for free
from Microsoft. You do not need to download Sysprep for Windows 7 or
Windows Server 2008 because it is included in the operating system.
  
  
  
  
The Sysprep files need to be downloaded, extracted, and then copied to the
management node. The format of the file available for download is
Microsoft's .cab format. It is easiest to extract the files on a Windows
computer. Windows Explorer is able to open the .cab file and then the files
contained within can be copied elsewhere.
  
  
  
  
1. # Windows XP
1. ## Download Sysprep for Windows XP: [Windows XP Service Pack 3 Deployment Tools](http://www.microsoft.com/downloads/details.aspx?FamilyID=673a1019-8e3e-4be0-ac31-70dd21b5afa7&displaylang=en)
1. ## Extract the Windows XP Sysprep Files
1. ## Copy the extracted Windows XP Sysprep files to the following directory
the management node:
{noformat}/usr/local/vcl/tools/Windows_XP/Utilities/Sysprep{noformat}
1. # Windows Server 2003
1. ## Download Sysprep for Windows Server 2003: [System Preparation tool for Windows Server 2003 Service Pack 2 Deployment](http://www.microsoft.com/downloads/details.aspx?familyid=93F20BB1-97AA-4356-8B43-9584B7E72556&displaylang=en)
1. ## Extract the Windows Server 2003 Sysprep Files
1. ## Copy the extracted Windows Server 2003 Sysprep files to the following
directory the management node:
{noformat}/usr/local/vcl/tools/Windows_Server_2003/Utilities/Sysprep{noformat}
1. h2. Download Windows Drivers (Optional)
Drivers which aren't included with Windows must be downloaded and saved to
the management node. The drivers required will vary greatly depending on
the hardware. The only way to know what additional drivers you need is to
install Windows on a computer and check for missing drivers.
  
  
  
  
The drivers must be copied to the appropriate directory on the management
node. The VCL image capture process copies the driver directories to the
computer before an image is captured. Drivers from multiple directories
will be copied based on the version of Windows being captured. There are
driver directories under *tools* for each version of Windows (Windows XP,
Windows 7) and for each version group of Windows (version 5, 6). This
allows drivers which are common to multiple versions of Windows to be
shared in the management node tools directory structure.
  
  
Examples:
  
  
  
  
If a chipset driver works for all versions of Windows it should be saved
in:
*/var/lib/vcl/tools/Windows/Drivers/Chipset*
  
  
  
  
If Windows XP and Windows Server 2003 both use the same network driver it
can be saved in:
*/var/lib/vcl/tools/Windows_Version_5/Drivers/Network*
  
  
  
  
If a storage driver only works for Windows XP it should be saved in:
*/var/lib/vcl/tools/Windows_XP/Drivers/Storage*
  
  
  
  
During the image capture process, each Windows version directory is copied
to the computer under C:\Cygwin\home\root\VCL. The order in which the
Windows version directories are copied goes from most general to most
specific. In the example above, the order would be:
*/var/lib/vcl/tools/Windows/\**
*/var/lib/vcl/tools/Windows_Version_5/\**
*/var/lib/vcl/tools/Windows_XP/\**
  
  
  
  
The following list shows which driver files should be saved in the driver
directories:
*/var/lib/vcl/tools/Windows/Drivers* \- drivers common to all versions of
Windows
*/var/lib/vcl/tools/Windows_Version_5/Drivers* \- drivers used by Windows
XP and Server 2003
*/var/lib/vcl/tools/Windows_XP/Drivers* \- drivers only used by Windows XP
*/var/lib/vcl/tools/Windows_Server_2003/Drivers* \- drivers only used by
Windows Server 2003
  
  
*/var/lib/vcl/tools/Windows_Version_6/Drivers* \- drivers used by Windows
Vista and Server 2008
*/var/lib/vcl/tools/Windows_7/Drivers* \- drivers only used by Windows 7
*/var/lib/vcl/tools/Windows_Server_2008/Drivers* \- drivers only used by
Windows Server 2008

The directory structure under each Drivers directory does not matter. It is
helpful to organize each directory by driver class, and each directory
should be organized using the same theme. For example:
*/var/lib/vcl/tools/Windows_Version_XP/Drivers{*}*/Chipset*
*/var/lib/vcl/tools/Windows_Version_XP/Drivers{*}*/Network*
*/var/lib/vcl/tools/Windows_Version_XP/Drivers{*}*/Storage*
*/var/lib/vcl/tools/Windows_Version_XP/Drivers{*}*/Video*
1. h2. Install & Configure Provisioning Engines and Hypervisors
VCL supports the following, please see the related websites for
installation and configuration instructions:
1. # xCAT - Extreme Cluster Administration Toolkit
1. #* Versions Supported:
1. #** 1.3
1. #** 2.x
1. #* See the xCAT website for installation & configuration information: [http://xcat.sourceforge.net](http://xcat.sourceforge.net)
1. # VMware
1. ## See the VMware website for installation & configuration information: [http://www.vmware.com](http://www.vmware.com)
1. ## See the following pages for additional VCL VMware configuration
information:
1. ### [VCL 2.2.1 - Further steps if using only VMware](vcl-2.2.1---further-steps-if-using-vmware.html)
1. ### [VCL:VMware Configuration](vcl:vmware-configuration.html)
