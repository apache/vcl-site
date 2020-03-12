---
title: Install Windows for a Base Image
---

{excerpt}This page describes how to mount the Windows installation media
and install Windows for a base image.{excerpt}

<a name="InstallWindowsforaBaseImage-MounttheInstallationMedia"></a>
## Mount the Installation Media

The Windows installation media needs to be mounted as a drive on the
computer. The method to do this varies widely based on the provisioning
engine being used and resources available. The following lists some ways to
mount the installation media:

h4. VMware - Configure the VM to mount the&nbsp;ISO image&nbsp;as a CD-ROM
drive

_Note: these instructions assume a VM has already been created_

1. Copy the Windows installation ISO file to the VMware host server
1. Add a CD-ROM drive which mounts the Windows installation ISO image by
editing the virtual machine settings:
1. # Connection: *Use ISO image*:
1. # Browse to path of Windows installation ISO image
1. # Save the VM configuration

<a name="InstallWindowsforaBaseImage-xCATusingIBMAdvancedManagementModule"></a>
#### xCAT using IBM Advanced Management Module

1. Copy the Windows installation ISO file to the management node
1. Determine the IP address or hostname of the IBM Advanced Management
Module (AMM) for the BladeCenter chassis which contains the blade you are
installing
1. Open a web browser and enter the AMM's address
1. Log in to the AMM
1. Select Inactive session timeout value: *no timeout*
1. Click *Start New Session*
1. Click *Remote Control*
1. Click *Start Remote Control*
1. Set the *Media Tray* and *KVM* dropdown menus to the blade you are
installing
1. Click *Select Image* and click the arrow button to the right of it
1. Navigate to the Windows installation ISO file which was saved to the
management node and click *Open*
1. Click *Mount All*


<a name="InstallWindowsforaBaseImage-BoottotheWindowsInstallationCDorDVD"></a>
## Boot to the Windows Installation CD or DVD

1. Power on the computer
1. Press the key to display the boot menu as soon as the computer's POST
screen is displayed (usually *F12* for bare metal blades or *ESC* for
VMware)
1. Boot from the CD-ROM drive
1. Press a key to boot from the CD (this may be displayed at bottom of
screen as soon as the computer begins to boot)

<a name="InstallWindowsforaBaseImage-InstallWindows"></a>
## Install Windows

The Windows installation sequence varies by version. The&nbsp;next 2
sections describe&nbsp;the recommended answers for Windows XP and Windows
7.

<a name="InstallWindowsforaBaseImage-WindowsXPInstallation"></a>
### Windows XP Installation

