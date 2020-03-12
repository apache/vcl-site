---
title: Apache VCL Release Notes
---

## 2.5.1 Release Notes {#2.5.1}
2.5.1 is a bugfix release. See the [Change Log](changelog.html#2.5.1) for a list of 
issues resolved in this release. Below is a list of a few notable changes.

* PHP code updated to work with PHP 7.x.
* Rudimentary NFS file share mounting extended to work with Windows
* Added method for using HTML in user emails through external script

## 2.5 Release Notes {#2.5}

2.5 is a major release. Many changes and bug fixes were done. Below
is a list containing some of the more notable items. See the 
[Change Log](changelog.html#2.5) for a full list of changes completed 
in this release.

Added:

* Support for Windows 10 and Windows Server 2016 images
* Responsive theme (dropdownmenus) to web site
* Support for automatically joining Windows images to an Active Directory domain
* Basic automatic mounting of NFS shares for all users
* Customization of email messages sent to users on a per-affiliation basis
* Support for the automatic configuration of ufw and firewalld-based firewalls
  within Linux images
* Support for NAT hosts which use ufw os firewalld-based firewalls including
  Ubuntu and RedHat/CentOS 7 and later
* Support for the execution of custom scripts on a management node at various
  stages of the reservation
* Display of reservation times in the user's own timezone

Removed:

* Server Profiles
* Use of the Windows Administrator user account for imaging reservations

## 2.4.2 Release Notes {#2.4.2}

2.4.2 is a major release. Many changes and bugs fixes were done. Below
is a list containing some of the more notable items. See the 
[Change Log](changelog.html#2.4.2) for a full list of changes completed 
in this release.

Added:

* Scripted installation and upgrade
* Ability to run multiple web servers
* NAT support for connecting to reservations
* Provisioning to OpenStack
* Provisioning to OpenNebula
* Provisioning to ESXi 5.5
* Windows 8.x and Server 2012 images
* Use of 64 bit cygwin
* Improved interface for resource management

Removed: 

* xCAT 1.x no longer supported

## 2.4.1 Release Notes {#2.4.1}

After 2.4.1 was created, but before it was announced, a notable
bug was found. It was decided not to announce the release of 2.4.1
but to move on to releasing 2.4.2 instead. Therefore, 2.4.1 was
never officially released.

## 2.4 Release Notes {#2.4}

After 2.4 was created, but before it was announced, a notable
bug was found. It was decided not to announce the release of 2.4
but to move on to releasing 2.4.1 instead. Therefore, 2.4 was
never officially released.

## 2.3.2 Release Notes {#2.3.2}
2.3.2 is a bugfix release. See the [Change Log](changelog.html#2.3.2) for a list of 
issues resolved in this release.

## 2.3.1 Release Notes {#2.3.1}
2.3.1 is a bugfix release. See the [Change Log](changelog.html#2.3.1) for a list of 
issues resolved in this release.

There are a few particular issues worth highlighting:

* 2.3 was missing a default entry in the database that prevented KVM deploys from working that is now fixed
* additional methods were added to the XMLRPC API - see [VCL-617](https://issues.apache.org/jira/browse/VCL-617) for the details.

## 2.2.2 Release Notes {#2.2.2}
2.2.2 is a bugfix release. See the [Change Log](changelog.html#2.2.2) for a list of 
issues resolved in this release.