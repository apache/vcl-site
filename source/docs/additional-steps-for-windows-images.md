---
title: Additional Steps for Windows Images
---

On the **Connect!** page, the following connection information will be
displayed:

* The remote VCL computer's IP address
* The user ID you will use: Administrator<br/>
*Note: the user ID is always Administrator for Windows imaging
reservations*
* A one-time password for the Administrator account

Log in using Remote Desktop Connection. You can either enter the connection
information manually after launching the Remote Desktop Connection program
or you can use a pre-configured RDP file:

* Click the Get RDP File button
* Save the RDP file to your computer
* Double-click the RDP file to launch the Remote Desktop Connection program
with the VCL connection information pre-configured

If you have not selected to capture the image by the end of the reservation time, VCL
will automatically capture the image so that you will not lose any work.

The following steps form a good guideline of what to do while creating your
image:

1. Run Windows Update before saving an image.&nbsp; It's OK if the computer
needs to reboots. &nbsp;It can take 4-6 minutes for the computer to reboot
before you can connect via RDP again.
1. Install your applications. Here are some suggestions/tips on loading
software to the remote machine:

 * Copy the&nbsp;software from your local computer to the remote computer
by sharing your local drives through Remote Desktop Connection.&nbsp; The
shared drives show up in Windows Explorer on the&nbsp;remote machine.&nbsp;
Do not run the software's installation program directly from the shared
drive.&nbsp; Copy it to the remote computer first, run the setup program,
then delete the installation files.
 * If you have an ISO image of the software, copy the ISO file to the
remote machine using a shared drive then mount the ISO image as a drive
letter.&nbsp; The freeware program MagicDisc does this very well:
[http://www.magiciso.com/tutorials/miso-magicdisc-overview.htm](http://www.magiciso.com/tutorials/miso-magicdisc-overview.htm)
Install MagicDisc, mount the ISO file, and then run the application's
installation program from the mounted drive.&nbsp; When the installation is
done, unmount the drive and delete the ISO file from the remote
machine.&nbsp; Uninstall MagicDisc before saving your image if you don't
want it included.
If you have a physical CD or DVD, you can create an ISO image using a
program such as LC ISO Creator:
[http://www.lucersoft.com/freeware.php](http://www.lucersoft.com/freeware.php)
 * If you have access to enough network storage, you can copy the software
installation files&nbsp;to the&nbsp;network filespace and access them from
the remote machine.
 * Copy the media contents using SCP from the remote computer.&nbsp; If you
have a personal machine running an SSH server you can use this
method.&nbsp; You could also do the same thing using FTP.
1. Post install of software:
 * Remove any copies of software media (needlessly takes up space in the
image which increases the loading time for new reservations of the image)
 * make sure all wanted desktop icons are in "All users" desktop.
 * Configure any application customizations
 * [perform customizations to the default user profile](configure-the-default-profile.html)
1. [Save the Image](save-the-image.html)
