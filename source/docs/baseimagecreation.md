---
title: Creating Base Images from an ISO - Part 1
---

This page describes how to create a base image from an install media. 

These instructions are broken up into parts to assist in providing 
detailed instructions based on the supported provisioning modules and 
Operating Systems. The supported provisioning methods for VCL are (xCAT, 
VMware, and KVM).

{{% toc %}}

### Requirements

Before getting started make sure you have the following requirements 
completed or on hand:
 
 - A working VCL web,database, and management node
 - A Hypervisor either VMWare or KVM(if using hypervisor based images)
 - A working xCAT system(if using bare-metal images)
 - Install media ISO file
 - Appropriate licensing for Windows or RedHat
 
The following must be done before an image can be captured:

 - A computer for the machine being captured has already been added to 
the VCL database
 - VMware or KVM:
    - A VM host computer on which the guest is running has been added 
to the VCL database
    - The guest VM has been assigned to the VM host via the Virtual 
Hosts link on the VCL website
    - Obtain the **private** IP address of the VM from the 
**Manage Computers > Edit Computer Information** part of the site 
for use later in the process


These instructions assume you have root access on your management 
node and are using a bash shell.

### Preparing node under a supported provisioning system

#### VMware ESX/ESXi 4.x, 5.x, vCenter

The instructions assume that VMware has been configured with the 
following bridged networks:

 - **Private**: bridged to private interface: eth0
 - **Public**: bridged to public interface: eth1

 - Launch the vSphere Client, connect to the ESXi host and login
 - Click File > New > Virtual Machine
 - Configuration: **Custom**
 - Name: (doesn't matter)
 - Select a datastore where the VM will reside
 - Virtual Machine Version: **7**
 - Select the appropriate guest OS
 - Number of virtual processors: **1**
 - Memory: **4GB**
 - How many NICs: **2**
     - NIC 1: **Private**, E1000, Connect at Power On: **Yes**
     - NIC 2: **Public**, E1000, Connect at Power On: **Yes**
 - SCSI controller: **LSI Logic Parallel**
 - Create a new virtual disk
    - Disk Size: **at least 30 GB**
    - Allocate and commit space on demand (Thin Provisioning): **Yes**
    - Location: Store with the virtual machine
    - Virtual Device Node: **SCSI (0:0)**
    - Mode: **Not Independent (unchecked)**
 - Edit the virtual machine settings before completion: **Yes**
 - In the Hardware pane, select **Add...**
    - Device Type: CD/DVD Drive
    - Select CD/DVD Media: **Use ISO image**
    - Select ISO Image:
        - Click **Browse**
        - Select the datastore where the ISO is located
        - Click **Open**
        - Select the ISO file
        - Click **Open**
    - Connect at power on: **Yes**
 -Select the New NIC (adding) entry with **Private** listed next to it
 - Under MAC Address, select **Manual**
 - Enter the private MAC address you retrieved earlier
 - Click **Finish**


#### KVM

 - Create guest OS on KVM host...

#### Bare Metal via xCAT

The requirement in this section is to have a working xCAT system.

### Next Steps - Installing OS

#### Install Windows OS for a Base Image



#### Install Linux OS for a Base Image

- Power on the VM and follow the installation instructions for the
Linux distribution and version you are installing.
- On the Linux computer being captured, create a /root/.ssh directory:

    ```bash
    mkdir /root/.ssh
    ```

- On the management node, copy the public SSH identity key to the 
authorized_keys file on the Linux computer being captured: 

    ```bash
    scp /etc/vcl/vcl.key.pub <hostname or IP address>:/root/.ssh/authorized_keys
    ```

- Or replace the above two steps with the following on the management 
node:

    ```bash
    ssh-copy-id -i /etc/vcl/vcl.key <hostname or IP address>
    ```

- Make sure you can login from the management node to the Linux 
computer being captured using the identity key:

    ```bash
    ssh -i /etc/vcl/vcl.key <hostname or IP address>
    ```

Configure the ifcfg-* Files

- Navigate to the network-scripts directory:

    ```bash
    cd /etc/sysconfig/network-scripts
    ```

- Delete any ifcfg-*.bak files:

    ```bash
    rm -f /etc/sysconfig/network-scripts/ifcfg-*.bak
    ```

- Edit every ifcfg-eth* file in the network-scripts directory. Remove 
the HWADDRESS= line if it exists:

    ```bash
    vi ifcfg-eth0
    vi ifcfg-eth1
    ```

- The ifcfg-eth0 file should contain the following:

    ```bash
    DEVICE=eth0
    BOOTPROTO=dhcp
    ONBOOT=yes
    ```

- The ifcfg-eth1 file should contain the following:

    ```bash
    DEVICE=eth1
    BOOTPROTO=dhcp
    ONBOOT=yes
    ```

- Reboot the computer:

    ```bash
    shutdown -r now
    ```

- Check the ifcfg-eth* files to make sure there are no new ifcfg-eth* 
files and that the HWADDRESS= lines have not been automatically added 
back:

    ```bash
    ls /etc/sysconfig/network-scripts
    cat /etc/sysconfig/network-scripts/ifcfg-eth0
    cat /etc/sysconfig/network-scripts/ifcfg-eth1
    ```

### Capture the Image

- Run the following command on the management node:

    ```bash
    /usr/local/vcl/bin/vcld --setup
    ```

- Navigate through the menu options to capture the image

The following happens once you enter an image name and press enter:

   - A new image is added to the VCL database
   - An imaging request is added to the VCL database
   - The vcld -setup automatically initiates 'tail -f /var/log/vcld.log' 
to monitor the vcld log file.  The output should be displayed on the 
screen.

Watch the vcld logfile output to determine if the image capture process 
is successful or terminated because a problem occurred.  When the 
capture process terminates, there will either be a message near the end 
of the output saying "image capture successful" or there will be several 
WARNING messages, the last of which says something to the effect "image 
failed to be captured".  Further troubleshooting is required if the 
image fails to be captured.

### Add the Base Image to an Image Group

The vcld --setup utility does not add the new base image to any image 
groups.  You must add the image to an image group using the VCL website 
after the image capture process is complete.  Reservations for the 
image cannot be made until this is done.  To add the image to an image 
group, browse to the VCL website and select 
**Manage Images > Edit Grouping & Mapping.**
