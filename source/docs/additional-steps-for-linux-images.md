---
title: Additional Steps for Linux Images
---

On the **Connect!** page, the following connection information will be
displayed:
* The remote VCL computer's IP address
* The userid to use (it should be your own)
* The password to use when connecting

Log in using ssh. You can use X11 forwarding (and if not connecting from
unix, an X11 server on your own machine) to run graphical applications.

After you have logged in to the remote machine, you can gain root access by
running the command **sudo bash**

If you have not selected to capture the image by the end of the reservation time, 
VCL will automatically capture the image so that you will not lose any work.

The following steps form a good guideline of what to do while creating your
image:

1. Install your applications. Here are some suggestions/tips on loading
software to the remote machine:
 * If you have access to enough network storage, it may be easiest to copy
the software installation files in network filespace and access them from
the remote machine.
 * Copy the media to the remote machine using SCP (WinSCP is a good and
simple SCP application for Windows)
1. Post install of software:
 * remove any copies of software media (needlessly takes up space in the
image which increases the loading time for new reservations of the image)
 * Configure any application customizations
1. [Save the Image](save-the-image.html)
