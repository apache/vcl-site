---
title: Adding xCAT kickstart based image
---

# Guide for adding kickstart installs using xCAT to the VCL database.


xCAT is the bare-metal provisioning tool primarily used within VCL. It has
the ability to install physical nodes with an operating system such
as; windows Red Hat, CentOS, ESX, SLES on x86 based hardware. This
guide will discuss adding support to VCL for kickstart based or diskfull
installs.

Prerequisites are that you need to have a working xCAT install. Please
see xCAT installation guide in order to install and configure xCAT.

* xCAT main page: [http://xcat.sourceforge.net/](http://xcat.sourceforge.net/)
* xCAT Getting Started guide: [http://sourceforge.net/apps/mediawiki/xcat/index.php?title=XCAT_Documentation](http://sourceforge.net/apps/mediawiki/xcat/index.php?title=XCAT_Documentation)

## Kickstart Template files

The template files used by xCAT reside in
/opt/xcat/share/xcat/install/&lt;distro&gt;. distro can be rh, centos, fedora,
esx, etc. Make sure to have a working template file. There are several
examples in either of the distro directories that can used as a starting
point. Once you have a working template, proceed to adding to the VCL
database.

## Adding kickstart based install to the VCL database

The name of the template file and the image.name must match. VCL uses this
name to check for and properly load using kickstart method. The xcat name
will have the .tmpl, for example the vcl image.name entry of
**rhel5-base25-v0** the template file for xcat will be
**rhel5-base25-v0.tmpl.**

There are three tables that need to have entries before you can start using
the image through the VCL web interface. The tables used are:

* image
* imagerevision
* resource

Depending on your OS and the version of VCL, you might need to also create
a new entry in the OS table. An example of adding a new OSid is discussed
below.

In our sql statement examples we will use RedHat 5 and the image id of 25
as above **rhel5-base25-v0.** In the below sql statement make any
changes as needed such as ownerid, in this example it is set to 1 or the
admin user id.

```sql
INSERT INTO `image` (id, `name`, `prettyname`, `ownerid`, `platformid`, `OSid`, `minram`, `minprocnumber`, `minprocspeed`, `minnetwork`,`reloadtime`, `deleted`, `lastupdate`, `forcheckout`, `maxinitialtime`,`project`, `size`) VALUES (25, 'rhel5-base25-v0', 'RHEL 5 base', 1, 1, 19, 1024, 1, 0, 10, 14, 0, NOW(), 1, 0, 'vcl', 1045);

INSERT INTO `imagerevision` (`imageid`, `revision`, `userid`, `datecreated`, `deleted`, `production`, `comments`, `imagename`) VALUES (25, 0, 1, NOW(), 0, 1, NULL, 'rhel5-base25-v0');

INSERT INTO `resource` (`resourcetypeid`, `subid`) VALUES (13, 25);
```

Again, the xCAT template .tmpl file must match the the
entry VCL database entry of image.name.


VCL image.name = **rhel5-base25-v0**<br>
xCAT template file name = **rhel5-base25-v0.tmpl**

At this point you will be able to manage this image through the VCL
interface.

* Go to Manage images
* Edit image grouping
* Select image group mapped to load onto your bare-metal blades. See 
[Add computers](docs/addcomputers.html) if you have not added any physical nodes
yet.
* Add **RHEL 5 base** to the desired image group

## Testing kickstart file

Test the load, by either making a reservation for the new
environment or try to reload a physical node through manage computers
computer utilities. Watch the vcld.log file to view the processing and to
debug any issues that may occur.

## Extending the OS table

If VCL supports the OS, extending the OS table for a new OS is fairly
straight forward. In this example we will use Red Hat 6.

```sql
INSERT INTO `OS` (`name`, `prettyname`, `type`, `installtype`, `sourcepath`, `moduleid`) VALUES ('rhel6','RedHat Enterprise 6','linux','kickstart','rhel6', (SELECT `id` FROM `module` WHERE `name` LIKE 'os_linux'));
```
