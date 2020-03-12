---
title: Creating a Virtual Machine for the VCL Server
---

1. {color:#000000}Create a reservation for the vSphere client image{color}##
{color:#000000}Log into{color} [https://vcl.ncsu.edu](https://vcl.ncsu.edu/)
1. # {color:#000000}Click{color} {color:#000000}New Reservation{color}
1. # {color:#000000}Select{color} {color:#000000}VMware vSphere Client
Bootcamp 2011{color}
1. # {color:#000000}Click Create Reservation{color}{color:#000000}Wait for
the reservation to be ready, Connect button appears{color}
1. # {color:#000000}Click{color} {color:#000000}Connect{color}
1. # {color:#000000}Connect to the reservation via RDP and login{color}
1. {color:#000000}Log into the ESXi host{color}## {color:#000000}Launch
the{color} {color:#000000}VMware vSphere Client{color}
{color:#000000}application{color}### {color:#000000}IP Address:{color}
{color:#000000}enter the IP address you were given{color}
1. ## {color:#000000}Username:{color} {color:#000000}root{color}
1. ## {color:#000000}Password:{color}
{color:#000000}{*}_<password>_{*}{color}
1. # {color:#000000}Click Login{color}
1. # {color:#000000}If presented with a Security Warning box, click the
“Install this certificate...” checkbox and then click Ignore{color}
1. {color:#000000}Create a virtual machine for your VCL server{color}##
{color:#000000}Click File > New > Virtual Machine{color}
1. # {color:#000000}Configuration:{color} {color:#000000}Custom{color}
1. # {color:#000000}Name:{color} {color:#000000}vcl-server{color}
1. # {color:#000000}Datastore:{color} {color:#000000}local{color}
1. # {color:#000000}Virtual Machine Version:{color} {color:#000000}7{color}
1. # {color:#000000}Guest Operating System:{color}
{color:#000000}Linux{color}### {color:#000000}Version:{color}
{color:#000000}CentOS 4/5 (32-bit){color}
1. # {color:#000000}Number of virutal processors: 1{color}
1. # {color:#000000}Memory Size: 1 GB{color}
1. # {color:#000000}How many Nics: 2{color}### {color:#000000}NIC 1:{color}
{color:#000000}Private{color}{color:#000000}, Adapter: E1000, Connect at
Power On: Yes{color}
1. ## {color:#000000}NIC 2:{color}
{color:#000000}Public{color}{color:#000000}, Adapter: E1000, Connect at
Power On: Yes{color}
1. # {color:#000000}SCSI controller: LSI Logic Parallel{color}
1. # {color:#000000}Disk: Create a new virtual disk{color}###
{color:#000000}Disk Size: 8 GB{color}
1. ## {color:#000000}Allocate and commit space on demand (Thin
Provisioning):{color} {color:#000000}Yes{color}
1. ## {color:#000000}Support clustering: No{color}
1. ## {color:#000000}Location: Store with the virtual machine{color}
1. # {color:#000000}Virtual Device Node: SCSI (0:0){color}###
{color:#000000}Mode:{color}
{color:#000000}Independent{color}{color:#000000},{color}
{color:#000000}Persistent{color}
1. # {color:#000000}Edit the virtual machine settings before
completion:{color} {color:#000000}Yes{color}
1. # {color:#000000}Select the CD/DVD device{color}### {color:#000000}Change
Device Type to:{color} {color:#000000}Datastore ISO File{color}
1. ## {color:#000000}Click Browse{color}#### {color:#000000}Navigate
to{color} {color:#000000}local/iso{color}
1. ### {color:#000000}Select:{color}
{color:#000000}CentOS-5.6-i386-bin-DVD.iso{color}
1. ## {color:#000000}Connect at power on:{color} {color:#000000}Yes{color}
1. # {color:#000000}Click{color} {color:#000000}Finish{color}
1. {color:#000000}Install the VCL Server OS{color}## {color:#000000}Click
the plus sign in the left pane to display the VM{color}
1. # {color:#000000}Select the{color} {color:#000000}VCL Server{color}
{color:#000000}VM{color}
1. # {color:#000000}Click the{color} {color:#000000}Console{color}
{color:#000000}tab{color}
1. # {color:#000000}Click the play button to start the VM{color}
1. # {color:#000000}To install in or upgrade in graphical mode: press
Enter{color}
1. # {color:#000000}Choose{color} {color:#000000}Skip{color}
{color:#000000}to skip the media testthe GUI installation begins...{color}
1. # {color:#000000}Click Next{color}
1. # {color:#000000}Select English{color}
1. # {color:#000000}Would you like to initialize this drive:{color}
{color:#000000}Yes{color}
1. # {color:#000000}Click Next to use the default partitioning scheme{color}
1. # {color:#000000}Network Devices:{color}### {color:#000000}Select{color}
{color:#000000}eth0{color} {color:#000000}and click Edit{color}####
{color:#000000}Enable IPv4 support: Yes{color}##### {color:#000000}Manual
configuration{color}###### {color:#000000}IP Address:{color}
{color:#000000}10.100.0.1{color}
1. ##### {color:#000000}Prefix (Netmask):{color}
{color:#000000}255.255.255.0{color}
1. ### {color:#000000}Enable IPv6 support:{color} {color:#000000}No{color}
1. ## {color:#000000}Select{color} {color:#000000}eth1{color}
{color:#000000}and click Edit{color}#### {color:#000000}Enable IPv4
support: Yes{color}##### {color:#000000}Dynamic IP configuration
(DHCP){color}
1. ### {color:#000000}Enable IPv6 support:{color} {color:#000000}No{color}
1. ## {color:#000000}eth1 - Activate on Boot:{color}
{color:#000000}Yes{color}
1. # {color:#000000}Select a timezone{color}
1. # {color:#000000}Root Password:{color} {color:#000000}_<password>_{color}
1. # {color:#000000}Software packages - uncheck{color} {color:#000000}Desktop
- Gnome{color}
1. # {color:#000000}Reboot the VM when the installation is complete{color}
1. # {color:#000000}Select the item that you wish to modify: click
Exit{color}
1. # {color:#000000}Login as root{color}
1. # {color:#000000}Verify the networking: ifconfig{color}###
{color:#000000}eth0 should be assigned 10.100.0.1{color}
1. ## {color:#000000}eth1 should be assigned a public IP address:
152.46.x.x{color}
1. {color:#000000}Log in via SSH{color}## {color:#000000}Launch PuTTY from
the computer you connected to via RDP{color}### {color:#000000}Host Name:
Enter the public IP address of the VCL server which is displayed in the
ifconfig output{color}
1. ## {color:#000000}Saved Sessions: enter ‘vcl-server’{color}
1. ## {color:#000000}Click Save{color}
1. # {color:#000000}Connect to vcl-server{color}
1. # {color:#000000}Login as root{color}
1. {color:#000000}Install the VCL components:{color}[https://cwiki.apache.org/confluence/display/VCL/VCL+2.2.1+Installation](https://cwiki.apache.org/display/VCL/VCL+2.2.1+Installation)
