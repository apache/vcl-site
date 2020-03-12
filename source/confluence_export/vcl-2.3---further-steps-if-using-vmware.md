---
title: VCL 2.3 - Further Steps if Using VMware
---

If you are using standalone VMware servers (i.e. ones that VCL did not
deploy using xCAT), you first need to configure a VM Profile to match your
setup. Next, add the VMWare servers. Then, you need to add the virtual
machines. You can either add them individually (Adding Individual VMWare
Servers/Virtual Machines), or if they have sequential hostnames and IP
addresses, you can add them all at once (Adding Multiple VMWare
Servers/Virtual Machines).

Once you have added at least one computer, you can add more computers by
going to Manage Computers->Edit Computer Information and clicking *Add
Single Computer* or *Add Multiple Computers*.

1. [Configure VM Profile(s)](vcl-2.3---further-steps-if-using-vmware#vmprofile.html)
1. [Add VMware Host Servers](vcl-2.3---further-steps-if-using-vmware#addhosts.html)
1. [Add Virtual Machines](vcl-2.3---further-steps-if-using-vmware#addvms.html)
1. [Assign Virtual Machine(s) to a Virtual Host](vcl-2.3---further-steps-if-using-vmware#assignvms.html)
1. [Add entries to dhcpd.conf](vcl-2.3---further-steps-if-using-vmware#adddhcp.html)
1. [Add entries to /etc/hosts](vcl-2.3---further-steps-if-using-vmware#addetchosts.html)

{anchor:vmprofile}

<a name="VCL2.3-FurtherStepsifUsingVMware-ConfigureVMProfile(s)"></a>
## Configure VM Profile(s)

1. Click *Virtual Hosts*
1. Select the *VM Host Profiles* tab
1. Select a profile whose name matches your setup or click *New Profile...*
1. # If using an existing profile, click *Configure Profile*
1. # If creating a new profile:
1. ## Enter the name of the profile
1. ## Click *Create Profile*
1. Configure the profile to match your setup. Hover over any ? icons to get
further information about that field. More information is available on the [VMware Configuration](vmware-configuration.html)
 page
{tip}
Just click on the text of any field you want to edit to change it. After
changing it, click somewhere else to save the changed value for that field.
Changes are immediate; there is no "save" button for this tab.
{tip}

{anchor:addhosts}

<a name="VCL2.3-FurtherStepsifUsingVMware-AddVMwareHostServers"></a>
## Add VMware Host Servers

<a name="VCL2.3-FurtherStepsifUsingVMware-AddingIndividualVMwareServers"></a>
### Adding Individual VMware Servers

1. Click *Manage Computers*
1. Select the *Add Single Computer* radio button
1. Click *Submit*
1. Fill in the following:
1. * *Hostname*
1. * *Type* \- blade
1. * *Public IP Address*
1. * *Private IP Address* (optional)
1. * *Public MAC Address* (optional)
1. * *Private MAC Address* (optional)
1. * *Provisioning Engine* \- "None"
1. * *State* \- vmhostinuse
1. * *VM Host Profile* \- use a default profile or one configured in the
previous step
1. * *Owner* \- admin@Local
1. * *RAM*
1. * *No. Cores*
1. * *Processor Speed*
1. * *Network Speed*
1. * *Physical Location* (optional)
1. * Click the checkbox under *allComputers*
1. Click *Confirm Computer*
1. Click *Submit*
{info}The computer you just added isn't listed after clicking Submit. This
is not a problem.{info}

<a name="VCL2.3-FurtherStepsifUsingVMware-AddingMultipleVMWareServers"></a>
### Adding Multiple VMWare Servers

1. Click *Manage Computers*
1. Select the *Add Multiple Computers* radio button
1. Click *Submit*
1. Fill in the following:
1. * *Hostname* \- the hostnames of all the computers must have a numerical
part that is sequential, use a % as a placeholder where that part would be
1. * *Start value* \- the first number of the numerical part of the hostname
1. * *End value* \- the last number of the numerical part of the hostname
1. * *Type* \- blade
1. * *Start Public IP Address* \- if using static public addresses, the IP
addresses must be sequential; enter the first address here; if using DHCP,
just enter something like 1.1.1.1
1. * *End Public IP address* \- the last IP address of the sequence; if using
DHCP, you'll need to enter something that would work out to the last
address relative to *Start Public IP Address* (i.e. if adding 3 computers,
use 1.1.1.1 for start and 1.1.1.3 for end)
1. * *Start Private IP Address* (optional) - the IP addresses must be
sequential; enter the first private address here
1. * *End Private IP Address* (optional) - the last IP address of the
sequence
1. * *Start MAC Address* (optional) - if MAC addresses are sequential, with
the first one being the private MAC address for the first computer, the
second one being the public MAC address for the first computer, the third
one being the private MAC address of the second computer, etc, you can
enter the first one here and then have the option of downloading data to
add to your dhcpd.conf file from the Computer Utilities page
1. * *Provisioning Engine* \- "None"
1. * *State* \- vmhostinuse
1. * *VM Host Profile* \- use a default profile or one configured in the
previous step
1. * *Owner* \- admin@Local
1. * *RAM*
1. * *No. Cores*
1. * *Processor Speed*
1. * *Network Speed*
1. * *Physical Location* (optional)
1. * Click the checkbox under *allComputers*
1. Click *Confirm Computers*
1. Click *Submit*

{anchor:addvms}

<a name="VCL2.3-FurtherStepsifUsingVMware-AddVirtualMachines"></a>
## Add Virtual Machines

<a name="VCL2.3-FurtherStepsifUsingVMware-AddingIndividualVirtualMachines"></a>
### Adding Individual Virtual Machines

1. Click *Manage Computers*
1. Select *Edit Computer Information*
1. Click *Submit*
1. Click *Add Single Computer*
1. Fill in the following:
1. * *Hostname*
1. * *Type* \- virtualmachine
1. * *Public IP Address*
1. * *Private IP Address*
1. * *Public MAC Address*
1. * *Private MAC Address*
{note}For VMware virtual machines, the MAC addresses you choose must be in
the range {color:#008000}{*}00:50:56:00:00:00{*}{color}
{color:#008000}\-{color}{color:#008000}{*}00:50:56:3F:FF:FF{*}{color}.
Pay special attention to the upper bound of this range.
{color:#ff0000}{*}00:50:56:40:00:00{*}{color} {color:#ff0000}\-{color}
{color:#ff0000}{*}00:50:56:FF:FF:FF{*}{color} are *NOT* valid VMware
virtual machines.{note}
1. * *Provisioning Engine* \- VMware
1. * *State* \- maintenance
1. * *Owner* \- admin@Local
1. * *RAM*
1. * *No. Cores*
1. * *Processor Speed*
1. * *Network Speed*
1. * Check *All VM Computers* and *newvmimages*
1. Click *Confirm Computer*
1. Click *Submit*

<a name="VCL2.3-FurtherStepsifUsingVMware-AddingMultipleVirtualMachines"></a>
### Adding Multiple Virtual Machines

1. Click *Manage Computers*
1. Select *Edit Computer Information*
1. Click *Submit*
1. Click *Add Multiple Computers*
1. Fill in the following:
1. * *Hostname* \- the hostnames of all the computers must have a numerical
part that is sequential, use a % as a placeholder where that part would be
1. * *Start value* \- the first number of the numerical part of the hostname
1. * *End value* \- the last number of the numerical part of the hostname
1. * *Type* \- virtualmachine
1. * *Start Public IP Address* \- if using static public addresses, the
Public IP addresses must be sequential; enter the first address here; if
using DHCP, just enter something like 1.1.1.1
1. * *End Public IP address* \- the last Public IP address of the sequence;
if using DHCP, you'll need to enter something that would work out to the
last address relative to Start IP Address (i.e. if adding 3 computers, use
1.1.1.1 for start and 1.1.1.3 for end)
1. * *Start Private IP Address* \- similar to Start Public IP Address, but
for the private side
1. * *End Private IP Address* \- similar to the End Public IP Address but for
the private side
1. * *Start MAC Address* \- if mac addresses are sequential, with the first
one being the private MAC address for the first computer, the second one
being the public MAC address for the first computer, the third one being
the private MAC address of the second computer, etc, you can enter the
first one here and then have the option of generating data to add to your
dhcpd.conf file from the *Computer Utilities* page.
{note}For VMware virtual machines, the MAC addresses you choose must be in
the range {color:#008000}{*}00:50:56:00:00:00{*}{color}
{color:#008000}\-{color}{color:#008000}{*}00:50:56:3F:FF:FF{*}{color}.
Pay special attention to the upper bound of this range.
{color:#ff0000}{*}00:50:56:40:00:00{*}{color} {color:#ff0000}\-{color}
{color:#ff0000}{*}00:50:56:FF:FF:FF{*}{color} are *NOT* valid VMware
virtual machines.{note}
1. * *Provisioning Engine* \- VMware
1. * *State* \- maintenance
1. * *Owner* \- admin@Local
1. * *RAM*
1. * *No. Cores*
1. * *Processor Speed*
1. * *Network Speed*
1. * Check *All VM Computers* and *newvmimages*
1. Click *Confirm Computers*
1. Click *Submit*

{anchor:assignvms}

<a name="VCL2.3-FurtherStepsifUsingVMware-AssignVirtualMachine(s)toaVirtualHost"></a>
## Assign Virtual Machine(s) to a Virtual Host

1. Click *Virtual Hosts*
1. On the *VM Hosts* tab, select the virtual host server added previously
1. Click *Configure Host*, You should see VM limit set to a number along
with the vm profile, two columns of VM's assigned to host and Unassigned
VMs
1. Adjust the VM limit to the desired number of vms you would like to run on
this host.
{note}
Please consult your hypervisor documentation for the&nbsp;recommended
number of virtual machines to run concurrently for your virtual server
configuration
{note}
1. Select the virtual machine nodes from the Unassigned VMs: column
1. Click Add

{anchor:adddhcp}

<a name="VCL2.3-FurtherStepsifUsingVMware-Addentriestodhcpd.conf"></a>
## Add entries to dhcpd.conf

You need to add entries for your VMs to your dhcpd.conf file so that they
will correctly be assigned their private addresses at boot.
1. Click *Manage Computers*
1. Select the *All VM Computers* group in the list at the top
1. Select the *Computer Utilities* radio button
1. Click *Submit*
1. Click the *Check All* link at the bottom of the table
1. Next to *For selected computers, generate computer data for*, select
*dhcpd*
1. Click *Generate Data*
1. Enter the private IP address for your management node
1. Click *Generate Data*
1. Copy/Paste the data for dhcpd.conf to the dhcpd.conf file on your
management node (ignore the part for dhcpd.leases)
1. Restart dhcpd
{tip}service dhcpd restart{tip}
1. Scroll to the bottom and click *Close*

{anchor:addetchosts}

<a name="VCL2.3-FurtherStepsifUsingVMware-Addentriesto/etc/hosts"></a>
## Add entries to /etc/hosts

You need to add entries for your VM hosts and VMs to /etc/hosts
1. Click *Manage Computers*
1. Select the *All VM Computers* and the *allComputers* groups in the list
at the top
1. Select the *Computer Utilities* radio button
1. Click *Submit*
1. Click the *Check All* link at the bottom of the table
1. Next to *For selected computers, generate computer data for*, select
*/etc/hosts*
1. Click *Generate Data*
1. Copy/Paste the data to your /etc/hosts file
1. Click *Close*
