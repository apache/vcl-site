---
title: Modularized Architecture
---

<a name="ModularizedArchitecture-Background"></a>
# Background

The VCL backend code was significantly reworked in version 2.0
to&nbsp;utilize a&nbsp;"modularized" framework.&nbsp; This framework allows
certain parts of the code to be separated from the core code through the
implementation of modules.

VCL interacts with external technologies including:
* provisioning engines
* operating systems
* monitoring utilities

The technology being used may vary based on the VCL deployment, management
node, image, computer, and so on.&nbsp; Modules make configuring VCL to use
a certain technology easy while simplifying the core code.

The advantages of implementing modules are not limited to external
technologies.&nbsp;&nbsp;Modules may be implemented for functions
applicable only to VCL, but may vary based on the environment.&nbsp; For
example, research is being conducted to compare different algorithms
which&nbsp;are used to select the image that is loaded on a computer after
a reservation is complete.&nbsp; A module is created for each algorithm,
and configuring a management node to use a certain algorithm is as simple
as changing one value in the database.

<a name="ModularizedArchitecture-ObjectOrientationandInheritance"></a>
## Object Orientation and Inheritance

Object orientation and inheritance are used in the VCL modular framework,
allowing modules to access functionality from&nbsp;the classes which they
inherit from.&nbsp; This relieves module developers from having
to&nbsp;worry about many&nbsp;underlying details and reduces code
duplication.

The following diagram shows how inheritance is organized:
!inheritance.jpg|align=center!
*Figure: VCL module inheritance organization*
&nbsp;&nbsp;A few notes about the diagram:
* The yellow modules represent the core VCL modules
* The blue and green modules represent auxiliary modules
* Core&nbsp;modules that should not need to be changed regardless of the
auxiliary modules being used
* The core modules provide many functions to the auxiliary modules
including:
** default constructors
** data access
** module initialization
** access to&nbsp;other auxiliary modules where appropriate

