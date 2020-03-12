---
title: "VCL Image Scripts: Post-Load, Post-Reserve, & Post-Reservation"
---

Scripts may be saved within VCL images which are automatically executed at specific stages of the 
VCL 
reservation process.  The scripts are added by the image creator prior to saving the image.  They 
must be 
located and named exactly as specified below.

For Windows image scripts, the output is saved in C:\Cygwin\root\VCL\Scripts\Logs.  The name of 
the log file name corresponds to the name of the script.  Example: 
C:\Cygwin\root\VCL\Scripts\Logs\vcl_post_load.log

## Post-Load

Location:

* Linux: /usr/local/vcl/vcl_post_load
* Windows: C:\Windows\vcl_post_load.cmd

The post-load script will be executed every time a compute node is loaded, meaning:

* Whether or not the compute node is assigned to a user's reservation
* After a user's reservation ends and the compute node is automatically reloaded with another 
image
* After a compute node is reloaded with a specific image via the Manage Computers utility

The post-load script is executed after all of the standard *post-load* steps are performed via 
SSH by the 
management node's vcld process.  For Linux images, these steps include:

* Secure the firewall to only allow access from the management node
* Configure the SSH service so access is only permitted from the management node
* Randomize the root password
* Set the node's hostname

It is **important** to recognize that the steps listed above to not include any steps related to 
the creation 
or configuration of user accounts intended for end user connections.  The user accounts have not 
been created 
prior to the stage when the post-load script is executed.

The post-load script is useful for:

* Making changes to configuration files which require the IP address of the compute node to be 
known
* Registering the compute node with an external service such as for OS activation or software 
licensing
* Mounting external storage intended for system files or logs

## Post-Reserve

Location:

* Linux: /usr/local/vcl/vcl_post_reserve
* Windows: C:\Windows\vcl_post_reserve.cmd

The post-reserve script is only executed when a user makes a reservation for an image and 
acknowledges the 
reservation by clicking the Connect button.  It is executed after the standard *reserve* steps 
are performed 
via SSH by the management node's vcld process.  These steps include:

* Add user account(s) and set passwords if applicable
* Grant access via SSH and other connect methods
* For cluster reservations, the /etc/cluster_info file is created

The post-reserve script is useful for:

* Making changes to configuration files which require the username(s) to be known
* Starting services which should only run when the compute node is available to an end user
* Configuring the firewall to allow access to a particular service
* Configuring interaction with other compute nodes assigned to a cluster by parsing the 
cluster_info file and 
modifying configuration files with information about the other cluster nodes
* Mounting external storage intended for user files

## Post-Reservation

Location:

* Linux: /usr/local/vcl/vcl_post_reservation
* Windows: C:\Windows\vcl_post_reservation.cmd

The post-reservation script is executed prior to a compute node being reloaded.  It does not 
matter if the 
compute node is reloaded with the same or a different image, nor does it matter if the compute 
node was 
assigned to an end user reservation or simply is being reloaded via the *Manage Computers* 
utility.

The post-reservation script is useful for:

* Stopping services
* Unregistering the compute node from external services such as a license server in order to free 
up a license 
for other users
* Removing/unregistering the node from an external shared filesystem