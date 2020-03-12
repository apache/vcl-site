---
title: Further steps if using only VMWare
---

If you are using standalone VMWare servers (i.e. ones that VCL did not
deploy using xCAT), you first need to add the VMWare servers; then, you
need to add the virtual machines. You can either add them individually
(Adding Individual VMWare Servers/Virtual Machines), or if they have
sequential hostnames and IP addresses, you can add them all at once (Adding
Multiple VMWare Servers/Virtual Machines).

Once you have added at least one computer, you can get to the "Add Single
Computer" page by going to Manage Computers->Edit Computer Information and
clicking Add. You can get to the "Add Multiple Computers" page by doing the
same thing but checking the "Add Multiple" checkbox.

<a name="FurtherstepsifusingonlyVMWare-AddingIndividualVMWareServers"></a>
### Adding Individual VMWare Servers

1. click "Manage Computers"
1. select the "Add Single Computer" radio button
1. click Submit
1. fill in
 * Hostname
 * IP Address
 * State - vmhostinuse - double check this because you will not be able to
change it later
 * owner (admin@Local)
 * RAM
 * Proc Speed
 * Network Speed
 * Type - blade
 * Provisioning Engine - xCAT 2.x Provisioning
 * click the checkbox under "allcomputers"
1. click Confirm Computer
1. click Submit
1. select a VM Host Profile to use with this host - you can edit the VM Host
Profile later if needed
1. click Add Computer (don't worry about the fact that the computer you just
added isn't listed after clicking Submit)

<a name="FurtherstepsifusingonlyVMWare-AddingIndividualVirtualMachines"></a>
### Adding Individual Virtual Machines

VM computers cannot be added individually at the current time because some
required database properties such as the&nbsp;MAC address&nbsp;do not get
populated.&nbsp; Instead, use the steps described below to add multiple
virtual machines.

<a name="FurtherstepsifusingonlyVMWare-AddingMultipleVMWareServers"></a>
### Adding Multiple VMWare Servers

1. click "Manage Computers"
1. select the "Add Multiple Computers" radio button
1. click Submit
1. fill in
 * Hostname - the hostnames of all the computers must have a numerical part
that is sequential, use a % as a placeholder where that part would be
 * Start value - the first number of the numerical part of the hostname
 * End value - the last number of the numerical part of the hostname
 * Start IP Address - if using static public addresses, the IP addresses
must be sequential; enter the first address here; if using DHCP, just enter
something like 1.1.1.1
 * End IP address - the last IP address of the sequence; if using DHCP,
you'll need to enter something that would work out to the last address
relative to Start IP Address (i.e. if adding 3 computers, use 1.1.1.1 for
start and 1.1.1.3 for end)
 * State - vmhostinuse - double check this because you will not be able to
change it later
 * Owner - owner of the computer
 * RAM
 * Processor Speed
 * Network Speed
 * Type - blade
 * Provisioning Engine - xCAT 2.x
 * check allComputers
1. click Confirm Computers
1. click Submit
1. select a VM Host Profile to use with these hosts - you can edit the VM
Host Profile later if needed
1. click Add Computers

<a name="FurtherstepsifusingonlyVMWare-AddingMultipleVirtualMachines"></a>
### Adding Multiple Virtual Machines

1. click "Manage Computers"
1. select the "Add Multiple Computers" radio button
1. click Submit
1. fill in
 * Hostname - the hostnames of all the computers must have a numerical part
that is sequential, use a % as a placeholder where that part would be
 * Start value - the first number of the numerical part of the hostname
 * End value - the last number of the numerical part of the hostname
 * Start IP Address - if using static public addresses, the IP addresses
must be sequential; enter the first address here; if using DHCP, just enter
something like 1.1.1.1
 * End IP address - the last IP address of the sequence; if using DHCP,
you'll need to enter something that would work out to the last address
relative to Start IP Address (i.e. if adding 3 computers, use 1.1.1.1 for
start and 1.1.1.3 for end)
 * Start private IP Address - similar to Start IP Address, but for the
private side
 * End private IP Address - similar to the End IP Address but for the
private side
 * Start MAC Address - if mac addresses are sequential, with the first one
being the private MAC address for the first computer, the second one being
the public MAC address for the first computer, the third one being the
private MAC address of the second computer, etc, you can enter the first
one here and then have the option of generating data to add to your
dhcpd.conf file later in the process.
**Important**: for VMware VMs, the MAC addresses
you choose must be in the range&nbsp;00:50:56:00:00:00 - 00:50:56:3F:FF:FF
 * State - maintenance
 * Owner - owner of the computer
 * RAM
 * Processor Speed
 * Network Speed
 * Type - virtualmachine
 * Provisioning Engine - VMware
 * check "All VM Computers" and newvmimages
1. click Confirm Computers
1. click Submit
1. If you filled in the private address fields and the Start MAC Address,
you can now enter the private IP address of the management node that will
be handling these virtual machines to generate information to add to your
dhcpd.conf file.
