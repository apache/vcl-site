---
title: VCL 2.1
---

<a name="VCL2.1-TableofContents"></a>
## Table of Contents
   * [Download links](#VCL2.1-Downloadlinks)
   * [Release Notes](#VCL2.1-ReleaseNotes)
         * [I. Intro and Description](#VCL2.1-I.IntroandDescription)
         * [II. VCL Roadmap](#VCL2.1-II.VCLRoadmap)
         * [III. Getting Involved in the ASF VCL Community](#VCL2.1-III.GettingInvolvedintheASFVCLCommunity)
         * [IV. How to Submit Bugs and Feature Requests](#VCL2.1-IV.HowtoSubmitBugsandFeatureRequests)
   * [Change Log](#VCL2.1-ChangeLog)
         * [Sub-task](#VCL2.1-Sub-task)
         * [Bug](#VCL2.1-Bug)
         * [Improvement](#VCL2.1-Improvement)
         * [New Feature](#VCL2.1-NewFeature)
         * [Task](#VCL2.1-Task)

<a name="VCL2.1-Downloadlinks"></a>
## Download links

Please make sure to download VCL from an mirror server. The following link
will automatically select one for you that should be close to you. After
downloading it *make sure* you verify it with MD5 or SHA1 sums *AND* the
GPG signature (sums and signature files should be downloaded directly from
Apache, not from mirrors).

[Download ASF VCL 2.1](http://www.apache.org/dyn/closer.cgi/incubator/vcl/apache-VCL-2.1-incubating.tar.bz2)
[GPG Signature](http://www.apache.org/dist/incubator/vcl/apache-VCL-2.1-incubating.tar.bz2.asc)
[MD5 Sum](http://www.apache.org/dist/incubator/vcl/apache-VCL-2.1-incubating.tar.bz2.md5)
[SHA1 Sum](http://www.apache.org/dist/incubator/vcl/apache-VCL-2.1-incubating.tar.bz2.sha1)
[VCL KEYS file](http://www.apache.org/dist/incubator/vcl/KEYS)

Run the following command to verify the MD5 sum. You should get the same
number that is in apache-VCL-2.1-incubating.tar.bz2.md5:
md5sum apache-VCL-2.1-incubating.tar.bz2

Similarly, Run the following command to verify the SHA1 sum. You should get
the same number that is in apache-VCL-2.1-incubating.tar.bz2.sha1:
sha1sum apache-VCL-2.1-incubating.tar.bz2

To verify the GPG signature (you'll need to have [GnuPG](http://www.gnupg.org/)
 installed):
1. download and import the VCL KEYS file:
gpg \--import KEYS
1. download the GPG Signature to the same location as the release file
1. from the directory containing both the release file and the GPG
signature, run
gpg \--verify apache-VCL-2.1-incubating.tar.bz2.asc

<a name="VCL2.1-ReleaseNotes"></a>
## Release Notes

<a name="VCL2.1-I.IntroandDescription"></a>
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

The release supports provisioning nodes using xCAT 1.3, xCAT 2.1, vmware
server 1.x, ESX standard Server using the toolkit the vmware-cmd on the esx
host, ESXi using the vmware toolkit.

<a name="VCL2.1-II.VCLRoadmap"></a>
#### II. VCL Roadmap

VCL 2.1 (this release)
* completed modularization of vcld
* xCAT 2.1 support
* Shibboleth authentication
* VMWare management via VMWare toolkit
* ESXi with thin provisioning on a NetApp
* Only supports xCAT 1.3 and xCAT 2.1 versions

VCL 2.2
* support for xCAT 2.3 or later versions
* -improve cluster reservations- {color:#ff0000}VMWare Free Server
2.x{color} {color:#000000}(changed after 2.1 release){color}
* improve block reservations(rename to block allocations)

VCL 2.3
* Service deployments
* power management
* -VMWare Free Server 2.x- {color:#ff0000}improve cluster
reservations{color} {color:#000000}(changed after 2.1 release){color}

VCL 2.4
* improve hypervisor support
* dynamic provisioning of host servers
* possibly XEN or KVM

VCL 2.5
* develop tools for managing both system and user storage

With each release, we'll be working toward making VCL easier to install. As
part of our move to development at the Apache Software Foundation, it is an
obvious goal to create a community of users and more developers around VCL.
Bringing in more developers should become easier as VCL becomes easier to
install.

<a name="VCL2.1-III.GettingInvolvedintheASFVCLCommunity"></a>
#### III. Getting Involved in the ASF VCL Community

There are five ways to become involved in the ASF VCL community.

* Join the mailing lists and participate in discussion. There are two
mailing lists: vcl-user@incubator.apache.org
vcl-dev@incubator.apache.org
To join vcl-user, send an empty message to
[vcl-user-subscribe@incubator.apache.org](mailto:vcl-user-subscribe@incubator.apache.org|click-to-subscribe.html)
. To join vcl-dev, send an empty
message to [vcl-dev-subscribe@incubator.apache.org](mailto:vcl-dev-subscribe@incubator.apache.org|click-to-subscribe.html)
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

<a name="VCL2.1-IV.HowtoSubmitBugsandFeatureRequests"></a>
#### IV. How to Submit Bugs and Feature Requests

If you find a bug, please submit a bug report to our JIRA bug tracking
system at [http://issues.apache.org/jira/browse/VCL](http://issues.apache.org/jira/browse/VCL)
 (you will need to set up an account there if you haven't already done so -
it's free to anyone). Also, we would appreciate it if you mentioned that
you filed a bug on the vcl-dev list to make sure we don't miss it.

If you would like to requrest a new feature, you can also submit that in
the same way through JIRA (just select "New Feature" or "Improvement" as
the Issue Type). Again, it would be helpful if you mentioned that you filed
a feature
request on the vcl-dev list.

After you have created a JIRA issue, you have the option to vote on it to
help us know how to prioritize issues. You can also "watch" the issue to
see when activity related to it is submitted.

<a name="VCL2.1-ChangeLog"></a>
## Change Log

<a name="VCL2.1-Sub-task"></a>
#### Sub-task

* \[[VCL-67](https://issues.apache.org/jira/browse/VCL-67)
\] -	     Allow OS, provisioning engine, and other module objects to
access each other

<a name="VCL2.1-Bug"></a>
#### Bug

* \[[VCL-14](https://issues.apache.org/jira/browse/VCL-14)
\] -	     xCAT.pm's capture_monitor output always displays "attempt
1/80"
* \[[VCL-26](https://issues.apache.org/jira/browse/VCL-26)
\] -	     get_reservation_remote_ip subroutine redefined warning
* \[[VCL-34](https://issues.apache.org/jira/browse/VCL-34)
\] -	     When adding computers, missing requirement for the
provisioning module
* \[[VCL-51](https://issues.apache.org/jira/browse/VCL-51)
\] -	     user groups that have a name that is a number cause problems
on the privilege page
* \[[VCL-54](https://issues.apache.org/jira/browse/VCL-54)
\] -	     disable LDAP referrals for all LDAP connections to handle
firewalls
* \[[VCL-55](https://issues.apache.org/jira/browse/VCL-55)
\] -	     processBulkComputerInput in computers.php not always setting
startpripaddress, endpripaddress, startmac
* \[[VCL-61](https://issues.apache.org/jira/browse/VCL-61)
\] -	     blockrequest and the reload state
* \[[VCL-62](https://issues.apache.org/jira/browse/VCL-62)
\] -	     Calls to \_rpower in Windows.pm cause reservation processes to
die
* \[[VCL-64](https://issues.apache.org/jira/browse/VCL-64)
\] -	     EmptyRecycleBin.exe utility causes problems during image
capture
* \[[VCL-69](https://issues.apache.org/jira/browse/VCL-69)
\] -	     Unknown column 'af.shibonly' in 'field list'
* \[[VCL-71](https://issues.apache.org/jira/browse/VCL-71)
\] -	     Reservation processes being killed unexpectedly
* \[[VCL-73](https://issues.apache.org/jira/browse/VCL-73)
\] -	     new.pm::computer_not_being_used hangs occasionally
* \[[VCL-74](https://issues.apache.org/jira/browse/VCL-74)
\] -	     Reservation may fail if user's UID value is null
* \[[VCL-75](https://issues.apache.org/jira/browse/VCL-75)
\] -	     Bug in Perl 5.8.0 causes exit status to be reported
incorrectly
* \[[VCL-76](https://issues.apache.org/jira/browse/VCL-76)
\] -	     form tags outside of td tags on Edit Image Profiles page
* \[[VCL-79](https://issues.apache.org/jira/browse/VCL-79)
\] -	     error in how the end time for schedule times is computed
* \[[VCL-81](https://issues.apache.org/jira/browse/VCL-81)
\] -	     Image retrieval does not verify if it was successful
* \[[VCL-85](https://issues.apache.org/jira/browse/VCL-85)
\] -	     watchInFlight error appears if image description contains
special characters
* \[[VCL-88](https://issues.apache.org/jira/browse/VCL-88)
\] -	     vclreload account assumed to match the default affiliation
* \[[VCL-90](https://issues.apache.org/jira/browse/VCL-90)
\] -	     Image reservation for sub-image with "nousercheckout" flag set
* \[[VCL-91](https://issues.apache.org/jira/browse/VCL-91)
\] -	     edit reservation allows saving/updaing image for cluster
reservations
* \[[VCL-96](https://issues.apache.org/jira/browse/VCL-96)
\] -	     < and > in user's passwords not handled properly
* \[[VCL-101](https://issues.apache.org/jira/browse/VCL-101)
\] -	     forimaging flag causes wrong user when imaging linux in
reserved.pm
* \[[VCL-103](https://issues.apache.org/jira/browse/VCL-103)
\] -	     vclreload account has invalid curiculumid
* \[[VCL-108](https://issues.apache.org/jira/browse/VCL-108)
\] -	     apostrophe in image name causes AJAX updates to privilege page
to break
* \[[VCL-109](https://issues.apache.org/jira/browse/VCL-109)
\] -	     viewing requests from timetable not using continuations
* \[[VCL-111](https://issues.apache.org/jira/browse/VCL-111)
\] -	     missing default values for vmtype table
* \[[VCL-119](https://issues.apache.org/jira/browse/VCL-119)
\] -	     Reservations insert log.ending = EOR when they shouldn't
* \[[VCL-126](https://issues.apache.org/jira/browse/VCL-126)
\] -	     get_new_dbh() doesn't return correct value if different
database is specified
* \[[VCL-129](https://issues.apache.org/jira/browse/VCL-129)
\] -	     LockerWrtUser doesn't work with usernames containing
underscores
* \[[VCL-131](https://issues.apache.org/jira/browse/VCL-131)
\] -	     utils getdynamicaddress routine - bad regex
* \[[VCL-136](https://issues.apache.org/jira/browse/VCL-136)
\] -	     missing perlpackage for id 6 in module table
* \[[VCL-143](https://issues.apache.org/jira/browse/VCL-143)
\] -	     need to drop allowing new reservations to take priority over
reload reservations
* \[[VCL-151](https://issues.apache.org/jira/browse/VCL-151)
\] -	     apostrophe in last name can cause an error when adding user to
database
* \[[VCL-166](https://issues.apache.org/jira/browse/VCL-166)
\] -	     Windows firewall subs not catching "Object already exists" in
netsh.exe output
* \[[VCL-167](https://issues.apache.org/jira/browse/VCL-167)
\] -	     run_ssh_command not catching host key differs warning messages
* \[[VCL-172](https://issues.apache.org/jira/browse/VCL-172)
\] -	     xCAT21.pm - xcat database is locked at dbdimp.c error
* \[[VCL-186](https://issues.apache.org/jira/browse/VCL-186)
\] -	     Windows images losing default gateway
* \[[VCL-187](https://issues.apache.org/jira/browse/VCL-187)
\] -	     Ubuntu.pm - not  completed
* \[[VCL-191](https://issues.apache.org/jira/browse/VCL-191)
\] -	     path changes in vshpere SDK vmware perl toolkit
* \[[VCL-207](https://issues.apache.org/jira/browse/VCL-207)
\] -	     Predictive reload modules not accounting for machines in block
computers table
* \[[VCL-213](https://issues.apache.org/jira/browse/VCL-213)
\] -	     Bug in retrieve_image sub in vmware.pm and xCAT.pm calls next
instead of return
* \[[VCL-218](https://issues.apache.org/jira/browse/VCL-218)
\] -	     vmware.pm may delete image being captured by cleanup process
* \[[VCL-226](https://issues.apache.org/jira/browse/VCL-226)
\] -	     Windows reboot fails - processing another action error
* \[[VCL-238](https://issues.apache.org/jira/browse/VCL-238)
\] -	     Linux.pm  pre-capture routine not shuting down OS
* \[[VCL-240](https://issues.apache.org/jira/browse/VCL-240)
\] -	     utils.pm - insert_reload_request
* \[[VCL-246](https://issues.apache.org/jira/browse/VCL-246)
\] -	     READY flag check for VMware and xCAT is being thrown off by
other processes running on machines
* \[[VCL-247](https://issues.apache.org/jira/browse/VCL-247)
\] -	     computer with shortname  only in database not being reloaded
after being used
* \[[VCL-263](https://issues.apache.org/jira/browse/VCL-263)
\] -	     Linux.pm - add default vcl user group

<a name="VCL2.1-Improvement"></a>
#### Improvement

* \[[VCL-3](https://issues.apache.org/jira/browse/VCL-3)
\] -	     clean up database
* \[[VCL-6](https://issues.apache.org/jira/browse/VCL-6)
\] -	     update healthcheck.pl to use modularized code
* \[[VCL-15](https://issues.apache.org/jira/browse/VCL-15)
\] -	     modify blockrequest module to use frontend API for scheduling
* \[[VCL-20](https://issues.apache.org/jira/browse/VCL-20)
\] -	     Configuration of sshd port for image retrieval
* \[[VCL-23](https://issues.apache.org/jira/browse/VCL-23)
\] -	     Modularize Windows OS code
* \[[VCL-63](https://issues.apache.org/jira/browse/VCL-63)
\] -	     Remove critical notification if image is configured with a
user group containing 0 members
* \[[VCL-65](https://issues.apache.org/jira/browse/VCL-65)
\] -	     Remove pagefile from all drives during image capture
* \[[VCL-72](https://issues.apache.org/jira/browse/VCL-72)
\] -	     die and warning signals are not handled by the backend code
* \[[VCL-84](https://issues.apache.org/jira/browse/VCL-84)
\] -	     Prevent users from starting create image until computer is in
inuse state
* \[[VCL-105](https://issues.apache.org/jira/browse/VCL-105)
\] -	     an image cannot have itself as a subimage
* \[[VCL-106](https://issues.apache.org/jira/browse/VCL-106)
\] -	     mail notifications notify routine
* \[[VCL-107](https://issues.apache.org/jira/browse/VCL-107)
\] -	     User email notifications
* \[[VCL-110](https://issues.apache.org/jira/browse/VCL-110)
\] -	     2 second deley in vcld may cause problems with imaging
* \[[VCL-112](https://issues.apache.org/jira/browse/VCL-112)
\] -	     Provide access to image affiliation data via DataStructure.pm
* \[[VCL-115](https://issues.apache.org/jira/browse/VCL-115)
\] -	     allow user groups with the same name but different
affiliations
* \[[VCL-118](https://issues.apache.org/jira/browse/VCL-118)
\] -	     Add delay to run_ssh_command() & run_scp_command() retry
attempts
* \[[VCL-120](https://issues.apache.org/jira/browse/VCL-120)
\] -	     Add subroutine to set IE's runonce registry keys so user isn't
presented with it
* \[[VCL-124](https://issues.apache.org/jira/browse/VCL-124)
\] -	     locally affiliated users need a way to change their password
* \[[VCL-128](https://issues.apache.org/jira/browse/VCL-128)
\] -	     Update reclaim.pm
* \[[VCL-132](https://issues.apache.org/jira/browse/VCL-132)
\] -	     vcld check_time
* \[[VCL-156](https://issues.apache.org/jira/browse/VCL-156)
\] -	     insert current_image.txt file on kickstart based nodes
* \[[VCL-157](https://issues.apache.org/jira/browse/VCL-157)
\] -	     Add support for xCAT 2.1 partimage format
* \[[VCL-173](https://issues.apache.org/jira/browse/VCL-173)
\] -	     add power_off,power_on,power_reset,power_status routines to
xCAT21 module
* \[[VCL-175](https://issues.apache.org/jira/browse/VCL-175)
\] -	     Set virtual switch 0 from database value for VMware GSX
* \[[VCL-176](https://issues.apache.org/jira/browse/VCL-176)
\] -	     Prevent vmware.pm from looping 15 times before checking ssh
during load
* \[[VCL-177](https://issues.apache.org/jira/browse/VCL-177)
\] -	     Remove Windows OS post-load configuration tasks from vmware.pm
* \[[VCL-183](https://issues.apache.org/jira/browse/VCL-183)
\] -	     DataStructure.pm contains duplicate subroutines:
get_computer_private_ip and get_computer_private_ip_address
* \[[VCL-184](https://issues.apache.org/jira/browse/VCL-184)
\] -	     Update database schema for 2.1 release
* \[[VCL-185](https://issues.apache.org/jira/browse/VCL-185)
\] -	     Modularize Linux OS Code
* \[[VCL-188](https://issues.apache.org/jira/browse/VCL-188)
\] -	     Document Windows tools dependencies
* \[[VCL-190](https://issues.apache.org/jira/browse/VCL-190)
\] -	     Add time configuration and synchronization commands to Windows
post_load
* \[[VCL-205](https://issues.apache.org/jira/browse/VCL-205)
\] -	     allow esx provisioing module to set MAC addresses
* \[[VCL-212](https://issues.apache.org/jira/browse/VCL-212)
\] -	     Add code to set SysprepStatus registry keys for Windows 6
* \[[VCL-217](https://issues.apache.org/jira/browse/VCL-217)
\] -	     xcat modules - Throttle control
* \[[VCL-228](https://issues.apache.org/jira/browse/VCL-228)
\] -	     Windows image capture fails to delete user profiles because
file is open

<a name="VCL2.1-NewFeature"></a>
#### New Feature

* \[[VCL-1](https://issues.apache.org/jira/browse/VCL-1)
\] -	     xCAT 2.0 module
* \[[VCL-4](https://issues.apache.org/jira/browse/VCL-4)
\] -	     add support for Shibboleth authentication
* \[[VCL-7](https://issues.apache.org/jira/browse/VCL-7)
\] -	     modify healthcheck.pl to monitor vms
* \[[VCL-18](https://issues.apache.org/jira/browse/VCL-18)
\] -	     allow dynamic change of predictive loading module
* \[[VCL-19](https://issues.apache.org/jira/browse/VCL-19)
\] -	     add configuration of v2 fields for management nodes
* \[[VCL-21](https://issues.apache.org/jira/browse/VCL-21)
\] -	     add check for existance of image libraries
* \[[VCL-29](https://issues.apache.org/jira/browse/VCL-29)
\] -	     author an ESX and ESX 3i provisioning module (using netboot)
* \[[VCL-33](https://issues.apache.org/jira/browse/VCL-33)
\] -	     add user group management to XML RPC API
* \[[VCL-78](https://issues.apache.org/jira/browse/VCL-78)
\] -	     API for backend to allocate computers for block reservations
via the frontend
* \[[VCL-123](https://issues.apache.org/jira/browse/VCL-123)
\] -	     add Ubuntu Support using the new OS Module framework
* \[[VCL-209](https://issues.apache.org/jira/browse/VCL-209)
\] -	     create a page that will test for required php modules and
correct configuration

<a name="VCL2.1-Task"></a>
#### Task

* \[[VCL-70](https://issues.apache.org/jira/browse/VCL-70)
\] -	     Create a basic helloworld.pm provisioning module
* \[[VCL-95](https://issues.apache.org/jira/browse/VCL-95)
\] -	     Set Subversion properties for files in repository
* \[[VCL-135](https://issues.apache.org/jira/browse/VCL-135)
\] -	     remove all references to ncsu
* \[[VCL-198](https://issues.apache.org/jira/browse/VCL-198)
\] -	     Release tasks
* \[[VCL-264](https://issues.apache.org/jira/browse/VCL-264)
\] -	     VCL 2.1 RC2 todo items
