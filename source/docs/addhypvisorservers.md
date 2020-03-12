---
title: Adding VM Host Servers
---

## Adding Individual VMware Servers

1. Click Manage Computers
2. Select the Add Single Computer radio button
3. Click Submit
4. Fill in the following:
    * Hostname
    * Type - blade
    * Public IP Address
    * Private IP Address
    * Public MAC Address (optional)
    * Private MAC Address (optional)
    * Provisioning Engine - "None"
    * State - vmhostinuse
    * VM Host Profile - use a default profile or one configured in the previous step
    * Owner - admin@Local
    * RAM
    * No. Cores
    * Processor Speed
    * Network Speed
    * Physical Location (optional)
    * Click the checkbox under allComputers
5. Click Confirm Computer
6. Click Submit
    * The computer you just added isn't listed after clicking Submit. This is not a problem.                                                     

## Adding Multiple VMWare Servers

1. Click Manage Computers
2. Select the Add Multiple Computers radio button
3. Click Submit
4. Fill in the following:
    * Hostname - the hostnames of all the computers must have a
                 numerical part that is sequential, use a % as a placeholder
                 where that part would be
    * Start value - the first number of the numerical part of the
                 hostname
    * End value - the last number of the numerical part of the
                 hostname
    * Type - blade
    * Start Public IP Address - if using static public addresses, the
                 IP addresses must be sequential; enter the first address here;
                 if using DHCP, just enter something like 1.1.1.1
    * End Public IP address - the last IP address of the sequence; if
                 using DHCP, you'll need to enter something that would work out
                 to the last address relative to Start Public IP Address (i.e.
                 if adding 3 computers, use 1.1.1.1 for start and 1.1.1.3 for
                 end)
    * Start Private IP Address (optional) - the IP addresses must be
                 sequential; enter the first private address here
    * End Private IP address (optional) - the last IP address of the
                 sequence
    * Start MAC Address (optional) - if MAC addresses are sequential,
                 with the first one being the private MAC address for the first
                 computer, the second one being the public MAC address for the
                 first computer, the third one being the private MAC address of
                 the second computer, etc, you can enter the first one here and
                 then have the option of downloading data to add to your
                 dhcpd.conf file from the Computer Utilities page
    * Provisioning Engine - "None"
    * State - vmhostinuse
    * VM Host Profile - use a default profile or one configured in
                 the previous step
    * Owner - admin@Local
    * RAM
    * No. Cores
    * Processor Speed
    * Network Speed
    * Physical Location (optional)
    * Click the checkbox under allComputers
5. Click Confirm Computers
6. Click Submit

