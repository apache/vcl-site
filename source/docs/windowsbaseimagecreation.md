---
title:  Install a Windows Base Image
---

This page describes how to mount the Windows installation media and install Windows for a base image.

**Mount the Installation Media**

The Windows installation media needs to be mounted as a drive on the computer. The method to do this varies widely based on the provisioning engine being used and resources available. The following lists some ways to mount the installation media:

**VMware - Configure the VM to mount the ISO image as a CD-ROM drive**

Note: these instructions assume a VM has already been created

 1. Copy the Windows installation ISO file to the VMware host server 
 2. Add a CD-ROM drive which mounts the Windows installation ISO image by
    editing the virtual machine settings:
     - Connection: **Use ISO image**:
     - Browse to path of Windows installation ISO image 
     - Save the VM configuration
 
**xCAT using IBM Advanced Management Module**

 1.  Copy the Windows installation ISO file to the management node
 2.  Determine the IP address or hostname of the IBM Advanced Management Module (AMM) for the BladeCenter chassis which contains the blade you are installing
 3.  Open a web browser and enter the AMM's address
 4.  Log in to the AMM
 5.  Select Inactive session timeout value: no timeout
 6.  Click Start New Session
 7.  Click Remote Control
 8.  Click Start Remote Control
 9.  Set the Media Tray and KVM dropdown menus to the blade you are installing
 10. Click Select Image and click the arrow button to the right of it
 11. Navigate to the Windows installation ISO file which was saved to the management node and click Open
 12 . Click Mount All


**Boot to the Windows Installation CD or DVD**

 1. Power on the computer
 2. Press the key to display the boot menu as soon as the computer's POST screen is displayed (usually F12 for bare metal blades or ESC for VMware)
 3. Boot from the CD-ROM drive
 4. Press a key to boot from the CD (this may be displayed at bottom of screen as soon as the computer begins to boot)


**Install Windows**

The Windows installation sequence varies by version. The next 2 sections describe the recommended answers for Windows XP and Windows 7.


**Windows XP Installation**

 1. Press Enter to setup up Windows XP now
 2. Press F8 to agree to the license agreement
 3. Configure the Windows partition
       - Press Enter to set up Windows XP on the selected item (should be called "Unpartitioned space")
       - Format the partition using the NTFS file system (Quick)
 4. Region and Language Options - click Next
 5. Name: VCL
 6. Organization: Apache.org
 7. Enter your Windows XP product key
 8. Computer name: (doesn't matter)
 9. Administrator password: (doesn't matter, but it's recommended that password should match the WINDOWS_ROOT_PASSWORD setting in /etc/vcl/vcld.conf)
 10. Select the timezone
 11. Networking settings: Typical
 12. Member of a domain: No, leave default workgroup settings
 13. Automatic updates: Not right now
 14. Connect to Internet: Skip
 15. Register: no
 16. User name: root 
        - Windows XP setup should finish and the root account created during installation should automatically log on
 17. Once the desktop appears, set root's password via the Windows GUI or by executing the following command from a command prompt:
net user root <password>


**Windows 7 Installation**

 1. Enter the regional information:
      - Language to install: English
      - Time and currency format: English (United States)
      - Keyboard or input method: US
 2. Click Next
 3. Click Install now
     *Setup is starting...*
 4. Click the checkbox next to "I accept the license terms"
 5. Click Next
 6. Click Custom (advanced)
 7. On the "Where do you want to install Windows?" page, delete all existing partitions and create a new partition using all of the available space:
      - Click Drive options (advanced)
      - Click Delete, then click OK to confirm
      - Click New
      - Click Apply (the size should be set to the maximum amount available
                 *To ensure that all Windows features work correctly, Windows might create additional partitions for system files.*
      - Click OK
 8. Click Next
       - *Installing Windows...*
       - *Windows restarts*
       - *Starting Windows*
       - *Setup is updating registry settings*
 9. A screen titled "Set Up Windows" appears:
       - Type a user name: root
       - Type a computer name: it's best to name the computer after the OS (Example: win7sp1-ent)
 10. Enter a password, password hint, and click Next
 11. Help protect your computer and improve Windows automatically: Ask me later
 12. Select a time zone, set the correct time, and click Next
         - *Windows is finalizing your settings*
         - *Preparing your desktop*
         - *Desktop appears*
 13. If asked to set a network location, choose Work network
      - *The root account logs in...*


**Windows Server 2008**

