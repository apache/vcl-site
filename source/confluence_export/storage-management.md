---
title: Storage Management
---

Something VCL has been lacking is automated management of storage, both on
the system side and on the user side. This is a list of areas that should
be addressed when designing storage management and automation:

* System storage:
** block attached image store for management nodes
** network attached image store for management nodes
** block attached image store for hypervisors
** network attached image store for hypervisors
** block attached images for node booting (i.e. iSCSI booting)
** file/block/LUN cloning
** LUN/share management of existing stores
** LUN/share management of temporary stores (things created/destroyed
dynamically)
** logging/auditing
** where does security fit in?
* User storage:
** block attached
** networked filesystems
** allocation
** authentication/authorization
** quota management
** lifetime of storage (just for reservation vs. lifetime of user)
** backups
** request process
** logging/auditing
