---
title: Configuring a Standalone VCL Environment using VMware Server 2.0
---

<a name="ConfiguringaStandaloneVCLEnvironmentusingVMwareServer2.0-{color:#ff0000}DISCLAIMER\!{color}"></a>
## {color:#ff0000}DISCLAIMER\!{color}

This document provides instuctions for configuring a standalone VCL
environment running on a single computer which is able to provision VCL
reservations using VMware. It is only provided to help you understand how
the various components of VCL operate. This document *DOES NOT* describe
how to configure a production VCL environment. The environment described in
this document can however be used to learn, test, and help develop VCL.

<a name="ConfiguringaStandaloneVCLEnvironmentusingVMwareServer2.0-GatherRequiredFiles&Information"></a>
## Gather Required Files & Information

<a name="ConfiguringaStandaloneVCLEnvironmentusingVMwareServer2.0-Requirements"></a>
### Requirements

* *VMware Server 2.x RPM Installer* \- These instructions assume the VMware
Server RPM has been downloaded to the following location on the management
node:
/root/VMware-server-2.0.2-203138.x86_64.rpm
* *VMware Server 2.x serial number* \- A serial number can be obtained when
you download VMware Server 2.0 from vmware.com.&nbsp;You will need to
register.

<a name="ConfiguringaStandaloneVCLEnvironmentusingVMwareServer2.0-Assumptions"></a>
### Assumptions

* These instructions assume you are logged in to the management node as
*root*
* These instructions assume you&nbsp;are using a *bash* shell.

<a name="ConfiguringaStandaloneVCLEnvironmentusingVMwareServer2.0-Networking"></a>
### Networking

The&nbsp;computer used to host the standalone VCL
environment&nbsp;described in these instructions only needs a single
network interface.&nbsp;These instructions will also work if it has
multiple interfaces. The&nbsp;computer used to create these instructions
had the following interfaces:
* *eth0* \- connected to the private VCL network (not used or referenced in
these instructions)
* *eth1* \- connected to the public network

<a name="ConfiguringaStandaloneVCLEnvironmentusingVMwareServer2.0-VMwareServer2.0Configuration"></a>
## VMware Server 2.0 Configuration

<a name="ConfiguringaStandaloneVCLEnvironmentusingVMwareServer2.0-RemoveExistingVirtualizationComponents"></a>
#### Remove Existing Virtualization Components

{tip}
yum groupremove "Virtualization" \-y
{tip}

<a name="ConfiguringaStandaloneVCLEnvironmentusingVMwareServer2.0-MakeSureTheHostComputerIsNotRunningAXenKernel"></a>
#### Make Sure The Host Computer Is Not Running A Xen Kernel

VMWare Server cannot be installed on a computer running a Xen kernel. To
determine if a Xen kernel is being used:
{tip}
uname \-a
{tip}

