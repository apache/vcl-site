---
title: Dependencies
---

<a name="Dependencies-Frontend"></a>
## Frontend

* Apache HTTP Server v1.3 or v2.x with SSL enabled - while VCL may run
under another webserver capable of running PHP code, it has only been
tested to work with Apache HTTP Server
* PHP 4 or 5, including these modules:
** php-mcrypt
** php-mysql
** php-xmlrpc
** php-gd
** php-xml
* Dojo Toolkit
* JPGraph
* FCKEditor (optional)
* useful to have the server set up to be able to send debugging emails

<a name="Dependencies-Backend"></a>
## Backend

* Perl
* Perl Modules (available from cpan.org)
** [http://search.cpan.org/CPAN/authors/id/M/MA/MARKOV/MailTools-2.04.tar.gz](http://search.cpan.org/CPAN/authors/id/M/MA/MARKOV/MailTools-2.04.tar.gz)
** [http://search.cpan.org/CPAN/authors/id/T/TM/TMTM/Class-Data-Inheritable-0.08.tar.gz](http://search.cpan.org/CPAN/authors/id/T/TM/TMTM/Class-Data-Inheritable-0.08.tar.gz)
** [http://search.cpan.org/CPAN/authors/id/D/DR/DROLSKY/Devel-StackTrace-1.20.tar.gz](http://search.cpan.org/CPAN/authors/id/D/DR/DROLSKY/Devel-StackTrace-1.20.tar.gz)
** [http://search.cpan.org/CPAN/authors/id/D/DR/DROLSKY/Exception-Class-1.26.tar.gz](http://search.cpan.org/CPAN/authors/id/D/DR/DROLSKY/Exception-Class-1.26.tar.gz)
** [http://search.cpan.org/CPAN/authors/id/J/JD/JDHEDDEN/Object-InsideOut-3.52.tar.gz](http://search.cpan.org/CPAN/authors/id/J/JD/JDHEDDEN/Object-InsideOut-3.52.tar.gz)
** [http://search.cpan.org/CPAN/authors/id/K/KW/KWILLIAMS/Module-Build-0.30.tar.gz](http://search.cpan.org/CPAN/authors/id/K/KW/KWILLIAMS/Module-Build-0.30.tar.gz)
** [http://search.cpan.org/CPAN/authors/id/A/AG/AGROLMS/GSSAPI-0.26.tar.gz](http://search.cpan.org/CPAN/authors/id/A/AG/AGROLMS/GSSAPI-0.26.tar.gz)
** [http://search.cpan.org/CPAN/authors/id/G/GB/GBARR/Authen-SASL-2.12.tar.gz](http://search.cpan.org/CPAN/authors/id/G/GB/GBARR/Authen-SASL-2.12.tar.gz)
** [http://search.cpan.org/CPAN/authors/id/R/RE/REATMON/XML-Stream-1.22.tar.gz](http://search.cpan.org/CPAN/authors/id/R/RE/REATMON/XML-Stream-1.22.tar.gz)
** [http://search.cpan.org/CPAN/authors/id/H/HA/HACKER/Net-XMPP-1.02.tar.gz](http://search.cpan.org/CPAN/authors/id/H/HA/HACKER/Net-XMPP-1.02.tar.gz)
** [http://search.cpan.org/CPAN/authors/id/R/RE/REATMON/Net-Jabber-2.0.tar.gz](http://search.cpan.org/CPAN/authors/id/R/RE/REATMON/Net-Jabber-2.0.tar.gz)
** [http://www.cpan.org/modules/by-module/XML/XML-Parser-2.36.tar.gz](http://www.cpan.org/modules/by-module/XML/XML-Parser-2.36.tar.gz)
** [http://www.cpan.org/modules/by-module/RPC/RPC-XML-0.64.tar.gz](http://www.cpan.org/modules/by-module/RPC/RPC-XML-0.64.tar.gz)
** [http://www.cpan.org/modules/by-module/Crypt/Crypt-SSLeay-0.57.tar.gz](http://www.cpan.org/modules/by-module/Crypt/Crypt-SSLeay-0.57.tar.gz)

<a name="Dependencies-BackendScripting&ProgrammingLanguages"></a>
### Backend Scripting & Programming Languages

* Perl - the backend is predominantly driven by Perl code
* DOS/Windows Batch - several batch (.cmd) files perform tasks
to&nbsp;configure Windows&nbsp;images&nbsp;
* VBScript - several VBScript (.vbs) files perform tasks to configure
Windows images
* INI files - Windows .ini files need to be configured to customize the
Windows installation (sysprep.ini, cmdlines.ini)

<a name="Dependencies-ProvisioningEngines"></a>
## Provisioning Engines

* xCAT 1.3 or xCAT 2.1 [xCAT.org](http://xcat.sourceforge.net)
* VMWare Free Server
* VMWare ESX can use native vmware-cmd or VMware perl toolkit
* VMWare ESXi requires [VMware perl toolkit](http://www.vmware.com/support/developer/viperltoolkit/)
* KVM
* IBM Smart Cloud computing ( in development, ask on the mailing list)

<a name="Dependencies-Images"></a>
## Images


<a name="Dependencies-WindowsImageUtilities&OtherFiles"></a>
### Windows Image Utilities & Other Files

* Windows Sysprep for each version of Windows being used, available from
microsoft.com( only needed for bare-metal loads)
* Driver files specific to each version/platform of Windows being used
* spdrvscn.exe utility - scans Windows drivers before an image is saved,
available from vernalex.com
* wsname.exe utility - renames computer according to registered DNS name,
available from mystuff.clarke.co.nz
* Cygwin with OpenSSH - allows management nodes to control loaded Windows
OS on blades, available from cygwin.com

<a name="Dependencies-LinuxKickstartDeployment"></a>
### Linux Kickstart Deployment

* installation media for Linux distribution that is supported by xCAT

<a name="Dependencies-Database"></a>
## Database

* MySQL
* PHPMyAdmin (optional)

<a name="Dependencies-Network"></a>
## Network

Two or Three networks (see [Network Layout](network-layout.html)
):
1. private network - where most control operations happen and where images
are pushed around
1. public network - how end users connect to the nodes
1. Blade Center management network - this is only needed if doing bare metal
deployment; it is used to communicate with the blade server management
modules to power on/off the blades and to configure the boot process

<a name="Dependencies-Hardware"></a>
## Hardware

VCL can deploy images on various types of hardware depending on your needs.
The following deployment methods have been tested with the listed hardware:
* bare metal kickstart deploys using xCAT:
** IBM BladeCenter Blade models HS20, HS21, HS22's
** Sun blade models X6220 and X6250
* bare metal image deploys using xCAT:
** IBM BladeCenter Blade models HS20 and HS21
* VMWare Free Server image deploys should work on any hardware with VMWare
Free Server installed and 2 network interfaces
* VMWare ESX or ESXi image deploys should work on any hardware with VMWare
ESX installed and 2 network interfaces
* VMWare vcenter
* KVM based image deploys should work on any VT capable hardware with KVM
hypervisor installed and 2 network interfaces

<a name="Dependencies-DevelopmenttoolsusedbyVCLcommitters"></a>
## Development tools used by VCL committers

* ActiveState Komodo IDE - used to develop several types of files,
commercial product
* SlickEdit
* VI/VIM
* Firebug plugin for Firefox
* WinSCP - used to manually transfer files to/from Windows images and
to/from Windows development machines
* PuTTY
