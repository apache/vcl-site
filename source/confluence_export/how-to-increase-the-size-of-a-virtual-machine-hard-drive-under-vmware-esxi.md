---
title: How to Increase the Size of a Virtual Machine Hard Drive under VMware ESXi
---

{excerpt}This page describes how to increase the size of a VM's hard drive.
This is useful if additional space is needed to install large
applications.{excerpt}

<a name="HowtoIncreasetheSizeofaVirtualMachineHardDriveunderVMwareESXi-CreateaFullCopyoftheVirtualDisk"></a>
### Create a Full Copy of the Virtual Disk

* Determine the VMware host the VM is on
* Shutdown the VM
* Log in to the VM host via SSH
* Navigate to the VM's working directory _(under the VM Working Directory
Path configured in the VM profile)_

{tip:icon=false}cd /vmfs/volumes/vmpath/vclv99-77_1846-v14{tip}

You should see several files in the directory:

    /vmfs/volumes/19873c05-fcd3d912/vclv99-77_1846-v14 # ls -l
    -rw-rw----    1 root	 root		    8684 Aug 13 16:34 nvram
    -rw-------    1 root	 root	      4294967296 Aug 13 16:32
vclv99-77_1846-v14-6197888b.vswp
    -rw-rw----    1 root	 root		   18926 Aug 13 16:32
vclv99-77_1846-v14-Snapshot1.vmsn
    -rw-rw----    1 root	 root		     498 Aug 13 16:32
vclv99-77_1846-v14.vmsd
    --wxrw--wx    1 root	 root		    3464 Aug 13 16:37
vclv99-77_1846-v14.vmx
    --w-rw--w-    1 root	 root		     273 Aug 13 16:32
vclv99-77_1846-v14.vmxf
    -rw-r--r--    1 root	 root		  137538 Aug 13 16:43 vmware.log
    -rw-rw----    1 root	 root	       268505088 Aug 13 19:50
vmwarewin7-Windows764bit1846-v14-000001-delta.vmdk
    -rw-rw----    1 root	 root		     432 Aug 13 16:32
vmwarewin7-Windows764bit1846-v14-000001.vmdk


The VM is configured to run in linked clone mode because a snapshot was
created before the VM was powered on for the first time.  The .vmdk files
in this directory only contain changes made to the master image.  The
master image can be determined by lookin in the vmsn file:

    
    A full copy of the master image and delta files needs to be created in
order to be able to resize the virtual disk.  Run the following command
from the VM's working directory on the VM host:
    {tip:icon=false}vmkfstools \-i vmwarewin7-Windows764bit1846-v14-000001.vmdk
copy.vmdk \-d thin{tip}
    

/vmfs/volumes/19873c05-fcd3d912/vclv99-77_1846-v14 # vmkfstools -i
vmwarewin7-Windows764bit1846-v14-000001.vmdk copy.vmdk -d thin
Destination disk format: VMFS thin-provisioned
Cloning disk 'vmwarewin7-Windows764bit1846-v14-000001.vmdk'...
Clone: 100% done.

    
    h3. Resize the Virtual Disk
    
    Run the following command to resize the virtual disk.  The \-X argument
should specify the total size you want the virtual disk to be, not the
amount of space to add to it:
    {tip:icon=false}vmkfstools \-X 50G copy.vmdk{tip}
    
    h3. Download Gparted Live CD
    
    Download the [GParted Live CD ISO image|http://gparted.sourceforge.net/download.php]
 to one of the datastores mounted on the VM host.&nbsp; The .iso file must
reside on one of the datastores in order to be able to mount it on a VM.
    
    h3. Replace the VM's Hard Drive with the Full Copy
    
    After the copy has been created, reconfigure the VM to use the copy of the
disk instead of the original linked clone.
    * Open vSphere Client
    * Right-click on the VM and select *Edit Settings...*
    * Select *Hard disk 1*
    * Click *Remove*
    * Click *Add...*
    * Select *Use an existing virtual disk*
    * Navigate to the VM's working directory and select the .vmdk corresponding
to the full copy of the virtual disk you created earlier _(copy.vmdk)_
    
    h3. Add a CD Drive to the VM Pointing to the GParted Live CD ISO File
    
    * Click *Add...*
    * Select *CD/DVD Drive*
    * *Use ISO image*
    * Navigate to the Gparted ISO image you downloaded earlier
    * Make sure _Connect at power on_ is selected
    
    !vm-reconfigure.jpg!
    
    h3. Increase the Power On Boot Delay
    
    It can be difficult to catch the initial boot screen when the VM is powered
on in order to press Escape to display the boot menu.&nbsp; Add a delay:
    * Click on the *Options* tab
    * Select *Boot Options*
    * Set the *Power On Boot Delay* to a few seconds _(4000 = 4 seconds)_
    
    !vm-boot-delay.jpg|border=1!
    
    h3. Use GParted to Reconfigure the Partitions
    
    Simply increasing the size of the virtual disk does not cause the amount of
usable space within the VM to increase.&nbsp; The partitions within the
virtual disk need to be reconfigured to use all of the available
space.&nbsp; This cannot be done from the OS of the image stored on the
virtual disk.&nbsp; You must boot the VM using a live CD containing a
partition reconfiguration utility.&nbsp; The GParted Live CD is free and
easy to use.
    
    * With the VM powered off, select the *Console* tab
    * Power on the VM
    * Quickly click inside the *Console* pane
    * Press *Esc* to display the Boot Menu
    * Select *CD-ROM Drive*
    
    The GParted menu should appear.
    
    * Select *GParted Live (Default settings)*
    * Accept the defaults
    
    
    
    Increase the size of the main partition to use all of the space
    * Select the main partition _(should be the largest)_
    * Open the *Partition* menu _(use the mouse of press Alt-p if mouse
operations are difficult)_
    * Select *Resize/Move*
    * Set *New Size (MiB)* to the _Maximum size_ listed above in the box
    * Click *Resize/Move*
    * Open the *Edit* menu
    * Click *Apply All Operations*
    * Click *Apply*
    You should eventually see a message stating _All operations successfully
completed_
    * Click *Close*
    * Reboot the VM to its hard drive
    _If a message appears saying the hard drive needs to be checked for
consistency allow the procedure to complete._
    * Once the VM is rebooted, log in to the image and verify the size of the
hard drive has been increased
    
    The saved VCL image will contain the larger hard drive.
