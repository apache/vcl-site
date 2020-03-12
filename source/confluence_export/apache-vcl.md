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
** The VCL [XMLRPC API](http://people.apache.org/~jfthomps/vcl_xmlrpc_api.html)
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
* Search: [http://markmail.org/set/jlmr2rdvup4w2](http://markmail.org/set/jlmr2rdvup4w2)
* User (old): [http://mail-archives.apache.org/mod_mbox/incubator-vcl-user](http://mail-archives.apache.org/mod_mbox/incubator-vcl-user)
* User (current): [http://mail-archives.apache.org/mod_mbox/vcl-user](http://mail-archives.apache.org/mod_mbox/vcl-user)
* Development (old): [http://mail-archives.apache.org/mod_mbox/incubator-vcl-dev](http://mail-archives.apache.org/mod_mbox/incubator-vcl-dev)
* Development (current): [http://mail-archives.apache.org/mod_mbox/vcl-dev](http://mail-archives.apache.org/mod_mbox/vcl-dev)

<a name="ApacheVCL-ProjectResources"></a>
# Project Resources

<table>
<tr><td> Confluence </td><td> [http://cwiki.apache.org/confluence/display/VCL](http://cwiki.apache.org/confluence/display/VCL)
 </td></tr>
<tr><td> Subversion Repository </td><td> [https://svn.apache.org/repos/asf/vcl](https://svn.apache.org/repos/asf/vcl)
 </td></tr>
<tr><td> JIRA </td><td> [http://issues.apache.org/jira/browse/VCL](http://issues.apache.org/jira/browse/VCL)
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

See the [VCL Installation](http://cwiki.apache.org/confluence/display/VCL/VCL+Installation)
 documentation for more information

<a name="ApacheVCL-WebFrontend"></a>
#### Web Frontend

* [Apache HTTP Server](http://httpd.apache.org/)
 1.3 or 2.x with SSL enabled ([Apache
License|http://www.apache.org/licenses/LICENSE-2.0])
* [PHP](http://www.php.net/)
&nbsp;5.0 or later ([PHP License|http://www.php.net/license/3_01.txt])
* PHP&nbsp;modules ([PHP License](http://www.php.net/license/3_01.txt)
):
** php-gd
** php-json
** php-mcrypt
** php-mysql
** php-openssl
** php-sysvsem
** php-xml
** php-xmlrpc
* [libmcrypt and mcrypt](http://sourceforge.net/projects/mcrypt/)
 libraries installed for php-mcrypt
([GPL|http://www.opensource.org/licenses/gpl-license.php])
* [Dojo Toolkit](http://dojotoolkit.org/)
 0.4.0 and 1.1.0 ([modified BSD license or the Academic Free License
version 2.1|http://dojotoolkit.org/license])

<a name="ApacheVCL-Database"></a>
#### Database

* [MySQL](http://dev.mysql.com)
 5.0 or later ([GPL|http://www.opensource.org/licenses/gpl-license.php])

<a name="ApacheVCL-ManagementNodeBackend"></a>
#### Management Node Backend

* Operating system - tested on CentOS 5 ([GPL](http://www.opensource.org/licenses/gpl-license.php)
), RedHat Advanced Server 4 and 5 ([Red
Hat|http://www.redhat.com/licenses/advancedservereula.html]), and RedHat
Fedora Core 7 and 9
([GPL|http://www.opensource.org/licenses/gpl-license.php])
* perl-DBD-MySQL ([Artistic](http://dev.perl.org/licenses/artistic.html)
 and [GPL|http://www.opensource.org/licenses/gpl-license.php]
)
* MySQL 5 client ([GPL](http://www.opensource.org/licenses/gpl-license.php)
)
* [Nmap](http://nmap.org/)
 security scanner ([Nmap|http://nmap.org/svn/COPYING] and [GPL|http://www.opensource.org/licenses/gpl-license.php]
)
* [OpenSSH](http://www.openssh.org/index.html)
 client (BSD)
* Perl 5.8.x ([Artistic](http://dev.perl.org/licenses/artistic.html)
 and [GPL|http://www.opensource.org/licenses/gpl-license.php]
)
* Perl modules available from CPAN
** [Class-Data-Inheritable](http://search.cpan.org/dist/Class-Data-Inheritable/)
 ([Artistic|http://dev.perl.org/licenses/artistic.html] and [GPL|http://www.opensource.org/licenses/gpl-license.php]
)
** [Compress-Raw-Zlib](http://search.cpan.org/dist/Compress-Raw-Zlib/)
([Artistic|http://dev.perl.org/licenses/artistic.html] and [GPL|http://www.opensource.org/licenses/gpl-license.php]
)
** [Crypt-SSLeay](http://search.cpan.org/dist/Crypt-SSLeay/)
 ([Artistic|http://dev.perl.org/licenses/artistic.html] and [GPL|http://www.opensource.org/licenses/gpl-license.php]
)
** [DBI](http://search.cpan.org/dist/DBI/)
 ([Artistic|http://dev.perl.org/licenses/artistic.html] and [GPL|http://www.opensource.org/licenses/gpl-license.php]
)
** [Devel-StackTrace](http://search.cpan.org/dist/Devel-StackTrace/)
 ([Artistic|http://dev.perl.org/licenses/artistic.html] and [GPL|http://www.opensource.org/licenses/gpl-license.php]
)
** [Exception-Class](http://search.cpan.org/dist/Exception-Class/)
 ([Artistic|http://dev.perl.org/licenses/artistic.html] and [GPL|http://www.opensource.org/licenses/gpl-license.php]
)
** [HTML-Parser](http://search.cpan.org/dist/HTML-Parser/)
 ([Artistic|http://dev.perl.org/licenses/artistic.html] and [GPL|http://www.opensource.org/licenses/gpl-license.php]
)
** [IO-Compress](http://search.cpan.org/dist/IO-Compress/)
 ([Artistic|http://dev.perl.org/licenses/artistic.html] and [GPL|http://www.opensource.org/licenses/gpl-license.php]
)
** [libwww-perl](http://search.cpan.org/dist/libwww-perl/)
 ([Artistic|http://dev.perl.org/licenses/artistic.html] and [GPL|http://www.opensource.org/licenses/gpl-license.php]
)
** [MailTools](http://search.cpan.org/dist/MailTools/)
 ([Artistic|http://dev.perl.org/licenses/artistic.html] and [GPL|http://www.opensource.org/licenses/gpl-license.php]
)
** [Object-InsideOut](http://search.cpan.org/dist/Object-InsideOut/)
 ([Artistic|http://dev.perl.org/licenses/artistic.html] and [GPL|http://www.opensource.org/licenses/gpl-license.php]
)
** [RPC-XML](http://search.cpan.org/dist/RPC-XML/)
 ([Artistic|http://dev.perl.org/licenses/artistic.html] and [LGPL|http://www.opensource.org/licenses/lgpl-2.1.php]
)
** [XML-Parser](http://search.cpan.org/dist/XML-Parser/)
 ([Artistic|http://dev.perl.org/licenses/artistic.html] and [GPL|http://www.opensource.org/licenses/gpl-license.php]
)
** [YAML](http://search.cpan.org/dist/YAML/)
 ([Artistic|http://dev.perl.org/licenses/artistic.html] and [GPL|http://www.opensource.org/licenses/gpl-license.php]
)