{color:#6600ff}{_}Explain:_{color}
* {color:#6600ff}{_}abstract and concrete classes - abstract are not
instantiated{_}{color}
* {color:#6600ff}{_}classes can be empty, contain no subs, but act as a
placeholder in case it's decided later on that a sub would be
useful{_}{color}{color:#6600ff}&nbsp;{color}

<a name="ModularizedArchitecture-Advantages"></a>
## Advantages

* Modules make it easier for developers to implement new technologies to be
used with VCL&nbsp;easily
* Core VCL code does not need to be altered in order to support additional
technologies or functionality
* Increased flexibility for different configurations
* Consistent methods to access data stored in the database
* Code maintainability is increased because each module focuses on a
distinct task and the core code does not need to check for numerous
different conditions based on the technology being used

{color:#6600ff}{_}Explain:&nbsp;_{color}
* {color:#6600ff}{_}more about benefits of inheritance{_}{color}
* {color:#6600ff}{_}give OS example and include diagram{_}{color}
** {color:#6600ff}{_}Windows - Desktop - XP - Vista{_}{color}
** {color:#6600ff}{_}implement subs as high up as possible so child classes
inherit them{_}{color}
** {color:#6600ff}{_}child classes can override an inherited sub if it
doesn't fit its needs{_}{color}
** {color:#6600ff}{_}use example of firewalls in Windows.&nbsp; Windows.pm
implements a firewall sub which works for everything but Vista.&nbsp;
Vista.pm can implement a sub with the same name and it will override the
one in Windows.pm, yet Vista.pm still enjoys everthing else Windows.pm
offers._{color}

<a name="ModularizedArchitecture-CoreModules"></a>
# Core Modules

&nbsp;&nbsp;{color:#6600ff}{_}Explain:_{color}
* {color:#6600ff}{_}only core modules should ever change the request
state/laststate/computer state{_}{color}
* {color:#6600ff}{_}only core modules should change anything in the request
and rsvp tables{_}{color}
* {color:#6600ff}{_}provide state flow{_}{color}
* {color:#6600ff}{_}provide data access{_}{color}
* {color:#6600ff}{_}provide utility functions&nbsp;_{color}
* {color:#6600ff}{_}database and data structure are abstracted from
auxiliary modules{_}{color}
* {color:#6600ff}{_}ongoing - should not contain code specific to something
that can be modularized such as "if windows... else linux..."_{color}

<a name="ModularizedArchitecture-vcld(VCL::vcld)"></a>
### vcld (VCL::vcld)

{color:#6600ff}{_}Explain:_{color}
* {color:#6600ff}{_}main exe{_}{color}
* {color:#6600ff}{_}loops every 12 seconds by default{_}{color}
* {color:#6600ff}{_}doesn't inherit{_}{color}
* {color:#6600ff}{_}creates DataStructure object{_}{color}
* {color:#6600ff}{_}forks{_}{color}
* {color:#6600ff}{_}sets some $ENV variables{_}{color}
* {color:#6600ff}{_}reaps dead processes{_}{color}

<a name="ModularizedArchitecture-DataStructure.pm(VCL::DataStructure)"></a>
### DataStructure.pm (VCL::DataStructure)

{color:#6600ff}{_}Explain:_{color}
* {color:#6600ff}{_}abstracts database and data structure{_}{color}
* {color:#6600ff}{_}aux modules shouldn't know about the DB or data
structure{_}{color}
* {color:#6600ff}{_}should be able to change db or data structure and still
have aux modules work{_}{color}
* {color:#6600ff}{_}uses "Inside Out" technique to accessing modules can't
get to the underlying data{_}{color}
* {color:#6600ff}{_}data is encapsulated, can only be accessed using
accessor functions{_}{color}
** {color:#6600ff}{_}encapsulation is good, explain what it is{_}{color}
* {color:#6600ff}{_}usage: $self->data->get_image_name()_{color}
* {color:#6600ff}{_}need to list methods somewhere (not here), there are
tons of them{_}{color}
* {color:#6600ff}{_}gets created by vcld when it finds a
reservation{_}{color}
* {color:#6600ff}{_}passed to&nbsp;module constructor{_}{color}
* {color:#6600ff}{_}Module.pm sets up access via data()_{color}
* {color:#6600ff}{_}Result: any class that inherits from VCL::Module gets
access{_}{color}

<a name="ModularizedArchitecture-utils.pm(VCL::utils)"></a>
### utils.pm (VCL::utils)

{color:#6600ff}{_}Explain:_{color}
* {color:#6600ff}{_}contains several utility subs{_}{color}
* {color:#6600ff}{_}doesn't inherit from Module.pm (might be a good idea to
look into this)_{color}
* {color:#6600ff}{_}contains some legacy stuff - some subs will be removed
and moved to OS or provisioing modules{_}{color}
* {color:#6600ff}{_}should probably make a page describing utility subs
such as notify, run_ssh_command..._{color}
** {color:#6600ff}{_}This should really get sucked out of POD comments in
the actual code{_}{color}
* {color:#6600ff}{_}have to 'use VCL::utils' in order to use it{_}{color}

<a name="ModularizedArchitecture-Module.pm(VCL::Module)"></a>
### Module.pm (VCL::Module)

* Provides a constructor for all derived objects to use
** Objects which inherit from VCL::Module do not need to implement their
own new() subroutines
** Objects which inherit from VCL::Module do not need to deal with
"blessing" themselves
* Provides access to the database data for the reservation via the data()
subroutine implemented by Module.pm
** Any module derived from VCL::Module can call $self->data->\[get_something\](get_something\.html)
 or $self->data->\[set_something\]

<a name="ModularizedArchitecture-State.pm(VCL::Module::State)"></a>
### State.pm (VCL::Module::State)

* Supports the core VCL state modules such as new.pm, image.pm, reclaim.pm,
and others
* Provides an initialize() subroutine which performs common tasks whenever
a state object is created
** initialize() creates the provisioning and OS objects
* Provides an os() subroutine which allows the state objects to interact with the resource's operating system by calling $self->os->\[subroutine\](subroutine\.html)
* Provides a provisioner() subroutine which allows the state objects to interact with the provisioning engine that has been configured for the resource&nbsp;by calling $self->provisioner->\[subroutine\](subroutine\.html)
* Provides other subroutines such as reservation_failed() which
performs&nbsp;a consistent set of&nbsp;tasks when a reservation fails

<a name="ModularizedArchitecture-Provisioning.pm(VCL::Module::Provisioning)"></a>
### Provisioning.pm (VCL::Module::Provisioning)

* Provisioning engine modules should inherit from VCL::Module::Provisioning
* Modules which are a subclass of VCL::Module::Provisioning
also&nbsp;receive the&nbsp;functionality provided by VCL::Module through
inheritance
* VCL::Module::Provisioning provides provisioning modules with access to
the OS object created for the reservation

<a name="ModularizedArchitecture-OS.pm(VCL::Module::OS)"></a>
### OS.pm (VCL::Module::OS)

* OS&nbsp;modules should inherit from VCL::Module::OS
* Modules which are a subclass of VCL::Module::OS also&nbsp;receive
the&nbsp;functionality provided by VCL::Module through inheritance
* VCL::Module::OS provides OS modules with access to the&nbsp;provisioning
object created for the reservation
** This is useful if the OS needs to perform a task such as power cycling
the computer if a reboot fails

<a name="ModularizedArchitecture-ImplementationDetails"></a>
# Implementation Details


<a name="ModularizedArchitecture-WorkingwithInheritance"></a>
### Working with Inheritance

{color:#6600ff}{_}Explain:_{color}
* {color:#6600ff}{_}code to set up inheritance{_}{color}
* {color:#6600ff}{_}using $self->_{color}
* {color:#6600ff}{_}when to use $self-> (object method) and when to call a
sub directly (class method)_{color}
* {color:#6600ff}how to check if sub was called as an object method or
not{color}

<a name="ModularizedArchitecture-IncludingNon-InheritedModules"></a>
### Including Non-Inherited Modules

&nbsp;{color:#6600ff}{_}Explain:_{color}
* {color:#6600ff}{_}use{_}{color} {color:#6600ff}_[file::bin](file::bin.html)
_{color} {color:#6600ff}{_}to include the lib directory{_}{color}
* {color:#6600ff}{_}use warnings, strict, diagnostics are a good
practice{_}{color}
* {color:#6600ff}{_}use 'VCL::utils' is the only VCL module you should need
to include, all else should be handled by inheritance/objects{_}{color}

<a name="ModularizedArchitecture-ModuleInitialization"></a>
### Module Initialization

{color:#6600ff}{_}Explain how modules can implement initialize() subs which
are automatically called{_}{color}

<a name="ModularizedArchitecture-DatabaseConfigurationforModules"></a>
### Database Configuration for Modules

{color:#6600ff}{_}Explain module table, computer.moduleid,
managementnode.predictivemoduleid{_}{color}

<a name="ModularizedArchitecture-Cross-ModuleAccess"></a>
### Cross-Module Access

{color:#6600ff}{_}Explain why some modules shouldn't have access to others,
which is why Module.pm doesn't make os() and provisioner()
available{_}{color}

<a name="ModularizedArchitecture-Required&OptionalModuleSubroutines"></a>
### Required & Optional Module Subroutines

{color:#6600ff}{_}Explain:_{color}
* {color:#6600ff}{_}Perl's can() function{_}{color}
* {color:#6600ff}{_}core modules use can() to check if module
implements&nbsp;a subroutine{_}{color}
* {color:#6600ff}{_}some subs should be required such as OS::load(), most
should not{_}{color}
* {color:#6600ff}{_}if you can think of an exception why a sub wouldn't be
needed it shouldn't be required{_}{color}

<a name="ModularizedArchitecture-PackageOrganization"></a>
### Package Organization

{color:#6600ff}{_}Explain:_{color}
* {color:#6600ff}{_}how directories under lib/VCL should be
organized{_}{color}
* {color:#6600ff}{_}the 'package' line in the modules should match the
location of the file{_}{color}
** {color:#6600ff}{_}Example: "package VCL::Module::OS::Windows" resides in
"lib/VCL/Module/OS/Windows.pm"_{color}
* {color:#6600ff}{_}some core modules don't follow this - the state modules
reside directly under lib/VCL, should eventually reside under
lib/VCL/Module/State{_}{color}
