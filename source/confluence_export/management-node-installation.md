---
title: Management Node Installation
---

{excerpt}This page describes how to install and configure the backend VCL
management node components including the required Perl modules, VCL daemon
(vcld), and Windows utility dependencies.{excerpt}

<a name="ManagementNodeInstallation-Assumptions"></a>
## Assumptions

The following instructions assume the VCL [database has been installed and configured](database-configuration.html)
 and that the managment node information has been added to the database as
described on the [web code installation page|Web Code Installation]
.  This also assumes that the perl-DBD-MySQL-3.x and the mysql client
(mysql-5.x) packages are installed, for database communications.

<a name="ManagementNodeInstallation-DownloadtheBackendManagementNodeVCLCode"></a>
## Download the Backend Management Node VCL Code

Install the Subversion client if it is not already installed:






<a name="ManagementNodeInstallation-InstallRequiredPackages"></a>
## Install Required Packages

The following packages to be installed on the OS before installing the
required Perl modules.&nbsp;  These packages must be installed if they were
not installed as part of your base Linux install.&nbsp;  It is easiest to
use the package management utility for your OS \--\- yum, rpm, or other.

* expat
* expat-devel
* gcc
* krb5-libs
* krb5-devel
* libxml2
* libxml2-devel
* nmap
* openssl
* openssl-devel
* perl-DBD-MySQL
* xmlsec1-openssl

To install these packages using yum:



<a name="ManagementNodeInstallation-InstallRequiredPerlModules"></a>
## Install Required Perl Modules

