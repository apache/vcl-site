---
title: VCL Release Procedures - 2.3.1 ToDo
---

# Prerequisites: Things that must be done before a release

* <s>all items from the JIRA roadmap for the release must be completed or
moved to a future release</s>
* <s>ALL human readable files must contain the Apache license header
    * this includes style sheets, test code, and documentation - when in
	 doubt, add a header
    * files that are part of other software packages that are bundled with 
	 a release must not contain the header (unless that software is also ASF 
	 software) and should be clearly documented as being bundled software</s>
* <s>LICENSE and NOTICE files should be reviewed
    * LICENSE: This file should have the Apache License at the top of it; 
	 any third party artifacts or documents included in the release should 
	 have their licenses included in this file along with a clear explanation 
	 of which files each license applies to.
    * NOTICE: This file is for additional copyright and attribution 
	 statements any third party licenses may require. A typical NOTICE 
	 document at a minimum includes a copyright and attribution statement for 
	 The Apache Software Foundation. Nothing else belongs in the NOTICE document.
    * Make sure copyright date is correct in NOTICE file</s>
* <s>Files containing the VCL version should be updated to the version being 
released
    * The backend Perl files contain a line defining a $VERSION variable, 
	 this should be updated in every file</s>
* <s>documentation on how to upgrade from a previous release must be created
    * if appropriate, scripts to help users upgrade should be created 
	 (don't forget steps/scripts to upgrade the database schema)</s>
* <s>RELEASE_NOTES file needs to be updated and should contain:</s>
    * <s>release version
    * an intro to VCL
    * a brief description of the aims of VCL</s>
    * <s>a brief roadmap of VCL and how this release fits in to it</s>
    * <s>a list of ways for users to get involved
    * a description of how users can submit issues</s>
* <s>the README file must also contain all dependencies (this includes PHP, 
Perl, MySQL versions in addition to perl and php modules, dojo, etc.) for 
running VCL, any changes in dependencies since the last release must be 
listed in the CHANGLOG file</s>
* <s>generate a CHANGELOG file
    * go to the [Create Release Notes][1] page of the JIRA site
    * select the release version
    * select **text** as the style
    * click **Create**
    * scroll down to **Edit/Copy Release Notes**
    * copy/paste the contents to a new section in the CHANGELOG file
    * make sure to add any changes in the dependencies since the last release</s>
* <s>make sure INSTALLATION file is up to date with content from Confluence on 
how to install each part</s>
* <s>ensure LICENSE, NOTICE, RELEASE_NOTES, CHANGELOG, INSTALLATION, UPGRADE, 
and README files are in top level directory of trunk (or the branch that 
will be used for the release)</s>
* <s>an export from HEAD should result in a directory tree with all files and 
directories having appropriate permissions</s>
* <s>release manager's GPG signing key must be in KEYS file in toplevel 
directory of SVN (one above trunk)</s>
* <s>a release/download page needs to be created for the specific release 
containing:
    * link to release artifact (link to a mirror)
    * link to signatures and checksums (link directly to apache.org)
    * steps explaining how to verify artifact using signatures and checksums
    * either a link to release notes or contain them inline
    * either a link to a change log or contain it inline</s>
* <s>a decision needs to be made determining which, if any, previously released 
artifacts should be removed from the main distribution site after this 
release is completed</s>
* <s>make sure the index.php file from the web code has the correct VCL 
version at the top of it</s>

# Steps to create a release candidate artifact

* <s>A tag for the release candidate needs to be created in subversion. It 
should be created under the **tags** directory of the repository and should be 
named **release-W.X.Y-RCZ** (with Z being the release candidate number, starting 
with 1 and with .Y only being included if Y > 0)
* export from this tag to get the code for the release candidate
* add Dojo Toolkit
    * download and extract most recent (and tested to work with web code) 
	 version of Dojo Toolkit under 'web'
    * rename extracted dojo directory to just 'dojo'
    * change to themes directory and run './copydojocss.sh default'
    * update the version listed for Dojo in the README file
* remove any VCL perl modules that should not be part of the release
* create a tarball of the directory
    * compress it with bzip2
    * name it apache-VCL-W.X.Y-RCZ-incubating.tar.bz2 (the .Y should only 
	 be included if Y > 0)
* create MD5 and SHA-1 sums of the tarball
* sign the tarball with GPG
    * [This document][2] contains information on how to sign the tarball
* distribute the RC through the release manager's personal web space on 
people.apache.org (RC are not to be release from the main distribution area 
to cut down on archive storage and mirroring bandwidth)</s>

# Community and PMC voting process

* <s>release manager should start a [VOTE][3] thread on the dev list; [this is a 
good example][4]
* the release manage's vote should be posted in a separate message from the 
one calling for the vote
* the VOTE thread should be ended with a reply post including [RESULT] in the 
subject; [this is a good example][5] except that it is missing the [RESULT] part from 
the subject</s>

# Steps to make the RC available as a release artifact

* <s>create a tag for the release from the approved RC tag (svn copy from RC 
tag to new release tag)
* create a copy of the approved RC artifact and name it 
apache-VCL-X.Y.Z-incubating.tar.bz2 (the .Z should only be included if Z > 0) - 
untar old one, rename director to not have RC part, create new tarball
* sign the file with GPG
* create md5 and sha1 sum files</s>

# Steps to make release artifact available to users

* <s>place the release artifact, sums, and signature in 
/www/www.apache.org/dist/vcl on people.apache.org
* ensure the artifact has permissions 664 and is owned by the vcl group</s>
* wait 24 hours for the artifact to propagate to the mirrors before 
announcing the release
    * ideally, a test download should be done from the mirror and a check 
	 of the sums and signatures should be done
* After successfully performing a test download from the mirror, 
announcements should be made
    * on the dev@ list
    * on the user@ list
    * update currently listed version and download link on [download page][6]
* Set the newly released version to the Release status in JIRA so that people 
will be able to see it as released when reporting bugs
    * Go to the [versions page][7] of the JIRA site
    * click **Manage Versions**
    * mouse over the line of the release version
    * click the gear menu drop down
    * click Release and follow the instructions

**IMPORTANT**: Once a release is copied to the dist location, it **must not be 
modified**. This can signal that an attack is being performed. If an error is 
found, a new .Z release should be made.


  [1]: https://issues.apache.org/jira/secure/ConfigureReleaseNote.jspa?projectId=12310840&version=12322740
  [2]: http://www.apache.org/dev/release-signing.html#sign-release
  [3]: http://www.apache.org/foundation/voting.html#ReleaseVotes
  [4]: http://markmail.org/message/ysdor5uddhviawln
  [5]: http://markmail.org/message/kanwckkfrnbcs2s7
  [6]: http://vcl.apache.org/downloads/download.cgi
  [7]: https://issues.apache.org/jira/browse/VCL#selectedTab=com.atlassian.jira.plugin.system.project%3Aversions-panel