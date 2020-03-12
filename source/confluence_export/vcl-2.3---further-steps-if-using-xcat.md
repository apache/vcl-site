---
title: VCL 2.3 - Further steps if using xCAT
---

Once you have added at least one computer, you can add more computers by
going to Manage Computers->Edit Computer Information and clicking *Add
Single Computer* or *Add Multiple Computers"*.

<a name="VCL2.3-FurtherstepsifusingxCAT-AddingIndividualComputers"></a>
### Adding Individual Computers

1. Click *Manage Computers*
1. Select the *Add Single Computer* radio button
1. Click *Submit*
1. Fill in the following:
1. * *Hostname*
1. * *Type* - blade
1. * *Public IP Address*
1. * *Private IP Address* (optional)
1. * *Public MAC Address* (optional)
1. * *Private MAC Address* (optional)
1. * *Provisioning Engine* - xCAT 2.x
1. * *State* - available (or maintenance if you do not want it to be
immediately available)
1. * *Owner* - admin@Local
1. * *RAM*
1. * *No. Cores*
1. * *Processor Speed*
1. * *Network Speed*
1. * *Physical Location* (optional)
1. * Click the checkboxs under *allComputers* and *newimages*
1. Click *Confirm Computer*
1. Click *Submit*
{info}The computer you just added isn't listed after clicking Submit. This
is not a problem.{info}

<a name="VCL2.3-FurtherstepsifusingxCAT-AddingMultipleComputers"></a>
### Adding Multiple Computers

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
1. * *Provisioning Engine* \- xCAT 2.x
1. * *State* \- available (or maintenance if you do not want them to be
immediately available)
1. * *Owner* - owner of the computer
1. * *RAM*
1. * *Processor Speed*
1. * *Network Speed*
1. * Click the checkboxs under *allComputers* and *newimages*
1. Click *Confirm Computers*
1. Click *Submit*
{info}The computer you just added isn't listed after clicking Submit. This
is not a problem.{info}

<a name="VCL2.3-FurtherstepsifusingxCAT-Addentriesto/etc/hosts"></a>
## Add entries to /etc/hosts

You need to add entries for your nodes to /etc/hosts
1. Click *Manage Computers*
1. Select the *allComputers* group in the list at the top
1. Select the *Computer Utilities* radio button
1. Click *Submit*
1. Click the *Check All* link at the bottom of the table
1. Next to *For selected computers, generate computer data for*, select
*/etc/hosts*
1. Click *Generate Data*
1. Copy/Paste the data to your /etc/hosts file
1. Click *Close*
