---
title: VCL Release Procedures
---

<a name="VCLReleaseProcedures-Prerequisites:Thingsthatmustbedonebeforearelease"></a>
## Prerequisites: Things that must be done before a release

* all items from the JIRA roadmap for the release must be completed or
moved to a future release
* ALL human readable files must contain the Apache license header
** this includes style sheets, test code, and documentation - when in
doubt, add a header
** files that are part of other software packages that are bundled with a
release must not contain the header (unless that software is also ASF
software) and should be clearly documented as being bundled software
* LICENSE and NOTICE files should be reviewed
** LICENSE: This file should have the Apache License at the top of it; any
third party artifacts or documents included in the release should have
their licenses included in this file along with a clear explanation of
which files each license applies to.
** NOTICE: This file is for additional copyright and attribution statements
any third party licenses may require. A typical NOTICE document at a
minimum includes a copyright and attribution statement for The Apache
Software Foundation. Nothing else belongs in the NOTICE document.
** Make sure copyright date is correct in NOTICE file
* Files containing the VCL version should be updated to the version being
released
** The backend Perl files contain a line defining a $VERSION variable, this
should be updated in every file
* documentation on how to upgrade from a previous release must be created
** if appropriate, scripts to help users upgrade should be created (don't
forget steps/scripts to upgrade the database schema)
* RELEASE_NOTES file needs to be updated and should contain:
** release version
** an intro to VCL
** a brief description of the aims of VCL
** a brief roadmap of VCL and how this release fits in to it
** a list of ways for users to get involved
** a description of how users can submit issues
* the README file must also contain all dependencies (this includes PHP,
Perl, MySQL versions in addition to perl and php modules, dojo, etc.) for
running VCL, any changes in dependencies since the last release must be
listed in the CHANGLOG file
* generate a CHANGELOG file
** go to the [JIRA site](http://issues.apache.org/jira/browse/VCL)
** click *Release Notes*
** select the release version
** select *text* as the style
** scroll down to *Edit/Copy Release Notes*
** copy/paste the contents to a new section in the CHANGELOG file
** make sure to add any changes in the dependencies since the last release
* make sure INSTALLATION file is up to date with content from Confluence on
how to install each part
* ensure LICENSE, NOTICE, RELEASE_NOTES, CHANGELOG, INSTALLATION, UPGRADE,
and README files are in top level directory of trunk (or the branch that
will be used for the release)
* an export from HEAD should result in a directory tree with all files and
directories having appropriate permissions
* release manager's GPG signing key must be in KEYS file in toplevel
directory of SVN (one above trunk)
* a release/download page needs to be created for the specific release
containing:
** link to release artifact (link to a mirror)
** link to signatures and checksums (link directly to apache.org)
** steps explaining how to verify artifact using signatures and checksums
** either a link to release notes or contain them inline
** either a link to a change log or contain it inline
* a decision needs to be made determining which, if any, previously
released artifacts should be removed from the main distribution site after
this release is completed
* make sure the index.php file from the web code has the correct VCL
version at the top of it

<a name="VCLReleaseProcedures-Stepstocreateareleasecandidateartifact"></a>
## Steps to create a release candidate artifact

* A tag for the release candidate needs to be created in subversion. It
should be created under the *tags* directory of the repository and should
be named *release-W.X.Y-RCZ* (with Z being the release candidate number,
starting with 1 and with .Y only being included if Y > 0)
* export from this tag to get the code for the release candidate
* add Dojo Toolkit
** download and extract most recent (and tested to work with web code)
version of Dojo Toolkit under 'web'
** rename extracted dojo directory to just 'dojo'
** change to themes directory and run './copydojocss.sh default'
** update the version listed for Dojo in the README file
* remove any VCL perl modules that should not be part of the release
* create a tarball of the directory
** compress it with bzip2
** name it apache-VCL-W.X.Y-RCZ-incubating.tar.bz2 (the .Y should only be
included if Y > 0)
* create MD5 and SHA-1 sums of the tarball
* sign the tarball with GPG
** [This document](http://www.apache.org/dev/release-signing.html#sign-release)
 contains information on how to sign the tarball
* distribute the RC through the release manager's personal web space on
people.apache.org (RC are not to be release from the main distribution area
to cut down on archive storage and mirroring bandwidth)

<a name="VCLReleaseProcedures-CommunityandPMCvotingprocess"></a>
## Community and PMC voting process

*NOTICE: these steps may not be completely correct*
* release manager should start a [VOTE](http://incubator.apache.org/guides/releasemanagement.html#note-votes)
 thread on the dev list; [this is a good example|http://mail-archives.apache.org/mod_mbox/incubator-stdcxx-dev/200601.mbox/%3C43C1C0A0.7040401%40roguewave.com%3E]
; however, the example is missing an explicit vote block that needs to be
included:
\[ \](-\.html)
 \+1 yes, release VCL W.X.Y
\[ \](-\.html)
 0 dunno
\[ \](-\.html)
 \-1 no, don't release VCL W.X.Y (provide reasons if this is your vote)
* the release manage's vote should be posted in a separate message from the
one calling for the vote
* the VOTE thread should be ended with a reply post including \[RESULT\](result\.html)
 in the subject; [this is a good example|http://mail-archives.apache.org/mod_mbox/incubator-general/200605.mbox/<5BDE9EBE-2645-4940-9CB9-C038E531B8A2%40gmail.com>]

<a name="VCLReleaseProcedures-StepstomaketheRCavailableasareleaseartifact"></a>
## Steps to make the RC available as a release artifact

* create a tag for the release from the approved RC tag (svn copy from RC
tag to new release tag)
* create a copy of the approved RC artifact and name it
apache-VCL-X.Y.Z-incubating.tar.bz2 (the .Z should only be included if Z >
0) - untar old one, rename director to not have RC part, create new tarball
* sign the file with GPG
* create md5 and sha1 sum files

<a name="VCLReleaseProcedures-Stepstomakereleaseartifactavailabletousers"></a>
## Steps to make release artifact available to users

* place the release artifact, sums, and signature in
/www/www.apache.org/dist/vcl on people.apache.org
* ensure the artifact has permissions 664 and is owned by the vcl group
* wait 24 hours for the artifact to propagate to the mirrors before
announcing the release
** ideally, a test download should be done from the mirror and a check of
the sums and signatures should be done
* After successfully performing a test download from the mirror,
announcements should be made
** on the dev@ list
** on the user@ list
** update currently listed version and download link on confluence Index
page
** (update this list as the community grows)
* Set the newly released version to the Release status in JIRA so that
people will be able to see it as released when reporting bugs
** Go to the [JIRA site](https://issues.apache.org/jira/secure/project/ViewProject.jspa?pid=12310840)
** click "Manage versions" under the Versions section
** In the Operations column, click the Release link for the specified
version

*IMPORTANT*: Once a release is copied to the dist location, it *must not be
modified*. This can signal that an attack is being performed. If an error
is found, a new .Z release should be made.
