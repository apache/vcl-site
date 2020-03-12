---
title: Operating System Module Interface Specification
---

<a name="OperatingSystemModuleInterfaceSpecification-Background"></a>
# Background

* OS module objects are created by State.pm::initialize() when a new state
object is created.
* OS module objects are available&nbsp;within state and
provisioning&nbsp;modules
* OS module objects are not available within other types of modules for
safety.&nbsp;&nbsp; For example,&nbsp;a monitoring or other utility module
should not be able&nbsp;to call the OS module's shutdown subroutine.

<a name="OperatingSystemModuleInterfaceSpecification-OSModuleSubroutines"></a>
# OS Module Subroutines

It is highly recommended that all OS modules implement the following
subroutines.&nbsp; There may be many additional subroutines implemented
within an OS module.&nbsp; These will not be called by any of the core VCL
modules nor any of the provisioning engine modules.
* [#pre_capture](#pre_capture.html)
* [#post_load](#post_load.html)
* [#sanitize](#sanitize.html)
* [#reboot](#reboot.html)
* [#shutdown](#shutdown.html)
* [#get_current_image_name](#get_current_image_name.html)
* [#reserve](#reserve.html)
* [#grant_access](#grant_access.html)

&nbsp;&nbsp;

----
<a name="OperatingSystemModuleInterfaceSpecification-pre_capture{anchor:pre_capture}"></a>
## pre_capture {anchor:pre_capture}

* Description
** Configures the&nbsp;OS so that it can be captured by a provisioning
module.
** Configures the OS so that it will successfully boot after the captured
image is reloaded on another resource.
** Adds and configures drivers so that the image will load on other
resources.
** Removes&nbsp;files which should not be saved in the image.
** Examples of tasks performed by the pre_capture subroutine:
*** Log off users which were created for the imaging reservation and delete
the accounts
*** Set root and administrator passwords to standard, known values&nbsp;
*** Disable and delete page or swap files
*** Delete temp files
*** Copy scripts and utilities to the computer which are required after the
computer boots up but before it has network connectivity
*** Copy drivers to the computer
*** Run a generalization or sealing utility such as Sysprep.exe
* Expected Beginning State
** Resource is up and accessible
** Administrator has configured the resource
** Administrator&nbsp;may or may not have logged out
* Expected Ending State
** (Default) Resource is shut down and turned off
** Image captured of resource can be loaded and booted on other hardware
** Loaded image will successfully boot up, establish network connectivity,
and be accessible by the OS module's post_load() subroutine
* Called By
** Provisioning module's capture() subroutine
* Arguments & Calling Environment
** Must only be called as an object method&nbsp;of an OS object
($os->pre_capture())&nbsp;
** Optional Argument:
*** Name: end_state
*** Type: hash reference
*** Description:
**** Instructs pre_capture() to leave the resource in a particular state
after the subroutine's tasks are complet instead of shutting down the
resource.
*** Possible Values:
**** on - Leave the resource on.&nbsp; Do not shut it down or reboot it.
**** off (Default) - Shut the resource down.
**** reboot - Initiate a reboot and return.
* Return Values
** 1
*** All pre_capture tasks completed successfully.
*** Resource was either shut down or left in the state specified by the
end_state argument.
*** Provisioning module can proceed to capture the image.
** 0
*** Resource OS could not be completely prepared to be captured.
*** Provisioning module should not proceed to capture the image.

<a name="OperatingSystemModuleInterfaceSpecification-post_load{anchor:post_load}"></a>
## post_load {anchor:post_load}

* Description
** Performs tasks to configure the OS&nbsp;after an image was loaded.
** Does not configure the resource for a particular reservation.
** Examples of tasks performed by the post_load subroutine:
*** Make sure OS licensing has been activated
*** Configure&nbsp;services
*** Rename the computer or resource
*** Randomize passwords
*** Configure the firewall
* Expected Beginning State
** Resource has been powered on&nbsp;
** Resource may or may not be accessible
** It's expected that the resource will become accessible automatically
after it boots and performs any initialization tasks which were
preconfigured by the pre_capture subroutine.
* Expected Ending&nbsp;State
** Resource has been loaded with an image and the OS was configured so that
it is ready to be reserved.
* Called By
** Provisioning module's load() subroutine
* Arguments & Calling Environment
** Must only be called as an object method&nbsp;of an OS object
($os->post_load())&nbsp;
** No arguments
* Return Values
** 1
*** All OS post-load tasks were completed successfully
** 0
*** All OS post-load tasks could not be completed but the resource became
accessible
** Undefined
*** Resource never became accessible

<a name="OperatingSystemModuleInterfaceSpecification-sanitize{anchor:sanitize}"></a>
## sanitize {anchor:sanitize}

* Description
** Reverts the changes made when preparing a resource for a particular
reservation.
** A resource needs to be sanitized if it was successfully reserved for a
reservation but not used.
** The goal of the sanitize subroutine should be to&nbsp;clean up and
reconfigure&nbsp;a resource so that it can be provisioned for another
reservation without having to be reloaded.
** An attempt is made to sanitize the resource by reclaim.pm if it
determines that the resource was never used for a reservation.&nbsp; This
will occur if a reservation is made, enters the reserved state, but never
enters the inuse state.
** Examples of tasks performed by the sanitize subroutine:
*** Delete user accounts which were created for a reservation
*** Revoke access to the resource which was granted for a reservation
* Expected Beginning State
* Expected Ending State&nbsp;
* Called By
** reclaim.pm::process()
** May be called by the same OS module's pre_capture() subroutine to
sanitize the resource after it was reserved and used by the image creator.
* Arguments & Calling Environment
** Must only be called as an object method&nbsp;of an OS object
($os->sanitize())
** No arguments will be passed to sanitize()
* Return Values
** 1
*** Sanitization was completely successful
*** Resource is ready to be provisioned and reserved for another
reservation
*** Resource does not need&nbsp;to be reloaded
** 0
*** Sanitization could not be completed
*** Resource needs to be reloaded

<a name="OperatingSystemModuleInterfaceSpecification-reboot{anchor:reboot}"></a>
## reboot {anchor:reboot}

* Description
** Performs a complete graceful reboot of the OS.
** May forcibly log off users if necessary.
** Waits for the reboot to complete.
** Returns after the reboot is complete.
* Expected Beginning State
** Computer is up and accessible.
** Users may be logged on to the computer.
* Expected Ending&nbsp;State
** Computer has been rebooted.
** Computer is accessible.
* Called By
** May be called by any module which has access to the OS object
* Arguments & Calling Environment
** Must only be called as an object method&nbsp;of an OS object
($os->reboot())
** Argument:
*** Name: timeout
*** Description:
**** Instructs reboot() to wait a maximum number of minutes for the reboot
to complete
**** If timeout has been reached and computer has not finished rebooting, 0
should be returned
*** Required: No
*** Default Value: 5 minutes
*** Data Type: integer
*** Possible Values:
**** Any positive integer
* Return Values
** 1
*** Reboot completed successfully
*** Computer is accessible
** 0
*** Reboot was initiated but computer never came back online
*** Timeout was reached
** Undefined
*** Reboot could not be initiated

<a name="OperatingSystemModuleInterfaceSpecification-shutdown{anchor:shutdown}"></a>
## shutdown {anchor:shutdown}

* Description
** Performs a graceful shutdown of the OS.
** May forcibly log off users if necessary.
** Waits for the shutdown to complete.
** Returns after the shutdown is complete and the computer is off.
* Expected Beginning State
** Computer is up and accessible.
** Users may be logged on to the computer.
* Expected Ending State
** Computer is off.
* Called By
** May be called by any module which has access to the OS object
* Arguments & Calling Environment
** Must only be called as an object method&nbsp;of an OS object
($os->reboot())
** Argument:
*** Name: timeout
*** Description:
**** Instructs shutdown() to wait a maximum number of minutes for the
shutdown to complete
**** If timeout has been reached and computer has not finished shutting
down, 0 should be returned
*** Required: No
*** Default Value: 5 minutes
*** Data Type: integer
*** Possible Values:
**** Any positive integer
* Return Values
** 1
*** Shudown completed successfully
** 0
*** Shutdown was initiated but computer never shut down
*** Timeout was reached
** Undefined
*** Shutdown could not be initiated

<a name="OperatingSystemModuleInterfaceSpecification-get_current_image_name{anchor:get_current_image_name}"></a>
## get_current_image_name {anchor:get_current_image_name}

* Description
** Returns the name of the current image that is loaded on the
resource(currentimage.txt file).
** The name corresponds to the image.name column in the database.
** Returning a name implies that the resource is accessible.
** The OS.pm will probably handle this subroutine.
* Expected Beginning State
** Resource is accessible.
* Expected Ending&nbsp;State
** The resource state should be identical to before get_current_image_name
was called.
* Called By
** Provisioning module's node_status() subroutine.
** Used to determine if the OS and provisioning engine agree on the current
image loaded on a resource.
** Can be used to determine if a resource is accessible.&nbsp; A valid
string will be returned if the resource is accessible.
* Arguments & Calling Environment
** Must only be called as an object method&nbsp;of an OS object
($os->get_current_image_name())
** No arguments
* Return Values
** String
*** String contains a VCL image name
** 0
*** Computer is accessible but failed&nbsp;to determine the current loaded
image
** Undefined
*** Computer is not accessible

<a name="OperatingSystemModuleInterfaceSpecification-reserve&nbsp;{anchor:reserve}"></a>
## reserve&nbsp;{anchor:reserve}

* Description
** reserve() gets called by new.pm after a machine has been reloaded if the
state is "new" (new.pm also handles the "reload" state and others)
** It should perform the steps necessary to take a reloaded machine and
prepare it for a particular reservation
** Anything reservation-specific that doesn't require knowing the user's IP
should be done in reserve()
** After reserve() has run, the state can be changed to reserved and the
"Connect" button can be presented to the user
** reserve() would normally add&nbsp;the reservation user and any users set
in imagemeta usergroup to the computer, set their passwords, and add them
to the appropriate groups
** reserve()&nbsp;does not configure the firewall or do anything networking
related because at the time it's called, the state has not been changed to
reserved and the user has not been shown the "Connect" button.&nbsp;
Hence,&nbsp;the user's IP is not known.
** reserve() is called by new.pm before the "Connect" button is shown to
the user because adding several user accounts may take a long time.&nbsp;
If adding users was done after the state was changed to reserved, a user
could attempt to connect before all of the users accounts were added.
* Expected Beginning State
** Request state is pending/new&nbsp;
** Computer has been reloaded
* Expected Ending&nbsp;State
** Computer has been configured for a particular reservation
** User accounts have been added and configured
** Request state can be changed to reserved and the "Connect" button can be
presented to the user
* Called By
** new.pm
* Arguments & Calling Environment
** Must only be called as an object method&nbsp;of an OS object
($os->reserve())
** No arguments
* Return Values
** True (1)&nbsp;
*** Computer has successfully been configured for a particular reservation
** False (0 or undefined)&nbsp;
*** Computer could not be configured for a particular reservation

<a name="OperatingSystemModuleInterfaceSpecification-grant_access&nbsp;{anchor:grant_access}"></a>
## grant_access&nbsp;{anchor:grant_access}

* Description
** grant_access()&nbsp;gets called by reserved.pm after the user has
clicked the&nbsp;"Connect" button
** The user's IP address is known when grant_access() is called
** grant_access() should perform all the steps necessary to open up the
machine so the user(s) added by reserve() can connect
** grant_access() may&nbsp;enables RDP or public SSH traffic depending on
the OS
* Expected Beginning State
** User has just clicked the "Connect" button&nbsp;
** Request state is pending/reserved
* Expected Ending&nbsp;State
** Computer has been configured to allow the user to connect
* Called By
** reserved.pm
* Arguments & Calling Environment
** Must only be called as an object method&nbsp;of an OS object
($os->get_current_image_name())
** No arguments
* Return Values
** True (1)&nbsp;
*** Computer was successfully configured to allow access for the
reservation users
** False (0 or undefined)
*** Computer could not be configured to allow access for the reservation
users
