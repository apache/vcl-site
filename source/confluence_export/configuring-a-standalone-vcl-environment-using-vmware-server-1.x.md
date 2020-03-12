---
title: Configuring a Standalone VCL Environment using VMware Server 1.x
---

<a name="ConfiguringaStandaloneVCLEnvironmentusingVMwareServer1.x-{color:#ff0000}DISCLAIMER\!{color}"></a>
## {color:#ff0000}DISCLAIMER\!{color}

This document provides instuctions for configuring a standalone VCL
environment running on a single computer which is able to provision VCL
reservations using VMware.&nbsp; It is only provided to help you understand
how the various components of VCL operate.&nbsp; This document *DOES NOT*
describe how to configure a production VCL environment.&nbsp; The
environment described in this document can however be used to learn, test,
and help develop VCL.

<a name="ConfiguringaStandaloneVCLEnvironmentusingVMwareServer1.x-InstallVCLComponents"></a>
## Install VCL Components

Begin by completing the installation instructions for the VCL components:

* [Database](database-configuration.html)
* [Web server](web-code-installation.html)
* [Management node](management-node-installation.html)

<a name="ConfiguringaStandaloneVCLEnvironmentusingVMwareServer1.x-GatherRequiredFiles&Information"></a>
## Gather Required Files & Information

You will need the following:
* VMware Server 1.x RPM installation file
* VMWare Server 1.x serial number

The following instructions assume the following locations on the management
node:
* VMWare Server RPM: /install/VMware-server-1.0.8-126538.i386.rpm

These instructions assume you have root access and are using a bash shell:
{panel}
sudo bash
{panel}

<a name="ConfiguringaStandaloneVCLEnvironmentusingVMwareServer1.x-Configure&nbsp;theVCLDatabasefortheVMGuestandHost&nbsp;"></a>
## Configure&nbsp;the VCL Database for the VM Guest and Host&nbsp;

* Create the following computer groups:
Go to Manage Groups \-> Resource Groups \-> Add
** all vm host computers
** all vm guest computers

* Map all computer groups to management node group
** Management Nodes \-> Edit Management Node Mapping

