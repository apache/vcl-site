---
title: VMware Configuration
---

<a name="VMwareConfiguration-Terminology"></a>
## Terminology


<a name="VMwareConfiguration-VMHost"></a>
#### VM Host

* A VM host is a physical computer running a VMware hypervisor
* A VCL computer entry must be added for each VM
host&nbsp;({color:#000000}{_}Manage Computers > Edit Computer
Information)_{color}
* {color:#000000}After the computer has been added to VCL, it is designated
as a VM host by changing the computer state to vmhostinuse{color}
{color:#000000}_(Manage Computers > Computer Utilities)_{color}

<a name="VMwareConfiguration-VM"></a>
#### VM

* A VM is a virtual machine managed by VCL
* A computer entry must be added to VCL for each VM
({color:#000000}{_}Manage Computers > Edit Computer Information)_{color}
* {color:#000000}Each VM must be assigned to a VM host{color}
{color:#000000}_(Virtual Hosts > VM Hosts tab > Configure Host)_{color}
* VMs do not need to be created manually in VMware, VCL automatically
creates and deletes VMs

<a name="VMwareConfiguration-VMHostProfile"></a>
#### VM Host Profile

* A VM host profile contains&nbsp;several parameters which describe how a
VM host is configured so that VCL knows how to manage it
* Each VM host is assigned a VM host profile
* A VM host profile may be assigned to multiple VM hosts if they are
configured identically
* VM host profiles may be added or modified via _Virtual Hosts > VM Host
Profiles tab_

<a name="VMwareConfiguration-VMwareProductsSupported"></a>
## VMware Products Supported

* VMware Server 2.x
* VMware ESX 3.5 - 4.x
* VMware ESXi 4.x
* VMware ESXi 5.x

<a name="VMwareConfiguration-VMHost&nbsp;ManagementOptions"></a>
### VM Host&nbsp;Management Options

&nbsp;The VCL&nbsp;management node must be able to control the VM host and
the VMs running on it.&nbsp; VMware provides several different&nbsp;ways of
doing this.&nbsp; VCL currently supports the following methods for remote
VM host management:
* VMware vSphere SDK
* Use SSH to execute&nbsp;commands directly on the VM (_not officially
supported by VMware_)

The vSphere SDK can only&nbsp;be used if management is not&nbsp;restricted
due to the VMware license key installed on the host.&nbsp; This mainly
affects hosts running the free version of ESXi.&nbsp; Remote management
using any of the&nbsp;methods supported by VMware&nbsp;is restricted once a
free license key is entered.

If remote management is restricted, the VM host can be managed if SSH is
enabled on it.&nbsp; VCL will execute vim-cmd and other commands on the VM
host via SSH.&nbsp;


<a name="VMwareConfiguration-HowtoenableSSHontheVMhost:"></a>
#### How to enable SSH on the VM host:

<a name="VMwareConfiguration-VMwareServer2.x"></a>
##### VMware Server 2.x

Enable the SSH daemon and configure identity key authentication according
to the underlying VM host OS

<a name="VMwareConfiguration-ESX/ESXi3.5&4.0"></a>
##### ESX/ESXi 3.5 & 4.0

* Connect to the console of the ESX/ESXi host
* Press *ALT-F1* \- you should see a black screen with the VMware product
name at the top
* Type the word *unsupported* and press *Enter* (you won't see the letters
appear as you type them)
* You should see a password prompt, type&nbsp;in the *root
password*&nbsp;and press *Enter*
* Edit the file: *vi /etc/inetd.conf*
* Uncomment the first line beginning with _\#ssh_ by deleting the #
character
* Save the file - press *Esc* and then *:wq*
* Kill the inetd process
** Determine the PID of the inetd process: *ps \| grep inetd*
You should see a line that looks like: _5065 5065 busybox inetd_
** Kill the process (enter the PID from the output of the previous
command): *kill \-HUP 5065*

<a name="VMwareConfiguration-ESXi4.1"></a>
##### ESXi 4.1

Beginning with *ESXi 4.1*, SSH&nbsp;can be enabled using the vSphere
Client:
* Select the ESXi host
* Select the *Configuration* tab
* Select&nbsp;*Security Profile* under Software
* Click *Properties*
* Select *Remote Tech Support (SSH)*
* Click *Options*
* Select *Start automatically*
* Click *Start*
* Click *OK*

<a name="VMwareConfiguration-ESX5.0"></a>
##### ESX 5.0

In the case of *ESX 5.0*:
* Select the ESXi host
* Select the *Configuration* tab
* Select&nbsp;*Security Profile* under Software
* Click *Properties*
* Select *SSH Server*
* Click *Options*
* Confirm that *Start automatically* is selected
* Click *OK*

<a name="VMwareConfiguration-HowtoconfigureESX/ESXitouseSSHidentitykeyauthentication:"></a>
#### How to configure ESX/ESXi to use SSH identity key authentication:

SSH identity key authentication&nbsp;must be configured if SSH is used to
manage the VM host.
* Create an SSH key pair on the management node (or use a key you
previously created):
{tip}
ssh-keygen \-t rsa \-f /etc/vcl/vcl.key \-N '' \-b 1024 \-C 'VCL root
account'
{tip}
* Log into the ESX host via SSH (password authentication should work) and
create the directory:
{tip}
ssh <ESXi host> 'mkdir /.ssh'
{tip}
* Copy the public key to the ESXi host:
ESXi 4.x:
{tip}
scp /etc/vcl/vcl.key.pub <ESXi host>:/.ssh/authorized_keys
{tip}
ESXi 5.x:
{tip}
scp /etc/vcl/vcl.key.pub <ESXi host>:/etc/ssh/keys-root/authorized_keys
{tip}
* Test making an SSH connection using the key:
{tip}
ssh \-i /etc/vcl/vcl.key <ESXi host>
{tip}

{color:#ff0000}{*}IMPORTANT:*{color} Under ESXi 4.x, the authorized_keys
file is erased when the ESXi VM host is rebooted.&nbsp;Complete the
following steps to&nbsp;make&nbsp;the authorized_keys file&nbsp;persistent:

_Note: VCL will perform these steps automatically when the 1st reservation
assigned to the host is processed._


* Create a compressed tarball file containing the /.ssh directory:
{tip}
tar \-C / \-czf bootbank/vcl.tgz .ssh
{tip}
* Edit the /bootbank/boot.cfg file and append *_' \--\- vcl.tgz'_* to
modules line as shown in the following example:
{panel}
kernel=b.z
kernelopt=
modules=k.z --- s.z --- c.z --- oem.tgz --- license.tgz --- m.z ---
state.tgz --- vcl.tgz
build=4.1.0-260247
updated=2
bootstate=0
{panel}
{tip}
Optionally you can run the following two commands:
tar \-C / \-czf vcl.tgz .ssh
BootModuleConfig.sh \--add=vcl.tgz \--verbose
{tip}

<a name="VMwareConfiguration-VMHostProfileParameters"></a>
## VM Host Profile Parameters

<a name="VMwareConfiguration-GeneralParameters"></a>
### General Parameters


<a name="VMwareConfiguration-"></a>
#### 

<a name="VMwareConfiguration-*Name*"></a>
##### *Name*

* Descriptive name of the VM host&nbsp;profile


<a name="VMwareConfiguration-*Type*_(deprecated)_"></a>
##### *Type* _(deprecated)_

* Removed in VCL 2.3

<a name="VMwareConfiguration-*Image*_(optional)_"></a>
##### *Image* _(optional)_

* VCL hypervisor image installed on VM host computers using xCAT
{info}{_}xCAT is not required. &nbsp;VM host computers may be installed
manually or by some other means._{info}
* If xCAT is not used, select "No Image"
* VCL has the ability to install a hypervisor image on bare-metal computers
using xCAT. &nbsp;If the image property is configured, the image is
installed when a computer's state is changed to vmhostinuse via _Manage
Computers > Computer Utilities_

<a name="VMwareConfiguration-*Username/Password*_(optional)_"></a>
##### *Username/Password* _(optional)_

* Name and password&nbsp;of the&nbsp;administrative or root user residing
on the VM host
* This account is used to manage the VM host and VMs assigned to the host
* The username and password are currently only used if the vSphere SDK is
used to manage the VM host and VMs

<a name="VMwareConfiguration-StorageParameters"></a>
### Storage Parameters

{anchor:resource}

<a name="VMwareConfiguration-ResourcePath_(optional)_"></a>
##### Resource Path _(optional)_

Resource Path only needs to be configured if VMware vCenter is used. It
defines the location where VMs will be created in the vCenter inventory
tree. The inventory tree contains at least one Datacenter, and may also
contain Folders, Clusters, and Resource Pools.
Example: /DatacenterA/Folder1/Cluster2/ResourcePool3

{anchor:repository}

<a name="VMwareConfiguration-*RepositoryPath*_(optional)_"></a>
##### *Repository Path* _(optional)_

* Path where master copies of images are stored which are&nbsp;used to
transfer images to VM host datastores or to other repositories:
** If a reservation is assigned to a host but the image does not  exist in
that host's datastore, it is copied from the repository to the virtual disk
path when the VM is loaded
** If the VCL environment contains multiple management nodes and the  image
does not exist in the repository or the host's datastore, the  image will
be retrieved from another management node's repository by  copying it via
SCP
* The Repository Path parameter does not need to be configured if the  VCL
environment contains a single management node and all VM hosts	share the
same Virtual Disk Path
* Example:&nbsp;_/vmfs/volumes/nfs-repository1_
* VMs do not run directly off of the images stored in the repository
* Setting the Repository Path parameter determines whether or not an 
additional copy of an image is created when an image is captured
** If repository path is not configured then only a single copy of the
image will exist in the virtual disk path after an image is captured
** If repository path is configured then two copies of the image will 
exist after an image is captured - one in the virtual disk path and one in
the  repository
* Repository Path location can refer to and be mounted on either the
management node or VM host
** It is highly recommended that the repository be mounted on the VM host
*** When mounted on the VM host, vmdk operations can be done directly on
the VM host in a single step
* Images in the repository are stored in the 2 GB sparse vmdk format
** The size of the vmdk files will approximately be equal to the  amount of
actual data saved in the image regardless of the size of the  VM's hard
drive
** Storing images in the 2 GB sparse format is necessary to allow  images
to be transferred via SCP without having to transfer data equal  to the
entire size of the VM's hard drive

<a name="VMwareConfiguration-RepositoryImageType"></a>
##### Repository Image Type

Virtual disk file format for images stored in the repository.
{anchor:datastore}

<a name="VMwareConfiguration-*VirtualDiskPath(previouslyDatastorePath)*"></a>
##### *Virtual Disk Path (previously Datastore Path)*

* Location where master copies of images are stored which are used by
running VMs
* Example:&nbsp;_/vmfs/volumes/nfs-datastore1_
{info}For ESXi, the path configured in the profile may simply be the short
datastore name as it appears in the vSphere Client: nfs-datastore1{info}
* Storage location should be large enough to store all of the images which
may be loaded on the VM host _(from 100's of GB to several TB)_
* VCL creates a directory for each image in the Virtual Disk Path
* Images are stored in the [vmfs thin vmdk format](http://www.sanbarrow.com/vmdk-basics.html)
* Virtual Disk Path may either reside on local or network storage
* Multiple VM hosts can share the same datastore if network storage is used
** A single datastore may be used by all VM hosts if performance is
adequate
** Multiple VMs on different hosts may access the same Virtual Disk Path
image at the same time
** It is recommended that datastores are shared among hosts so that fewer
copies of each image have to be stored
** The underlying storage hardware and network connectivity from the hosts
to the storage must be adequate
** Storage where the datastore is located should be optimized for read
performance
* VCL configures VMs to access images stored in the Virtual Disk Path in
read-only mode
** Changes made to the VM's hard drive are written to delta files located
in the VM Working Directory Path dedicated for the VM

<a name="VMwareConfiguration-VirtualDiskImageType"></a>
##### Virtual Disk Image Type

Virtual disk file format for images stored in the virtual disk path.

<a name="VMwareConfiguration-VirtualDiskMode(previously*VMDisk)*"></a>
##### Virtual Disk Mode (previously *VM Disk)*

* Defines whether the storage where the VM host's Virtual Disk Path 
resides is dedicated to a single host or shared among multiple hosts:
** dedicated (previously localdisk)
*** The VM host's Virtual Disk Path&nbsp;is located on local disks or
dedicated network storage
*** The VM host is the only host which accesses the Virtual Disk Path
*** Repository Path must be configured
** shared (previously networkdisk)
*** The VM host's Virtual Disk Path&nbsp;is located on network storage
which is shared by other VM hosts
*** Repository Path is optional

{note}
The Virtual Disk Mode (VM Disk) parameter does *not* determine whether or
not:
...images are copied from the datastore to the repository during image
capture
...images are copied from the repository to the datastore during image load
These are determined by whether or not Repository Path is configured in the
profile
{note}


{anchor:vmpath}

<a name="VMwareConfiguration-VMWorkingDirectoryPath_(optional)_(previously*VMPath*)"></a>
##### VM Working Directory Path _(optional)_ (previously *VM Path*)

* Defines path on VM host where VM working directories will reside
(contains .vmx, delta, .vswp, nvram files)
* If not configured, the Virtual Disk Path location will be used
* VCL creates a directory under the VM Working Directory Path for each VM
it creates
** Contains the .vmx file which defines the VM
** Contains delta vmdk files which are written to as changes are made to
the VM's hard drive
* VM Working Directory Path may either reside on local or network storage
* Location should be dedicated for each VM host
** Multiple VM hosts should not share the same VM Working Directory Path
location for performance and image safety reasons
** VM Working Directory Paths of multiple hosts may reside on the same
volume but a subdirectory should be created for each host
* Storage where the VM Working Directory Path is located should be
optimized for read-write performance




<a name="VMwareConfiguration-"></a>
##### 

<a name="VMwareConfiguration-NetworkingParameters"></a>
#### Networking Parameters

<a name="VMwareConfiguration-*VMNetwork(previouslyVirtualSwitch)*"></a>
##### *VM Network (previously Virtual Switch)*

* VM Network 0 (previously Virtual Switch 0) - private VCL
management&nbsp;network
* VM Network 1 (previously Virtual Switch 1) - public network used by user
making reservation&nbsp;to access the VMs

* The VM Network parameters should match the network names configured on
the VM host
** For ESXi, the _VM Network_ parameters must match the _Virtual Machine
Port Group Network Labels_ configured in the vSphere Client, example:
*** VM Network 0: Public
*** VM Network 1: Private
&nbsp; !vmware-network-labels.gif|border=1!

* For VMware Server 2.x, the _VM Network_ parameters must match the
_Network Names_ configured&nbsp;by running&nbsp;vmware-config.pl

<a name="VMwareConfiguration-*Generateeth0/eth1MAC*"></a>
##### *Generate eth0/eth1 MAC*

* New in VCL 2.3
* Determines whether VMs are assigned MAC addresses defined in the VCL
database or if random MAC addresses should be assigned

<a name="VMwareConfiguration-ConfigurationExamples"></a>
## Configuration Examples


<a name="VMwareConfiguration-LocalDiskOnly-RepositoryMountedviaNFS"></a>
### Local Disk Only - Repository Mounted via NFS


<a name="VMwareConfiguration-!local-only-nfs.gif!"></a>
### !local-only-nfs.gif!


The diagram above shows a simple VCL configuration with 1 management node
and 2 VMware ESXi hosts.&nbsp; Network storage is not used.
The local disks on the VM hosts are used to store all of the files used by
running VMs including the VM's working directory and the master vmdk image.

A directory on the local disk on the management node is used to as the
image repository.&nbsp;  This directory is exported via NFS.&nbsp; VM hosts
mount this directory  as a datastore named "repository".&nbsp; Mounting the
repository directly on	the VM hosts allows the vmkfstools utility to be
used on the VM hosts to  copy and convert images directly from the
repository to the local  datastore in a single step.

If an image is to be loaded on a VM host and that image does not already
exist in the VM host's local datastore (Virtual Disk Path), it is
automatically copied from the repository to the VM host's local datastore
(Virtual Disk Path) at the beginning of the load process.

During image capture, images are automatically copied to from the VM host's
local datastore (Virtual Disk Path) to the repository.&nbsp; This allows
images captured on a VM host to be loaded on any other VM host.

The VM host profile Virtual Disk Mode parameter is set to dedicated.&nbsp;
This indicates to the load process that the VM host's Virtual Disk Path is
dedicated to the VM host and not shared by other VM hosts.&nbsp; This
allows images to be deleted from the VM host's local datastore (Virtual
Disk Path) if another image must be copied from the repository and not
enough space is available.


<a name="VMwareConfiguration-LocalDiskOnly-RepositoryNotAvailableviaNFS"></a>
### Local Disk Only - Repository Not Available via NFS


!local-only-scp.gif!

This example is identical to the one above except that the repository
located on the management node's local disk is not exported via NFS.&nbsp;
Because of this, images must be transferred using SCP instead of
vmkfstools.&nbsp; This is less desirable than mounting the repository
directly on the VM hosts because images cannot be copied and converted in a
single step.&nbsp; Images are stored in the repository in the 2GB sparse
format.&nbsp; This allows the images to be copied via SCP while only
transferring the data stored in the image, not the entire size of the hard
drive stored in the image.&nbsp; VMware ESXi cannot run VMs using vmdk
images stored in the 2GB sparse format.&nbsp; Images are converted to the
vmfs thin format so that they can be loaded on VMware ESXi.&nbsp; This adds
extra time to the load process if an image does not exist in the VM's local
datastore (Virtual Disk Path) and must be copied from the repository.&nbsp;
It also requires additional space in the VM host's local datastore (Virtual
Disk Path) becuase 2 copies of the image exist while it is being converted.
Note that the VM host profile Repository Path parameter is set to the path
on the management node's hard drive.&nbsp; The code first checks if the
path exists on the VM host.&nbsp; If not, it assumes the repository is not
mounted directly on the VM host and the Repository Path value refers to a
location on the management node.

<a name="VMwareConfiguration-NetworkStorageOnly-NoRepository"></a>
### Network Storage Only - No Repository

!network-only-no-repo.gif!

This is an example of a simple configuration where the network storage is
used.

A repository is not used in this configuration. &nbsp;This implies that all
VM hosts which will ever be added to this VCL environment will need to be
able to connect to the network storage.

A datastore to be used as the Virtual Disk Path named "datastore" is
mounted on every VM host. &nbsp;Each of these mounts points to the same
location on the network storage. &nbsp;The datastore will contain the
master vmdk images. &nbsp;VMs loaded on the VM hosts will read from these
master vmdk images.

A datastore to be used as the VM Working Directory Path named "vmpath" is
also mounted on each VM host. &nbsp;However, the location to which each VM
host points should be different. &nbsp;In the example above, vmhost-a-01
points to th the /vmpath01 directory on the network storage and vmhost-a-02
points to the /vmpath02 directory. &nbsp;These locations may be different
network storage filesystems or may be different directories on the same
network filesystem. &nbsp;Even though the mounts on the VM hosts point to
different locations, the datastore names configured under ESXi are
identical. &nbsp;This allows you to use the same VCL VM host profile for
all of the VM hosts.

The VM host profile Virtual Disk Mode parameter is set to shared.&nbsp;
This indicates to the load process that the VM host's Virtual Disk Path is
shared by other VM hosts.