1. Press *Enter* to setup up Windows XP now
1. Press *F8* to agree to the license agreement
1. Configure the Windows partition
1. # Press *Enter* to set up Windows XP on the selected item (should be
called "Unpartitioned space")
1. # Format the partition using the *NTFS file system (Quick)*
1. Region and Language Options - click *Next*
1. Name: *VCL*
1. Organization: *Apache.org*
1. Enter your *Windows XP product key*
1. Computer name: _(doesn't matter)_
1. Administrator password: _(doesn't matter, but it's&nbsp;recommended that
password should match the_ *{_}WINDOWS_ROOT_PASSWORD{_}* _setting in_
*_/etc/vcl/vcld.conf{_}{*}_)_
1. Select the timezone
1. Networking settings: *Typical*
1. Member of a domain: *No, leave default workgroup settings*
1. Automatic updates: *Not right now*
1. Connect to Internet: *Skip*
1. Register: *no*
1. User name:&nbsp;*root*
{color:#888888}{_}Windows XP setup should finish and the root account
created during installation should automatically log on{_}{color}
1. Once the desktop appears, set root's password&nbsp;via the Windows GUI or
by executing the following command from a command prompt:
*net user root* *_<password>_*

<a name="InstallWindowsforaBaseImage-Windows7Installation"></a>
### Windows 7 Installation

1. Enter the regional information:
1. * Language to install: *English*
1. * Time and currency format: *English (United States)*
1. * Keyboard or input method: *US*
1. Click *Next*
1. Click *Install now*
{color:#888888}{_}Setup is starting..._{color}
1. Click the checkbox next to "I accept the license terms"
1. Click *Next*
1. Click *Custom (advanced)*
1. On the "Where do you want to install Windows?" page, delete all existing
partitions and create a new partition using all of the available space:
1. # Click *Drive options (advanced)*
1. # Click *Delete*, then click *OK* to confirm
1. # Click *New*
1. # Click Apply (the size should be set to the maximum amount available
{color:#888888}{_}To ensure that all Windows features work correctly,
Windows might create additional partitions for system files._{color}
1. # Click *OK*
1. Click *Next*
{color:#888888}{_}Installing Windows..._{color}
{color:#888888}{_}Windows restarts{_}{color}
{color:#888888}{_}Starting Windows{_}{color}
{color:#888888}{_}Setup is updating registry settings{_}{color}
1. A screen titled "Set Up Windows" appears:
1. * Type a user name: *root*
1. * Type a computer name: it's best to name the computer after the OS
(_Example: win7sp1-ent)_
1. Enter a password, password hint,&nbsp;and click *Next*
1. Help protect your computer and improve Windows automatically: *Ask me
later*
1. Select a time zone, set the correct time,&nbsp;and click *Next*
{color:#888888}{_}Windows is finalizing your settings{_}{color}
{color:#888888}{_}Preparing your desktop{_}{color}
{color:#888888}{_}Desktop appears{_}{color}
1. If asked to set a network location, choose *Work network*
_The root account logs in..._

<a name="InstallWindowsforaBaseImage-WindowsServer2008"></a>
### Windows Server 2008

1. Select the language and click *Next*
1. Click *Install Now*
1. Select the version of Windows you want to install from the list and click
*Next.* (_Windows Server 2008 R2 Datacenter (Full Installation)_ was
selected when creating these instructions.)
1. Click the checkbox next to *I accept the license terms* and click *Next*
1. Click *Custom (advanced)*
1. Configure the disk partitions and click *Next.&nbsp;* Unless you have
reason not to, it's best to delete all existing partitions and then select
Unallocated Space. This causes the disk to be repartitioned using all of
the available space.
_Windows is installed..._
1. Click *OK*&nbsp;and set a password for the Administrator account, click
*OK*
_The Administrator account logs in..._

The root user account is not created during the installation of Windows
Server 2008. It must be created after Windows is installed. Do this using
the GUI or run the following commands in a command window:
1. Click *Start* > *Administrative Tools* > *Server Manager*
1. Open *Configuration* > *Local Users and Groups* > *Users*
1. Open the&nbsp;*Action* menu > *New User*
1. # User name: *root*
1. # Enter a password twice
1. # User must change password at next logon: *no*
1. # Password never expires: *yes*
1. # Click *Create*
1. # Click *Close*
1. Double-click the *root* user
1. Select the *Member Of* tab
1. Click *Add*
1. # Enter the object names to select: *Administrators*
1. Click *OK* twice

The *Disk Cleanup* utility (cleanmgr.exe) is not available on Windows
Server 2008 unless the the *Desktop Experience* feature is installed. VCL
runs cleanmgr.exe before an image is captured to reduce the amount of space
the image consumes. Image captures will not fail if cleanmgr.exe is not
installed but it is recommended to install the *Desktop Experience* feature
so that it is available:
1. Open the *Control Panel*
1. Click *Turn Windows features on or off*
1. Click *Features*
1. Click *Add Features*
1. Click the checkbox next to *Desktop Experience*
1. Click *Add Required Features*
1. Click *Next*
1. Click *Install*
_The features are installed..._
1. Click *Close*
1. Click *No* to not reboot the computer
1. Restart the computer after the installation is complete

<a name="InstallWindowsforaBaseImage-OptionalWindowsConfigurationTasks"></a>
## Optional Windows Configuration Tasks

<a name="InstallWindowsforaBaseImage-EnableRemoteDesktop"></a>
#### Enable Remote Desktop

The remaining configuration tasks will be easier if you are able to connect
to the Windows computer via RDP rather than using the VMware or BladeCenter
Management Module console. This step is optional. The VCL image capture
process will configure RDP on the Windows computer during image capture and
load processes.

<a name="InstallWindowsforaBaseImage-WindowsXP&&nbsp;WindowsServer2003:"></a>
###### Windows XP &&nbsp;Windows Server 2003:

1. Open *Control Panel* > *System* > *Remote* tab
1. Click the checkbox next to *Allow users to connect remotely to this
computer*
1. Click *OK*

<a name="InstallWindowsforaBaseImage-WindowsVista,Windows7,&WindowsServer2008:"></a>
###### Windows Vista, Windows 7, & Windows Server 2008:

1. Open *Control Panel* > *System and Security* > System
1. Click *Remote settings*
1. Select *Allow connections from computers running any version of Remote
Desktop (less secure)*
1. Click *OK*

Use an RDP client to connect to the Windows computer using either its
public or private IP address as appropriate. If the public address is not
available for some reason, you can attempt to connect to the private IP
address by installing rdesktop&nbsp;on the management node:

{tip}yum install rdesktop \-y{tip}

{tip}rdesktop \-g 1024x768 _<IP address>_ &{tip}

<a name="InstallWindowsforaBaseImage-DisableInternetExplorerEnhancedSecurityConfiguration"></a>
#### Disable Internet Explorer Enhanced Security Configuration

<a name="InstallWindowsforaBaseImage-_(WindowsServer2003andWindowsServer2008&nbsp;only)_"></a>
###### _(Windows Server 2003 and Windows Server 2008&nbsp;only)_

Internet Explorer Enhanced Security Configuration (IE ESC) prevents you
from being able to access websites unless you add them to the Trusted sites
zone.
1. Open *Administrative Tools* > *Server Manager*
1. Click *Configure IE ESC* (on the right side&nbsp;under Security
Information)
1. Select *Off* for Administrators and Users
1. Click *OK*

<a name="InstallWindowsforaBaseImage-SettheComputerName&nbsp;"></a>
#### Set the Computer Name&nbsp;

The computer may have been assigned a random computer name. This name will
be saved in the captured image. If Sysprep is disabled, this computer name
will also be assigned to other computers loaded with the image. It's
helpful to name the computer something descriptive of the image so that you
can tell what the image is when you connect to it via SSH.
1. Open the *Control Panel*
1. Click *System and Security* > *Set the name of this computer*
1. Click *Change settings*
1. Click *Change*
1. # Enter a Computer name and Workgroup
1. # Click *OK* 3 times
1. Click Close
1. Click Restart Later

<a name="InstallWindowsforaBaseImage-DisableUserAccountControl"></a>
#### Disable User Account Control

<a name="InstallWindowsforaBaseImage-(WindowsVista,Windows7,&WindowsServer2008only)"></a>
###### (Windows Vista, Windows 7, & Windows Server 2008 only)

User Account Control (UAC) is the mechanism that causes may of the pop-up
windows to appear when you attempt to run programs on Windows 7 and Windows
Server 2008. VCL will disable it when the image is captured but you can
disable it while configuring the base image to make things a little easier.
1. Open the *Control Panel*
1. Click *System and Security* > *Change User Account Control settings*
_(Under Action Center)_
1. Move the slider to the bottom:&nbsp;*Never notify*
1. Click *OK*
1. Reboot the computer

<a name="InstallWindowsforaBaseImage-ConfigureWindowsBootOptions"></a>
#### Configure Windows Boot Options

It can be helpful to configure the Windows boot options as follows in order
to be able to troubleshoot boot problems.
1. Run *msconfig.exe*
1. Select the *Boot* tab
1. Click the checkboxes next to:
1. # *No GUI boot* \- Does not display the Windows Welcome screen when
starting
1. # *Boot log* \- Stores all information from the startup process in the
file %SystemRoot%Ntbtlog.txt
1. # *OS boot information* \- Shows driver names as drivers are being loaded
during the startup process
1. # *Make all boot settings permanent*
1. Click *OK*
1. Click *Yes*
1. Restart the computer

<a name="InstallWindowsforaBaseImage-VerifyNetworkConnectivity"></a>
## Verify Network Connectivity

The computer must be able to connect to the public and private networks.
1. If DHCP is not being used, configure the IP addresses manually
1. Verify that the computer has IP addresses for both the public and private
network adapters:
1. # Open a command prompt:
{tip}cmd.exe{tip}
1. # Check the network configuration:
{tip}ipconfig /all{tip}
1. Verify Internet access by opening Internet Explorer and browsing to a
public website

Some Windows versions (especially Windows Vista) have trouble properly
routing outward network traffic if there are multiple network interfaces.
If you can not get to the Internet, set the *private* network interface to
*ignore default routes* which causes all outward traffic not destined for
the private network to be sent through the public interface:

1. Open a command prompt (this must be done as Administrator under Windows
6.x):
*Start* > *All Programs* > *Accessories* > right-click *Command prompt* >
*Run as Administrator*
1. Determine the name of the private interface from the *ipconfig* output
_(should be either "Local Area Connection" or "Local Area Connection 2")_
1. Execute the command using the private interface name from step 2:
{tip}netsh.exe interface ip set interface "_Local Area Connection_"
ignoredefaultroutes=enabled{tip}
1. * The command should display *Ok.*
1. Attempt to access the Internet again

<a name="InstallWindowsforaBaseImage-InstallWindowsUpdates"></a>
## Install Windows Updates

1. Open *Internet Explorer*
1. Run *Windows Update*
1. * Install all recommended updates, reboot if necessary
1. Run *Windows Update* again to check for additional updates

<a name="InstallWindowsforaBaseImage-InstallDrivers"></a>
## Install Drivers

Open up the Device Manager: *Control Panel* > *System* > *Hardware* tab >
*Device Manager*

If any devices are unknown or missing drivers, you will need to locate and
download the appropriate driver and install it.

Save a copy of the drivers you had to install in the appropriate *Drivers*
directory on the management node:
{panel}/usr/local/vcl/tools/Windows.../Drivers{panel}
There are multiple *Windows...* directories under /usr/local/vcl/tools. The
names create a&nbsp;hierarchy so that files which can be used by multiple
versions of Windows only need to be stored in a single location on the
management node.&nbsp; There are 3 levels that make up the hierarchy:

1. The directory named *Windows* should contain files that work on all
versions of Windows:
{panel}/usr/local/vcl/tools/Windows/Drivers{panel}
1. The directories named *Windows_Version_x* should contain files that only
work on a particular major version of Windows.
{info}The Windows version number can be obtained by executing ver from a
command prompt{info}
1. * *Windows_Version_5* should contain files that work on versions of
Windows numbered 5.x (Windows XP and Windows Server 2003).
{panel}/usr/local/vcl/tools/Windows_Version_5/Drivers{panel}
1. * *Windows_Version_6* should contain files that work on versions of
Windows numbered 6.x (Windows Vista, Windows Server 2008, and Windows 7).
{panel}/usr/local/vcl/tools/Windows_Version_5/Drivers{panel}
1. The directories named after a specific version (Windows_XP,
Windows_Server_2008, etc.) should contain files that only work on that
version.&nbsp; For example, if a driver only works under XP save it under:
{panel}/usr/local/vcl/tools/Windows_XP/Drivers{panel}

During the image capture process, the Windows\* directories that pertain to
the OS being captured are copied to *C:\cygwin\home\root\VCL* on the
Windows computer.&nbsp;&nbsp;Each Windows\* directory is overlayed into the
same&nbsp;*VCL* directory. &nbsp;They are copied in the order listed above,
from most general to most specific. For example, if a Windows Server 2008
image is being captured the directories copied are:
1. {panel}/usr/local/vcl/tools/Windows{panel}
1. {panel}/usr/local/vcl/tools/Windows_Version_6{panel}
1. {panel}/usr/local/vcl/tools/Windows_Server_2008{panel}

The directory organization under each Drivers directory does not
matter.&nbsp;&nbsp;However, it's&nbsp;recommended that they be
organized&nbsp;by device type:
* {panel}/usr/local/vcl/tools/Windows.../Drivers/Chipset{panel}
* {panel}/usr/local/vcl/tools/Windows.../Drivers/Network{panel}
* {panel}/usr/local/vcl/tools/Windows.../Drivers/Storage{panel}
* {panel}/usr/local/vcl/tools/Windows.../Drivers/Video{panel}

For example, after testing several drivers you determine the following:
* An Intel chipset driver works for all versions of Windows. Save it in:
{panel}/usr/local/vcl/tools/Windows/Drivers/Chipset/Intel-5000{panel}
* A Broadcom NetXtreme network driver only works for Windows XP and Windows
Server 2003. Save it in:
{panel}/usr/local/vcl/tools/Windows_Version_5/Drivers/Network/Broadcom-NetXtreme{panel}
* An ATI video driver only works for Windows. Save it in:
{panel}/usr/local/vcl/tools/Windows_XP/Drivers/Video/ATI-ES1000{panel}

When a Windows XP image is captured, the drivers will be copied to:
* {panel}C:\cygwin\home\root\VCL\Drivers\Chipset\Intel-5000{panel}
* {panel}C:\cygwin\home\root\VCL\Drivers\Network\Broadcom-NetXtreme{panel}
* {panel}C:\cygwin\home\root\VCL\Drivers\Video\ATI-ES1000{panel}

The VCL image capture process then configures the Windows computer to
locate and install the drivers copied to the computer when the image is
loaded.

<a name="InstallWindowsforaBaseImage-InstallHotfixKB942589"></a>
## Install Hotfix KB942589

  
  

{color:#000000}The&nbsp;hotfix available from the
following&nbsp;page&nbsp;must be installed i{color}f you are
installing&nbsp;the 64-bit version of Windows XP or Windows&nbsp;Server
2003:
[http://support.microsoft.com/kb/942589](http://support.microsoft.com/kb/942589)


You will need to click on the *View and request hotfix downloads* link,
enter your email address, and a download link will be sent to you.
----
Next Step: [VCL:Install & Configure Cygwin SSHD](vcl:install-&-configure-cygwin-sshd.html)
