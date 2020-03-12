---
title: VCL 2.2
---

{{% toc %}}

<a name="VCL2.2-Downloadlinks"></a>
## Download links

Please make sure to download VCL from an mirror server. The following link
will automatically select one for you that should be close to you. After
downloading it *make sure* you verify it with MD5 or SHA1 sums *AND* the
GPG signature (sums and signature files should be downloaded directly from
Apache, not from mirrors).

[Download ASF VCL 2.2](http://vcl.apache.org/downloads/download.cgi?Preferred=http://archive.apache.org/dist/&action=download&filename=%2Fincubator%2Fvcl%2Fapache-VCL-2.2-incubating.tar.bz2)<br>
[GPG Signature](http://archive.apache.org/dist/incubator/vcl/apache-VCL-2.2-incubating.tar.bz2.asc)<br>
[MD5 Sum](http://archive.apache.org/dist/incubator/vcl/apache-VCL-2.2-incubating.tar.bz2.md5)<br>
[SHA1 Sum](http://archive.apache.org/dist/incubator/vcl/apache-VCL-2.2-incubating.tar.bz2.sha1)<br>
[VCL KEYS file](http://www.apache.org/dist/vcl/KEYS)

Run the following command to verify the MD5 sum. You should get the same
number that is in apache-VCL-2.2-incubating.tar.bz2.md5:

    md5sum apache-VCL-2.2-incubating.tar.bz2

Similarly, Run the following command to verify the SHA1 sum. You should get
the same number that is in apache-VCL-2.2-incubating.tar.bz2.sha1:

    sha1sum apache-VCL-2.2-incubating.tar.bz2

To verify the GPG signature (you'll need to have [GnuPG](http://www.gnupg.org/)
 installed):

1. download and import the VCL KEYS file:

    gpg --import KEYS
1. download the GPG Signature to the same location as the release file
1. from the directory containing both the release file and the GPG
signature, run

    gpg --verify apache-VCL-2.2-incubating.tar.bz2.asc

For new installs, visit the on-line [installation guide](vcl-2.2-installation.html).

For upgrades from version 2.1, visit the on-line [upgrade guide](upgrade-from-previous-version.html).



<a name="VCL2.2-ReleaseNotes"></a>
## Release Notes

<a name="VCL2.2-I.IntroandDescription"></a>
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

The release supports provisioning nodes using xCAT 1.3, xCAT 2.x, VMWare
Server 1.x, VMWare Server 2.x, VMWare ESX 3.5, and VMWare ESXi with both
purchased licenses and free licenses.

<a name="VCL2.2-II.VCLRoadmap"></a>
#### II. VCL Roadmap

VCL 2.2 (this release)

* support for xCAT 2.x
* VMWare Free Server 2.x and ESXi 4
* improve block reservations (renamed to block allocations)

VCL 2.3

* Service deployments
* power management
* improve cluster reservations

VCL 2.4

* additional and improved hypervisor support
* KVM and possibly others (virtual box and XEN)
* Allow for additional access methods for environments (port, other
protocols, etc)

VCL 2.5

* develop tools for managing both system and user storage

With each release, we'll be working toward making VCL easier to install. As
part of our move to development at the Apache Software Foundation, it is an
obvious goal to create a community of users and more developers around VCL.
Bringing in more developers should become easier as VCL becomes easier to
install.

<a name="VCL2.2-III.GettingInvolvedintheASFVCLCommunity"></a>
#### III. Getting Involved in the ASF VCL Community

There are five ways to become involved in the ASF VCL community.

* Join the mailing lists and participate in discussion. There are two
mailing lists:<br>
user@vcl.apache.org<br>
dev@vcl.apache.org<br>
To join user, send an empty message to
[user-subscribe@vcl.apache.org](mailto:user-subscribe@vcl.apache.org). 
To join dev, send an empty message to 
[dev-subscribe@vcl.apache.org](mailto:dev-subscribe@vcl.apache.org).

* Submit bug reports and feature requests to our JIRA bug tracking system.
See section IV below for more information on doing this.

* [Create documentation](/comm/contribute-documentation.html) on our CMS site. 

* Submit patches through the dev mailing list and via the JIRA bug
tracking system. Once you have become familiar with VCL, you can begin
assisting with the development of it by picking a JIRA issue to fix or by
adding a feature needed at your site. Then, contribute a patch of your
changes through the JIRA tracking system and send a message to the dev
list explaining what you have done.

* Become an official committer to the project. Once you have shown that you
have a good grasp of the project by submitting patches, you can further
join the development work by submitting a contributor license agreement
(CLA) to ASF and having a committer account created to directly contribute
code to the project.

* If you are interested in contributing something to the project, please
discuss it on the dev list BEFORE starting work on it. This allows the
community to be involved in decisions and allows current developers to
provide some guidance.


<a name="VCL2.2-IV.HowtoSubmitBugsandFeatureRequests"></a>
#### IV. How to Submit Bugs and Feature Requests

If you find a bug, please submit a bug report to our JIRA bug tracking
system at [http://issues.apache.org/jira/browse/VCL](http://issues.apache.org/jira/browse/VCL)
 (you will need to set up an account there if you haven't already done so -
it's free to anyone). Also, we would appreciate it if you mentioned that
you filed a bug on the dev list to make sure we don't miss it.

If you would like to requrest a new feature, you can also submit that in
the same way through JIRA (just select "New Feature" or "Improvement" as
the Issue Type). Again, it would be helpful if you mentioned that you filed
a feature request on the dev list.

After you have created a JIRA issue, you have the option to vote on it to
help us know how to prioritize issues. You can also "watch" the issue to
see when activity related to it is submitted.

<a name="VCL2.2-ChangeLog"></a>
## Change Log


Release Notes - VCL - Version 2.2

<a name="VCL2.2-Bug"></a>
####    Bug 

* \[[VCL-121](https://issues.apache.org/jira/browse/VCL-121)
\] -	     special characters in API passwords not handled correctly 
* \[[VCL-150](https://issues.apache.org/jira/browse/VCL-149)
\] -	     Pages do not display correctly with IE8 
* \[[VCL-154](https://issues.apache.org/jira/browse/VCL-154)
\] -	     run_scp_command() is not catching permission denied errors 
* \[[VCL-158](https://issues.apache.org/jira/browse/VCL-158)
\] -	     utils.pm setstaticaddress() does not work correctly for
Windows 
* \[[VCL-159](https://issues.apache.org/jira/browse/VCL-159)
\] -	     xCAT.pm is not always waiting long enough for ssh to respond
on load 
* \[[VCL-160](https://issues.apache.org/jira/browse/VCL-160)
\] -	     Sysprep is overwriting DevicePath key after spdrvscn.exe runs 
* \[[VCL-165](https://issues.apache.org/jira/browse/VCL-165)
\] -	     Fix syntax bugs cause reservation processes to die 
* \[[VCL-181](https://issues.apache.org/jira/browse/VCL-181)
\] -	     VCL desktop request tool - use API to make reservations 
* \[[VCL-189](https://issues.apache.org/jira/browse/VCL-189)
\] -	     cannot add a computer in maintenance state 
* \[[VCL-193](https://issues.apache.org/jira/browse/VCL-193)
\] -	     IP address field not large enough for 15-characters 
* \[[VCL-194](https://issues.apache.org/jira/browse/VCL-194)
\] -	     Marking new computer to be &quot;maintenance&quot; status
causes indexing error 
* \[[VCL-197](https://issues.apache.org/jira/browse/VCL-197)
\] -	     _is_user_added routine  
* \[[VCL-210](https://issues.apache.org/jira/browse/VCL-210)
\] -	     getdynamicaddress returns 127.0.01 for missing public adapter 
* \[[VCL-214](https://issues.apache.org/jira/browse/VCL-214)
\] -	     Windows modules don't always disable autoadminlogon 
* \[[VCL-215](https://issues.apache.org/jira/browse/VCL-215)
\] -	     reservation_failed sub in State.pm may change state of
computer currently in maintenance 
* \[[VCL-220](https://issues.apache.org/jira/browse/VCL-220)
\] -	     VMs in the available state which aren't assigned to a VM host
may be reserved 
* \[[VCL-221](https://issues.apache.org/jira/browse/VCL-221)
\] -	     Add check to make sure post_load tasks have run before
reserving a computer 
* \[[VCL-227](https://issues.apache.org/jira/browse/VCL-227)
\] -	     deleting user group that owns a resource group 
* \[[VCL-233](https://issues.apache.org/jira/browse/VCL-233)
\] -	     all calls to simpleAddRequest need to check for all return
codes 
* \[[VCL-241](https://issues.apache.org/jira/browse/VCL-241)
\] -	     detailed loading summary does not compute times correctly for
future reservations that are preloaded 
* \[[VCL-242](https://issues.apache.org/jira/browse/VCL-242)
\] -	     currentimage.txt permissions incorrect set 
* \[[VCL-245](https://issues.apache.org/jira/browse/VCL-245)
\] -	     esx.pm - always reloads  
* \[[VCL-250](https://issues.apache.org/jira/browse/VCL-250)
\] -	     authentication for XML RPC X-User doesn't properly check to
see if no authtype was found 
* \[[VCL-258](https://issues.apache.org/jira/browse/VCL-258)
\] -	     cluster loads - cluster_info file 
* \[[VCL-260](https://issues.apache.org/jira/browse/VCL-260)
\] -	     Problems occur if root is not the owner of /home/root for
Windows images 
* \[[VCL-261](https://issues.apache.org/jira/browse/VCL-261)
\] -	     Windows.pm filesystem_entry_exists() subroutine may return
true even if output contains &quot;file not found&quot; 
* \[[VCL-262](https://issues.apache.org/jira/browse/VCL-262)
\] -	     Windows capture may remove &quot;Log on as a service&quot;
right for existing accounts 
* \[[VCL-265](https://issues.apache.org/jira/browse/VCL-265)
\] -	     Linux adduser cmd - remove uid parameter if uid not defined in
user table  
* \[[VCL-266](https://issues.apache.org/jira/browse/VCL-266)
\] -	     New process detects another reload process being complete
before it should 
* \[[VCL-267](https://issues.apache.org/jira/browse/VCL-267)
\] -	     cluster loads  listing wrong parent and child addresses
cluster_info file 
* \[[VCL-269](https://issues.apache.org/jira/browse/VCL-269)
\] -	     Windows.pm logoff_users() does not detect disconnected users 
* \[[VCL-273](https://issues.apache.org/jira/browse/VCL-273)
\] -	     Single quotes in image pretty name can cause image capture to
fail 
* \[[VCL-299](https://issues.apache.org/jira/browse/VCL-299)
\] -	     shib users may have incorrect full name and email address. 
* \[[VCL-300](https://issues.apache.org/jira/browse/VCL-300)
\] -	     shib users always have email notices turned off 
* \[[VCL-303](https://issues.apache.org/jira/browse/VCL-303)
\] -	     tomaintenance reservations inserting wrong image revision 
* \[[VCL-306](https://issues.apache.org/jira/browse/VCL-306)
\] -	     Web GUI code has hard coded Eastern Time Zone information -
breaks in other time zones 
* \[[VCL-307](https://issues.apache.org/jira/browse/VCL-307)
\] -	     add empty post_reserve routine UnixLab.pm OS module 
* \[[VCL-317](https://issues.apache.org/jira/browse/VCL-317)
\] -	     scheduler doesn't take imagerevision into account 
* \[[VCL-318](https://issues.apache.org/jira/browse/VCL-318)
\] -	     API error if invalid affiliation is used 
* \[[VCL-325](https://issues.apache.org/jira/browse/VCL-325)
\] -	     removing a subimage from a cluster can result in all subimages
getting removed 
* \[[VCL-327](https://issues.apache.org/jira/browse/VCL-327)
\] -	     set_computer_name.vbs causes Sysprep to hang if certain
applications are installed 
* \[[VCL-329](https://issues.apache.org/jira/browse/VCL-329)
\] -	     DataStructure.pm get_computer_private_ip_address() not
handling all valid formats in /etc/hosts 
* \[[VCL-331](https://issues.apache.org/jira/browse/VCL-331)
\] -	     Windows code does not handle special characters in Scheduled
Task names when changing passwords 
* \[[VCL-332](https://issues.apache.org/jira/browse/VCL-332)
\] -	     cannot delete block requests once the start date has passed 
* \[[VCL-333](https://issues.apache.org/jira/browse/VCL-333)
\] -	     DataStructure %ENV hash not get detected in _initialize
routine  
* \[[VCL-334](https://issues.apache.org/jira/browse/VCL-334)
\] -	     numeric userids are not handled correctly 
* \[[VCL-337](https://issues.apache.org/jira/browse/VCL-337)
\] -	     Windows.pm delete_files_by_pattern may delete unintended files
if an environment variable isn't defined 
* \[[VCL-338](https://issues.apache.org/jira/browse/VCL-338)
\] -	     vmprofiles that are in use can be deleted 
* \[[VCL-340](https://issues.apache.org/jira/browse/VCL-340)
\] -	     cannot change name of vmprofile 
* \[[VCL-346](https://issues.apache.org/jira/browse/VCL-346)
\] -	     getdynamicaddress routine regex issue 
* \[[VCL-347](https://issues.apache.org/jira/browse/VCL-347)
\] -	     cluster connect page rdp file 
* \[[VCL-349](https://issues.apache.org/jira/browse/VCL-349)
\] -	     sql insert queries for image and imagerevision tables 
* \[[VCL-353](https://issues.apache.org/jira/browse/VCL-353)
\] -	     vmware.pm inserting new images - if original name is not in
proper format $oldname does not get set correctly. 
* \[[VCL-356](https://issues.apache.org/jira/browse/VCL-356)
\] -	     vmware esx pm - vmware image directories 
* \[[VCL-362](https://issues.apache.org/jira/browse/VCL-362)
\] -	     vmware.pm power command output not detected under ESX 3.5 
* \[[VCL-363](https://issues.apache.org/jira/browse/VCL-363)
\] -	     Passwords for existing Linux accounts are reset when the root
password is set 
* \[[VCL-364](https://issues.apache.org/jira/browse/VCL-364)
\] -	     vmhostid removed when vm put in maintenance state 
* \[[VCL-368](https://issues.apache.org/jira/browse/VCL-368)
\] -	     pre-capture and post load linux steps correct sed cmd line
options 
* \[[VCL-370](https://issues.apache.org/jira/browse/VCL-370)
\] -	     Reservation ID not defined errors occur for cluster
reservations 
* \[[VCL-371](https://issues.apache.org/jira/browse/VCL-371)
\] -	     Private IP address is not being found in /etc/hosts under some
circumstances 
* \[[VCL-377](https://issues.apache.org/jira/browse/VCL-377)
\] -	     multiple clicks on Create Reservation button gives multiple
reservations 
* \[[VCL-378](https://issues.apache.org/jira/browse/VCL-378)
\] -	     reservation can be extended into a block allocation for user
not in block group 
* \[[VCL-382](https://issues.apache.org/jira/browse/VCL-382)
\] -	     vmware.pm incorrectly handles free server with network
datastores 

<a name="VCL2.2-Improvement"></a>
####    Improvement 

* \[[VCL-2](https://issues.apache.org/jira/browse/VCL-2)
\] -	     migrate preferredimage to nextimage 
* \[[VCL-9](https://issues.apache.org/jira/browse/VCL-9)
\] -	     Update reclaim.pm to use DataStructure methods 
* \[[VCL-11](https://issues.apache.org/jira/browse/VCL-11)
\] -	     Update blockrequest.pm to use database subroutines 
* \[[VCL-31](https://issues.apache.org/jira/browse/VCL-31)
\] -	     rename conf.php and secrets.php to include -default in the
name 
* \[[VCL-32](https://issues.apache.org/jira/browse/VCL-32)
\] -	     modify XMLRPCaddRequest to allow an end time to be specified 
* \[[VCL-93](https://issues.apache.org/jira/browse/VCL-93)
\] -	     LDAP part of a login to fail silently on errors when
Shibboleth authentication is used 
* \[[VCL-94](https://issues.apache.org/jira/browse/VCL-94)
\] -	     Rework image capture flow 
* \[[VCL-98](https://issues.apache.org/jira/browse/VCL-98)
\] -	     upgrade all of dojo-0.4.0 code to recent version of dojo 
* \[[VCL-125](https://issues.apache.org/jira/browse/VCL-125)
\] -	     Add ability to control whether or not users have
root/administrator access 
* \[[VCL-137](https://issues.apache.org/jira/browse/VCL-137)
\] -	     Update vmware.pm to use provisioning module interface
subroutine names 
* \[[VCL-145](https://issues.apache.org/jira/browse/VCL-145)
\] -	     Store product keys in the database 
* \[[VCL-148](https://issues.apache.org/jira/browse/VCL-148)
\] -	     Add management node to current reservations view for
ADMIN_DEVELOPER 
* \[[VCL-149](https://issues.apache.org/jira/browse/VCL-149)
\] -	     Prevent multiple vcld processes 
* \[[VCL-153](https://issues.apache.org/jira/browse/VCL-153)
\] -	     Update interface subroutines in xCAT21.pm to match xCAT.pm 
* \[[VCL-155](https://issues.apache.org/jira/browse/VCL-155)
\] -	     Decrease initial Current Reservation page refresh interval 
* \[[VCL-161](https://issues.apache.org/jira/browse/VCL-161)
\] -	     remove  xmlrpcKey table from vcl.sql  
* \[[VCL-162](https://issues.apache.org/jira/browse/VCL-162)
\] -	     create structure to add throttling to provisioning modules 
* \[[VCL-163](https://issues.apache.org/jira/browse/VCL-163)
\] -	     move throttle variable from vcld.conf to managment node table 
* \[[VCL-164](https://issues.apache.org/jira/browse/VCL-164)
\] -	     Make installation and configuration easier 
* \[[VCL-200](https://issues.apache.org/jira/browse/VCL-200)
\] -	     add edit node name option in Privilege tree 
* \[[VCL-204](https://issues.apache.org/jira/browse/VCL-204)
\] -	     remove private ssh identity keys from known locations- post
load / pre-capture routines 
* \[[VCL-206](https://issues.apache.org/jira/browse/VCL-206)
\] -	     Alphabetize list of virtual hosts 
* \[[VCL-211](https://issues.apache.org/jira/browse/VCL-211)
\] -	     image creation mode - administrator timeout 
* \[[VCL-223](https://issues.apache.org/jira/browse/VCL-223)
\] -	     Remove information user should not be able to access on
post_load 
* \[[VCL-224](https://issues.apache.org/jira/browse/VCL-224)
\] -	     Move settings from vcld.conf to database except for database
connection settings 
* \[[VCL-244](https://issues.apache.org/jira/browse/VCL-244)
\] -	     Staticics page - show number of failed loads per image 
* \[[VCL-248](https://issues.apache.org/jira/browse/VCL-248)
\] -	     Update provisioning modules' node_status to return READY if
SSH works but ping doesn't 
* \[[VCL-251](https://issues.apache.org/jira/browse/VCL-251)
\] -	     Make &quot;Later&quot; reservation time default to a time in
the future. 
* \[[VCL-252](https://issues.apache.org/jira/browse/VCL-252)
\] -	     XMLHttpTransport Error 
* \[[VCL-254](https://issues.apache.org/jira/browse/VCL-254)
\] -	     block request improvements 
* \[[VCL-255](https://issues.apache.org/jira/browse/VCL-255)
\] -	     xmlrpc_call routine add better error control 
* \[[VCL-271](https://issues.apache.org/jira/browse/VCL-271)
\] -	     clean out unused routines 
* \[[VCL-272](https://issues.apache.org/jira/browse/VCL-272)
\] -	     block request form 
* \[[VCL-275](https://issues.apache.org/jira/browse/VCL-275)
\] -	     Predictive reloading level_1 module 
* \[[VCL-284](https://issues.apache.org/jira/browse/VCL-284)
\] -	     vmware.pm power_reset sub does not catch error if VMware tools
are not running 
* \[[VCL-286](https://issues.apache.org/jira/browse/VCL-286)
\] -	     post_linux load operation - set hostname that matches public
IP address 
* \[[VCL-288](https://issues.apache.org/jira/browse/VCL-288)
\] -	     Add Global affiliation to schema 
* \[[VCL-293](https://issues.apache.org/jira/browse/VCL-293)
\] -	     check for remote ldap server being up before connecting to it 
* \[[VCL-295](https://issues.apache.org/jira/browse/VCL-295)
\] -	     Combine normal new reservation and imaging new reservation
code 
* \[[VCL-302](https://issues.apache.org/jira/browse/VCL-302)
\] -	     provide feedback to users about block reservation status 
* \[[VCL-305](https://issues.apache.org/jira/browse/VCL-305)
\] -	     update code to work with php 5.3 
* \[[VCL-314](https://issues.apache.org/jira/browse/VCL-314)
\] -	     change Documentation link to have links to ASF docs 
* \[[VCL-320](https://issues.apache.org/jira/browse/VCL-320)
\] -	     random selection of computer for reservations 
* \[[VCL-326](https://issues.apache.org/jira/browse/VCL-326)
\] -	     Shutdown Event Tracker causes autologin to fail 
* \[[VCL-335](https://issues.apache.org/jira/browse/VCL-335)
\] -	     max allowed ram for computers needs to be increased 
* \[[VCL-357](https://issues.apache.org/jira/browse/VCL-357)
\] -	     create update sql script to upgrade to the latest schema 
* \[[VCL-359](https://issues.apache.org/jira/browse/VCL-359)
\] -	     Remove DHCP and static IP configuration sections from
provisioning modules 

<a name="VCL2.2-NewFeature"></a>
####    New Feature 

* \[[VCL-134](https://issues.apache.org/jira/browse/VCL-134)
\] -	     Add ability to control whether or not users have
root/administrator access 
* \[[VCL-142](https://issues.apache.org/jira/browse/VCL-142)
\] -	     Add KMS activation server configuration per affiliation 
* \[[VCL-146](https://issues.apache.org/jira/browse/VCL-146)
\] -	     add linux support for all VMWare modules 
* \[[VCL-180](https://issues.apache.org/jira/browse/VCL-180)
\] -	     add power_X(off,on,reset,status)  routines to provisioning
modules  
* \[[VCL-182](https://issues.apache.org/jira/browse/VCL-182)
\] -	     Linux virtual machine support 
* \[[VCL-195](https://issues.apache.org/jira/browse/VCL-195)
\] -	     Add support for Windows Server 2008 
* \[[VCL-196](https://issues.apache.org/jira/browse/VCL-196)
\] -	     Add support for 64-bit Windows 
* \[[VCL-201](https://issues.apache.org/jira/browse/VCL-201)
\] -	     Add support for Windows Vista VMware images 
* \[[VCL-208](https://issues.apache.org/jira/browse/VCL-208)
\] -	     Ability to easily put the VCL site into a maintenance state to
prevent user access 
* \[[VCL-239](https://issues.apache.org/jira/browse/VCL-239)
\] -	     xcat 2.X module 
* \[[VCL-268](https://issues.apache.org/jira/browse/VCL-268)
\] -	     OS table - create additional OS ids 
* \[[VCL-278](https://issues.apache.org/jira/browse/VCL-278)
\] -	     Add setup mechanism to vcld 
* \[[VCL-279](https://issues.apache.org/jira/browse/VCL-279)
\] -	     Add post_load_custom script functionality for Linux images 
* \[[VCL-292](https://issues.apache.org/jira/browse/VCL-292)
\] -	     option to save selected authentication method in cookie 
* \[[VCL-294](https://issues.apache.org/jira/browse/VCL-294)
\] -	     create a login log 
* \[[VCL-298](https://issues.apache.org/jira/browse/VCL-298)
\] -	     Add support for VMware Server 2.x and ESXi 4.x 
* \[[VCL-301](https://issues.apache.org/jira/browse/VCL-301)
\] -	     Add support for Windows 7 
* \[[VCL-351](https://issues.apache.org/jira/browse/VCL-351)
\] -	     extend vm profile to have more virtualswitches 
* \[[VCL-352](https://issues.apache.org/jira/browse/VCL-352)
\] -	     Add additional pre-capture steps for Linux OS 
* \[[VCL-365](https://issues.apache.org/jira/browse/VCL-365)
\] -	     change select box for environment on new reservation page to
dojo filteringselect 

<a name="VCL2.2-Task"></a>
####    Task 

* \[[VCL-138](https://issues.apache.org/jira/browse/VCL-138)
\] -	     remove antiquated vcldquery support 
* \[[VCL-139](https://issues.apache.org/jira/browse/VCL-139)
\] -	     make users' names optional 
* \[[VCL-274](https://issues.apache.org/jira/browse/VCL-274)
\] -	     check for SQL injection / XSS
