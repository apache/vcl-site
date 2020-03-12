---
title: Pre-release test procedures
---

Recommended test cases for release candidates.

<a name="Pre-releasetestprocedures-Webfrontend"></a>
### Web frontend

* Block Allocations
** For each of these, test for weekly, monthly, and list
** Create new block allocations; try adding multiple times per test
** Edit block allocations
** Delete block allocations
** Request new block allocations; try both specifying a user group and
selecting "(group not listed)"; try with and without comments; try with
users with and without an email address in the user table
** Accept requested block allocations; try accepting from users with and
without an email address in the user table
** Reject requested block allocations; try rejecting from users with and
without an email address in the user table
** Create an entry where you are in the user group that is active during
the current time to check viewing the block status

<a name="Pre-releasetestprocedures-WebfrontendXMLRPCAPI"></a>
### Web frontend XML RPC API

(placeholder)

<a name="Pre-releasetestprocedures-Backend-Managementnode"></a>
### Backend - Management node

General range of tests for the back-end processing. The tests would more
detailed depending on the provisioning module and OS module.

* Reservation flow:
** start - proper loading through provisioning module
** monitor - during inuse state, based on check user connection flag
** end - warning of upcoming end time, reclaim / reload node if applicable
* End User Notifications: start, end time near, end. Image creation. (User
pref dependent)
* Sysadmin Notifications: Warnings and Criticals
* Image Creation: pre-capture process(write currentimage.txt, setup OS with
boot scripts), proper flow from start - complete. Dependent on provisioning
and OS modules.
* Cluster reservations: Flow - parent /child dependency. Parent process
waits on children node to load, etc Children load/processes depend on
parent process to handle request state change and notify end-user
* Block allocations (previously called Block Reservations): Correct
processing, notifications/warnings, etc