* Configure the management node to check in&nbsp;with the database
** Management Nodes \-> Edit Management Node Information \-> Add
*** Hostname: localhost
*** IP&nbsp;Address: 127.0.0.1
*** Owner: admin
*** State: available
*** Predictive Loading Module: Predictive Loading Level 0 Module
*** Check-in Interval: 5
*** Install Path: /install
*** End Node SSH Identitiy Key Files: /etc/vcl/vcl.key
*** SSH Port for this node: 22
*** Enable Image Library: no
* Add VM host computer:
** Manage Computers \-> Edit&nbsp;Computer Information \-> Submit \-> Add
*** Hosthame: localvmhost
*** IP Address: 192.168.0.1 (NOTE: there is currently a bug restricting the
size of the field, so hopefully one octet has less than 3 digits.)
*** State:&nbsp;available
*{_}Note:_* _do not attempt to add the computer in&nbsp;the maintenance
state because of the following issue:_
[https://issues.apache.org/jira/browse/VCL-189](https://issues.apache.org/jira/browse/VCL-189)
*** Owner: admin
*** Platform: i386
*** Schedule: VCL 24x7&nbsp;
*** RAM: 1024
*** No Processors: 1
*** Processor Speed: 2000
*** Network Speed: 100&nbsp;
*** Type: blade
*** Provisioning engine: xCAT 1.x
*{_}Note:_* _the Type and Provisioning engine values don't matter for the
localvmhost computer in this test environment because vcld isn't
provisioning it_
*** Computer Groups: all vm host computers
* Add VM guest computer:
** Manage Computers \-> Edit Computer Information \-> Submit \-> Add
*** Hosthame: vmguest-1
*** IP Address: current public ip address used by Windows XP VM
*** State: available&nbsp;
*** Owner: admin
*** Platform: i386
*** Schedule: VCL 24x7&nbsp;
*** RAM: 1024
*** No Processors: 1
*** Processor Speed: 2000
*** Network Speed: 100&nbsp;
*** Type: virtualmachine
*** Provisioning engine: VMWare Server Provisioning
*** Computer Groups: all vm guest computers
* Note the fix for the IP address bug is recorded here: [https://issues.apache.org/jira/browse/VCL-193](https://issues.apache.org/jira/browse/VCL-193)
* Configure the VM guest's MAC address in the computer table in the
database (as there currently does not seem to be a way to do this through
the UI):
** eth0: 00:50:56:1a:01:01
** eth1: 00:50:56:1a:01:02
* Configure the VM host profile:
** Virtual Hosts \-> VM Host Profiles tab \-> VMware GSX standard \->
configure Profile
*** Virtual Switch 0: VMnet1
*** Virtual Switch 1: VMnet0
* Change state of localvmhost to vmhostinuse (edit the database directly,
do not use the Virtual Hosts utility on the website)
* Assign vm guests to localvmhost
* Create node in priviledge tree
** Name: VM image access
** Add resource groups:
*** all vm guest computers
*** all vm guest images

<a name="ConfiguringaStandaloneVCLEnvironmentusingVMwareServer1.x-RemoveExistingVirtualizationComponents"></a>
## Remove Existing Virtualization Components

{panel}
yum groupremove "Virtualization" \-y&nbsp;&nbsp;
{panel}

<a name="ConfiguringaStandaloneVCLEnvironmentusingVMwareServer1.x-MakeSureTheHostComputerIsNotRunningAXenKernel"></a>
## Make Sure The Host Computer Is Not Running A Xen Kernel

VMWare Server cannot be installed on a computer running a Xen kernel.&nbsp;
To determine if a Xen kernel is being used:
{panel}
uname \-a
{panel}The following output indicates a Xen kernel is being used:
{panel}
Linux blade1g6-4 2.6.18-92.el5{color:#cc0000}{*}xen{*}{color} \#1 SMP Tue
Jun 10 19:20:18 EDT 2008 x86_64 x86_64 x86_64 GNU/Linux
{panel}If "xen" appears in the output of the previous command, replace the
Xen Kernel with the following commands:
{panel}
yum update ecryptfs-utils \-y
yum install kernel kernel-devel \-y
yum remove xen kernel-xen \-y
{panel}Check the grub.conf file to make sure it is not configured to boot
using the Xen Kernel
{panel}
less /boot/grub/grub.conf&nbsp;
{panel}The grub.conf file should {color:#cc0000}{*}NOT{*}{color} look like
this:
{panel}
\# grub.conf generated by anaconda
\#
\# Note that you do not have to rerun grub after making changes to this
file
\# NOTICE:&nbsp; You have a /boot partition.&nbsp; This means that
\#&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; all kernel and
initrd paths are relative to /boot/, eg.
\#&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; root (hd0,0)
\#&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; kernel
/vmlinuz-version ro root=/dev/sda3
\#&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; initrd
/initrd-version.img
\#boot=/dev/sda
default=0
timeout=5
splashimage=(hd0,0)/grub/splash.xpm.gz
hiddenmenu
title CentOS (2.6.18-92.el5{color:#cc0000}{*}xen{*}{color})
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; root (hd0,0)
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; kernel /xen.gz-2.6.18-92.el5
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; module
/vmlinuz-2.6.18-92.el5{color:#cc0000}{*}xen{*}{color} ro root=LABEL=/
pci=nommconf
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; module
/initrd-2.6.18-92.el5xen.img
{panel}The grub.conf file {color:#336600}{*}SHOULD{*}{color} look like
this:
{panel}
\# grub.conf generated by anaconda
\#
\# Note that you do not have to rerun grub after making changes to this
file
\# NOTICE:&nbsp; You have a /boot partition.&nbsp; This means that
\#&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; all kernel and
initrd paths are relative to /boot/, eg.
\#&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; root (hd0,0)
\#&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; kernel
/vmlinuz-version ro root=/dev/sda3
\#&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; initrd
/initrd-version.img
\#boot=/dev/sda
default=0
timeout=5
splashimage=(hd0,0)/grub/splash.xpm.gz
hiddenmenu
title CentOS (2.6.18-128.1.14.el5)
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; root (hd0,0)
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; kernel
/vmlinuz-2.6.18-128.1.14.el5 ro root=LABEL=/1 pci=nommconf
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; initrd
/initrd-2.6.18-128.1.14.el5.img
{panel}After removing the Xen kernel, reboot the computer:
{panel}
reboot
{panel}

<a name="ConfiguringaStandaloneVCLEnvironmentusingVMwareServer1.x-InstallVMwareServer"></a>
## Install VMware Server

Download the latest VMware Server 1.x RPM from [http://www.vmware.com](http://www.vmware.com)
(Note: these instructions assume you saved the RPM into /install)

Install the VMware Server RPM:
{panel}
rpm \-ivh /install/VMware-server-1.0.8-126538.i386.rpm
{panel}Configure VMware Server:
{panel}
vmware-config.pl
{panel}{_}Note:_ if you receive an error message you may need to install or
update some libraries and then run vmware-config.pl again:
{panel}
yum install glibc-devel \-y
yum&nbsp;install glibc \-y&nbsp;
yum install libXtst-devel \-y
{panel}VMware networking should be configured as follows after answering
the questions asked by vmware-config.pl
* vmnet0 is bridged to eth1
* vmnet1 is a host-only network on private subnet 192.168.0.0

The following lists the sequence of answers to be entered after issuing the
vmware-config.pl command:
1. Press *ENTER* to view the license agreement, scroll to the bottom, type
*yes* and press *ENTER*
1. In which directory do you want to install the mime type icons?
\[/usr/share/icons\](/usr/share/icons\.html)
 *ENTER*
1. What directory contains your desktop menu entry files?
These files have a .desktop file extension. \[/usr/share/applications\](/usr/share/applications\.html)
 *ENTER*
1. In which directory do you want to install the application's icon?
\[/usr/share/pixmaps\](/usr/share/pixmaps\.html)
 *ENTER*
1. None of the pre-built vmmon modules for VMware Server is suitable for
your
running kernel.&nbsp; Do you want this program to try to build the vmmon
module for
your system (you need to have a C compiler installed on your system)? \[yes\](yes\.html)
 *ENTER*
1. What is the location of the directory of C header files that match your
running
kernel? \[/lib/modules/2.6.18-128.1.14.el5/build/include\](/lib/modules/2.6.18-128.1.14.el5/build/include\.html)
 *ENTER*
1. Do you want networking for your virtual machines? (yes/no/help) \[yes\](yes\.html)
 *ENTER*
1. Your computer has multiple ethernet network interfaces available: eth0,
eth1,
virbr0. Which one do you want to bridge to vmnet0? \[eth0\](eth0\.html)
 *eth1*
1. Do you wish to configure another bridged network? (yes/no) \[no\](no\.html)
 *ENTER*
1. Do you want to be able to use NAT networking in your virtual machines?
(yes/no)
\[yes\](yes\.html)
 *no*
1. Do you want to be able to use host-only networking in your virtual
machines?
\[no\](no\.html)
 *yes*
1. Do you want this program to probe for an unused private subnet?
(yes/no/help)
\[yes\](yes\.html)
 *no*
1. What will be the IP address of your host on the private
network? *192.168.0.1*
1. What will be the netmask of your private network? *255.255.0.0*
1. DHCP information is displayed, press *ENTER*
1. Do you wish to configure another host-only network? (yes/no) \[no\](no\.html)
 *ENTER*
1. The default port : 902 is not free. We have selected a suitable
alternative
port for VMware Server use. You may override this value now.
Remember to use this port when connecting to this server.
Please specify a port for remote console connections to use \[904\](904\.html)
 *ENTER*
1. In which directory do you want to keep your virtual machine files?
\[/var/lib/vmware/Virtual Machines\](/var/lib/vmware/virtual-machines\.html)
 *ENTER*
1. The path "/var/lib/vmware/Virtual Machines" does not exist currently.
This
program is going to create it, including needed parent directories. Is this
what you want? \[yes\](yes\.html)
 *ENTER*
1. Please enter your 20-character serial number
Type XXXXX-XXXXX-XXXXX-XXXXX or 'Enter' to cancel: *enter the serial
number*

Verify the host-only network was configured correctly:
{panel}
/sbin/ifconfig
{panel}You should see a *vmnet1* interface using IP address *192.168.0.1*:
{panel}
*vmnet1*&nbsp;&nbsp;&nbsp; Link encap:Ethernet&nbsp; HWaddr
00:50:56:C0:00:01
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; inet
addr:*192.168.0.1*&nbsp; Bcast:192.168.255.255&nbsp; Mask:255.255.0.0
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; inet6 addr:
fe80::250:56ff:fec0:1/64 Scope:Link
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; UP BROADCAST RUNNING
MULTICAST&nbsp; MTU:1500&nbsp; Metric:1
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; RX packets:0
errors:0 dropped:0 overruns:0 frame:0
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; TX packets:4
errors:0 dropped:0 overruns:0 carrier:0
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; collisions:0
txqueuelen:1000
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; RX bytes:0 (0.0
b)&nbsp; TX bytes:0 (0.0 b)
{panel}Restart the vmware service (*/sbin/service vmware restart*), you
should see the following:
{panel}
Starting VMware services:
&nbsp;&nbsp; Virtual machine monitor&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp; \[ OK \](-ok-\.html)
&nbsp;&nbsp; Virtual ethernet&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp; \[ OK \](-ok-\.html)
&nbsp;&nbsp; Bridged networking on /dev/vmnet0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; \[ OK \](-ok-\.html)
&nbsp;&nbsp; Host-only networking on /dev/vmnet1 (background)&nbsp;\[ OK \](-ok-\.html)
&nbsp;&nbsp; Starting VMware virtual machines...&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; \[ OK \](-ok-\.html)
{panel}

<a name="ConfiguringaStandaloneVCLEnvironmentusingVMwareServer1.x-Configure/etc/hosts"></a>
## Configure /etc/hosts

Modify the /etc/hosts file to include entries for the VM host and guest
computers:
{panel}
vi /etc/hosts
{panel}Add the entries in bold:
{panel}
127.0.0.1 localhost
*192.168.0.1 localvmhost*
*192.168.1.1 vmguest-1*
{panel}

h2. Configure the sshd Service to Listen on the Virtual Private
Network&nbsp;

{panel}
vi /etc/ssh/sshd_config
{panel}Add the following line to the end of the file:
{panel}
ListenAddress 192.168.0.1
{panel}Restart the sshd service on the management node:
{panel}
/sbin/service sshd restart
{panel}

<a name="ConfiguringaStandaloneVCLEnvironmentusingVMwareServer1.x-ConfigureTheVMHostToBeAbleToSSHToItself"></a>
## Configure The VM Host To Be Able To SSH To Itself

Add the VM host's public key to its own authorized_keys file to allow it to
SSH to itself without a password prompt:&nbsp;
{panel}
cat /etc/vcl/vcl.key.pub >> /root/.ssh/authorized_keys
{panel}The following command should execute without having to enter a
password:
{panel}
ssh localvmhost 'ls /'
{panel}

<a name="ConfiguringaStandaloneVCLEnvironmentusingVMwareServer1.x-Configurevcldtousevcl.key"></a>
## Configure vcld to use vcl.key

Configure the keys column in the managementnode table in the VCL database
* Edit the managementnode table in the database: set the *keys* column to
*/etc/vcl/vcl.key*

Configure the vcld.conf file to use vcl.key:
{panel}
vi /etc/vcl/vcld.conf
{panel}Modify all of the IDENTITY lines to specify the vcl.key file:
{panel}
IDENTITY_blade_linux=/etc/vcl/vcl.key
IDENTITY_solaris_lab=/etc/vcl/vcl.key
IDENTITY_linux_lab=/etc/vcl/vcl.key
IDENTITY_blade_win=/etc/vcl/vcl.key
{panel}

<a name="ConfiguringaStandaloneVCLEnvironmentusingVMwareServer1.x-ConfigureThe&nbsp;DHCPService&nbsp;"></a>
## Configure The&nbsp;DHCP Service&nbsp;

Save a copy of the original dhcpd.conf file:
{panel}
mv /etc/dhcpd.conf /etc/dhcpd.conf.orig
{panel}Configure the dhcpd.conf file:
{panel}
vi /etc/dhcpd.conf
{panel}The dhcpd.conf file should contain the following:

    ddns-update-style none; shared-network vmnet1 {
     ������� subnet 192.168.0.0 netmask 255.255.0.0 {
     ��������������� ignore unknown-clients;
     ��������������� option routers 192.168.0.1;
    ���������������  host vmguest-1 {
     ����������������������� option host-name "vmguest-1";
     ����������������������� hardware ethernet 00:50:56:1a:01:01;
     ����������������������� fixed-address 192.168.1.1;
     ����������������������� filename "/tftpboot/pxelinux.0";
     ����������������������� option dhcp-server-identifier 192.168.0.1;
     ����������������������� next-server 192.168.0.1;
     ��������������� }
    	  }
    }

The DHCP daemon should only listen on the virtual private network (vmnet1)
to avoid conflicts with other production VCL networks.&nbsp; Configure the
dhcpd service startup script to only listen on the vmnet1 interface:
{panel}
vi /etc/init.d/dhcpd
{panel}Add *vmnet1*&nbsp;the to the *daemon $dhcpd* line as shown:

    start() {
     [ -x $dhcpd ]
 || return 5
     [ -f $conf ]
 || return 6
     pidofproc $prog >/dev/null 2>&1
     RETVAL=$?
     [ $RETVAL -eq 0 ]
 && return $RETVAL
     echo -n $"Starting $prog: "
     daemon $dhcpd vmnet1 $DHCPDARGS 2>/dev/null
     RETVAL=$?
     echo
     [ $RETVAL = 0 ]
 && touch $lockfile
     return $RETVAL
    }

Configure the dhcpd service to automatically start at runlevels 3-5:
{panel}
/sbin/chkconfig \--level 345 dhcpd on
{panel}Start the dhcpd service:&nbsp;&nbsp;
{panel}
/sbin/service dhcpd start
{panel}
