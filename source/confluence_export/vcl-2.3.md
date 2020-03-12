---
title: VCL 2.3
---

VCL 2.3 was release on July 20th, 2012

<a name="VCL2.3-TableofContents"></a>
## Table of Contents
   * [Download links](#VCL2.3-Downloadlinks)
   * [Release Notes](#VCL2.3-ReleaseNotes)
         * [I. Intro and Description](#VCL2.3-I.IntroandDescription)
         * [II. VCL Roadmap](#VCL2.3-II.VCLRoadmap)
         * [III. Getting Involved in the ASF VCL Community](#VCL2.3-III.GettingInvolvedintheASFVCLCommunity)
         * [IV. How to Submit Bugs and Feature Requests](#VCL2.3-IV.HowtoSubmitBugsandFeatureRequests)
   * [Change Log](#VCL2.3-ChangeLog)
         * [Sub-task](#VCL2.3-Sub-task)
         * [Bug](#VCL2.3-Bug)
         * [Improvement](#VCL2.3-Improvement)
         * [New Feature](#VCL2.3-NewFeature)
         * [Task](#VCL2.3-Task)

<a name="VCL2.3-Downloadlinks"></a>
## Download links

Please make sure to download VCL from a mirror server. The following link
will automatically select one for you that should be close to you. After
downloading it *make sure* you verify it with MD5 or SHA1 sums *AND* the
GPG signature (sums and signature files should be downloaded directly from
Apache, not from mirrors).

[Download ASF VCL 2.3](http://vcl.apache.org/downloads/download.cgi)
[GPG Signature](http://www.apache.org/dist/vcl/apache-VCL-2.3.tar.bz2.asc)
[MD5 Sum](http://www.apache.org/dist/vcl/apache-VCL-2.3.tar.bz2.md5)
[SHA1 Sum](http://www.apache.org/dist/vcl/apache-VCL-2.3.tar.bz2.sha1)
[VCL KEYS file](http://www.apache.org/dist/vcl/KEYS)


1. Verify the MD5 sum (output should be "apache-VCL-2.3.tar.bz2: OK"):
{tip}
md5sum \-c apache-VCL-2.3.tar.bz2.md5
{tip}
1. Verify the SHA1 sum (output should be "apache-VCL-2.3.tar.bz2: OK"):
{tip}
sha1sum \-c apache-VCL-2.3.tar.bz2.sha1
{tip}
1. Verify the GPG signature (you'll need to have [GnuPG](http://www.gnupg.org/)
 installed):
1. # download and import the VCL KEYS file (if you've imported the KEYS file
for previously releases, you do not need to import it again):
{tip}
gpg \--import KEYS
{tip}
1. # download the GPG Signature to the same location as the release file
1. # from the directory containing both the release file and the GPG
signature, run
{tip}
gpg \--verify apache-VCL-2.3.tar.bz2.asc
{tip}
1. For new installs, visit the on-line [installation guide](vcl-2.3-installation.html)
.
1. For upgrades, visit the on-line guide for your installed version (you can
find your version number after the Apache license header in vcl/index.php
in the web code - i.e. "ASF VCL 2.2.1"):
1. * [2.2.1 upgrade guide](vcl:upgrade-from-previous-version-(2.2.1-to-2.3).html)
1. * [2.2 upgrade guide](vcl:upgrade-from-previous-version-(2.2-to-2.3).html)
1. * [2.1 upgrade guide](vcl:upgrade-from-previous-version-(2.1-to-2.3).html)

<a name="VCL2.3-ReleaseNotes"></a>
## Release Notes

<a name="VCL2.3-I.IntroandDescription"></a>
#### I. Intro and Description

VCL, Virtual Computing Lab. The VCL can be many things, first and foremost
it is an open-source system used to dynamically provision and broker remote
access to a dedicated compute environment for an end-user. The provisioned
computers are typically housed in a data center and may be physical blade
servers, traditional rack mounted servers, or virtual machines. VCL can
also broker access to standalone machines such as a lab computers on a
university campus.

One of the primary goals of VCL is to deliver a dedicated compute
environment to a user for a limited time through a web interface. This
compute environment can range from something as simple as a virtual machine
running productivity software to a machine room blade running high end
software (i.e. a CAD, GIS, statistical package or an Enterprise level
application) to a cluster of interconnected physical (bare metal) compute
nodes.

Also using the scheduling API it can be used to automate the provisioning
of servers in a server farm or HPC cluster.

The release supports provisioning compute nodes using
* xCAT 1.3 and 2.x
* VMware Server 1.x and 2.x
* VMware ESX 3.5
* VMware ESXi 4.x and 5.x
* VMware vCenter
* KVM
* Virtual Box

<a name="VCL2.3-II.VCLRoadmap"></a>
#### II. VCL Roadmap

VCL 2.3 (this release)
* Service deployments
* Allow for additional connect methods for environments (port, other
protocols, etc)
* Added framework support for libvirt
* Added support for KVM
* Added support for OS X under ESX
* Added support for VMware VCenter
* Added multilingualization to frontend

VCL 2.4
* Improve additional connect methods
* NAT support
* Remove requirement for 2 NICs
* Support for Spice remote display protocol
* Scripted installation
* Support for ESX OS for end users
* Initial support for EC2 API and OpenStack

VCL 2.5
* Power management
* Improve cluster reservations
* Service deployment configuration management
* Initial support for Libcloud

VCL 2.6
* develop tools for managing both system and user storage

With each release, we'll be working toward making VCL easier to install. As
part of our move to development at the Apache Software Foundation, it is an
obvious goal to create a community of users and more developers around VCL.
Bringing in more developers should become easier as VCL becomes easier to
install.

<a name="VCL2.3-III.GettingInvolvedintheASFVCLCommunity"></a>
#### III. Getting Involved in the ASF VCL Community

There are five ways to become involved in the ASF VCL community.

* Join the mailing lists and participate in discussion. There are two
mailing lists: user@vcl.apache.org
dev@vcl.apache.org
To join user, send an empty message to
[user-subscribe@vcl.apache.org](mailto:user-subscribe@vcl.apache.org|click-to-subscribe.html)
. To join dev, send an empty
message to [dev-subscribe@vcl.apache.org](mailto:dev-subscribe@vcl.apache.org|click-to-subscribe.html)
.

* Submit bug reports and feature requests to our JIRA bug tracking system.
See section IV below for more information on doing this.

* Create documentation on our Confluence site. Create an account at [http://cwiki.apache.org/confluence/display/VCL/Index](http://cwiki.apache.org/confluence/display/VCL/Index)
 and just start adding content. (Note to current community: We should
create a page explaining the layout so new people will know where to add
content better.)

* Submit patches through the vcl-dev mailing list and via the JIRA bug
tracking system. Once you have become familiar with VCL, you can begin
assisting with the development of it by picking a JIRA issue to fix or by
adding a feature needed at your site. Then, contribute a patch of your
changes through the JIRA tracking system and send a message to the vcl-dev
list explaining what you have done.

* Become an official committer to the project. Once you have shown that you
have a good grasp of the project by submitting patches, you can further
join the development work by submitting a contributor license agreement
(CLA) to ASF and having a committer account created to directly contribute
code to the project.

* If you are interested in contributing something to the project, please
discuss it on the vcl-dev list BEFORE starting work on it. This allows the
community to be involved in decisions and allows current developers to
provide some guidance.


<a name="VCL2.3-IV.HowtoSubmitBugsandFeatureRequests"></a>
#### IV. How to Submit Bugs and Feature Requests

If you find a bug, please submit a bug report to our JIRA bug tracking
system at [http://issues.apache.org/jira/browse/VCL](http://issues.apache.org/jira/browse/VCL)
 (you will need to set up an account there if you haven't already done so -
it's free to anyone). Also, we would appreciate it if you mentioned that
you filed a bug on the vcl-dev list to make sure we don't miss it.

If you would like to requrest a new feature, you can also submit that in
the same way through JIRA (just select "New Feature" or "Improvement" as
the Issue Type). Again, it would be helpful if you mentioned that you filed
a feature request on the vcl-dev list.

After you have created a JIRA issue, you have the option to vote on it to
help us know how to prioritize issues. You can also "watch" the issue to
see when activity related to it is submitted.

<a name="VCL2.3-ChangeLog"></a>
## Change Log


Release Notes - VCL - Version 2.3

<a name="VCL2.3-Sub-task"></a>
####    Sub-task 

* \[[VCL-319](https://issues.apache.org/jira/browse/VCL-319)
\] -	     API LDAP authentication problem with servers where DN must be
looked up 
* \[[VCL-339](https://issues.apache.org/jira/browse/VCL-339)
\] -	     Add the KVM support for VCL 
* \[[VCL-419](https://issues.apache.org/jira/browse/VCL-419)
\] -	     allow private IP address to be set and modified for computers 

<a name="VCL2.3-Bug"></a>
####    Bug 

* \[[VCL-114](https://issues.apache.org/jira/browse/VCL-114)
\] -	     catch-22 with new installs for creating a vmprofile 
* \[[VCL-154](https://issues.apache.org/jira/browse/VCL-154)
\] -	     run_scp_command() is not catching some errors 
* \[[VCL-192](https://issues.apache.org/jira/browse/VCL-192)
\] -	     xCAT21.pm - does_image_exist routine  
* \[[VCL-225](https://issues.apache.org/jira/browse/VCL-225)
\] -	     no user groups to select from when adding a new user group 
* \[[VCL-230](https://issues.apache.org/jira/browse/VCL-230)
\] -	     duplicate entries created in userpriv table 
* \[[VCL-297](https://issues.apache.org/jira/browse/VCL-297)
\] -	     Windows code is using the private IP address from the database
rather than the hosts file 
* \[[VCL-328](https://issues.apache.org/jira/browse/VCL-328)
\] -	     shibboleth sp logout URL not using SSL 
* \[[VCL-342](https://issues.apache.org/jira/browse/VCL-342)
\] -	     problem selecting image revision id when making a cluster
reservation with identical subimages 
* \[[VCL-344](https://issues.apache.org/jira/browse/VCL-344)
\] -	     local admin account make sure has full access 
* \[[VCL-345](https://issues.apache.org/jira/browse/VCL-345)
\] -	     check for whitespace in add computers IP address field 
* \[[VCL-348](https://issues.apache.org/jira/browse/VCL-348)
\] -	     Setting privileges in web gui -- Slightly broken 
* \[[VCL-387](https://issues.apache.org/jira/browse/VCL-387)
\] -	     xcat 1.3 getmac regex not account for A-F 
* \[[VCL-396](https://issues.apache.org/jira/browse/VCL-396)
\] -	     vmprofiles displayed as &#39;Array&#39; when changing a
computer to vmhostinuse on computer utilities 
* \[[VCL-400](https://issues.apache.org/jira/browse/VCL-400)
\] -	     virtual hosts page shows all unassigned vms instead of
checking which ones the user can access 
* \[[VCL-420](https://issues.apache.org/jira/browse/VCL-420)
\] -	     Linux code not setting static IP address correctly 
* \[[VCL-422](https://issues.apache.org/jira/browse/VCL-422)
\] -	     Windows image capture may hang when cleanmgr.exe is executed
or the utility may not be installed 
* \[[VCL-427](https://issues.apache.org/jira/browse/VCL-427)
\] -	     for block allocations, setting the managing user group to none
means no one can edit it if a normal user created it 
* \[[VCL-429](https://issues.apache.org/jira/browse/VCL-429)
\] -	     Windows code does not always detect the correct public network
interface 
* \[[VCL-433](https://issues.apache.org/jira/browse/VCL-433)
\] -	     new revisions can be captured of kickstart images 
* \[[VCL-447](https://issues.apache.org/jira/browse/VCL-447)
\] -	     Notice: Uninitialized string offset: 0 in
.../vcl/.ht-inc/utils.php on line 3206 
* \[[VCL-452](https://issues.apache.org/jira/browse/VCL-452)
\] -	     Linux.pm get_file_size does not handle thinly-provisioned
files correctly 
* \[[VCL-456](https://issues.apache.org/jira/browse/VCL-456)
\] -	     groupwasnone variable is not properly initialized 
* \[[VCL-458](https://issues.apache.org/jira/browse/VCL-458)
\] -	     $virtual undefined in utils.php line 3678 
* \[[VCL-464](https://issues.apache.org/jira/browse/VCL-464)
\] -	     SSH password authentication not enabled for Linux images 
* \[[VCL-466](https://issues.apache.org/jira/browse/VCL-466)
\] -	     Support for Cygwin 1.7 
* \[[VCL-467](https://issues.apache.org/jira/browse/VCL-467)
\] -	     Members of a group from one affiliation have access to groups
with the same name from other affiliations 
* \[[VCL-468](https://issues.apache.org/jira/browse/VCL-468)
\] -	     health_check update 
* \[[VCL-469](https://issues.apache.org/jira/browse/VCL-469)
\] -	     Windows.pm may fail to return public IP address if the same
interface also has a non-public IP address bound 
* \[[VCL-470](https://issues.apache.org/jira/browse/VCL-470)
\] -	     The vSphere module does not implement the get_total_space
subroutine 
* \[[VCL-471](https://issues.apache.org/jira/browse/VCL-471)
\] -	     Problem copying vmware files from a datastore to a management
node using the vSphere API 
* \[[VCL-472](https://issues.apache.org/jira/browse/VCL-472)
\] -	     xCAT.pm fails if boot image mounts storage from a host other
than the management node 
* \[[VCL-473](https://issues.apache.org/jira/browse/VCL-473)
\] -	     query in findManagementNode in utils.php doesn&#39;t have
conditional to join tables 
* \[[VCL-474](https://issues.apache.org/jira/browse/VCL-474)
\] -	     recent versions of mysql don&#39;t accept double quotes to
signify strings in where clauses 
* \[[VCL-475](https://issues.apache.org/jira/browse/VCL-475)
\] -	     addShibUser in shibauth.php returns an array when it should be
returning a user id 
* \[[VCL-476](https://issues.apache.org/jira/browse/VCL-476)
\] -	     manage block allocation page may show incorrect next start
time 
* \[[VCL-478](https://issues.apache.org/jira/browse/VCL-478)
\] -	     Windows 6.x Sysprep code results in incorrect root password 
* \[[VCL-480](https://issues.apache.org/jira/browse/VCL-480)
\] -	     XMLRPCproccessBlockTime can throw an error about VMhostCheck
table already existing 
* \[[VCL-482](https://issues.apache.org/jira/browse/VCL-482)
\] -	     scheduler does not order VMs properly when no VMs are
preloaded with the selected image 
* \[[VCL-483](https://issues.apache.org/jira/browse/VCL-483)
\] -	     RPC::XML fails with latest version of libwww-perl 
* \[[VCL-484](https://issues.apache.org/jira/browse/VCL-484)
\] -	     Requests in the inuse and image states may be changed to
failed 
* \[[VCL-486](https://issues.apache.org/jira/browse/VCL-486)
\] -	     Measures against cross site scripting on the Login form 
* \[[VCL-487](https://issues.apache.org/jira/browse/VCL-487)
\] -	     Problem in screen transition after successful login
authentication 
* \[[VCL-488](https://issues.apache.org/jira/browse/VCL-488)
\] -	     Injected user&#39;s UID is hardcoded 
* \[[VCL-492](https://issues.apache.org/jira/browse/VCL-492)
\] -	     edit computer info for VM in maintenance state 
* \[[VCL-494](https://issues.apache.org/jira/browse/VCL-494)
\] -	     Typo in testsetup.php 
* \[[VCL-500](https://issues.apache.org/jira/browse/VCL-500)
\] -	     tomaintenance requests may start too early or fail if
scheduled in the future 
* \[[VCL-501](https://issues.apache.org/jira/browse/VCL-501)
\] -	     Linux.pm does not set the default gateway in the ifcfg file
for statically assigned addresses 
* \[[VCL-507](https://issues.apache.org/jira/browse/VCL-507)
\] -	     Deleted VMs appear in the list of unassigned VMs 
* \[[VCL-508](https://issues.apache.org/jira/browse/VCL-508)
\] -	     Modifying reservations to overlap past max causes hang 
* \[[VCL-509](https://issues.apache.org/jira/browse/VCL-509)
\] -	     error when adding computer with no groups selected 
* \[[VCL-510](https://issues.apache.org/jira/browse/VCL-510)
\] -	     insert correct architecture in image table when adding new
entry 
* \[[VCL-511](https://issues.apache.org/jira/browse/VCL-511)
\] -	     Errors in vcl.sql connectmethodmap 
* \[[VCL-512](https://issues.apache.org/jira/browse/VCL-512)
\] -	     Linux.pm does not determine correct block size for some
versions of Linux 
* \[[VCL-519](https://issues.apache.org/jira/browse/VCL-519)
\] -	     New-line control bug in an Edit Image page 
* \[[VCL-522](https://issues.apache.org/jira/browse/VCL-522)
\] -	     Error in vcl.sql line 1694 
* \[[VCL-523](https://issues.apache.org/jira/browse/VCL-523)
\] -	     Windows code does not set scheduled task credentials when
changing user passwords 
* \[[VCL-524](https://issues.apache.org/jira/browse/VCL-524)
\] -	     Windows get_network_configuration may return an empty hash 
* \[[VCL-529](https://issues.apache.org/jira/browse/VCL-529)
\] -	     invalid IP addresses are marked as valid in the
is_public_ip_address 
* \[[VCL-530](https://issues.apache.org/jira/browse/VCL-530)
\] -	     Database field for computer.RAM is limited to 65535 
* \[[VCL-533](https://issues.apache.org/jira/browse/VCL-533)
\] -	     error when trying to download dhcp data when private IP
address was not entered 
* \[[VCL-534](https://issues.apache.org/jira/browse/VCL-534)
\] -	     $cluster not reset in for loop in viewRequests 
* \[[VCL-536](https://issues.apache.org/jira/browse/VCL-536)
\] -	     xCAT partimage and image_architecture x86_64 
* \[[VCL-540](https://issues.apache.org/jira/browse/VCL-540)
\] -	     manageMapping not added to update-vcl.sql and vcl.sql files 
* \[[VCL-541](https://issues.apache.org/jira/browse/VCL-541)
\] -	     Remove &quot;return 0&quot; from all subroutines which
normally return an array or hash 
* \[[VCL-546](https://issues.apache.org/jira/browse/VCL-546)
\] -	     OS.pm does not determine the correct public interface name 
* \[[VCL-547](https://issues.apache.org/jira/browse/VCL-547)
\] -	     removing site maintenance entry from .ht-inc/maintenance
directory doesn&#39;t fully remove site from maintenance 
* \[[VCL-548](https://issues.apache.org/jira/browse/VCL-548)
\] -	     server reservations not owned by a user count toward that
user&#39;s overlapping reservation count 
* \[[VCL-549](https://issues.apache.org/jira/browse/VCL-549)
\] -	     AJAX error when creating a new schedule 
* \[[VCL-556](https://issues.apache.org/jira/browse/VCL-556)
\] -	     edit schedule groups code not doing permissions correctly 
* \[[VCL-558](https://issues.apache.org/jira/browse/VCL-558)
\] -	     vcld_cron_check uses incorrect name of VCL Daemon 
* \[[VCL-563](https://issues.apache.org/jira/browse/VCL-563)
\] -	     DHCP is not enabled during image capture 
* \[[VCL-567](https://issues.apache.org/jira/browse/VCL-567)
\] -	     image profile page does not reflect owner change after
changing the owner 
* \[[VCL-569](https://issues.apache.org/jira/browse/VCL-569)
\] -	     Incorrect public IP address being used if value in database
does not match computer&#39;s actual IP address 
* \[[VCL-573](https://issues.apache.org/jira/browse/VCL-573)
\] -	     Reservations which alter default imagemeta values may affect
other reservations 
* \[[VCL-574](https://issues.apache.org/jira/browse/VCL-574)
\] -	     reinstall option not happening when detecting inuse state 
* \[[VCL-588](https://issues.apache.org/jira/browse/VCL-588)
\] -	     Windows may retrieve network configuration before all network
interfaces are initialized 
* \[[VCL-589](https://issues.apache.org/jira/browse/VCL-589)
\] -	     Windows 7 and 2008 Sysprep not working 

<a name="VCL2.3-Improvement"></a>
####    Improvement 

* \[[VCL-82](https://issues.apache.org/jira/browse/VCL-82)
\] -	     Add additional information to notify() messages 
* \[[VCL-92](https://issues.apache.org/jira/browse/VCL-92)
\] -	     modify predictive loading algorithm level 1 to have 2
computers loaded with an image 
* \[[VCL-141](https://issues.apache.org/jira/browse/VCL-141)
\] -	     allow users to delete images that are set as currentimage 
* \[[VCL-168](https://issues.apache.org/jira/browse/VCL-168)
\] -	     Windows Media Player shortcut gets added to desktop for all
users 
* \[[VCL-219](https://issues.apache.org/jira/browse/VCL-219)
\] -	     Improve VMware disk cleanup - add checks for reservations 
* \[[VCL-234](https://issues.apache.org/jira/browse/VCL-234)
\] -	     give error when block reservations requests more resources
than concurrent use of image 
* \[[VCL-236](https://issues.apache.org/jira/browse/VCL-236)
\] -	     make Groups first tab on Manage Computers page 
* \[[VCL-249](https://issues.apache.org/jira/browse/VCL-249)
\] -	     denote which management node fields are required 
* \[[VCL-276](https://issues.apache.org/jira/browse/VCL-276)
\] -	     log Block reservation data 
* \[[VCL-311](https://issues.apache.org/jira/browse/VCL-311)
\] -	     add more fields to edit computer page 
* \[[VCL-313](https://issues.apache.org/jira/browse/VCL-313)
\] -	     need a way to set computers as vmhosts without a bare metal
provisioning engine 
* \[[VCL-321](https://issues.apache.org/jira/browse/VCL-321)
\] -	     user lookup tool doesn&#39;t show user group affiliation 
* \[[VCL-354](https://issues.apache.org/jira/browse/VCL-354)
\] -	     View Computers Table - State Coloring 
* \[[VCL-358](https://issues.apache.org/jira/browse/VCL-358)
\] -	     Improve VMware Windows image loading speed 
* \[[VCL-360](https://issues.apache.org/jira/browse/VCL-360)
\] -	     Allow users to delete images preloaded on computers which
aren&#39;t being used 
* \[[VCL-376](https://issues.apache.org/jira/browse/VCL-376)
\] -	     mark imagerevisions deleted when user deletes image. 
* \[[VCL-379](https://issues.apache.org/jira/browse/VCL-379)
\] -	     alert user if reservation has timed out when they click
Connect or Get RDP File 
* \[[VCL-381](https://issues.apache.org/jira/browse/VCL-381)
\] -	     Move firewall_compare_update to OS modules 
* \[[VCL-383](https://issues.apache.org/jira/browse/VCL-383)
\] -	     make future reservations that would be part of a block
allocation included in the block allocation 
* \[[VCL-384](https://issues.apache.org/jira/browse/VCL-384)
\] -	     Remove MAC addresses from ifcfg-eth* files for Linux images
during capture 
* \[[VCL-385](https://issues.apache.org/jira/browse/VCL-385)
\] -	     Hide noimage from showing in the list of images in Edit Image
Profiles 
* \[[VCL-390](https://issues.apache.org/jira/browse/VCL-390)
\] -	     Prevent auto-generated or invalid public IP address from being
displayed to user 
* \[[VCL-391](https://issues.apache.org/jira/browse/VCL-391)
\] -	     Windows Server 2003 shutdown and reboot fails 
* \[[VCL-393](https://issues.apache.org/jira/browse/VCL-393)
\] -	     Handle Windows computers going to sleep 
* \[[VCL-398](https://issues.apache.org/jira/browse/VCL-398)
\] -	     make block allocations tie up concurrent usage of image 
* \[[VCL-402](https://issues.apache.org/jira/browse/VCL-402)
\] -	     Login screensaver not needed for VMs 
* \[[VCL-404](https://issues.apache.org/jira/browse/VCL-404)
\] -	     Prevent and/or remove color code escape characters from SSH
output 
* \[[VCL-407](https://issues.apache.org/jira/browse/VCL-407)
\] -	     Add makesshgkh check in gen_node_key.sh 
* \[[VCL-408](https://issues.apache.org/jira/browse/VCL-408)
\] -	     Imaging reservations that fail very early on may not be put
into the maintenance state 
* \[[VCL-410](https://issues.apache.org/jira/browse/VCL-410)
\] -	     Update and improve install_perl_libs.pl script for VCL 2.3 
* \[[VCL-413](https://issues.apache.org/jira/browse/VCL-413)
\] -	     Management node OS object 
* \[[VCL-418](https://issues.apache.org/jira/browse/VCL-418)
\] -	     simplify adding LDAP authentication 
* \[[VCL-421](https://issues.apache.org/jira/browse/VCL-421)
\] -	     Update Windows code to work with Cygwin 1.7 
* \[[VCL-423](https://issues.apache.org/jira/browse/VCL-423)
\] -	     Suppress unnecessary warning messages from vcld.log 
* \[[VCL-432](https://issues.apache.org/jira/browse/VCL-432)
\] -	     auto capture for imaging and long-term reservations 
* \[[VCL-435](https://issues.apache.org/jira/browse/VCL-435)
\] -	     Add support for ESXi 4.1 scripted installs 
* \[[VCL-438](https://issues.apache.org/jira/browse/VCL-438)
\] -	     allow new users to be added to VCL when shibboleth
authentication is used without LDAP 
* \[[VCL-441](https://issues.apache.org/jira/browse/VCL-441)
\] -	     getPossibleRecentFailures in isAvailable can end up removing
only available machine 
* \[[VCL-444](https://issues.apache.org/jira/browse/VCL-444)
\] -	     time delay the display of the Get RDP File button to allow
vcld to grant access 
* \[[VCL-446](https://issues.apache.org/jira/browse/VCL-446)
\] -	     End of reservation notices  
* \[[VCL-450](https://issues.apache.org/jira/browse/VCL-450)
\] -	     Backend VMware improvements for 2.3 release 
* \[[VCL-453](https://issues.apache.org/jira/browse/VCL-453)
\] -	     iptables  
* \[[VCL-455](https://issues.apache.org/jira/browse/VCL-455)
\] -	     put alt text with a image generated by textimage.php 
* \[[VCL-460](https://issues.apache.org/jira/browse/VCL-460)
\] -	     Send critical notification if KMS or MAK activation fails 
* \[[VCL-461](https://issues.apache.org/jira/browse/VCL-461)
\] -	     Color depth is limited when connecting to Windows images via
RDP 
* \[[VCL-462](https://issues.apache.org/jira/browse/VCL-462)
\] -	     Remove Windows service pack installation files during image
capture 
* \[[VCL-479](https://issues.apache.org/jira/browse/VCL-479)
\] -	     remove dependency on mcrypt 
* \[[VCL-489](https://issues.apache.org/jira/browse/VCL-489)
\] -	     allow dhcp and hosts info to be downloaded about computers any
time instead of just when adding 
* \[[VCL-490](https://issues.apache.org/jira/browse/VCL-490)
\] -	     restrict fields when adding computers 
* \[[VCL-491](https://issues.apache.org/jira/browse/VCL-491)
\] -	     adding multiple computers - confusing error messages when
incorrect count entered 
* \[[VCL-495](https://issues.apache.org/jira/browse/VCL-495)
\] -	     Allow change of vmprofile for an active vmhost 
* \[[VCL-496](https://issues.apache.org/jira/browse/VCL-496)
\] -	     DataStructure.pm does not implement a
set_computer_private_ip_address subroutine 
* \[[VCL-497](https://issues.apache.org/jira/browse/VCL-497)
\] -	     dedup eppn 
* \[[VCL-498](https://issues.apache.org/jira/browse/VCL-498)
\] -	     simplify group time inputs 
* \[[VCL-499](https://issues.apache.org/jira/browse/VCL-499)
\] -	     support for controlling VMware vCenter infrastructure through
the vSphere SDK 
* \[[VCL-502](https://issues.apache.org/jira/browse/VCL-502)
\] -	     allow aspects of automatic user groups to be managed through
UI 
* \[[VCL-504](https://issues.apache.org/jira/browse/VCL-504)
\] -	     Multiple critical messages are generated if inuse process
fails to initialize 
* \[[VCL-505](https://issues.apache.org/jira/browse/VCL-505)
\] -	     Dojo is slow to load, especially on pages with many ancillary
class files 
* \[[VCL-506](https://issues.apache.org/jira/browse/VCL-506)
\] -	     Retrieve accurate computer hardware specs and update the
computer table 
* \[[VCL-513](https://issues.apache.org/jira/browse/VCL-513)
\] -	     allow block allocation control per affiliation 
* \[[VCL-514](https://issues.apache.org/jira/browse/VCL-514)
\] -	     decrease the number of queries done by the frontend 
* \[[VCL-515](https://issues.apache.org/jira/browse/VCL-515)
\] -	     suggest available time when selection not available instead of
showing time table 
* \[[VCL-517](https://issues.apache.org/jira/browse/VCL-517)
\] -	     Linux udev net-persistent rule 
* \[[VCL-520](https://issues.apache.org/jira/browse/VCL-520)
\] -	     Improving display control, on an detailed information of an
image 
* \[[VCL-521](https://issues.apache.org/jira/browse/VCL-521)
\] -	     An OS image named in japanese 2byte characters doesn&#39;t run 
* \[[VCL-528](https://issues.apache.org/jira/browse/VCL-528)
\] -	     customizing image capture flow using vcl_exclude_list 
* \[[VCL-543](https://issues.apache.org/jira/browse/VCL-543)
\] -	     OSX under ESXi 4.1 
* \[[VCL-544](https://issues.apache.org/jira/browse/VCL-544)
\] -	     Linux systemd services 
* \[[VCL-553](https://issues.apache.org/jira/browse/VCL-553)
\] -	     Make OS.pm wait_for_reboot arguments consistent with other
wait_* subroutines 
* \[[VCL-554](https://issues.apache.org/jira/browse/VCL-554)
\] -	     Add check to image capture to determine if user shutdown
computer 
* \[[VCL-557](https://issues.apache.org/jira/browse/VCL-557)
\] -	     xCAT2 reset node to boot state on DESTROY	
* \[[VCL-565](https://issues.apache.org/jira/browse/VCL-565)
\] -	     Convert code which directly accesses
$ENV\{management_node_info\} 
* \[[VCL-575](https://issues.apache.org/jira/browse/VCL-575)
\] -	     Improvements to gen-node-key.sh 
* \[[VCL-578](https://issues.apache.org/jira/browse/VCL-578)
\] -	     Improve how inuse reservations which aren&#39;t responding to
SSH are handled 

<a name="VCL2.3-NewFeature"></a>
####    New Feature 

* \[[VCL-30](https://issues.apache.org/jira/browse/VCL-30)
\] -	     additional user access methods for connecting to reserved
compute node  
* \[[VCL-323](https://issues.apache.org/jira/browse/VCL-323)
\] -	     ESX provisioning modules - based on snapshots 
* \[[VCL-367](https://issues.apache.org/jira/browse/VCL-367)
\] -	     make Connect and Get RDP File buttons check for reservation
being timed out 
* \[[VCL-399](https://issues.apache.org/jira/browse/VCL-399)
\] -	     add a dashboard where admins can see current state of VCL
system 
* \[[VCL-417](https://issues.apache.org/jira/browse/VCL-417)
\] -	     Provisioning module for VirtualBox 
* \[[VCL-463](https://issues.apache.org/jira/browse/VCL-463)
\] -	     add ability to deploy images as servers 
* \[[VCL-477](https://issues.apache.org/jira/browse/VCL-477)
\] -	     add caching of statistics data 
* \[[VCL-485](https://issues.apache.org/jira/browse/VCL-485)
\] -	     Multilingualization of Web UI 
* \[[VCL-527](https://issues.apache.org/jira/browse/VCL-527)
\] -	     Allow users to reinstall newer revisions 
* \[[VCL-545](https://issues.apache.org/jira/browse/VCL-545)
\] -	     Libvirt Provisioning Module 
* \[[VCL-550](https://issues.apache.org/jira/browse/VCL-550)
\] -	     Add post_reserve functionality to Windows code 

<a name="VCL2.3-Task"></a>
####    Task 

* \[[VCL-443](https://issues.apache.org/jira/browse/VCL-443)
\] -	     update XMLRPC example to use API v2 
* \[[VCL-576](https://issues.apache.org/jira/browse/VCL-576)
\] -	     Finalizing for 2.3 release
