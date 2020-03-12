---
title: Graduation Migration ToDo
---

This page is to track all the things that need to happen for migrating out
of the incubator. Put your name next to any you are working on. Strike them
out when completed.

<a name="GraduationMigrationToDo-TasksforPMCChair(AndyKurth)"></a>
## Tasks for PMC Chair (Andy Kurth)

* -Subscribe to the board mailing list-
{color:#008000}*(subscribed)*{color}
* -Subscribe to the infrastructure mailing list- {color:#008000}*(was
already subscribed)*{color}
* -Ensure that they have been added to the- -[PMC chairs group (pmc-chairs) in LDAP](http://people.apache.org/committers-by-project.html#pmc-chairs)
--. The pmc-chairs group is maintained by infrastructure. If they don't add
you, give them a nudge...- {color:#008000}*(confirmed)*{color}
* -Check out the foundation/officers folder from the private repository.
Users with member or pmc-chairs karma can do this.-
{color:#008000}*(done)*{color}
* -Add yourself to the foundation/officers/affiliations.txt and the
foundation/officers/irs-disclosures.txt files with the appropriate
information.- {color:#008000}*(done)*{color}
* Review appropriate documentation:
** [PMC Chair Duties](http://www.apache.org/dev/pmc.html#chair)
** PMC [documentation](http://www.apache.org/dev/#pmc)
** Jakarta [Chair guide](http://wiki.apache.org/jakarta/RoleOfChair)
** Incubator [Chair guide](http://incubator.apache.org/guides/chair.html)
** -Reporting- -[calendar ](http://www.apache.org/foundation/board/calendar.html)
--\- Work out a reporting schedule with the Board. For the first three
months after graduation this will be monthly. After that, the project
should slot into a quarterly reporting schedule. Now is a good time to
remove the project from the Incubator reporting schedule.-
{color:#008000}*(March, June, September, December)*{color}

* -Add the PMC chair details to the foundation web site Officer list at- -[http://www.apache.org/foundation/index.html](http://www.apache.org/foundation/index.html)
- {color:#008000}*(done)*{color}
* -Add the new project's PMC chair to the
foundation/officers/irs-disclosures.txt file. You will need a member to
help with this task.- {color:#008000}*(done)*{color}
* -Ensure the PMC is added to the committee-info.txt file at- -[https://svn.apache.org/repos/private/committers/board/committee-info.txt ](https://svn.apache.org/repos/private/committers/board/committee-info.txt)
-[{color:#008000}*(done)*{color}|https://svn.apache.org/repos/private/committers/board/committee-info.txt]
** -There are 3 sections which need to be updated; see instructions in the
file. You may need to get a member to help with this.-
* -Establish PMC-
** -Create private list- {color:#008000}*(existing list was
transferred)*{color}
** -Subscribe initial members to private list-

<a name="GraduationMigrationToDo-GeneralTasks"></a>
## General Tasks

Work with the Apache Infrastructure team to set up the top level project
infrastructure. The various infrastructure tasks that are required (see
check list) should be consolidated into a single issue (see this for
example). This should be created in the category TLP Admin.

h3. JIRA issue to track tasks:&nbsp; {color:#008000}[https://issues.apache.org/jira/browse/INFRA-4977](https://issues.apache.org/jira/browse/INFRA-4977)
{color}

Transfer resources from incubator to TLP
* Source
** -Post an announcement to the development list telling everyone that the
repository is about to be moved-
** -svn move the podling source tree-
** -Post an announcement containing instructions for developers describing
how to svn switch their workspaces-
** Update site, wikis, pom.xml and other resources to point to the new
repository location.
* Websites
** Transfer the podling website (request svnsubpub site)
** Load the website into its new home. See infra notes.
** Update the incubator/site-publish/.htaccess entry to redirect traffic
from the old URLs to the new. (svn location is at [http://svn.apache.org/repos/asf/incubator/public/trunk/content/.htaccess](http://svn.apache.org/repos/asf/incubator/public/trunk/content/.htaccess)
)
** Delete the podling website from /www/incubator.apache.org/content/vcl on
people.apache.org. If you do not have the necessary privileges, file a
ticket with Infra.
** Post an announcement to user and development lists
* Update the Incubator site
** Update the Incubator status page
** Update the podling status page. All sections should now be filled in
including EXIT. Take some time to read carefully since this page forms the
final public record for graduation.
** Edit the Incubator website to remove the podling from the list in
project.xml. Here explains how.
* Add Project To  www.apache.org
** Check out [https://svn.apache.org/repos/asf/infrastructure/site/trunk](https://svn.apache.org/repos/asf/infrastructure/site/trunk)
** Patch  xdocs/stylesheets/project.xml
** If you have karma, regenerated and apply patch
** If you do not have karma, submit patch to  infrastructure JIRA
* Mailing lists
** -Request that podlings lists be transferred to their new home. Any new
mailing lists should be requested at the same time.-
** When this has been executed by infrastructure, post an announcement to
user and development lists.
** Send notice to nabble.com (if they archive your incubator mailing list)
that the address has changed, and possibly the location of your project (if
it is listed as being part of the incubator). Repeat for other known
mailing list archivers.
** Update website: replace links to old archives with links to new ones and
add new links to historic archives from incubation.
** -Check project-private mailing list membership. Mentors should be
allowed to remain if they wish to do so. The subscriber list should
otherwise match that on the resolution. See  this and the EZMLM
"Moderator's and Administrator's Manual".-
** Update mail addresses including (The chair should have karma to perform
these tasks):
*** svn commit messages (see
infrastructure/trunk/subversion/authorization/asf-mailer.conf )
*** confluence commit messages (see adminstration documentation)
*** issue tracking messages (see administration documentation)
* Issue Tracking
** Check that the issue tracking system used by the podling reflects the
project's new status.
* Distribution mirrors
** After you have a release at your new home (/dist/vcl/ area), remove any
distribution artifacts from your old /dist/incubator/vcl/ area. Remember
from the mirror guidelines that everything is automatically added to
archive.apache.org anyway.

* Final Revision of Podling Incubation Records - When a project graduates,
then the incubator resources need to be updated to indicate that the
project is no longer incubating. Here are a few of the items that need to
be done:
** Update the svn incubator/trunk/content/projects/vcl.xml file to show the
project's status.
** Change the podling status to "graduated" in the podling summary file,
i.e update the incubator/trunk/content/podlings.xml svn file. Also add the
"enddate" attribute to document when the project graduated.
** Ensure that other svn resources for your project have moved to your new
home.
