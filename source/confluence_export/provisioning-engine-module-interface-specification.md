---
title: Provisioning Engine Module Interface Specification
---

<a name="ProvisioningEngineModuleInterfaceSpecification-Background"></a>
# Background

* Provisioning module objects are created by State.pm::initialize() when a
new state object is created.
* Provisioning module objects are available&nbsp;within state modules and
OS modules
* Provisioning module objects are not available within other types of
modules for safety.

{color:#6600ff}{_}Explain:_{color}
* {color:#6600ff}{_}define what we mean by "provisioning system"_{color}
* {color:#6600ff}{_}give examples of provisioning systems{_}{color}
* {color:#6600ff}{_}could be bare metal, virtual, differentiated,
undifferentiated, a service, a special piece of hardware, eventually VCL
could provision various types of resources{_}{color}
* {color:#6600ff}{_}relationships among mgt nodes, computers, provisioning
systems (such as computer is assigned 1 prov system at a time)_{color}
* {color:#6600ff}{_}computer.provisioningid{_}{color}
* {color:#6600ff}{_}provisioning table{_}{color}
* {color:#6600ff}{_}future: management node to provisioning
mapping{_}{color}
* {color:#6600ff}{_}provisioning module implementation is responsible for
knowing which OS interactions are necessary{_}{color}
** {color:#6600ff}{_}image.pm calls provisioner->capture, new.pm calls
provisioner->load, it calls OS subs as necessary{_}{color}

<a name="ProvisioningEngineModuleInterfaceSpecification-ProvisioningModuleSubroutines"></a>
# Provisioning Module Subroutines

It is highly recommended that all&nbsp;provisioning modules implement the
following subroutines.&nbsp; There may be many additional subroutines
implemented within a provisioning module.&nbsp; These will not be called by
any of the core VCL modules.
* [#node_status](#node_status.html)
* [#capture](#capture.html)
* [#load](#load.html)
* [#power_off](#power_off.html)
* [#power_on](#power_on.html)
* [#power_reset](#power_reset.html)
* [#get_current_image](#get_current_image.html)
* [#get_image_size](#get_image_size.html)

----

<a name="ProvisioningEngineModuleInterfaceSpecification-node_status{anchor:node_status}"></a>
## node_status {anchor:node_status}
* Description
** A provisioning module's node_status routine checks the current status of
the node. Through the module this routine is aware of how to figure out if
a node is available and loaded with the correct image or needs to be
reloaded.
** It returns a hash reference with various information, the most important
being the "status"

    ie for the xcat module:
    hashref: reference to hash with keys/values
    \{status\} => <"READY","RELOAD">
    \{ping\} => <0,1>
    \{ssh\} => <0,1>
    \{rpower\} => <0,1>
    \{nodeset\} => <"boot", "install", "image", ...>
    \{nodetype\} => <image name>
    \{currentimage\} => <image name>

** The status key/value tells the vcl system the node is ready or needs to
be reloaded.

<a name="ProvisioningEngineModuleInterfaceSpecification-capture{anchor:capture}"></a>
## capture {anchor:capture}

* Description
** A provisioning module's capture() subroutine saves the current state of
the resource.&nbsp;&nbsp;
** For the provisioning of computers, this means saving an image of the
contents of the hard drive.&nbsp; Although current VCL implementations
focus on provisioning computers, the capture() subroutine does not
necessarily need to save an image of a hard drive.&nbsp; A provisioning
module may be developed to save the configuration of a network service or
some other type of resource.
** The capture() subroutine is responsible for calling the OS module's
pre_capture&nbsp;subroutine.&nbsp; This is not called by the image.pm state
module because there may be cases where an OS isn't applicable.
** The capture() subroutine is responsible for waiting for the entire
capture process to complete.
* Expected Beginning State
** An administrator has configured the resource and initiated the capture
using the VCL website.
** The resource is on and accessible.
** The information contained in the data object describes the image which
does not yet exist and will be captured.
* Expected Ending State
** The entire capture process is complete or else an error occurred.
** The capture() subroutine has waited for an image to be captured.
* Called By
** image.pm::process()
* Arguments & Calling Environment
** Should only be called as an object method&nbsp;of a image.pm state
object ($self->capture())&nbsp;
** No Arguments
* Return Values
** 1
*** Resource was successfully captured.
*** image.pm may proceed to update the database tables making the image
available to be provisioned.
** 0
*** Resource was not successfully captured.
*** An administrator needs to investigate the problem.

<a name="ProvisioningEngineModuleInterfaceSpecification-load{anchor:load}"></a>
## load {anchor:load}

* Description
** A provisioning module's load() subroutine is responsible for
provisioning the node.
** This means starting a virtual machine, loading a image to disk, or
nothing in the case of the standalone lab machine.
* Expected Beginning State
** ...
* Expected Ending State
** ...
* Called By
** ...
* Arguments & Calling Environment
** Must only be called as an object method&nbsp;of a
provisioning&nbsp;object ($provisioner->pre_capture())&nbsp;
** No Arguments
* Return Values
** 1
*** ...
** 0
*** ...
** Undefined
*** ...

<a name="ProvisioningEngineModuleInterfaceSpecification-power_off{anchor:power_off}"></a>
## power_off {anchor:power_off}

* Description
** A provisioning module's power_off() subroutine is responsible for
powering off or down a node.
* Expected Beginning State
** ...
* Expected Ending State
** ...
* Called By
** ...
* Arguments & Calling Environment
** Must only be called as an object method&nbsp;of a
provisioning&nbsp;object ($provisioner->pre_capture())&nbsp;
** No Arguments
* Return Values
** 1
*** ...
** 0
*** ...
** Undefined
*** ...

<a name="ProvisioningEngineModuleInterfaceSpecification-power_on{anchor:power_on}"></a>
## power_on {anchor:power_on}

* Description
** A provisioning module's power_on() subroutine is responsible for
powering on a node.
* Expected Beginning State
** ...
* Expected Ending State
** ...
* Called By
** ...
* Arguments & Calling Environment
** Must only be called as an object method&nbsp;of a
provisioning&nbsp;object ($provisioner->pre_capture())&nbsp;
** No Arguments
* Return Values
** 1
*** ...
** 0
*** ...
** Undefined
*** ...

<a name="ProvisioningEngineModuleInterfaceSpecification-get_current_image{anchor:get_current_image}"></a>
## get_current_image {anchor:get_current_image}

* Description
** A provisioning module's get_current_image() subroutine is responsible
for trying to figure out what image is loaded on the node. By reading
currentimage.txt located on the node's in root's user directory. This
routine can be copied from another module.
* Expected Beginning State
** The node is expected to be online and accessible.
* Called By
** node_status()
* Arguments & Calling Environment
** Must only be called as an object method&nbsp;of a
provisioning&nbsp;object ($provisioner->pre_capture())&nbsp;
** No Arguments
* Return Values
** 1
*** ...
** 0
*** ...
** Undefined
*** ...

<a name="ProvisioningEngineModuleInterfaceSpecification-get_image_size&nbsp;{anchor:get_image_size}"></a>
## get_image_size&nbsp;{anchor:get_image_size}

* Description
** A provisioning module's get_image_size() subroutine is responsible for
collected the disk usage of the image within the image library.  
* Expected Beginning State
** N/A
* Expected Ending State
** ...
* Called By
** ...
* Arguments & Calling Environment
** Must only be called as an object method&nbsp;of a
provisioning&nbsp;object ($provisioner->pre_capture())&nbsp;
** No Arguments
* Return Values
** 1
*** ...
** 0
*** ...
** Undefined
*** ...
