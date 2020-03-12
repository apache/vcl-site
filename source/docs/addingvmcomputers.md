---
title: Adding computers
---

### Adding Individual Virtual Machines

 1. Click Manage Computers
 2. Select Edit Computer Information
 3. Click Submit
 4. Click Add Single Computer
 5. Fill in the following:
     * Hostname
     * Type - virtualmachine
     * Public IP Address
     * Private IP Address
     * Public MAC Address
     * Private MAC Address

            NOTE: For VMware virtual machines, the MAC addresses you choose
            must be in the range 00:50:56:00:00:00 - 00:50:56:3F:FF:FF. Pay
            special attention to the upper bound of this range. 
            00:50:56:40:00:00 - 00:50:56:FF:FF:FF are NOT valid VMware
            virtual machines.

     * Provisioning Engine - VMware or Libvirt Virtualization API
     * State - maintenance
     * Owner - admin@Local
     * RAM
     * No. Cores
     * Processor Speed
     * Network Speed
     * Check All VM Computers and newvmimages
 6. Click Confirm Computer
 7. Click Submit

### Adding Multiple Virtual Machines

 1. Click Manage Computers
 2. Select Edit Computer Information
 3. Click Submit
 4. Click Add Multiple Computers
 5. Fill in the following:
     * Hostname - the hostnames of all the computers must have a
        numerical part that is sequential, use a % as a placeholder
         where that part would be
     * Start value - the first number of the numerical part of the hostname
     * End value - the last number of the numerical part of the hostname
     * Type - virtualmachine
     * Start Public IP Address - if using static public addresses, the
         IP addresses must be sequential; enter the first address here;
          if using DHCP, just enter something like 1.1.1.1
      * End Public IP address - the last IP address of the sequence; if
         using DHCP, you'll need to enter something that would work out
          to the last address relative to Start Public IP Address (i.e.
          if adding 3 computers, use 1.1.1.1 for start and 1.1.1.3 for end)
     * Start Private IP Address - similar to Start IP Address, but for the private side
     * End Private IP Address - similar to the End IP Address but for the private side
     * Start MAC Address - if MAC addresses are sequential, with the
        first one being the private MAC address for the first computer,
        the second one being the public MAC address for the first
        computer, the third one being the private MAC address of the
         second computer, etc, you can enter the first one here and then
         have the option of downloading data to add to your dhcpd.conf
         file from the Computer Utilities page

                 NOTE: For VMware virtual machines, the MAC addresses you choose
                 must be in the range 00:50:56:00:00:00 - 00:50:56:3F:FF:FF. Pay
                 special attention to the upper bound of this range. 
                 00:50:56:40:00:00 - 00:50:56:FF:FF:FF are NOT valid VMware
                 virtual machines.

     * Provisioning Engine - VMware or Libvirt Virtualization API
     * State - maintenance
     * Owner - admin@Local
     * RAM
     * No. Cores
     * Processor Speed
     * Network Speed
     * Check All VM Computers and newvmimages

 6. Click Confirm Computers
 7. Click Submit


