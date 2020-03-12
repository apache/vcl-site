---
title: Operating System Module Inheritance
---

{gliffy:name=OS Modularization Transition|space=VCL|page=Operating System
Module Inheritance|align=center|size=L}
{gliffy:name=OS Module Inheritance|space=VCL|page=Operating System Module
Inheritance|align=center|size=L}
* Each row in the image table is configured with an OSid
(image.OSid),&nbsp;this points to the id column in the OS table (OS.id)
* Each&nbsp;row in the OS table is configured with a moduleid
(OS.moduleid), this points to the id column in the module table (module.id)
* The module table contains a column named perlpackage
(module.perlpackage), this tells the backend VCL code which Perl module to
load and use
* The module.perlpackage value, the package statement in the Perl module
file, and the directory structure of the Perl modules must all align
** module.perlpackage = VCL::Module::OS::Windows_mod::Version_5::XP_mod
** lib/VCL/Module/OS/Windows_mod/Version_5/XP_mod.pm:

    package VCL::Module::OS::Windows_mod::Version_5::XP_mod;

* Inheritance reduces redundant code
* Subroutines should reside as high up in the hierarchy as possible
** This allows all objects which&nbsp;are instantiated as a&nbsp;child
class to use the subroutine
* Child classes can implement subroutines with the same name as one
implemented by a parent class
** The child subroutine in the child class overrides the subroutine in the
parent class
{gliffy:name=Inheritance Example|space=VCL|page=Operating System Module
Inheritance|align=center|size=L}
