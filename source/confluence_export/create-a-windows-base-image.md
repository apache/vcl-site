---
title: Create a Windows Base Image
---

{excerpt}This page describes how to create a Windows base
image.{excerpt}These instructions should work regardless of the
provisioning engine being used (xCAT, VMware, etc.).&nbsp; Ignore the
{color:#0000ff}{*}VMware Only{*}{color}&nbsp;sections if you are attempting
to create an image using&nbsp;xCAT or some other bare metal provisioning
engine.&nbsp;

  
  

<a name="CreateaWindowsBaseImage-Requirements"></a>
### Requirements

You will need the following:
* Windows installation ISO file
* Windows product key or KMS server address

&nbsp;The following must be done before an image can be captured:
* A computer&nbsp;for the machine being captured has already been added to
the VCL database
* {color:#0000ff}{*}VMware Only{*}{color}:
** A VM host computer on which the guest is running as&nbsp;been added to
the VCL database
** The guest VM has been assigned to the VM host via the *Virtual Hosts*
link on the VCL website

These instructions assume you have root access and are using a *bash*
shell.

<a name="CreateaWindowsBaseImage-{color:#0000ff}VMwareOnly:{color}CreateaVirtualMachine"></a>
## {color:#0000ff}VMware Only:{color} Create a Virtual Machine


<a name="CreateaWindowsBaseImage-CreateaVirtualMachine"></a>
### Create a Virtual Machine

<a name="CreateaWindowsBaseImage-VMwareESXi4.x"></a>
#### VMware ESXi 4.x

The instructions assume that VMware has been configured with the following
bridged networks:
* *Private*: bridged to private interface: eth0
* *Public*: bridged to public interface: eth1

* Launch the vSphere Client, connect to the ESXi host and login
* Click File > New > Virtual Machine
* Configuration: *Custom*
* Name: _(doesn't matter)_
* Select a datastore where the VM will reside
* Virtual Machine Version: *7*
* Select the appropriate guest OS
* Number of virtual processors: 1
* Memory: 1GB
* How many NICs: 2
** NIC 1: *Private*, E1000
** NIC 2: *Public*, E1000
* SCSI controller: LSI Logic Parallel
* Create a new virtual disk
** Disk Size: at least 30 GB
** Allocate and commit space on demand (Thin Provisioning): *Yes*
** Location: Store with the virtual machine
** Virtual Device Node: SCSI (0:0)
** Mode: Independent, Persistent
* Edit the virtual machine settings before completion: *Yes*
* Select the CD/DVD device
** Device Type: *Datastore ISO File*
** Click Browse and browse to an ISO file that has previously been copied
to the datastore
** Connect at power on: *Yes*
* Click Finish

<a name="CreateaWindowsBaseImage-VMwareServer1.x"></a>
#### VMware Server 1.x

The instructions assume that VMware has been configured with the following
bridged networks:
* VMnet0: bridged to private interface: eth0
* VMnet2: bridged to public interface: eth1

* Launch the VMware Server console and connect to the local VMware host:
{tip}
vmware &
{tip}
* Virtual Machine Configuration: *Typical*
* Guest Operating System: *Microsoft Windows*
* Version: *Windows XP Professional* (select the appropriate version if you
are not installing XP)
* Name: *vmwarewinxp-base7-v1*
* Network connection: *Custom*
** /dev/vmnet0\*
* Disk size: *8.0 GB*
** Allocate all disk space now: *no*
** Split disk into 2GB files: *yes*
* Edit virtual machine settings
** Configure the VM CD-ROM drive to use the Windows XP ISO image
** Connection: *Use ISO image*: browse to path of Windows XP ISO image
copied to the VMware host
* Add: Ethernet Adapter
** Network Connection: *Custom*
** \*/dev/vmnet2\*

<a name="CreateaWindowsBaseImage-VMwareServer2.x"></a>
#### VMware Server 2.x

* Open the VMware Infrastructure Web Access page:
{info:icon=false}https://<IP address or hostname>:8333{info}
* Click the *Virtual Machine* menu
* Select *Create Virtual Machine*
* Name and Location
** Name: *Windows XP Base*
** Datastore: *standard* (This causes the VM to be created under
/var/lib/vmware/Virtual Machines)
* Guest Operating System
** Operating System: *Windows operating system*
** Version: *Microsoft Windows XP Professional (32-bit)*
** Product Compatibility: *4* (Optional - the hardware version can be set
to the default value of *7* if you do not have any older VMware Server 1.x
hosts in your environment)
* Memory and Processors
** Memory Size: *1024 MB*
** Processor Count: *1*
* Hard Disk
** Click *Create a New Virtual*
*** Capacity: at least *20 GB* (This value can be adjusted to suit the size
of the VMware host's disk. It is best to create the base image with a large
enough hard drive to accomodate your largest image. The hard drive of a VM
can be expanded but it is a manual, time-consuming process.)
*** File Options
**** Allocate all disk space now: no
**** Split disk into 2 GB files: yes
*** Disk Mode: *Independent/Persistent*
* Network Adapter
** Click *Add a Network Adapter*
*** Network Connection: select the name of your *private* network
* CD/DVD Drive
** Click *Use an ISO*
*** Select the Windows ISO image you copied to the host. The ISO file must
reside in */var/lib/vmware/Virtual Machines* in order to be able to select
it from this interface.
* Don't Add a Floppy Drive
* Don't Add a USB
* Click *Finish*
* Select the VM from the Inventory pane
* Click *Add Hardware* on the right side of the page
* Select *Network Adapter*
** Network Connection: select the name of your *public* network
* Click *Next* > *Finish*

<a name="CreateaWindowsBaseImage-InstallWindows"></a>
## Install Windows

[Install Windows for a Base Image](install-windows-for-a-base-image.html)

<a name="CreateaWindowsBaseImage-{color:#0000ff}VMwareOnly:{color}InstallVMwareTools"></a>
## {color:#0000ff}VMware Only:{color} Install VMware Tools

1. Power on the VM if it is not already powered on
1. Install VMWare Tools&nbsp; (Note: you must have a CD-ROM drive configured
for the VM in order to install VMware Tools)
1. # Click on the VM menu and select "Install VMWare Tools"
1. # Select Typical and proceed through the setup pages accepting the
defaults
1. # Reboot the VM when installation is complete

<a name="CreateaWindowsBaseImage-InstallCygwinSSHD"></a>
## Install Cygwin SSHD

Follow the steps: [Install & Configure Cygwin SSHD](install-&-configure-cygwin-sshd.html)

{include:Capture A Base Image}
