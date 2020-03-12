---
title: VCL 2.2.1 - Further Steps if Using VMware
---

If you are using standalone VMware servers (i.e. ones that VCL did not
deploy using xCAT), you first need to add the VMWare servers; then, you
need to add the virtual machines. You can either add them individually
(Adding Individual VMWare Servers/Virtual Machines), or if they have
sequential hostnames and IP addresses, you can add them all at once (Adding
Multiple VMWare Servers/Virtual Machines).

Once you have added at least one computer, you can get to the "Add Single
Computer" page by going to Manage Computers->Edit Computer Information and
clicking Add. You can get to the "Add Multiple Computers" page by doing the
same thing but checking the "Add Multiple" checkbox.

<a name="VCL2.2.1-FurtherStepsifUsingVMware-AddingIndividualVMwareServers"></a>
### Adding Individual VMware Servers

1. Click *Manage Computers*
1. Select the *Add Single Computer* radio button
1. Click *Submit*
1. Fill in the following:
1. * *Hostname*
1. * *IP Address*
1. * *State* \- vmhostinuse
{note}Double-check this because you will not be able to change it
later{note}
1. * *Owner* \- [admin@Local](mailto:admin@local.html)
1. * *RAM*
1. * *Processor Speed*
1. * *Network Speed*
1. * *Type* \- blade
1. * *Provisioning Engine* \- xCAT 2.x Provisioning
1. * Click the checkbox under *allcomputers*
1. Click *Confirm Computer*
1. Click *Submit*
1. Select a *VM Host Profile* these VMware hosts will use.&nbsp; See the [VCL:VMware Configuration](vcl:vmware-configuration.html)
&nbsp;page for more information about VM Host Profiles.&nbsp;
{info}You can modify the VM Host Profile later if needed{info}
1. Click Add Computer
{info}The computer you just added isn't listed after clicking Submit. This
is not a problem.{info}

<a name="VCL2.2.1-FurtherStepsifUsingVMware-AddingMultipleVMWareServers"></a>
### Adding Multiple VMWare Servers

1. Click *Manage Computers*
1. Select the *Add Multiple Computers* radio button
1. Click *Submit*
1. Fill in the following:
1. * *Hostname* \- the hostnames of all the computers must have a numerical
part that is sequential, use a % as a placeholder where that part would be
1. * *Start value* \- the first number of the numerical part of the hostname
1. * *End value* \- the last number of the numerical part of the hostname
1. * *Start IP Address* \- if using static public addresses, the IP addresses
must be sequential; enter the first address here; if using DHCP, just enter
something like 1.1.1.1
1. * *End IP address* \- the last IP address of the sequence; if using DHCP,
you'll need to enter something that would work out to the last address
relative to *Start IP Address* (i.e. if adding 3 computers, use 1.1.1.1 for
start and 1.1.1.3 for end)
1. * *State* \- vmhostinuse
{note}Double-check this because you will not be able to change it
later{note}
1. * *Owner* \- owner of the computer
1. * *RAM*
1. * *Processor Speed*
1. * *Network Speed*
1. * *Type* \- blade
1. * *Provisioning Engine* \- xCAT 2.x
1. * Check *allComputers*
1. Click *Confirm Computers*
1. Click *Submit*
1. Select a *VM Host Profile* these VMware hosts will use. See the [VCL:VMware Configuration](vcl:vmware-configuration.html)
&nbsp;page for more information about VM Host Profiles.&nbsp;
{info}You can modify the VM Host Profile later if needed{info}
1. Click *Add Computers*

<a name="VCL2.2.1-FurtherStepsifUsingVMware-AddingVirtualMachines"></a>
### Adding Virtual Machines

1. Click *Manage Computers*
1. Select the *Add Multiple Computers* radio button
1. Click *Submit*
1. Fill in the following:
1. * *Hostname* \- the hostnames of all the computers must have a numerical
part that is sequential, use a % as a placeholder where that part would be
1. * *Start value* \- the first number of the numerical part of the hostname
1. * *End value* \- the last number of the numerical part of the hostname
1. * *Start IP Address* \- if using static public addresses, the IP addresses
must be sequential; enter the first address here; if using DHCP, just enter
something like 1.1.1.1
1. * *End IP address* \- the last IP address of the sequence; if using DHCP,
you'll need to enter something that would work out to the last address
relative to Start IP Address (i.e. if adding 3 computers, use 1.1.1.1 for
start and 1.1.1.3 for end)
1. * *Start private IP Address* \- similar to Start IP Address, but for the
private side
1. * *End private IP Address* \- similar to the End IP Address but for the
private side
1. * *Start MAC Address* \- if mac addresses are sequential, with the first
one being the private MAC address for the first computer, the second one
being the public MAC address for the first computer, the third one being
the private MAC address of the second computer, etc, you can enter the
first one here and then have the option of generating data to add to your
dhcpd.conf file later in the process.
{note}For VMware virtual machines, the MAC addresses you choose must be in
the range {color:#008000}{*}00:50:56:00:00:00{*}{color}
{color:#008000}\-{color}{color:#008000}{*}00:50:56:3F:FF:FF{*}{color}.
Pay special attention to the upper bound of this range.
{color:#ff0000}{*}00:50:56:40:00:00{*}{color} {color:#ff0000}\-{color}
{color:#ff0000}{*}00:50:56:FF:FF:FF{*}{color} are *NOT* valid VMware
virtual machines.{note}
1. * *State* \- maintenance
1. * *Owner* \- owner of the computer
1. * *RAM*
1. * *Processor Speed*
1. * *Network Speed*
1. * *Type* \- virtualmachine
1. * *Provisioning Engine* \- VMware
1. * Check *All VM Computers* and *newvmimages*
1. Click *Confirm Computers*
1. Click *Submit*
1. If you filled in the private address fields and the Start MAC Address,
you can now enter the private IP address of the management node that will
be handling these virtual machines to generate information to add to your
dhcpd.conf file.

<a name="VCL2.2.1-FurtherStepsifUsingVMware-AssignaVMtoaVirtualHost"></a>
### Assign a VM to a Virtual Host

1. Click *Virtual Hosts*
1. On the *VM Hosts* tab, select the virtual host server added previously.
1. Click *Configure Host*, You should see VM limit set to a number along
with the vm profile, two columns of VM's assigned to host and Unassigned
VMs.
1. Adjust the VM limit to the desired number of vms you would like to run on
this host. Warning please consult your hypervisor documentation for
the&nbsp;recommended number of virtual machines to run concurrently for
your virtual server configuration.
1. Select the virtual machine nodes from the Unassigned VMs: column.&nbsp;
1. Click Add.
