---
title: Apache VCL
---

<a name="ApacheVCL-ApacheVCL"></a>
# Apache VCL

The Apache VCL project.

VCL, Virtual Computing Lab. The VCL can be many things, first and foremost
it is a open-source system used to dynamically provision and broker remote
access to a dedicated compute environment for an end-user. The provisioned
computers are typically housed in a data center and may be physical blade
servers, traditional rack mounted servers, or virtual machines. VCL can
also broker access to standalone machines such as a lab computers on a
university campus.

One of the primary goals of VCL is to deliver a dedicated compute
environment to a user for a limited time through a web interface. This
compute environment can range from something as simple as a virtual machine
running productivity software to a machine room blade running high end
software (i.e. a CAD, GIS,statistical package or an Enterprise level
application) to a cluster of interconnected physical (bare metal) compute
nodes.

Also using the scheduling API it can be used to automate the provisioning
of servers in a server farm or HPC cluster.

<a name="ApacheVCL-UserDocumentation"></a>
# User Documentation

* [Overview for VCL Users](for-vcl-users.html)
 (those doing daily management of a VCL installation)
** [Making a Reservation](making-a-reservation.html)
** [Creating a New Image from a Base Image](creating-a-new-image-from-a-base-image.html)
** [Granting Access to a New Image](granting-access-to-a-new-image.html)
** [Example - Granting Two Sets of Users Access to Two Different Sets of Images](example---granting-two-sets-of-users-access-to-two-different-sets-of-images.html)
** [managegroups.py - Remotely managing user groups](managegroups.py---remotely-managing-user-groups.html)
** The VCL [XMLRPC API](https://people.apache.org/~jfthomps/vcl_xmlrpc_api.html)
* Documentation for VCL Administrators (those doing a VCL installation)
** [VCL&nbsp;Architecture](https://cwiki.apache.org/confluence/display/VCL/VCL+Architecture)
** [Administrator's FAQ](administrator's-faq.html)
** [VCL Installation (Current Release)](vcl-2.3-installation.html)
*** [VCL 2.3 Database Installation](vcl-2.3-database-installation.html)
*** [VCL 2.3 Web Code Installation](vcl-2.3-web-code-installation.html)
*** [VCL 2.3 Management Node Installation](vcl-2.3-management-node-installation.html)
*** [Adding support for partimage and partimage-ng to xCAT 2.x (unofficial)](adding-support-for-partimage-and-partimage-ng-to-xcat-2.x-(unofficial).html)
*** [Creating a Base Image](base-image-creation.html)
*** [Troubleshooting](troubleshooting.html)
*** [Terms](terms.html)

<a name="ApacheVCL-Community"></a>
# Community

Interested in joining the community or giving back to open source? There
are several ways to assist:
* Join the mailing lists below and discuss ideas.
* Contribute bug-fixes or get involved in development.
** [How to Become a committer](vcl:becoming-a-committer.html)
* Help with the documentation, both end-user and installation.
* Help improve the website.

Mailing lists
* User mailing list&nbsp; [mailto:user-subscribe@vcl.apache.org](mailto:user-subscribe@vcl.apache.org.html)
* Development List [dev-subscribe@vcl.apache.org](mailto:dev-subscribe@vcl.apache.org.html)

Archives
* Search: [https://markmail.org/set/jlmr2rdvup4w2](https://markmail.org/set/jlmr2rdvup4w2)
* User (old): [https://mail-archives.apache.org/mod_mbox/incubator-vcl-user](https://mail-archives.apache.org/mod_mbox/incubator-vcl-user)
* User (current): [https://mail-archives.apache.org/mod_mbox/vcl-user](https://mail-archives.apache.org/mod_mbox/vcl-user)
* Development (old): [https://mail-archives.apache.org/mod_mbox/incubator-vcl-dev](https://mail-archives.apache.org/mod_mbox/incubator-vcl-dev)
* Development (current): [https://mail-archives.apache.org/mod_mbox/vcl-dev](https://mail-archives.apache.org/mod_mbox/vcl-dev)

<a name="ApacheVCL-ProjectResources"></a>
# Project Resources

<table>
<tr><td> Confluence </td><td> [https://cwiki.apache.org/confluence/display/VCL](https://cwiki.apache.org/confluence/display/VCL)
 </td></tr>
<tr><td> Subversion Repository </td><td> [https://svn.apache.org/repos/asf/vcl](https://svn.apache.org/repos/asf/vcl)
 </td></tr>
<tr><td> JIRA </td><td> [https://issues.apache.org/jira/browse/VCL](https://issues.apache.org/jira/browse/VCL)
 </td></tr>
<tr><td> Current version </td><td> [VCL 2.2.1](vcl-2.2.1.html)
 </td></tr>
<tr><td> Release Roadmap </td><td> [ASF VCL JIRA Roadmap](https://issues.apache.org/jira/browse/VCL?report=com.atlassian.jira.plugin.system.project:roadmap-panel)
 </td></tr>
  
  
  
  
<tr><td> IRC </td><td> [\#asfvcl on Freenode](irc://irc.freenode.net/asfvcl.html)
 </td></tr>
</table>

<a name="ApacheVCL-ConceptualOverview"></a>
# Conceptual Overview

The conceptual overview below shows that remote users connect to the VCL
Scheduling Application (the web VCL portal) and request access to a desired
application environment. The application environment consists of an
operating system and a suite of applications. The computer types are
machine room blade servers, vmware virtual machines, and standalone
machines.
<table>
<tr><td> !VCLconceptoverview.gif</td><td>align=left! </td></tr>
</table>

<a name="ApacheVCL-VCLFeatureList"></a>
# VCL Feature List

* Automated provisioning, on-demand or future based
* Brokers user sessions
* Block allocations - provisioning larger number of compute environments
for a specific event
** For the class room
** For a conference workshop
* Physical ([bare-metal](#baremetal.html)
) provisioning using xCAT
* Virtual machine provisioning on VMware ESXi, VMware ESX Standard server,
VMware Free Server
* Image creation - allow end-users to create custom environments
* Image revision control - create multiple revisions of an image
* Statistics of environment usage
* Privilege control - grant varying levels of control to end-users through
web interface
** Image checkout, image creation, manage users, manage [resources](#resource.html)
, manage resource schedules
* Set available/unavailable schedules for [nodes](#node.html)
* Multiple [Management Nodes](#managementnode.html)
 for scalability
* API support for making requests and provisioning resources

{panel}
*Terminology*:{anchor:baremetal}Bare-metal = a physical server (such as a
blade server) as opposed to a virtual machine{anchor:node}Node = a
computer{anchor:resource}Resource = a compute node, an image, a management
node, or a schedule{anchor:managementnode}Management Node = a process
server or the machine where vcld is running; processes user requests
assigned by the scheduler; does the provisioning
{panel}

<a name="ApacheVCL-SystemRequirements"></a>
# System Requirements

See the [VCL Installation](https://cwiki.apache.org/confluence/display/VCL/VCL+Installation)
 documentation for more information

<a name="ApacheVCL-WebFrontend"></a>
#### Web Frontend

* [Apache HTTP Server](https://httpd.apache.org/)
 1.3 or 2.x with SSL enabled ([Apache
License|https://www.apache.org/licenses/LICENSE-2.0])
* [PHP](https://www.php.net/)
&nbsp;5.0 or later ([PHP License|https://www.php.net/license/3_01.txt])
* PHP&nbsp;modules ([PHP License](https://www.php.net/license/3_01.txt)
):
** php-gd
** php-json
** php-mcrypt
** php-mysql
** php-openssl
** php-sysvsem
** php-xml
** php-xmlrpc
* [libmcrypt and mcrypt](https://sourceforge.net/projects/mcrypt/)
 libraries installed for php-mcrypt
([GPL|https://www.opensource.org/licenses/gpl-license.php])
* [Dojo Toolkit](https://dojotoolkit.org/)
 0.4.0 and 1.1.0 ([modified BSD license or the Academic Free License
version 2.1|https://dojotoolkit.org/license])

<a name="ApacheVCL-Database"></a>
#### Database

* [MySQL](https://dev.mysql.com)
 5.0 or later ([GPL|https://www.opensource.org/licenses/gpl-license.php])

<a name="ApacheVCL-ManagementNodeBackend"></a>
#### Management Node Backend

* Operating system - tested on CentOS 5 ([GPL](https://www.opensource.org/licenses/gpl-license.php)
), RedHat Advanced Server 4 and 5 ([Red
Hat|https://www.redhat.com/licenses/advancedservereula.html]), and RedHat
Fedora Core 7 and 9
([GPL|https://www.opensource.org/licenses/gpl-license.php])
* perl-DBD-MySQL ([Artistic](https://dev.perl.org/licenses/artistic.html)
 and [GPL|https://www.opensource.org/licenses/gpl-license.php]
)
* MySQL 5 client ([GPL](https://www.opensource.org/licenses/gpl-license.php)
)
* [Nmap](https://nmap.org/)
 security scanner ([Nmap|https://nmap.org/svn/COPYING] and [GPL|https://www.opensource.org/licenses/gpl-license.php]
)
* [OpenSSH](https://www.openssh.org/index.html)
 client (BSD)
* Perl 5.8.x ([Artistic](https://dev.perl.org/licenses/artistic.html)
 and [GPL|https://www.opensource.org/licenses/gpl-license.php]
)
* Perl modules available from CPAN
** [Class-Data-Inheritable](https://search.cpan.org/dist/Class-Data-Inheritable/)
 ([Artistic|https://dev.perl.org/licenses/artistic.html] and [GPL|https://www.opensource.org/licenses/gpl-license.php]
)
** [Compress-Raw-Zlib](https://search.cpan.org/dist/Compress-Raw-Zlib/)
([Artistic|https://dev.perl.org/licenses/artistic.html] and [GPL|https://www.opensource.org/licenses/gpl-license.php]
)
** [Crypt-SSLeay](https://search.cpan.org/dist/Crypt-SSLeay/)
 ([Artistic|https://dev.perl.org/licenses/artistic.html] and [GPL|https://www.opensource.org/licenses/gpl-license.php]
)
** [DBI](https://search.cpan.org/dist/DBI/)
 ([Artistic|https://dev.perl.org/licenses/artistic.html] and [GPL|https://www.opensource.org/licenses/gpl-license.php]
)
** [Devel-StackTrace](https://search.cpan.org/dist/Devel-StackTrace/)
 ([Artistic|https://dev.perl.org/licenses/artistic.html] and [GPL|https://www.opensource.org/licenses/gpl-license.php]
)
** [Exception-Class](https://search.cpan.org/dist/Exception-Class/)
 ([Artistic|https://dev.perl.org/licenses/artistic.html] and [GPL|https://www.opensource.org/licenses/gpl-license.php]
)
** [HTML-Parser](https://search.cpan.org/dist/HTML-Parser/)
 ([Artistic|https://dev.perl.org/licenses/artistic.html] and [GPL|https://www.opensource.org/licenses/gpl-license.php]
)
** [IO-Compress](https://search.cpan.org/dist/IO-Compress/)
 ([Artistic|https://dev.perl.org/licenses/artistic.html] and [GPL|https://www.opensource.org/licenses/gpl-license.php]
)
** [libwww-perl](https://search.cpan.org/dist/libwww-perl/)
 ([Artistic|https://dev.perl.org/licenses/artistic.html] and [GPL|https://www.opensource.org/licenses/gpl-license.php]
)
** [MailTools](https://search.cpan.org/dist/MailTools/)
 ([Artistic|https://dev.perl.org/licenses/artistic.html] and [GPL|https://www.opensource.org/licenses/gpl-license.php]
)
** [Object-InsideOut](https://search.cpan.org/dist/Object-InsideOut/)
 ([Artistic|https://dev.perl.org/licenses/artistic.html] and [GPL|https://www.opensource.org/licenses/gpl-license.php]
)
** [RPC-XML](https://search.cpan.org/dist/RPC-XML/)
 ([Artistic|https://dev.perl.org/licenses/artistic.html] and [LGPL|https://www.opensource.org/licenses/lgpl-2.1.php]
)
** [XML-Parser](https://search.cpan.org/dist/XML-Parser/)
 ([Artistic|https://dev.perl.org/licenses/artistic.html] and [GPL|https://www.opensource.org/licenses/gpl-license.php]
)
** [YAML](https://search.cpan.org/dist/YAML/)
 ([Artistic|https://dev.perl.org/licenses/artistic.html] and [GPL|https://www.opensource.org/licenses/gpl-license.php]
)
