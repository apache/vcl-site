---
title: VCL 2.2.1
---

<a name="VCL2.2.1-TableofContents"></a>
## Table of Contents
   * [Download links](#VCL2.2.1-Downloadlinks)
   * [Release Notes](#VCL2.2.1-ReleaseNotes)
         * [I. Intro and Description](#VCL2.2.1-I.IntroandDescription)
         * [II. VCL Roadmap](#VCL2.2.1-II.VCLRoadmap)
         * [III. Getting Involved in the ASF VCL Community](#VCL2.2.1-III.GettingInvolvedintheASFVCLCommunity)
         * [IV. How to Submit Bugs and Feature Requests](#VCL2.2.1-IV.HowtoSubmitBugsandFeatureRequests)
   * [Change Log](#VCL2.2.1-ChangeLog)
         * [Bug](#VCL2.2.1-Bug)
         * [Improvement](#VCL2.2.1-Improvement)
         * [New Feature](#VCL2.2.1-NewFeature)

<a name="VCL2.2.1-Downloadlinks"></a>
## Download links

Please make sure to download VCL from an mirror server. The following link
will automatically select one for you that should be close to you. After
downloading it *make sure* you verify it with MD5 or SHA1 sums *AND* the
GPG signature (sums and signature files should be downloaded directly from
Apache, not from mirrors).

[Download ASF VCL 2.2.1](http://www.apache.org/dyn/closer.cgi/incubator/vcl/apache-VCL-2.2.1-incubating.tar.bz2)
[GPG Signature](http://www.apache.org/dist/incubator/vcl/apache-VCL-2.2.1-incubating.tar.bz2.asc)
[MD5 Sum](http://www.apache.org/dist/incubator/vcl/apache-VCL-2.2.1-incubating.tar.bz2.md5)
[SHA1 Sum](http://www.apache.org/dist/incubator/vcl/apache-VCL-2.2.1-incubating.tar.bz2.sha1)
[VCL KEYS file](http://www.apache.org/dist/incubator/vcl/KEYS)






Run the following command to verify the MD5 sum. It should give output
similar to "apache-VCL-2.2.1-incubating.tar.bz2: OK":
md5sum \-c apache-VCL-2.2.1-incubating.tar.bz2.md5

Similarly, Run the following command to verify the SHA1 sum. You should get
output similar to "apache-VCL-2.2.1-incubating.tar.bz2: OK":
sha1sum \-c apache-VCL-2.2.1-incubating.tar.bz2.sha1

To verify the GPG signature (you'll need to have [GnuPG](http://www.gnupg.org/)
 installed):
1. download and import the VCL KEYS file (if you've imported the KEYS file
for previously releases, you do not need to import it again):
gpg \--import KEYS
1. download the GPG Signature to the same location as the release file
1. from the directory containing both the release file and the GPG
signature, run
gpg \--verify apache-VCL-2.2.1-incubating.tar.bz2.asc

For new installs, visit the on-line [installation guide](vcl-2.2.1-installation.html)
.

For upgrades from version 2.2, visit the on-line [upgrade guide](vcl:upgrade-from-previous-version-(2.2-to-2.2.1).html)
.
For upgrades from version 2.1, visit the on-line [upgrade guide for upgrading from 2.1](vcl:upgrade-from-previous-version-(2.1-to-2.2.1).html)
.


<a name="VCL2.2.1-ReleaseNotes"></a>
## Release Notes

<a name="VCL2.2.1-I.IntroandDescription"></a>
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

<a name="VCL2.2.1-II.VCLRoadmap"></a>
#### II. VCL Roadmap

VCL 2.2.1 (this release)
* removed frontend dependency on jpgraph
* remove any access control that is hard coded in frontend
* added support for VirtualBox hypervisor
* many bug fixes and improvements to VMWare support

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

<a name="VCL2.2.1-III.GettingInvolvedintheASFVCLCommunity"></a>
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

* If you are interested in contributing something to the project, please
discuss it on the vcl-dev list BEFORE starting work on it. This allows the
community to be involved in decisions and allows current developers to
provide some guidance.


<a name="VCL2.2.1-IV.HowtoSubmitBugsandFeatureRequests"></a>
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

<a name="VCL2.2.1-ChangeLog"></a>
## Change Log


Release Notes - VCL - Version 2.2.1

<a name="VCL2.2.1-Bug"></a>
#### Bug

* \[[VCL-113](https://issues.apache.org/jira/browse/VCL-113)
\] -	     inconsistances with "None" user group
* \[[VCL-116](https://issues.apache.org/jira/browse/VCL-116)
\] -	     manage groups interface doesn't correctly handle user groups
with editusergroupid set to NULL
* \[[VCL-152](https://issues.apache.org/jira/browse/VCL-152)
\] -	     problem removing vm from vmhost when vm in reloading state
without a reservation
* \[[VCL-361](https://issues.apache.org/jira/browse/VCL-361)
\] -	     Error is displayed on pages showing image list if last used
image is deleted
* \[[VCL-395](https://issues.apache.org/jira/browse/VCL-395)
\] -	     cannot add new vmprofiles
* \[[VCL-397](https://issues.apache.org/jira/browse/VCL-397)
\] -	     Hostname not set on Linux computers if DNS is not configured
remotely
* \[[VCL-411](https://issues.apache.org/jira/browse/VCL-411)
\] -	     Legacy VCL logon and logoff scripts may not be deleted during
capture causing immediate user logoff
* \[[VCL-412](https://issues.apache.org/jira/browse/VCL-412)
\] -	     clicking on tomaintenance reload reservation in timetable
gives an error
* \[[VCL-436](https://issues.apache.org/jira/browse/VCL-436)
\] -	     Predictive Level_1 reload module - can select wrong image for
computer
* \[[VCL-437](https://issues.apache.org/jira/browse/VCL-437)
\] -	     delete image/reservation bug
* \[[VCL-439](https://issues.apache.org/jira/browse/VCL-439)
\] -	     trailing commas in statistics.js keeps graphs from showing in
IE on stats page
* \[[VCL-440](https://issues.apache.org/jira/browse/VCL-440)
\] -	     dashboard last 12 hours of reservations graph not positioned
correctly in IE in compatibility mode

<a name="VCL2.2.1-Improvement"></a>
#### Improvement

* \[[VCL-140](https://issues.apache.org/jira/browse/VCL-140)
\] -	     General variable table
* \[[VCL-310](https://issues.apache.org/jira/browse/VCL-310)
\] -	     remove jpgraph dependency
* \[[VCL-312](https://issues.apache.org/jira/browse/VCL-312)
\] -	     remove View Mode and any uses of user.adminlevelid
* \[[VCL-373](https://issues.apache.org/jira/browse/VCL-373)
\] -	     Enable Windows Server 2008 RDP audio - it's disabled by
default
* \[[VCL-394](https://issues.apache.org/jira/browse/VCL-394)
\] -	     Backend VMware improvements for 2.2.1 release
* \[[VCL-414](https://issues.apache.org/jira/browse/VCL-414)
\] -	     modify XMLRPCaddUserGroup to accept a paramter specifying
value for custom field
* \[[VCL-424](https://issues.apache.org/jira/browse/VCL-424)
\] -	     Remove unused variables from subroutines in backend modules
* \[[VCL-425](https://issues.apache.org/jira/browse/VCL-425)
\] -	     modify scheduler to be aware of RAM allocated to VMs on each
VM host
* \[[VCL-426](https://issues.apache.org/jira/browse/VCL-426)
\] -	     modify scheduler to not give user same computer if user had
very recent, short reservation and other computers are available

<a name="VCL2.2.1-NewFeature"></a>
#### New Feature

* \[[VCL-232](https://issues.apache.org/jira/browse/VCL-232)
\] -	     add way to delete multiple computers
* \[[VCL-401](https://issues.apache.org/jira/browse/VCL-401)
\] -	     add manageMapping resource attribute to control resource
mapping
* \[[VCL-403](https://issues.apache.org/jira/browse/VCL-403)
\] -	     make the scheduler aware of image and machine types so that
virtual and bare images and computers can be mixed
* \[[VCL-405](https://issues.apache.org/jira/browse/VCL-405)
\] -	     create provisioningOSinstalltype table to map provisioning
methods to OSinstalltypes
* \[[VCL-406](https://issues.apache.org/jira/browse/VCL-406)
\] -	     add some charts to see how machines are allocated to block
allocations
