---
title: Create a Linux Base Image
---

{excerpt}This page describes how to create a Linux base image.{excerpt}


<a name="CreateaLinuxBaseImage-Requirements"></a>
## Requirements

* Computer being captured has been added to the VCL database
* Computer has been installed with Linux
* Two network adapters are enabled on the computer:
** eth0 - connected to the private network
** eth1 - connected to the public network
* The ability to log in as root via SSH using an identity key on the
private network from management node

<a name="CreateaLinuxBaseImage-ConfigureSSHIdentityKeyAuthentication"></a>
### Configure SSH Identity Key Authentication

1. On the Linux computer being captured, create a /root/.ssh directory:
{tip}mkdir /root/.ssh{tip}
1. On the management node, copy the public SSH identity key to the
authorized_keys file on the Linux computer being captured:
{tip}scp /etc/vcl/vcl.key.pub <hostname or IP
address>:/root/.ssh/authorized_keys{tip}
1. Or replace the above two steps with the following on the management node:
{tip}ssh-copy-id \-i /etc/vcl/vcl.key <hostname or IP address>{tip}
1. Make sure you can login from the management node to the Linux computer
being captured using the identity key:
{tip}ssh \-i /etc/vcl/vcl.key <hostname or IP address>{tip}

<a name="CreateaLinuxBaseImage-Configuretheifcfg-\*Files"></a>
### Configure the ifcfg-\* Files

1. Navigate to the network-scripts directory:
{tip}cd /etc/sysconfig/network-scripts{tip}
1. Delete any ifcfg-*.bak files:
{tip}rm \-f /etc/sysconfig/network-scripts/ifcfg-*.bak{tip}
1. Edit every ifcfg-eth\* file in the network-scripts directory. Remove the
*HWADDRESS=* line:
{tip}vi ifcfg-eth0{tip}
{tip}vi ifcfg-eth1{tip}
The ifcfg-eth0 file should contain the following:

    DEVICE=eth0
    BOOTPROTO=dhcp
    ONBOOT=yes

The ifcfg-eth1 file should contain the following:

    DEVICE=eth1
    BOOTPROTO=dhcp
    ONBOOT=yes

1. Reboot the computer:
{tip}shutdown \-r now{tip}
1. Check the ifcfg-eth\* files to make sure there are no ifcfg-eth\* files
and that the HWADDRESS= lines have not been automatically added back:
{tip}
ls /etc/sysconfig/network-scripts
{tip}
{tip}
cat /etc/sysconfig/network-scripts/ifcfg-eth0
{tip}
{tip}
cat /etc/sysconfig/network-scripts/ifcfg-eth1
{tip}

{include:Capture A Base Image}
