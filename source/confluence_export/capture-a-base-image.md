---
title: Capture A Base Image
---

<a name="CaptureABaseImage-Runvcld\-setup"></a>
### Run vcld \-setup

1. Run the following command on the management node:
{tip}/usr/local/vcl/bin/vcld \-setup{tip}
1. Navigate the menu options
(Note: the names and numbers of the menu items may not match your
installation):
1. # {color:#808080}Select a module to configure:{color} *VCL Image State
Module*
1. # {color:#808080}Choose an operation:{color} *Capture Base Image*
1. # {color:#808080}Enter the VCL login name or ID of the user who will own
the image:{color}
Enter your VCL user ID or the user ID of the user you want to own the
image.&nbsp; Pressing Enter without entering a user login ID will cause
admin to be&nbsp;the owner of the new base image.
1. # {color:#808080}Enter the hostname or IP address of the computer to be
captured:{color}
Enter the name or private IP address of&nbsp;the computer which has already
added to the VCL database.
1. # {color:#808080}Select the OS to be captured:{color}
{color:#888888}1. VMware Linux{color}
{color:#888888}2. VMware Windows 2003 Server{color}
{color:#888888}3. VMware Windows 7{color}
{color:#888888}4. VMware Windows Server 2008{color}
{color:#888888}5. VMware Windows Vista{color}
{color:#888888}6. VMware Windows XP{color}
1. # {color:#808080}Image architecture:{color}
{color:#888888}1. x86{color}
{color:#888888}2. x86_64{color}
1. # {color:#808080}Use Sysprep:{color}
{color:#888888}1. Yes{color}
{color:#888888}2. No{color}
Sysprep is usually&nbsp;only required if the image will be loaded on bare
metal computers with varying different hardware.
1. # {color:#808080}Enter the name of the image to be captured:{color}
The name you enter is the name that will be&nbsp;displayed in the list of
environments.&nbsp;&nbsp;It&nbsp;may contain spaces&nbsp;but including
other&nbsp;special characters is not recommended.

The following happens once you enter an image name and&nbsp;press enter:
* A new image is added to the VCL database
* An imaging request is added to the VCL database
* The vcld \-setup automatically initiates 'tail \-f /var/log/vcld.log' to
monitor the vcld log file.&nbsp;&nbsp;The output should be displayed on the
screen.

Watch the vcld logfile output to determine if the image capture process is
successful or terminated because a problem occurred.&nbsp; When the capture
process terminates, there will either be a message near the end of the
output saying "image capture successful" or there will be several WARNING
messages, the last of which says something to the effect "image failed to
be captured".&nbsp; Further troubleshooting is required if the image fails
to be captured.

<a name="CaptureABaseImage-AddtheBaseImagetoanImageGroup"></a>
### Add the Base Image to an Image Group

The vcld \-setup utility does not add the new base image to any image
groups.&nbsp; You must add the image to an image group using the VCL
website after the image capture process is complete.&nbsp; Reservations for
the image cannot be made until this is done.&nbsp; To add the image to an
image group, browse to the VCL website and select Manage Images > Edit
Image Grouping.
