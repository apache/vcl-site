---
title: VCL 2.2.1 - Further steps if using xCAT
---

You can initially add individual computers or multiple computers all
together. After you have added at least one computer, you will need to go
to Manage Computers \-> Edit Computer Information to additional ones.

<a name="VCL2.2.1-FurtherstepsifusingxCAT-AddingIndividualComputers"></a>
### Adding Individual Computers

1. click "Manage Computers"
1. select the "Add Single Computer" radio button
1. click Submit
1. fill in Hostname, IP Address, owner (admin@Local), RAM, Proc Speed,
Network Speed, select "blade" for Type, select "xCAT 2.x Provisioning" for
"Provisioning Engine", and click the checkbox under "allcomputers", and
"newimages"
1. click Confirm Computer
1. click Submit (don't worry about the fact that the computer you just added
isn't listed after clicking Submit)
1. after you've configured your image library and your management node has
started checking in, you should be able to make a reservation

<a name="VCL2.2.1-FurtherstepsifusingxCAT-AddingMultipleComputers"></a>
### Adding Multiple Computers

1. click "Manage Computers"
1. select the "Add Multiple Computers" radio button
1. click Submit
1. fill in
1. * Hostname - the hostnames of all the computers must have a numerical part
that is sequential, use a % as a placeholder where that part would be
1. * Start value - the first number of the numerical part of the hostname
1. * End value - the last number of the numerical part of the hostname
1. * Start IP Address - if using static public addresses, the IP addresses
must be sequential; enter the first address here; if using DHCP, just enter
something like 1.1.1.1
1. * End IP address - the last IP address of the sequence; if using DHCP,
you'll need to enter something that would work out to the last address
relative to Start IP Address (i.e. if adding 3 computers, use 1.1.1.1 for
start and 1.1.1.3 for end)
1. * Owner - owner of the computer
1. * RAM
1. * Processor Speed
1. * Network Speed
1. * Type - blade
1. * Provisioning Engine - xCAT 2.x
1. * check allComputers and newimages
1. click Confirm Computer
1. click Submit (don't worry about the fact that the computers you just
added aren't listed after clicking Submit)
1. after you've configured your image library and your management node has
started checking in, you should be able to make a reservation
