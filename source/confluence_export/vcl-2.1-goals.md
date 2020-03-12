---
title: VCL 2.1 goals
---

VCL 2.1 goals

1. xCAT 2.x module
1. * written and in testing stage
1. Get rid of preferredimage from image table, use nextimage instead
1. Clean up data base - removed unused variables
1. Shibboleth support
1. * testing stage
1. Web server load balance
1. healthcheck.pl - improve / bring up to date, add support for vms,&nbsp;
try to reinstall nodes if necessary.
1. Clean up / re-write blockrequest module, planning to use api calls to web
site.
1. Modularize OS code
1. Polish cluster reservation process
1. Allow dynamic change of predictive load module - currently have to
restart vcld after change in database.
1. * Done - committed to repos
1. Pull out check_ssh dep - binary from nagios
1. * Done - committed to repos
1. Additional management node configuration web tools.
1. image retrieval between management nodes - allow for defined ssh ports.
Store which port in db management node table
1. Add check for existence of image libraries and take appropriate action,
in case /install gets dropped for some reason.
1. Vista OS support
