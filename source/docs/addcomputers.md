---
title: Add computers
---

Adding computers is done by going to Manage Computers->Edit Computer 
Profiles and clicking Add New Computer

[Adding Individual Bare Metal Computers](#individualbare)<br>
[Adding Individual Virtual Computers](#individualvirtual)<br>
[Adding Multiple Bare Metal Computers](#multiplebare)<br>
[Adding Multiple Virtual Computers](#multiplevirtual)

#### Adding Individual Bare Metal Computers {#individualbare}

 1. Click Manage Computers
 2. Select the Edit Computer Profiles radio button
 3. Click Submit
 3. Click the Add New Computer button at the top of the page
 3. Ensure Single Computer is selected for Add at the top of the dialog
 4. Fill in the following:
       - Name - hostname of the computer
       - Owner - admin@Local
       - Type - Bare Metal
       - Public IP Address
       - Private IP Address (optional)
       - Public MAC Address (optional)
       - Private MAC Address (optional)
       - Provisioning Engine - None or xCAT
       - State - one of
           - available (only if xCAT is selected for Provisioning Engine)
           - vmhostinuse (only if None is selected for Provisioning Engine)
           - maintenance - if you do not want it to be immediately available
       - VM Host Profile - (only if vmhostinuse is selected for State) profile for this VM Host
       - RAM
       - No. Cores
       - Processor Speed
       - Network Speed
       - Connect Using NAT - check if this computer should be connected to using NAT (optional)
       - NAT Host - Host that will provide NAT to this host (optional)
       - Use as NAT Host - check if this host will provide NAT to other hosts (optional)
       - NAT Public IP Address - Public address for this NAT host (optional)
       - NAT Internal IP Address - internal IP address for this NAT Host (optional)
       - Location (optional)
 5. Click Add Computer
 5. A dialog will be displayed for adding the computer to computer groups
 5. Select allComputers and newimages on the right
 5. Click <-Add
 6. Click Close

#### Adding Individual Virtual Computers {#individualvirtual}

 1. Click Manage Computers
 2. Select the Edit Computer Profiles radio button
 3. Click Submit
 3. Click the Add New Computer button at the top of the page
 3. Ensure Single Computer is selected for Add at the top of the dialog
 4. Fill in the following:
       - Name - hostname of the computer
       - Owner - admin@Local
       - Type - Virtual Machine
       - Public IP Address
       - Private IP Address (optional)
       - Public MAC Address
       - Private MAC Address
       - Provisioning Engine - select the desired Provisioning Engine (use Libvirt when using KVM)
       - State - maintenance is the only option (will be moved to available when assigned to a VM Host)
       - RAM
       - No. Cores
       - Processor Speed
       - Network Speed
       - Connect Using NAT - check if this computer should be connected to using NAT (optional)
       - NAT Host - Host that will provide NAT to this host (optional)
       - Use as NAT Host - check if this host will provide NAT to other hosts (optional)
       - NAT Public IP Address - Public address for this NAT host (optional)
       - NAT Internal IP Address - internal IP address for this NAT Host (optional)
       - Location (optional)
 5. Click Add Computer
 5. A dialog will be displayed for adding the computer to computer groups
 5. Select All VM Computers and newvmimages on the right
 5. Click <-Add
 6. Click Close

#### Adding Multiple Bare Metal Computers {#multiplebare}

 1. Click Manage Computers
 2. Select the Edit Computer Profiles radio button
 3. Click Submit
 3. Click the Add New Computer button at the top of the page
 3. Select Multiple Computers for Add at the top of the dialog
 4. Fill in the following:
    * Name - the hostnames of all the computers must have a
        numerical part that is sequential, use a % as a placeholder
         where that part would be
    * Start - the first number of the numerical part of the hostname
    * End - the last number of the numerical part of the hostname
    * Owner - admin@Local
    * Type - Bare Metal
    * Start Public IP Address - if using static public addresses,
       the IP addresses must be sequential; enter the first address
       here; if using DHCP, just enter something like 1.1.1.1
    * End Public IP address - the last IP address of the sequence; if
        using DHCP, you'll need to enter something that would work out
        to the last address relative to Start IP Address (i.e. if
        adding 3 computers, use 1.1.1.1 for start and 1.1.1.3 for end)
    * Start Private IP Address (optional) - the IP addresses must be
       sequential; enter the first private address here
    * End Private IP Address (optional) - the last IP address of the sequence
    * Start MAC Address (optional) - if MAC addresses are sequential,
        with the first one being the private MAC address for the first
        computer, the second one being the public MAC address for the
        first computer, the third one being the private MAC address of
        the second computer, etc, you can enter the first one here and
        then have the option of downloading data to add to your
        dhcpd.conf file from the Computer Utilities page
    * Provisioning Engine - None or xCAT
    * State - one of
       * available (only if xCAT is selected for Provisioning Engine)
       * vmhostinuse (only if None is selected for Provisioning Engine)
       * maintenance - if you do not want it to be immediately available
    * VM Host Profile - (only if vmhostinuse is selected for State) profile for these VM Hosts
    * RAM
    * No. Cores
    * Processor Speed
    * Network Speed
    * Connect Using NAT - check if these computers should be connected to using NAT (optional)
    * NAT Host - Host that will provide NAT to these computers (optional)
    * Location (optional)
 5. Click Add Computers
 5. A dialog will be displayed for adding the computers to computer groups
 5. Select allComputers and newimages on the right
 5. Click <-Add
 6. Click Close


#### Adding Multiple Virtual Computers {#multiplevirtual}

 1. Click Manage Computers
 2. Select the Edit Computer Profiles radio button
 3. Click Submit
 3. Click the Add New Computer button at the top of the page
 3. Select Multiple Computers for Add at the top of the dialog
 4. Fill in the following:
    * Name - the hostnames of all the computers must have a
        numerical part that is sequential, use a % as a placeholder
         where that part would be
    * Start - the first number of the numerical part of the hostname
    * End - the last number of the numerical part of the hostname
    * Owner - admin@Local
    * Type - Virtual Machine
    * Start Public IP Address - if using static public addresses,
       the IP addresses must be sequential; enter the first address
       here; if using DHCP, just enter something like 1.1.1.1
    * End Public IP address - the last IP address of the sequence; if
        using DHCP, you'll need to enter something that would work out
        to the last address relative to Start IP Address (i.e. if
        adding 3 computers, use 1.1.1.1 for start and 1.1.1.3 for end)
    * Start Private IP Address - the IP addresses must be
       sequential; enter the first private address here
    * End Private IP Address - the last IP address of the sequence
    * Start MAC Address - if MAC addresses are sequential,
        with the first one being the private MAC address for the first
        computer, the second one being the public MAC address for the
        first computer, the third one being the private MAC address of
        the second computer, etc, you can enter the first one here and
        then have the option of downloading data to add to your
        dhcpd.conf file from the Computer Utilities page
    * Provisioning Engine - select the desired Provisioning Engine (use Libvirt when using KVM)
    * State - maintenance is the only option (will be moved to available when assigned to a VM Host)
    * RAM
    * No. Cores
    * Processor Speed
    * Network Speed
    * Connect Using NAT - check if these computers should be connected to using NAT (optional)
    * NAT Host - Host that will provide NAT to these computers (optional)
    * Location (optional)
 5. Click Add Computers
 5. A dialog will be displayed for adding the computers to computer groups
 5. Select All VM Computers and newvmimages on the right
 5. Click <-Add
 6. Click Close

