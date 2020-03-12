---
title: Configure the Default Profile
---

A Windows profile is the desktop environment configured for a
particular user. It contains various settings such as desktop colors,
backgrounds, icon placement, and Windows Explorer settings. The default
profile is a template profile that is used when a user logs on to a Windows
computer for the first time. The default profile can be customized by the
image creator.

  
# Windows XP and Windows Server 2003

### Create a profile configuration account:

1. While logged on as **Administrator**, create a local Windows user account
named **VCLProfile** and add it to the **Administrators** group
1. Configure the profile:
    <ol type="a">
    <li>Log on as **VCLProfile**
    <li>Make desired profile, desktop, and application changes
    <li>Log out<br/>
    **NOTE**: If you just disconnect but do not log out, 
    you will not be able to complete step 7 below.
    </ol>

### Copy the profile to "Default User":

1. Log back on as **Administrator**
1. Rename the **C:\Documents and Settings\Default User** directory to
something like **Default User Original**
1. Open the **Control Panel**
1. Open **System Properties**
1. Select the **Advanced** tab
1. Click the **Settings** button next to User Profiles
1. Select VCLProfile's profile, click **Copy To** :
Copy profile to: **C:\Documents and Settings\Default User**
Permitted to use: add the **Everyone** group
1. Click **OK**

### Clean up the profile configuration account:

1. Delete the **VCLProfile** user
1. Delete **C:\Documents and Settings\VCLProfile**

You can then create another account and log in using it to make sure your
profile settings take affect for new users. Be sure to delete it once
you're done testing.

# Windows 7 and Windows Server 2008

Microsoft does not support copying profiles under Windows 7 and Windows
Server 2008.  The "Copy To" button is grayed out for all profiles except
the default profile.  The only supported method is built into Sysprep and
this method is itself very problematic.  The following steps are not
supported or recommended by Microsoft but seem to work:

### Allow Desktop Backgrounds

1. Download and edit the RDP file for your imaging reservation from the VCL
website to allow desktop backgrounds or else you won’t be able to change
the desktop background color
    <ol type="a">
    <li>Right-click on the .rdp file and select *Edit*
    <li>Click on the *Experience* tab&nbsp;
    <li>*Enable* the checkbox next to *Desktop background*
    <li>Click on the *General* tab
    <li>Click *Save*
    </ol>
1. Login as Administrator
1. Configure Windows Explorer to show hidden and system file
    <ol type="a">
    <li>Open *Windows Explorer*
    <li>Click *Organize > Folder and search options*
    <li>Select the *View* tab
    <li>Select the radio button next to *Show hidden files, folders, and drives*
    <li>Click *OK*
    </ol>

### Create a profile configuration account:

1. Create a new local user account named Profile
    <ol type="a">
    <li>Open **Control Panel > Add or remove user accounts**
    <li>If there is already an account named **VCLProfile** and you want to start
over with a new account, delete the existing account and then create a new one:
        <ol type="i">
        <li>Click on the **VCLProfile** user
        <li>Click **Delete the account**
        <li>Click **Delete Files**
        <li>Click **Delete Account**
        </ol>
    <li>Click **Create a new account**
    <li>Enter the account name: **VCLProfile**
    <li>Click the radio button next to **Administrator**
    <li>Click **Create Account**
    </ol>
1. Set the password for the VCLProfile account
    <ol type="a">
    <li>Click on the VCLProfile account
    <li>Click **Create a password**
    <li>Enter the password and click **Create password**
    </ol>
1. Configure the user profile for the VCLProfile account
    <ol type="a">
    <li>Logout as Administrator and login as VCLProfile
    <li>Customize the user profile for the VCLProfile account
    <li>Logout as VCLProfile
    </ol>

### Copy the profile to "Default":

1. Rename the **VCLProfile** user profile folder to **Default**
    <ol type="a">
    <li>Login as Administrator
    <li>Open a Windows Explorer window and navigate to **C:\Users**
    <li>Rename the original default profile folder: C:\Users\\**Default** ->
C:\Users\\**Default Original**
1. Rename the customized profile folder: C:\Users\\**VCLProfile** ->
C:\Users\\**Default**<br/>
*Note: if you are unable to rename the VCLProfile folder, reboot the computer,
login as Administrator, and try again.	Run the following command from a
command prompt to reboot the computer:*

        shutdown.exe -r -f -t 0

    </ol>
1. Copy the customized profile folder using the Windows profile copying
utility<br/>
*Note: Windows 7 only allows its built-in profile copying utility to be
used to copy the default profile, not profiles of other user accounts. The
profile you customized now resides in the default profile location
(C:\Users\Default) so the utility can now be used to make a copy of it.*
    <ol type="a">
    <li>Open **Control Panel > System and Security > System**
    <li>Click **Advanced system settings** on the left
    <li>Click the **Settings...** button under User Profiles
    <li>Highlight **Default Profile**
    <li>Click **Copy To…**
        <ol type="i">
        <li>Copy profile to: **C:\Users\Default Copy**
        <li>Click **Change** under Permitted to use
        <li>Enter **Everyone** and click OK
        <li>Click OK
        </ol>
    </ol>
1. Replace the original customized profile directory with the one created by
the Windows profile copying utility<br/>
*Note: C:\Users\Default contains the original customized profile.  The same
profile also resides in C:\Users\Default Copy.	The Default Copy folder is
the one which has had the Windows profile copying utility transformations
applied to it.*
    <ol type="a">
    <li>Open **Windows Explorer**
    <li>Delete the C:\Users\\**Default** folder
    <li>Rename the folder: C:\Users\\**Default Copy** -> C:\Users\\**Default**
    </ol>
1. Delete the VCLProfile account
    <ol type="a">
    <li>Open **Control Panel > Add or remove user accounts**
    <li>Click on the **VCLProfile** account
    <li>Click **Delete the account**
    <li>Click **Delete Files**
    <li>Click **Delete Account**
    </ol>


Any new local user accounts created on the computer should receive a user
profile configured with the customizations you made to the VCLProfile account.

## How to Force the Desktop Background to Appear on Windows 7 & Windows Server 2008

1. Run **gpedit.msc**
1. Navigate to **User Configuration > Scripts**
1. Double-click **Logon**
1. Click **Add**
    <ol type="a">
    <li>Script Name: reg.exe
    <li>Script Parameters: **DELETE "HKCU\Remote\1\Control Panel\Desktop" /v 
Wallpaper /f**
    </ol>
1. Click **OK**
1. Run **gpupdate.exe /force**