The following output indicates a Xen kernel is being used:
{panel}
Linux blade1g6-4 2.6.18-92.el5{color:#cc0000}{*}xen{*}{color} \#1 SMP Tue
Jun 10 19:20:18 EDT 2008 x86_64 x86_64 x86_64 GNU/Linux
{panel}
If "xen" appears in the output of the previous command, replace the Xen
kernel:
{tip}
yum update ecryptfs-utils \-y
yum install kernel kernel-devel \-y
yum remove xen kernel-xen \-y
{tip}

Check the grub.conf file to make sure it is not configured to boot using
the Xen Kernel
{tip}
less /boot/grub/grub.conf
{tip}

The grub.conf file should {color:#cc0000}{*}NOT{*}{color} look like this:
{panel}
title CentOS (2.6.18-92.el5{color:#cc0000}{*}xen{*}{color})
module /vmlinuz-2.6.18-92.el5{color:#cc0000}{*}xen{*}{color} ro
root=LABEL=/ pci=nommconf
{panel}

After removing the Xen kernel, reboot the computer:
{tip}
reboot
{tip}

<a name="ConfiguringaStandaloneVCLEnvironmentusingVMwareServer2.0-DownloadVMwareServer2.0"></a>
#### Download VMware Server 2.0

Download the latest VMware Server 2.0 RPM from [http://www.vmware.com](http://www.vmware.com)
{info}
These instructions assume you saved the RPM into */root*
{info}

<a name="ConfiguringaStandaloneVCLEnvironmentusingVMwareServer2.0-InstallVMwareServer2.0"></a>
#### Install VMware Server 2.0
{tip}
rpm \-ivh /root/VMware-server-2.0.2-203138.x86_64.rpm
{tip}Configure VMware Server:
{tip}
vmware-config.pl
{tip}Answer the questions asked by *vmware-config.pl* as follows:
* Do you accept? (yes/no) *yes*
* Do you want networking for your virtual machines? (yes/no/help) *yes*
** Configuring a bridged network for vmnet0. Please specify a name for this
network. *Bridged*
** Your computer has multiple ethernet network interfaces available: eth0,
eth1. Which one do you want to bridge to vmnet0?
{color:#ff0000}{*}eth1{*}{color} {color:#000000}*(this should be set to the
public interface)*{color}
The following bridged networks have been defined:
. vmnet0 is bridged to eth1
** Do you wish to configure another bridged network? (yes/no) *no*
** Do you want to be able to use NAT networking in your virtual machines?
(yes/no) *no*
** Do you want to be able to use host-only networking in your virtual
machines? {color:#ff0000}{*}yes{*}{color}
** Configuring a host-only network for vmnet1. Please specify a name for
this network. {color:#ff0000}{*}HostOnly{*}{color}
** Do you want this program to probe for an unused private subnet?
(yes/no/help)&nbsp;{color:#ff0000}{*}no{*}{color}
** What will be the IP address of your host on the private network?
{color:#ff0000}{*}192.168.0.1{*}{color}
** What will be the netmask of your private network?
{color:#ff0000}{*}255.255.0.0{*}{color}
The following host-only networks have been defined:
. vmnet1 is a host-only network on private subnet 192.168.0.0.
** Do you wish to configure another host-only network? (yes/no) *no*
* Please specify a port for remote connections to use: *902*
* Please specify a port for standard http connections to use: *8222*
* Please specify a port for secure http (https) connections to use: *8333*
* The current administrative user for VMware Server&nbsp; is ''.&nbsp;
Would you like to specify a different administrator? *no*
Using root as the VMware Server administrator.
* In which directory do you want to keep your virtual machine files?
*/var/lib/vmware/Virtual Machines*
* The path "/var/lib/vmware/Virtual Machines" does not exist currently.
This program is going to create it, including needed parent directories. Is
this what you want? *yes*
* Please enter your 20-character serial number. *<Enter the serial number
you received from VMware>*
* In which directory do you want to install the VMware VIX API binary
files? */usr/bin*
* In which directory do you want to install the VMware VIX API library
files? */usr/lib/vmware-vix/lib*
* The path "/usr/lib/vmware-vix/lib" does not exist currently. This program
is going to create it, including needed parent directories. Is this what
you want? *yes*
* In which directory do you want to install the VMware VIX API document
pages? */usr/share/doc/vmware-vix*
* The path "/usr/share/doc/vmware-vix" does not exist currently. This
program is going to create it, including needed parent directories. Is this
what you want? *yes*

{info}
If you receive an error message when you execute
*vmware-config.pl*&nbsp;you may need to install or update the following
libraries and then run *vmware-config.pl* again:

{tip}
yum install glibc-devel \-y
yum install glibc \-y
yum install libXtst-devel \-y
{tip}
{info}
Verify the host-only network was configured correctly:
{tip}
/sbin/ifconfig
{tip}You should see a *vmnet1* interface using IP address *192.168.0.1*:
{panel}
*vmnet1* Link encap:Ethernet HWaddr 00:50:56:C0:00:01
inet addr:*192.168.0.1* Bcast:192.168.255.255 Mask:255.255.0.0
inet6 addr: fe80::250:56ff:fec0:1/64 Scope:Link
UP BROADCAST RUNNING MULTICAST MTU:1500 Metric:1
RX packets:0 errors:0 dropped:0 overruns:0 frame:0
TX packets:4 errors:0 dropped:0 overruns:0 carrier:0
collisions:0 txqueuelen:1000
RX bytes:0 (0.0 b) TX bytes:0 (0.0 b)
{panel}Restart the vmware service:

{tip}/sbin/service vmware restart
{tip}

You should see the following:
{panel}
Starting VMware services:
Virtual machine monitor \[{color:#339966}OK{color} \]({color:#339966}ok{color}-\.html)
Virtual ethernet \[{color:#339966}OK{color} \]({color:#339966}ok{color}-\.html)
Bridged networking on /dev/vmnet0 \[{color:#339966}OK{color} \]({color:#339966}ok{color}-\.html)
Host-only networking on /dev/vmnet1 (background) \[{color:#339966}OK{color} \]({color:#339966}ok{color}-\.html)
Starting VMware virtual machines... \[{color:#339966}OK{color} \]({color:#339966}ok{color}-\.html)
{panel}

<a name="ConfiguringaStandaloneVCLEnvironmentusingVMwareServer2.0-FixVMwareServer2.0glibcProblem"></a>
#### Fix VMware Server 2.0 glibc Problem

VMware Server 2.0 will not run reliably if the version of glibc installed
on the host is newer than *2.5-34*. This problem is known to affect recent
versions of Red Hat Enterprise Linux and CentOS. If not corrected, VMware
Server will crash intermittently and the VMware administration web pages
will lock up or fail to load.

Check the version of *glib* installed on the VMware host:

{tip}
yum list installed glibc
{tip}

You will need to configure VMware to use *glibc 2.5-34* if the version
installed on the host is newer than *2.5-34*:


    Installed Packages
    glibc.i686	 2.5-42      installed
    glibc.x86_64	 2.5-42      installed


For CentOS, you will need to download the glibc RPM included with CentOS
5.3. This is available from vault.centos.org:
* For 32-bit CentOS installations: [http://vault.centos.org/5.3/updates/i386/RPMS/glibc-2.5-34.el5_3.1.i686.rpm](http://vault.centos.org/5.3/updates/i386/RPMS/glibc-2.5-34.el5_3.1.i686.rpm)
* For 64-bit CentOS installations: [http://vault.centos.org/5.3/updates/x86_64/RPMS/glibc-2.5-34.el5_3.1.x86_64.rpm](http://vault.centos.org/5.3/updates/x86_64/RPMS/glibc-2.5-34.el5_3.1.x86_64.rpm)

Create a temp directory and cd to it:
{tip}
mkdir /tmp/glibc ; cd /tmp/glibc
{tip}

Download the glibc RPM (change the URL accordingly):
{tip}
wget [http://vault.centos.org/5.3/updates/x86_64/RPMS/glibc-2.5-34.el5_3.1.x86_64.rpm](http://vault.centos.org/5.3/updates/x86_64/RPMS/glibc-2.5-34.el5_3.1.x86_64.rpm)
{tip}

Extract the cpio archive from the glibc RPM:
{tip}
rpm2cpio glibc-2.5-34.el5_3.1.x86_64.rpm \| cpio \--extract
\--make-directories
{tip}

Create the following directory:
{tip}
mkdir /usr/lib/vmware/lib/libc.so.6
{tip}

Copy the&nbsp;following file to&nbsp;the new directory:
{tip}
cp /tmp/glibc/lib64/libc-2.5.so /usr/lib/vmware/lib/libc.so.6/libc.so.6
{tip}

Make a backup of the original vmware-hostd file:
{tip}
cp /usr/sbin/vmware-hostd /root/vmware-hostd.orig
{tip}

Edit vmware-hostd:
{tip}
vi /usr/sbin/vmware-hostd
{tip}

Navigate to the bottom of the file. You should see the following as the
last line:

    eval exec "$DEBUG_CMD" "$binary" "$@"


Add the following *export* line immediately before the last *eval* line in
vmware-hostd:

    export LD_LIBRARY_PATH=/usr/lib/vmware/lib/libc.so.6:$LD_LIBRARY_PATH
    eval exec "$DEBUG_CMD" "$binary" "$@"


The following sed command can also be used to add the line to vmware-hostd:
{tip}
{note}
Do not both manually edit *vmware-hostd* and run the following *sed*
command
{note}
sed \-i \-r \-e "s/(eval exec.*)/export
LD_LIBRARY_PATH=\/usr\/lib\/vmware\/lib\/libc.so.6:\$LD_LIBRARY_PATH\n\1/"
/usr/sbin/vmware-hostd
{tip}

Restart the *vmware* service:
{tip}
/sbin/service vmware restart
{tip}

<a name="ConfiguringaStandaloneVCLEnvironmentusingVMwareServer2.0-LogintoVMware"></a>
#### Login to VMware

At this point you should be able to log in as *root* to the VMware
Infrastructure Web Access page:
\*{nolink:https://<IP address or hostname>:8333}\*

<a name="ConfiguringaStandaloneVCLEnvironmentusingVMwareServer2.0-InstallVCLComponents"></a>
## Install VCL Components

Begin by completing the&nbsp;VCL installation&nbsp;instructions. Install
all of the components on the same computer:
1. [VCL:VCL 2.2.1 Database Installation](vcl:vcl-2.2.1-database-installation.html)
1. [VCL:VCL 2.2.1 Web Code Installation](vcl:vcl-2.2.1-web-code-installation.html)
{note}Complete the Web Code Installation&nbsp;steps up to the&nbsp;*Add a
Management Node to the Database* section. Use the instructions below to add
the management node, VM host computer, and VM computers to the VCL
database.{note}
1. [VCL:VCL 2.2.1 Management Node Installation](vcl:vcl-2.2.1-management-node-installation.html)

<a name="ConfiguringaStandaloneVCLEnvironmentusingVMwareServer2.0-Add&nbsp;theManagementNodetotheDatabase"></a>
#### Add&nbsp;the Management Node to the Database

* Click *Management Nodes* > *Edit Management Node Information*
* Click *Add*
** Hostname: *localhost*
** IP Address: *127.0.0.1*
** Owner: *admin@Local*
** State: *available*
** Predictive Loading Module: *Predictive Loading Level 0 Module*
** Check-in Interval: *5*
** Install Path: */install*
** End Node SSH Identitiy Key Files: */etc/vcl/vcl.key*
** SSH Port for this node: *22*
** Enable Image Library: *no*
* Click *Confirm Management Node*

<a name="ConfiguringaStandaloneVCLEnvironmentusingVMwareServer2.0-AddtheVMwareHostComputertotheVCLdatabase"></a>
#### Add the VMware Host Computer to the VCL database

* Click *Manage Computers* > *Add Single Computer* > *Submit*
** Hosthame: *localvmhost*
** IP Address: *192.168.0.1*
** State: *vmhostinuse*
Owner: *admin*
** Platform: *i386*
** Schedule: *VCL 24x7*
** RAM: *1024*
** No Processors: *1*
** Processor Speed: *2000*
** Network Speed: *1000*
** Type: *blade*
** Provisioning engine: *xCAT 2.x*
{info}The computer Type and Provisioning engine values don't matter for the
localvmhost computer in this test environment because vcld isn't
provisioning or reloading&nbsp;it{info}
** Computer Groups: *allComputers*
* Click *Confirm Computer*
* Click *Submit*
* Select a VM Host Profile to be used on this computer: *VMware Server 2.x
- local storage*
* Click *Add Computer*

<a name="ConfiguringaStandaloneVCLEnvironmentusingVMwareServer2.0-AddtheVirtualMachineComputerstotheVCLDatabase"></a>
#### Add the Virtual Machine Computers to the VCL Database

* Click *Manage Computers* > *Edit Computer Information* > *Submit*
* Click the *Add Multiple* checkbox
* Click *Add*
** Hosthame: *vmguest-%*
** Start value: *1*
** End value: *10*
** Start IP Address: *192.168.1.1*
** End IP Address: *192.168.1.10*
** Start private IP Address: *192.168.1.1*
** End private IP Address: *192.168.1.10*
** Start MAC Address: *00:50:56:1a:01:01*
** State: *maintenance*
** Owner: *admin*
** Platform: *i386*
** Schedule: *VCL 24x7*
** RAM: *4096*
** No Processors: *1*
** Processor Speed: *2000*
** Network Speed: *1000*
** Type: *virtualmachine*
** Provisioning engine: *VMware*
** Computer Groups:
*** *All VM Computers*
*** *allComputers*
*** *newvmimages*
* Click *Confirm Compute*
* Click *Submit*
* Enter the private address for the management node: *127.0.0.1*
* Click: *Download Data*, you should automatically generated dhcpd.conf
file entries. Keep this web page open and continue with the following
instructions.

<a name="ConfiguringaStandaloneVCLEnvironmentusingVMwareServer2.0-Install&ConfiguretheDHCPService"></a>
## Install & Configure the DHCP Service

VMware Server installs its own DHCP service (*vmnet-dhcpd*). This service
starts automatically when the vmware service is running. Either the VMware
*vmnet-dhcpd* service or the normal *dhcpd* service installed on the Linux
operating system can be used to assign IP addresses to the VMs' private
interfaces. The instructions below explain how to disable vmnet-dhcpd and
configure dhcpd.

<a name="ConfiguringaStandaloneVCLEnvironmentusingVMwareServer2.0-Disablevmnet-dhcpd"></a>
#### Disable vmnet-dhcpd

Stop the *vmware* service:
{tip}
/sbin/service vmware stop
{tip}

Edit the following file:
{tip}
/etc/vmware/locations
{tip}

Find all lines beginning with *answer VNET_1_DHCP yes* and change *yes* to
*no*:
{panel}
answer VNET_1_DHCP *no*
{panel}

Start the *vmware* service:
{tip}
/sbin/service vmware start
{tip}

<a name="ConfiguringaStandaloneVCLEnvironmentusingVMwareServer2.0-InstalltheDHCPService"></a>
#### Install the DHCP Service

Install *dhcp* if it is not already installed:
{tip}
yum install dhcp \-y
{tip}

The DHCP daemon should only listen on the virtual private network (vmnet1)
to avoid conflicts with other networks. Configure the dhcpd service startup
script to only listen on the vmnet1 interface:
{tip}
vi /etc/sysconfig/dhcpd
{tip}

Add *vmnet1* the to the *DHCPDARGS* line:

    # Command line options here
    DHCPDARGS=vmnet1


Configure the dhcpd service to automatically start at runlevels 3-5:
{tip}
/sbin/chkconfig \--level 345 dhcpd on
{tip}Start the dhcpd service:
{tip}
/sbin/service dhcpd start
{tip}

<a name="ConfiguringaStandaloneVCLEnvironmentusingVMwareServer2.0-Configuredhcpd.conf"></a>
#### Configure dhcpd.conf

* Edit the */etc/dhcpd.conf* file on the computer:
{tip}
vi /etc/dhcpd.conf
{tip}
* Paste the following into the *dhcpd.conf* file and save the file:
{info}The host sections below should be identical the the output displayed
on the VCL website after you added the VM computers.{info}

    ddns-update-style none; shared-network vmnet1 {
    	subnet 192.168.0.0 netmask 255.255.0.0 {
    		ignore unknown-clients;
    		option routers 192.168.0.1;
    		host vmguest-1 {
    			option host-name "vmguest-1";
    			hardware ethernet 00:50:56:1a:01:01;
    			fixed-address 192.168.1.1;
    			filename "/tftpboot/pxelinux.0";
    			option dhcp-server-identifier 127.0.0.1;
    			next-server 127.0.0.1;
    		}
    
    		host vmguest-2 {
    			option host-name "vmguest-2";
    			hardware ethernet 00:50:56:1a:01:03;
    			fixed-address 192.168.1.2;
    			filename "/tftpboot/pxelinux.0";
    			option dhcp-server-identifier 127.0.0.1;
    			next-server 127.0.0.1;
    		}
    
    		host vmguest-3 {
    			option host-name "vmguest-3";
    			hardware ethernet 00:50:56:1a:01:05;
    			fixed-address 192.168.1.3;
    			filename "/tftpboot/pxelinux.0";
    			option dhcp-server-identifier 127.0.0.1;
    			next-server 127.0.0.1;
    		}
    
    		host vmguest-4 {
    			option host-name "vmguest-4";
    			hardware ethernet 00:50:56:1a:01:07;
    			fixed-address 192.168.1.4;
    			filename "/tftpboot/pxelinux.0";
    			option dhcp-server-identifier 127.0.0.1;
    			next-server 127.0.0.1;
    		}
    
    		host vmguest-5 {
    			option host-name "vmguest-5";
    			hardware ethernet 00:50:56:1a:01:09;
    			fixed-address 192.168.1.5;
    			filename "/tftpboot/pxelinux.0";
    			option dhcp-server-identifier 127.0.0.1;
    			next-server 127.0.0.1;
    		}
    
    		host vmguest-6 {
    			option host-name "vmguest-6";
    			hardware ethernet 00:50:56:1a:01:0b;
    			fixed-address 192.168.1.6;
    			filename "/tftpboot/pxelinux.0";
    			option dhcp-server-identifier 127.0.0.1;
    			next-server 127.0.0.1;
    		}
    
    		host vmguest-7 {
    			option host-name "vmguest-7";
    			hardware ethernet 00:50:56:1a:01:0d;
    			fixed-address 192.168.1.7;
    			filename "/tftpboot/pxelinux.0";
    			option dhcp-server-identifier 127.0.0.1;
    			next-server 127.0.0.1;
    		}
    
    		host vmguest-8 {
    			option host-name "vmguest-8";
    			hardware ethernet 00:50:56:1a:01:0f;
    			fixed-address 192.168.1.8;
    			filename "/tftpboot/pxelinux.0";
    			option dhcp-server-identifier 127.0.0.1;
    			next-server 127.0.0.1;
    		}
    
    		host vmguest-9 {
    			option host-name "vmguest-9";
    			hardware ethernet 00:50:56:1a:01:11;
    			fixed-address 192.168.1.9;
    			filename "/tftpboot/pxelinux.0";
    			option dhcp-server-identifier 127.0.0.1;
    			next-server 127.0.0.1;
    		}
    
    		host vmguest-10 {
    			option host-name "vmguest-10";
    			hardware ethernet 00:50:56:1a:01:13;
    			fixed-address 192.168.1.10;
    			filename "/tftpboot/pxelinux.0";
    			option dhcp-server-identifier 127.0.0.1;
    			next-server 127.0.0.1;
    		}

* Restart the dhcpd service:
{tip}/sbin/service dhcpd restart{tip}


<a name="ConfiguringaStandaloneVCLEnvironmentusingVMwareServer2.0-Configure/etc/hosts"></a>
#### Configure /etc/hosts

* Modify the /etc/hosts file to include entries for the VM host and VM
computers:
{tip}
vi /etc/hosts
{tip}
* Add the following entries:
{panel}
192.168.0.1 localvmhost
192.168.1.1 vmguest-1
192.168.1.2 vmguest-2
192.168.1.3 vmguest-3
192.168.1.4 vmguest-4
192.168.1.5 vmguest-5
192.168.1.6 vmguest-6
192.168.1.7 vmguest-7
192.168.1.8 vmguest-8
192.168.1.9 vmguest-9
192.168.1.10 vmguest-10
{panel}

<a name="ConfiguringaStandaloneVCLEnvironmentusingVMwareServer2.0-ConfigurethesshdServicetoListenontheVirtualPrivateNetwork"></a>
## Configure the sshd Service to Listen on the Virtual Private Network

{tip}
vi /etc/ssh/sshd_config
{tip}Add the following line to the end of the file:
{tip}
ListenAddress 192.168.0.1
{tip}Restart the sshd service on the management node:
{tip}
/sbin/service sshd restart
{tip}

<a name="ConfiguringaStandaloneVCLEnvironmentusingVMwareServer2.0-ConfigureTheVMHostToBeAbleToSSHToItself"></a>
## Configure The VM Host To Be Able To SSH To Itself

If you have not already generated an SSH identity key on the management
node to be used to login to the computers the management node controls, run
the following command to generate a new key:

{tip}
mkdir /etc/vcl ; ssh-keygen \-t rsa \-f "/etc/vcl/vcl.key" \-N '' \-b 1024
\-C "VCL root account on $HOSTNAME"&nbsp;
{tip}

Add the VM host's public key to its own authorized_keys file to allow it to
SSH to itself without a password prompt:
{tip}
cat /etc/vcl/vcl.key.pub >> /root/.ssh/authorized_keys
{tip}The following command should execute without having to enter a
password:
{tip}
ssh \-i /etc/vcl/vcl.key localvmhost 'ls /'
{tip}

<a name="ConfiguringaStandaloneVCLEnvironmentusingVMwareServer2.0-ConfiguretheVMHostProfile"></a>
## Configure the VM Host Profile

* *Virtual Hosts* > *VM Host Profiles* tab > *VMware Server 2.x - local
storage* > *Configure Profile*
** Virtual Switch 0: *HostOnly*
** Virtual Switch 1: *Bridged*

<a name="ConfiguringaStandaloneVCLEnvironmentusingVMwareServer2.0-Assign&nbsp;theVM&nbsp;Computers&nbsp;totheVMHost"></a>
## Assign&nbsp;the VM&nbsp;Computers&nbsp;to the VM Host

* *Virtual Hosts* > *VM Hosts* tab
* Select *localvmhost*
* Click *Configure Host*
* Set *VM limit* to *10*
* Select *vmguest-1...vmguest-10* under *Unassigned VMs*
* Click *Add*

<a name="ConfiguringaStandaloneVCLEnvironmentusingVMwareServer2.0-CreateaBaseImage"></a>
## Create a Base Image

Proceed to follow the instructions to create a [Windows ](vcl:create-a-windows-base-image.html)
or [Linux |VCL:Create a Linux Base Image]
base image.