The VCL Perl code running on the management node requires additional Perl
modules in order to run.  These Perl modules are available from [CPAN - The Comprehensive Perl Archive Network](http://cpan.org/)
.  A search engine for CPAN modules is available at [search.cpan.org|http://search.cpan.org/]
.

*{_}Note:_* _Licensing information for each required Perl module is
included below.&nbsp; The content of the "License:" lines was copied from
the CPAN page for each module.&nbsp; The content of the other line was
copied from the copyright section in the module's source code or from the
module's readme file._
* [Class-Data-Inheritable](http://search.cpan.org/dist/Class-Data-Inheritable/)
** License: Perl ([Artistic](http://dev.perl.org/licenses/artistic.html)
 and [GPL|http://www.opensource.org/licenses/gpl-license.php]
)
** Copyright (c) 2000-2005, Damian Conway and Michael G Schwern. All Rights
 Reserved.
  
  
This module is free software. It may be used, redistributed and/or modified
 under the same terms as Perl itself.
* [Compress-Raw-Zlib](http://search.cpan.org/dist/Compress-Raw-Zlib/)
** License: Perl ([Artistic](http://dev.perl.org/licenses/artistic.html)
 and [GPL|http://www.opensource.org/licenses/gpl-license.php]
)
  
  
This program is free software; you can redistribute it and/or modify it
under  the same terms as Perl itself.
* [Crypt-SSLeay](http://search.cpan.org/dist/Crypt-SSLeay/)
** License: Perl ([Artistic](http://dev.perl.org/licenses/artistic.html)
 and [GPL|http://www.opensource.org/licenses/gpl-license.php]
)
** Copyright (c) 2006-2007 David Landgren.
Copyright (c) 1999-2003 Joshua Chamas.
Copyright (c) 1998 Gisle Aas.
This program is free software; you can redistribute it and/or modify it
under
the same terms as Perl itself.
* [DBI](http://search.cpan.org/dist/DBI/)
** License: Perl ([Artistic](http://dev.perl.org/licenses/artistic.html)
 and [GPL|http://www.opensource.org/licenses/gpl-license.php]
)
** The DBI module is Copyright (c) 1994-2009 Tim Bunce. Ireland. All rights
 reserved.
  
  
You may distribute under the terms of either the GNU General Public License
or the Artistic License, as specified in the Perl 5.10.0 README file.
* [Devel-StackTrace](http://search.cpan.org/dist/Devel-StackTrace/)
** License: Perl ([Artistic](http://dev.perl.org/licenses/artistic.html)
 and [GPL|http://www.opensource.org/licenses/gpl-license.php]
)
** Copyright (c) 2000-2006 David Rolsky. All rights reserved. This program
is free software; you can redistribute it and/or modify it under the same
terms as Perl itself.
  
  
* [Exception-Class](http://search.cpan.org/dist/Exception-Class/)
** License: Perl ([Artistic](http://dev.perl.org/licenses/artistic.html)
 and [GPL|http://www.opensource.org/licenses/gpl-license.php]
)
** Copyright (c) 2000-2009 David Rolsky. All rights reserved. This program
is  free software; you can redistribute it and/or modify it under the same
terms as  Perl itself.
  
  
* [HTML-Parser](http://search.cpan.org/dist/HTML-Parser/)
** License: Perl ([Artistic](http://dev.perl.org/licenses/artistic.html)
 and [GPL|http://www.opensource.org/licenses/gpl-license.php]
)
** Copyright 1996-2008 Gisle Aas. All rights reserved.
Copyright 1999-2000 Michael A. Chase.  All rights reserved.
This library is free software; you can redistribute it and/or modify it
under  the same terms as Perl itself.
* [IO-Compress](http://search.cpan.org/dist/IO-Compress/)
** License: Perl ([Artistic](http://dev.perl.org/licenses/artistic.html)
 and [GPL|http://www.opensource.org/licenses/gpl-license.php]
)
  
  
This program is free software; you can redistribute it and/or modify it
under  the same terms as Perl itself.
* [libwww-perl](http://search.cpan.org/dist/libwww-perl/)
** License: Perl ([Artistic](http://dev.perl.org/licenses/artistic.html)
 and [GPL|http://www.opensource.org/licenses/gpl-license.php]
)
** Copyright 1995-2004 Gisle Aas.
  
  
This library is free software; you can redistribute it and/or modify it
under  the same terms as Perl itself.
* [MailTools](http://search.cpan.org/dist/MailTools/)
** License: Perl ([Artistic](http://dev.perl.org/licenses/artistic.html)
 and [GPL|http://www.opensource.org/licenses/gpl-license.php]
)
** Copyrights 1995-2000 Graham Barr <gbarr@pobox.com> and 2001-2007 Mark 
Overmeer <perl@overmeer.net>.
  
  
This program is free software; you can redistribute it and/or modify it
under  the same terms as Perl itself.
* [Object-InsideOut](http://search.cpan.org/dist/Object-InsideOut/)
** License: Perl ([Artistic](http://dev.perl.org/licenses/artistic.html)
 and [GPL|http://www.opensource.org/licenses/gpl-license.php]
)
** Copyright 2005 - 2009 Jerry D. Hedden. All rights reserved.
  
  
This program is free software; you can redistribute it and/or modify it
under  the same terms as Perl itself.
* [RPC-XML](http://search.cpan.org/dist/RPC-XML/)
** License: Perl ([Artistic](http://dev.perl.org/licenses/artistic.html)
 and [GPL|http://www.opensource.org/licenses/gpl-license.php]
)
** This file and the code within are copyright (c) 2009 by Randy J. Ray.
  
  
Copying and distribution are permitted under the terms of the Artistic  License 2.0 ([http://www.opensource.org/licenses/artistic-license-2.0.php](http://www.opensource.org/licenses/artistic-license-2.0.php)
)  or the GNU LGPL 2.1
([http://www.opensource.org/licenses/lgpl-2.1.php|http://www.opensource.org/licenses/lgpl-2.1.php]).
* [XML-Parser](http://search.cpan.org/dist/XML-Parser/)
** License: Unknown
** _Note: The license type is shown as "Unknown" on the_ _[CPAN page](http://search.cpan.org/dist/XML-Parser/)
_ _for this module and the_ _[POD
documentation|http://search.cpan.org/dist/XML-Parser/Parser.pm]_ _conained
within the source code does not contain a copyright section.&nbsp; The_
_[README|http://cpansearch.perl.org/src/MSERGEANT/XML-Parser-2.36/README]_
\_file for this module does, however, contain a heading with the following
information:_Copyright (c) 1998-2000 Larry Wall and Clark Cooper. All
rights reserved.
This program is free software; you can redistribute it and/or modify it
under the same terms as Perl itself.
* [YAML](http://search.cpan.org/dist/YAML/)
** License: Perl ([Artistic](http://dev.perl.org/licenses/artistic.html)
 and [GPL|http://www.opensource.org/licenses/gpl-license.php]
)
** Copyright (c) 2005, 2006, 2008. Ingy d�t Net.
  
  
Copyright (c) 2001, 2002, 2005. Brian Ingerson.
  
  
Some parts copyright (c) 2009 Adam Kennedy
  
  
This program is free software; you can redistribute it and/or modify it
under  the same terms as Perl itself.

The following Perl modules are only required if VCL is configured to send
instant messages via Jabber.&nbsp; Jabber support can be enabled or
disabled by configuring the "jabber=" line in the vcld.conf file.&nbsp; The
following modules do not need to be installed if Jabber support is
disabled.

* [Net-Jabber](http://search.cpan.org/dist/Net-Jabber/)
** License: Unknown
** _Note: The license type is shown as "Unknown" on the_ _[CPAN page](http://search.cpan.org/dist/Net-Jabber/)
_ _for this module.&nbsp; However, the_
_[http://search.cpan.org/dist/XML-Parser/Parser.pm]__[POD
documentation|http://search.cpan.org/~reatmon/Net-Jabber-2.0/lib/Net/Jabber.pm]_
\_conained within the source code contains a copyright section with the
following text:_This module is free software, you can redistribute it
and/or modify it under	the same terms as Perl itself.
* [Net-XMPP](http://search.cpan.org/dist/Net-XMPP/)
** License: [LGPL](http://www.opensource.org/licenses/lgpl-license.php)
** This module is free software, you can redistribute it and/or modify it
under  the LGPL.
* [Module-Build](http://search.cpan.org/dist/Module-Build/)
** License: Perl ([Artistic](http://dev.perl.org/licenses/artistic.html)
 and [GPL|http://www.opensource.org/licenses/gpl-license.php]
)
** Copyright (c) 2001-2006 Ken Williams. All rights reserved.
  
  
This library is free software; you can redistribute it and/or modify it
under  the same terms as Perl itself.
* [XML-Stream](http://search.cpan.org/dist/XML-Stream/)
** License: Unknown
** _Note: The license type is shown as "Unknown" on the_ _[CPAN page](http://search.cpan.org/dist/XML-Stream/)
_ _for this module.&nbsp; However, the_ _[POD
documentation|http://search.cpan.org/dist/XML-Stream/lib/XML/Stream.pm#COPYRIGHT]_
\_conained within the source code contains a copyright section with the
following text:_This module is free software; you can redistribute it
and/or modify it under	the same terms as Perl itself.
* [Authen-SASL](http://search.cpan.org/dist/Authen-SASL/)
** License: Perl ([Artistic](http://dev.perl.org/licenses/artistic.html)
 and [GPL|http://www.opensource.org/licenses/gpl-license.php]
)
** Copyright (c) 1998-2005 Graham Barr. All rights reserved. This program
is  free software; you can redistribute it and/or modify it under the same
terms as  Perl itself.
* [Digest::SHA1](http://search.cpan.org/dist/Digest-SHA1/)
** License: Perl ([Artistic](http://dev.perl.org/licenses/artistic.html)
 and [GPL|http://www.opensource.org/licenses/gpl-license.php]
)
** This library is free software; you can redistribute it and/or modify it
under  the same terms as Perl itself.
Copyright 1999-2004 Gisle Aas.
Copyright 1997 Uwe Hollerbach.




<a name="ManagementNodeInstallation-Runinstall_perl_libs.plScript"></a>
#### Run install_perl_libs.pl Script

A script is provided in the managementnode/bin directory called
*install_perl_libs.pl* which will attempt to download and install the
required perl libraries.&nbsp; Run the script:



Run the script a 2nd time to check if all of the modules the script is
configured to install were successfully installed. Output similar to the
following should be displayed for each module:

    URL: http://search.cpan.org/CPAN/authors/id/T/TI/TIMB/DBI-1.609.tar.gz
    Module filename: DBI-1.609.tar.gz
    Module name: DBI-1.609
    Module package: DBI
    Checking if DBI is installed
    Module is already installed: DBI
    ==============================================================================


<a name="ManagementNodeInstallation-HowtoTestifRequiredPerlModulesareInstalled"></a>
#### How to Test if Required Perl Modules are Installed

Run the following command to execute the utils.pm file:

    perl /usr/local/vcl/lib/VCL/utils.pm

Executing utils.pm does not actually do anything but this will tell you if
VCL will be able to run.&nbsp; If any Perl modules are missing you will see
 "Can't locate" lines:



    pre-execution: config file being used: /etc/vcl/vcld.conf
    Uncaught exception from user code:
    ������� VCLD : /etc/vcl/vcld.conf does not exist, exiting --� No such file
or directory
    BEGIN failed--compilation aborted at /usr/local/vcl/lib/VCL/utils.pm line
616.
    �at /usr/local/vcl/lib/VCL/utils.pm line 616


<a name="ManagementNodeInstallation-WhattodoifaModuleisMissing"></a>
#### What to do if a Module is Missing

1. Determine the name of the missing module by looking at the "Can't locate"
line
1. Search for the missing module on search.cpan.org and install it manually


<a name="ManagementNodeInstallation-HowtoInstallaPerl&nbsp;ModuleManually"></a>
#### How to Install a Perl&nbsp;Module Manually

1. Change directories to /tmp:
*cd /tmp*&nbsp;
1. Download the module's source package using wget:
*wget* *[http://search.cpan.org/CPAN/authors/id/G/GA/GAAS/libwww-perl-5.827.tar.gz](http://search.cpan.org/CPAN/authors/id/G/GA/GAAS/libwww-perl-5.827.tar.gz)
*
1. Unpack the source package using tar:
*tar xzf libwww-perl-5.827.tar.gz*
1. The previous command should have created a libwww-perl-5.827 directory,
change to this directory:
*cd libwww-perl-5.827*
1. Create a makefile with the following command:
*perl Makefile.PL*
1. Compile the module:
*make*
1. Test the module:
*make test*
1. Install the module:
*make install*
The last line you should see should be:



<a name="ManagementNodeInstallation-HowtoInstallaPerlModuleUsingCPAN"></a>
#### How to Install a Perl Module Using CPAN

1. Enter the CPAN shell:
*perl \-MCPAN \-e shell*
1. You will need to configure CPAN if it's the first time it is being run.
Enter *No* at the first prompt to auto-configure the CPAN module.
1. Search for a module using the "m" command:
*m /Zlib/*
You should find the module you were looking for on a line like this:


1. Install the module:
*install Compress::Zlib*
1. Answer *yes* if asked to install any prerequisite modules
The last line you should see should be:



<a name="ManagementNodeInstallation-DownloadRequiredUtilities&Drivers"></a>
## Download Required Utilities & Drivers



<a name="ManagementNodeInstallation-WindowsXPandServer2003DeploymentTools(Sysprep)"></a>
#### Windows XP and Server 2003 Deployment Tools (Sysprep)


The Windows XP and Server 2003 Deployment Tools are available for free from
Microsoft and are required in order for the capture of Windows XP and
Server 2003 VCL images to work.&nbsp; The Sysprep utility is included in
the Deployment Tools.&nbsp; You do not need to download Sysprep for Windows
Vista or Server 2008 because it is included in the operating system.



Links to the downloads are below.&nbsp; You should be able to use the XP
SP2 or SP3 version assuming the image you are capturing contains Windows XP
Service Pack 3.&nbsp; We have seen problems with drivers not being
installed correctly using the SP3 version of the deployment tools so the
SP2 version is recommended.


Download: [Windows XP Service Pack 2 Deployment Tools](http://www.microsoft.com/downloads/details.aspx?familyid=3E90DC91-AC56-4665-949B-BEDA3080E0F6&displaylang=en)
Download: [Windows XP Service Pack 3 Deployment Tools](http://www.microsoft.com/downloads/details.aspx?FamilyID=673a1019-8e3e-4be0-ac31-70dd21b5afa7&displaylang=en)
Download: [System Preparation tool for Windows Server 2003 Service Pack 2 Deployment](http://www.microsoft.com/downloads/details.aspx?familyid=93F20BB1-97AA-4356-8B43-9584B7E72556&displaylang=en)

The Sysprep files need to be extracted from the file you download which is
in Microsoft's .cab format.&nbsp; It is easiest to extract the files on a
Windows computer.&nbsp; Windows Explorer is able to open the .cab file and
then the files contained within can be copied elsewhere.&nbsp; There are
also some Linux utilities which claim to be able to extract .cab files.

Copy the extracted Windows XP Sysprep files to the following directory on
the management node after they have been extracted:
{panel}
/usr/local/vcl/tools/Windows_XP/Utilities/Sysprep
{panel}Copy the extracted Windows Server 2003 Sysprep files to the
following directory on the management node after they have been extracted:
{panel}
/usr/local/vcl/tools/Windows_Server_2003/Utilities/Sysprep
{panel}The Sysprep directories should already exist on the management node
because they exist the Subversion repository.&nbsp; There should already be
a sysprep.inf file in each Sysprep directory.&nbsp; This is the base
Sysprep template file for VCL included in the Subversion repository.

The Sysprep directories should contain the following files at a minimum:
{panel}
\-rw-rw-r-\- 1 root root 25600 Aug 18 17:32 setupcl.exe
\-rw-rw-r-\- 1 root root 88576 Aug 18 17:32 sysprep.exe
\-rw-rw-r-\- 1 root root&nbsp; 2574 Aug 18 17:32 sysprep.inf
{panel}

<a name="ManagementNodeInstallation-Configuresysprep.inf"></a>
#### Configure sysprep.inf

Your organizations's Windows XP product key needs to be entered into the
Windows XP sysprep.inf file.&nbsp; Find the *ProductKey* line and replace
*WIN_XP_PRO_KEY* with *your organization's Windows XP product key* in  the
following file:
{panel}
/usr/local/vcl/tools/Windows_XP/Utilities/Sysprep/sysprep.inf
{panel}Your organizations's Windows Server 2003 product key needs to be
entered into the Windows Server 2003 sysprep.inf file.&nbsp; Find the
*ProductKey* line and replace *WIN_2003_ENT_KEY* with *your organization's
Windows Server 2003 product key* in  the following file:
{panel}
/usr/local/vcl/tools/Windows_Server_2003/Utilities/Sysprep/sysprep.inf
{panel}

<a name="ManagementNodeInstallation-DownloadDrivers"></a>
#### Download Drivers

Drivers which aren't included with Windows must be downloaded and saved to
the management node. The drivers required will vary greatly depending on
the hardware. The only way to know what additional drivers you need is to
install Windows on a computer and check for missing drivers.

The drivers must be copied to the appropriate directory on the management
node. The VCL image capture process copies the driver directories to the
computer before an image is captured. Drivers from multiple directories
will be copied based on the version of Windows being captured. There are
driver directories under *tools* for each version of Windows (Windows XP,
Windows Vista) and for each version group of Windows (version 5, 6). This
allows drivers which are common to multiple versions of Windows to be
shared in the management node tools directory structure.

For example, if a chipset driver works for all versions of Windows, it can
be saved in:
*tools/Windows/Drivers/Chipset*

If Windows XP and Windows Server 2003 both use the same network driver, it
can be saved in:
*tools/Windows_Version_5/Drivers/Network*

If a storage driver only works for Windows XP, it should be saved in:
*tools/Windows_XP/Drivers/Storage*


During the image capture process, each Windows version directory is copied
to the computer under C:\Cygwin\home\root\VCL. The order in which the
Windows version directories are copied goes from most general to most
specific.&nbsp; In the example above, the order would be:
1. *tools/Windows/Drivers/Chipset*
1. *tools/Windows_Version_5/Drivers/Network*
1. *tools/Windows_XP/Drivers/Storage*

The resulting directory structure on the Windows computer will be:
* *C:\Cygwin\home\root\VCL\Drivers*
** *\Chipset* \- driver works for all versions of windows
** *\Network* \- driver works for Windows XP and Server 2003
** *\Storage* \- driver only works for Windows XP

The following list shows which driver files should be saved in the driver
directories:

* *tools/Windows/Drivers* \- drivers common to all versions of Windows
** *tools/Windows_Version_5/Drivers* \- drivers used by Windows XP and
Server 2003
*** *tools/Windows_Version_XP/Drivers* \- drivers only used by Windows XP
*** *tools/Windows_Version_Server_2003/Drivers* \- drivers only used by
Windows Server 2003
** *tools/Windows_Version_6/Drivers* \- drivers used by Windows Vista and
Server 2008
*** *tools/Windows_Vista/Drivers* \- drivers only used by Windows Vista
*** *tools/Windows_Server_2008/Drivers* \- drivers only used by Windows
Server 2008

The directory structure under each Drivers directory does not matter. It is
helpful to organize each directory by driver class, and each directory
should be organized using the same theme.&nbsp; For example:
* *tools/Windows_Version_XP/Drivers*
** *Chipset*
** *Network*
** *Storage*
** *Video*

<a name="ManagementNodeInstallation-Add3rdPartyMassStorageDriverIDstosysprep.inf"></a>
#### Add 3rd Party Mass Storage Driver IDs to sysprep.inf

This step is complicated.&nbsp; 3rd party mass storage hardware IDs and
driver .inf file paths must be added to the SysprepMassStorage section in
sysprep.inf for Windows XP and Windows Server 2003 in order for the saved
image to boot properly on different hardware.
1. Identify the mass storage drivers required for your hardware which aren't
native to Windows
1. Download drivers for your hardware
1. Each driver will have 1 or more .inf files. Examine the .inf files. Find
all lines in this format containing a PnP device ID:
*%DevDescD1% = SYMMPI_Inst, PCI\VEN_1000&DEV_0054&SUBSYS_1F041028*
The PnP device ID in the example above is:
*PCI\VEN_1000&DEV_0054&SUBSYS_1F041028*
1. Each PnP device ID should be added to the sysprep.inf file under the \[SysprepMassStorage\](sysprepmassstorage\.html)
 section using the following format:
ID = "C:\Sysprep\Drivers\<driver directory>\<.inf file path>"

Example: LSI SAS drivers commonly need to be downloaded and the hardware
IDs need to be added to the sysprep.inf files in order for computers with
LSI SAS controllers to boot.
1. Download the LSI SAS driver from [ibm.com](http://www-947.ibm.com/systems/support/supportsite.wss/docdisplay?lndocid=MIGR-5073138&brandind=5000020)
: ibm_dd_mptsas_1.30.02.00_windows_32-64.exe
1. Extract the ZIP file (it's a self-extracting zip; you can unzip it with
whatever unzip tool you prefer)
1. Copy the files from the 32 bit XP directory (image/xp-32) to the
appropriate directory on the management node:
*tools/Windows/Drivers/Storage/LSI-SAS*
1. Locate the .inf file included with the driver is:
*tools/Windows/Drivers/Storage/LSI-SAS/*{*}symmpi.inf*
1. Locate the PnP ID lines in the .inf file:
{PANEL}
\[LSI\](lsi\.html)
%DevDesc2% = SYMMPI_Inst, PCI\VEN_1000&DEV_0622
%DevDesc3% = SYMMPI_Inst, PCI\VEN_1000&DEV_0624
%DevDesc4% = SYMMPI_Inst, PCI\VEN_1000&DEV_0626
%DevDesc5% = SYMMPI_Inst, PCI\VEN_1000&DEV_0628
%DevDesc6% = SYMMPI_Inst, PCI\VEN_1000&DEV_0030
%DevDesc7% = SYMMPI_Inst, PCI\VEN_1000&DEV_0032
%DevDesc8% = SYMMPI_Inst, PCI\VEN_1000&DEV_0050
%DevDesc9% = SYMMPI_Inst, PCI\VEN_1000&DEV_0054
%DevDesc10% = SYMMPI_Inst, PCI\VEN_1000&DEV_0058
%DevDesc11% = SYMMPI_Inst, PCI\VEN_1000&DEV_0056
%DevDesc12% = SYMMPI_Inst, PCI\VEN_1000&DEV_0640
%DevDesc13% = SYMMPI_Inst, PCI\VEN_1000&DEV_0646
%DevDesc14% = SYMMPI_Inst, PCI\VEN_1000&DEV_0062
\[DELL\](dell\.html)
%DevDescD1% = SYMMPI_Inst, PCI\VEN_1000&DEV_0054&SUBSYS_1F041028
%DevDescD2% = SYMMPI_Inst, PCI\VEN_1000&DEV_0054&SUBSYS_1F051028
%DevDescD3% = SYMMPI_Inst, PCI\VEN_1000&DEV_0054&SUBSYS_1F061028
%DevDescD4% = SYMMPI_Inst, PCI\VEN_1000&DEV_0054&SUBSYS_1F071028
%DevDescD5% = SYMMPI_Inst, PCI\VEN_1000&DEV_0054&SUBSYS_1F081028
%DevDescD6% = SYMMPI_Inst, PCI\VEN_1000&DEV_0054&SUBSYS_1F091028
%DevDescD7% = SYMMPI_Inst, PCI\VEN_1000&DEV_0058&SUBSYS_1F0E1028
%DevDescD8% = SYMMPI_Inst, PCI\VEN_1000&DEV_0058&SUBSYS_1F0F1028
%DevDescD9% = SYMMPI_Inst, PCI\VEN_1000&DEV_0058&SUBSYS_1F101028
{PANEL}
1. Based on the contents of the .inf file, the following is added to the Windows XP and Windows Server 2003 sysprep.inf files under \[SysprepMassStorage\](sysprepmassstorage\.html)
:
{PANEL}
PCI\VEN_1000&DEV_0622 = "C:\Sysprep\Drivers\Storage\LSI-SAS\symmpi.inf"
PCI\VEN_1000&DEV_0624 = "C:\Sysprep\Drivers\Storage\LSI-SAS\symmpi.inf"
PCI\VEN_1000&DEV_0626 = "C:\Sysprep\Drivers\Storage\LSI-SAS\symmpi.inf"
PCI\VEN_1000&DEV_0628 = "C:\Sysprep\Drivers\Storage\LSI-SAS\symmpi.inf"
PCI\VEN_1000&DEV_0030 = "C:\Sysprep\Drivers\Storage\LSI-SAS\symmpi.inf"
PCI\VEN_1000&DEV_0032 = "C:\Sysprep\Drivers\Storage\LSI-SAS\symmpi.inf"
PCI\VEN_1000&DEV_0050 = "C:\Sysprep\Drivers\Storage\LSI-SAS\symmpi.inf"
PCI\VEN_1000&DEV_0054 = "C:\Sysprep\Drivers\Storage\LSI-SAS\symmpi.inf"
PCI\VEN_1000&DEV_0058 = "C:\Sysprep\Drivers\Storage\LSI-SAS\symmpi.inf"
PCI\VEN_1000&DEV_0056 = "C:\Sysprep\Drivers\Storage\LSI-SAS\symmpi.inf"
PCI\VEN_1000&DEV_0640 = "C:\Sysprep\Drivers\Storage\LSI-SAS\symmpi.inf"
PCI\VEN_1000&DEV_0646 = "C:\Sysprep\Drivers\Storage\LSI-SAS\symmpi.inf"
PCI\VEN_1000&DEV_0062 = "C:\Sysprep\Drivers\Storage\LSI-SAS\symmpi.inf"
PCI\VEN_1000&DEV_0054&SUBSYS_1F041028 =
"C:\Sysprep\Drivers\Storage\LSI-SAS\symmpi.inf"
PCI\VEN_1000&DEV_0054&SUBSYS_1F051028 =
"C:\Sysprep\Drivers\Storage\LSI-SAS\symmpi.inf"
PCI\VEN_1000&DEV_0054&SUBSYS_1F061028 =
"C:\Sysprep\Drivers\Storage\LSI-SAS\symmpi.inf"
PCI\VEN_1000&DEV_0054&SUBSYS_1F071028 =
"C:\Sysprep\Drivers\Storage\LSI-SAS\symmpi.inf"
PCI\VEN_1000&DEV_0054&SUBSYS_1F081028 =
"C:\Sysprep\Drivers\Storage\LSI-SAS\symmpi.inf"
PCI\VEN_1000&DEV_0054&SUBSYS_1F091028 =
"C:\Sysprep\Drivers\Storage\LSI-SAS\symmpi.inf"
PCI\VEN_1000&DEV_0058&SUBSYS_1F0E1028 =
"C:\Sysprep\Drivers\Storage\LSI-SAS\symmpi.inf"
PCI\VEN_1000&DEV_0058&SUBSYS_1F0F1028 =
"C:\Sysprep\Drivers\Storage\LSI-SAS\symmpi.inf"
PCI\VEN_1000&DEV_0058&SUBSYS_1F101028 =
"C:\Sysprep\Drivers\Storage\LSI-SAS\symmpi.inf"
{PANEL}If you have hardware using an LSI SAS controller (IBM HS21 blades),
the section above can be copied and pasted into your sysprep.inf files:
{panel}
/usr/local/vcl/tools/Windows_XP/Utilities/Sysprep/sysprep.inf
{panel}
{panel}
/usr/local/vcl/tools/Windows_Server_2003/Utilities/Sysprep/sysprep.inf
{panel}

<a name="ManagementNodeInstallation-WSName-WorkstationNameChangingUtility"></a>
#### WSName - Workstation Name Changing Utility

{color:#ff0000}{*}NOTICE:*{color}&nbsp;The WSName.exe utility&nbsp;is no
longer	available.&nbsp;&nbsp;The set_computer_name.vbs script which calls
WSName.exe&nbsp;will be  rewritten for the 2.2 release of VCL. In the
meantime, this script is being left  intact in case you have a previously
released version of WSName.exe or are able  to obtain it from another
source.

The wsname.exe utility is used by VCL to name Windows computers.&nbsp; It
does a	reverse DNS lookup so that the computer name is set to the name
registered for	its public IP address.&nbsp; The utility is called by
set_computer_name.vbs when a  Windows image is loaded.&nbsp; The utility is
not vital for the load process to work.  &nbsp;However, the computer will
receive a random name if the script is missing or  fails to run.

If you do have a previously released version of WSName.exe or are able to 
locate it from another souce, save WSName.exe in the following location on
the  management node:
{panel}
/usr/local/vcl/tools/Windows/Utilities/WSName/wsname.exe
{panel}

<a name="ManagementNodeInstallation-NewSID-WindowsSIDChangingUtility"></a>
#### NewSID - Windows SID Changing Utility

NewSID.exe is used to change the SID of a Windows computer if Sysprep is
not used.&nbsp; Download the NewSID.exe utility:

Download: [NewSID.exe](http://technet.microsoft.com/en-us/sysinternals/bb897418.aspx)

Save the NewSID.exe utility in the following location on the management
node:
{panel}
/usr/local/vcl/tools/Windows/Utilities/NewSID/newsid.exe
{panel}

<a name="ManagementNodeInstallation-SPDrvScn-WindowsDriverScanningUtility"></a>
#### SPDrvScn - Windows Driver Scanning Utility

SPDrvScn.exe is used before an image is captured to enter the paths of
drivers to the Windows registry so that they are loaded when Sysprep
attempts to install devices.&nbsp; Download the SPDrvScn.exe utility:

Download: [SPDrvScn.exe](http://vernalex.com/tools/spdrvscn/)

Save the SPDrvScn.exe utility in the following location on the management
node:
{panel}
/usr/local/vcl/tools/Windows/Utilities/SPDrvScn/spdrvscn.exe
{panel}

<a name="ManagementNodeInstallation-ConfiguretheSSHClient"></a>
## Configure the SSH Client

To insure that the management node can SSH into your virtual machines
without problems, you will need to edit the SSH client config for the root
user:




Add the following lines to the top of the configuration file.


    Host <vmhost> <vmhost ip>
       UserKnownHostsFile /dev/null
       StrictHostKeyChecking no


Where:

* <vmhost> - Is a wildcard reference to the hostnames for your virtual
machines. 
** For example, if your VM hostnames look like: vmhost1, vmhost2,
vmhost3.... then replace <vmhost> with "vmhost*"

* <vmhost ip> - Is a wildcard IP reference to the IPs used by your virtual
machines. 
** For example, if your VMs all have IP addresses starting with 10.0.0,
then replace <vmhost ip> with "10.0.0.*"

This will insure that new VM hosts will not hang on the known hosts prompts
when the management node attempts to connect to them for the first time.

<a name="ManagementNodeInstallation-Configurevcld.conf"></a>
## Configure vcld.conf

1. Create the /etc/vcl directory:
*mkdir /etc/vcl*&nbsp;
1. Copy the generic vcld.conf file to /etc/vcl:
*cp /usr/local/vcl/etc/vcl/vcld.conf /etc/vcl*
1. Edit the /etc/vcl/vcld.conf file:
*vi /etc/vcl/vcld.conf*
The following lines must be configured in order to start the VCL daemon
(vcld) and allow it to check in to the database:
1. * FQDN - the fully qualified name of the management node, this should
match the name that was configured for the management node in the database
1. * server - the IP address or FQDN of the database server
1. * LockerWrtUser - database user account with write privileges
1. * wrtPass - database user password
1. Save the vcld.conf file

<a name="ManagementNodeInstallation-InstalltheVCLDaemon(vcld)&nbsp;Service"></a>
## Install the VCL Daemon (vcld)&nbsp;Service

1. Copy the vcld service script to /etc/init.d and name it vcld:
*cp /usr/local/vcl/bin/S99vcld.linux /etc/init.d/vcld*
1. Add the vcld service using chkconfig:
*/sbin/chkconfig \--add vcld*
1. Configure the vcld service to automatically run at runtime levels 3-5:
*/sbin/chkconfig \--level 345 vcld on*

<a name="ManagementNodeInstallation-StartandCheck&nbsp;thevcldService"></a>
## Start and Check&nbsp;the vcld Service

1. Start the vcld service:
*/sbin/service vcld start*
You should see output similar to the following:

    pre-execution: config file being used: /etc/vcl/vcld.conf
    FQDN is not listed
    pre-execution: process name is set to: vcld
    pre-execution: verbose mode is set to: 1
    pre-execution: testing mode is set to: 0
    pre-execution: log file being used: /var/log/vcld.log
    pre-execution: PID file being used: /var/run/vcld.pid
    Created process 23696 renamed to vcld ...
    ���������������������������������������������������������� [� OK� ]

*/etc/init.d/vcld start*
1. Check the vcld service by monitoring the vcld.log file:
*tail \-f /var/log/vcld.log*
You should see the following being added to the log file every few seconds
if the management node is checking in with the database:


