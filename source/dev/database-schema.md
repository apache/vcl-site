---
title: Database Schema
---

{{% toc %}}

### affiliation table
This table contains a list of affiliations that can access this VCL site.

* **id** - id of entry
* **name** - name of entry
* **shibname** - for affiliations using shibboleth - the name of the shibboleth affiliation (the part after @ in eduPersonScopedAffiliation)
* **dataUpdateText** - this will be displayed on the User Preferences-&gt;Personal Information page to provide information on how to update things other than Preferred Name in that box
* **sitewwwaddress** - URL for login page for this affiliation; typically it is just the URL encoded parameters to index.php to have the authentication method already selected (i.e. <a href="https://vcl.example.org/vcl/index.php?mode=selectauth&amp;authtype=EXAMPLE%20LDAP" class="external-link" rel="nofollow">https://vcl.example.org/vcl/index.php?mode=selectauth&amp;authtype=EXAMPLE%20LDAP</a>)
* **helpaddress** - support email address for this affiliation
* **shibonly** - 1 if this affiliation can only be authenticated via shibboleth, 0 if LDAP is also set up
* **theme** - theme to be used for the web UI for users with this affiliation; must match something under the themes directory of the web code

### blockComputers table
This table tracks which computers have been allocated to individual block allocation time slots.

* **blockTimeid** - reference to blockTimes.id
* **computerid** - reference to computer.id
* **imageid** - reference to image.id
* **reloadrequestid** - reference to request.id - reload reservation for preloading this node


### blockRequest table

This table contains all of the block allocations that have been requested and their current state.

* **id** - id of entry
* **name** - name of entry
* **imageid** - reference to image.id
* **numMachines** - number of machines to preload for this block allocation
* **groupid** - reference to usergroup.id - user group that will have access to machines in this block allocation
* **repeating** - enum field - weekly, monthly, or list - how this block allocation repeats
* **ownerid** - reference to user.id - owner of the block allocation
* **admingroupid** - reference to usergroup.id - (to be deprecated in 2.3) - user group that can modify this block allocation
* **managementnodeid** - reference to managementnode.id - management node that is to process this block allocation
* **expireTime** - last date and time of block allocation time slots
* **processing** - flag used by vcld to determine if a vcld process is processing this block allocation
* **status** - enum field - requested, accepted, completed, reject - current status of the block allocation
* **comments** - any comments entered by the person that requested the block allocation


### blockTimes table
This table contains all of the time slots associated with a block allocation that are active or have not yet been reached. Time slots are deleted after they are completed.

* **id** - id of entry
* **blockRequestid** - reference to blockRequest.id
* **start** - start of block time
* **end** - end of block time
* **processed** - flag for vcld - 1 if block time has been processed by vcld, 0 if not
* **skip** - flag for users to skip individual instances of repeating block allocations - 1 to skip, 0 to use


### blockWebDate table

This table contains date related items associated with a block allocation so that they can more easily be retrieved when editing a block allocation.

* **blockRequestid** - reference to blockRequest.id
* **start** - start date of block allocation
* **end** - end date of block allocation
* **days** - for weekly repeating blocks, this is a bitmask of the selected days; for monthly repeating blocks, this is the day of the week; for lists, this is the order the item is in the set of dates
* **weeknum** - only used for monthly repeating blocks - the selected week of the month


### blockWebTime table

This table contains time related items associated with a block allocation so that they can more easily be retrieved when editing a block allocation.

* **blockRequestid** - reference to blockRequest.id
* **starthour** - start hour of block allocation
* **startminute** - start minute of block allocation
* **startmeridian** - start meridian of block allocation
* **endhour** - end hour of block allocation
* **endminute** - end minute of block allocation
* **endmeridian** - end meridian of block allocation
* **order** - for weekly and monthly repeating blocks, this is the sequential order of the time slot; for lists, it is the sequential order of the date/time


### changelog table
This table logs changes made to reservations.

* **id** - id of entry
* **logid** - reference to log.id
* **userid** - user.id for the user that made the change (in case of server reservations, may not match owner of reservation)
* **reservationid** - reservation.id of the reservation affected by the change
* **start** - change to start time of reservation
* **end** - change to end time of reservation
* **computerid** - reference to computer.id - change to computer assigned to reservation
* **remoteIP** - change to remote IP of reservation user
* **wasavailable** - mostly deprecated - if submitted change to start/end time of reservation was available for use or not
* **timestamp** - datetime entry was added
* **other** - for recording events users cause to happen to reservations such as reinstalling, rebooting, or changing admin/login user groups (recorded by calling addChangeLogEntryOther in the web code)


### clickThroughs table
This table logs click through agreements users must agree to when they create images.

* **userid** - reference to user.id - user that clicked agreement
* **imageid** - reference to image.id - image for which agreement was clicked
* **imagerevisionid** - reference to imagerevision.id - image revision for which agreement was clicked
* **accepted** - datetime agreement clicked
* **agreement** - text of agreement at time it was clicked


### computer table
This table contains all information about compute nodes and VMs that VCL controls. All bare metal computers, virtual hosts, and virtual machines must have an entry in this table.

* **id** - id of entry
* **stateid** - reference to state.id - current state of computer
* **ownerid** - reference to owner.id - owner of computer
* **platformid** - reference to platform.id - platform of computer
* **scheduleid** - reference to schedule.id - schedule of computer
* **vmhostid** - reference to vmhost.id - only used for virtual machines, this is the host computer of the VM
* **currentimageid** - reference to image.id - image currently loaded on computer
* **nextimageid** - reference to image.id - image to be loaded next on computer, only used under certain circumstances
* **imagerevisionid** - reference to imagerevision.id - image revision currently loaded on computer (somewhat redundant with currentimageid)
* **RAM** - amount of RAM physical computer has, or maximum amount of RAM that can be allocated to virtual computer
* **procnumber** - number of processor cores physical computer has, or maximum number of processor cores that can be allocated to virtual computer
* **procspeed** - speed of processor cores in MHz
* **network** - speed of (public?) NIC(s) in Mbps
* **hostname** - private hostname of computer
* **IPaddress** - public IP address
* **privateIPaddress** - private IP address
* **eth0macaddress** - MAC address of private NIC
* **eth1macaddress** - MAC address of public NIC
* **type** - blade, lab, or virtualmachine - type of the computer
* **provisioningid** - reference to provisioning.id - provisioning module/method to be used for computer
* **drivetype** - hda or sda - type of drive in the computer (is this still used?)
* **deleted** - flag to show if computer has been deleted - 1 if deleted, 0 if not
* **datedeleted** - datetime field for when computer was flagged as deleted
* **notes** - any notes entered when computer placed into maintenance state
* **lastcheck** - date stamp of last time the computer was checked through healthcheck.pl
* **location** - physical location of node (Data Center 1, rack 1, etc)
* **dsa** - Not being used. Was planned for storing host keys for ssh
* **dsapub** - Not being used. Was planned for storing host keys for ssh
* **rsa** - Not being used. Was planned for storing host keys for ssh
* **rsapub** - Not being used. Was planned for storing host keys for ssh 
* **host** - Not being used. Was planned for storing host keys for ssh
* **hostpub** - Not being used. Was planned for storing host keys for ssh
* **vmtypeid** - reference to vmtype.id - only used for virtual machines, this is the type of the VM (vmware, xen, kvm, etc)
* **predictivemoduleid** - module.id for the perl module that handles what to do with the node after a reservation


### computerloadflow table
This table contains entries that establish a flow of states that are followed when a reservation is being deployed so that users can have feedback on the current reservations page about their reservations.

* **computerloadstateid** - reference to computerloadstate.id
* **nextstateid** - reference to computerloadstate.id - the computer load state that follows this one
* **type** - type of load this sequence is for


### computerloadlog table
This table contains actual log entries for each state processed when a reservation is being deployed so that users can have feedback on the current reservations page about their reservations.

* **id** - id of entry
* **reservationid** - reference to reservation.id - reservation this entry is for
* **computerid** - reference to computer.id
* **loadstateid** - reference to computerloadstate.id - state this entry is for
* **timestamp** - date/time entry entered into log
* **additionalinfo** - details about this entry


### computerloadstate table
This table contains the load states that a reservation goes through when being deployed and their estimated time so that an estimate of how much longer the deploy will take can be generated.

* **id** - id of entry
* **loadstatename** - short name of state
* **prettyname** - more descriptive name of state
* **est** - estimated time for state in minutes


### connectlog table
This table contains information about users connecting to reservations.

* **id** - id of entry
* **logid** - log.id for reservation
* **reservationid** - reservation.id for reservation
* **userid** - user.id for user connecting to reservation
* **remoteIP** - remote IP of user
* **varified** - 
* **timestamp** - time stamp when event occurred


### connectmethod table
This table contains all of the connect methods available to be assigned to an image.  Connect methods are things like RDP, ssh, VNC, etc.

* **id** - id of entry
* **name** - name of entry
* **description** - description of connect method
* **connecttext** - this text will be displayed on the Connect page, there are a few variable substitutions available to be used: #userid#, #password#, #connectIP#, and #connectport#
* **servicename** - name of service to be started to enable connect method on provisioned node
* **startupscript** - name of script to be run to enable connect method on provisioned node


### connectmethodmap table
This table contains two types of information and can be somewhat confusing.  It tracks which connect methods are mapped to which OS types, OSes, and image revisions.  It also contains which methods can be assigned to which OS types and OSes.  Entries that have autoprovisioned set to 0 or 1 are entries that tell whether or not the image can be assigned to that OS type or OS.  Entries that have autoprovisioned set to NULL tell whether that method is enabled in addition to default methods for the image, or whether that method is a default one but disable for the image.

* **connectmethodid** - reference to connectmethod.id
* **OStypeid** - reference to OStype.id - OS type this entry applies to (can be NULL)
* **OSid** - reference to OS.id - OS this entry applies to (can be NULL)
* **imagerevisionid** - reference to imagerevision.id - image revision this entry applies to (can be NULL)
* **disabled** - flag telling if method is enabled/disabled for combination of OStypeid, OSid, and imagerevisionid
* **autoprovisioned** - NULL, 0, or 1 - flag to tell if this connect method can be autoprovisioned by vcld or if the image owner must install the software to enable it


### connectmethodport
This table contains the ports associated with a connectmethod. The ports were initially part of the connectmethod table, but separating them out allowed for multiple ports per connect method.

* **id** - id of entry
* **connectmethodid** - connectmethod.id of which these ports are part
* **protocol** - TCP or UDP
* **port** - tcp or udp port number


### continuations table
This table contains "continuations" which are basically saved states that can then be submitted by the frontend to perform an action.

* **id** - id of entry
* **userid** - reference to user.id - who this entry belongs to
* **expiretime** - date/time entry expires
* **frommode** - mode transitioning from
* **tomode** - mode transitioning to
* **data** - serialized data saved with this continuation
* **multicall** - flag to tell if this continuation can be called more than one time
* **parentid** - reference to continuations.id - parent of this continuation for continuation chains (can be NULL)
* **deletefromid** - reference to continuations.id - id in a continuation chain from which to start deleting the chain



### documentation table
This table is deprecated.  At one time, there was a built in documentation wiki like part of the site.

* **name** - name of entry
* **title** - title of documentation item
* **data** - text of documentation item

### image table
This table contains all information about the images available through VCL.  It comes with a single required special image - "No image" that is used to signify when a computer is not loaded with anything.

* **id** - id of entry
* **name** - system name of image
* **prettyname** - name of image that is displayed to users
* **ownerid** - reference to user.id - owner of image
* **imagetypeid** - reference to imagetype.id - type of the image
* **platformid** - reference to platform.id - platform of image
* **OSid** - reference to OS.id - OS of image
* **imagemetaid** - reference to imagemeta.id - NULL or id from imagemeta table where additional image information is stored
* **minram** - minimum RAM required for this image in MB; for VM images, this is how much RAM to allocate to the VM - however, vcld controls the minimum that will be allocated to a VM
* **minprocnumber** - minimum number of cores required by image
* **minprocspeed** - minimum processor speed required by image in MHz
* **minnetwork** - minimum (public?) network speed required by image in Mbps
* **maxconcurrent** - maximum concurrent reservations that can be made for image
* **reloadtime** - reload time for image - used by backend for knowing how long to wait during certain parts of deploying the image; only used by the frontend the first time the image is loaded, after which historical data is used to estimate loading time
* **deleted** - flag to show if image has been deleted - 1 if deleted, 0 if not
* **test** - flag to show if there is a test version of this image available (depricated?)
* **lastupdate** - date/time image was last updated
* **forcheckout** - flag to tell if the image should show up in the list of images on the new reservations page - this is designed to be used for subimages in clusters where the subimages should not be directly reserved
* **maxinitialtime** - maximum initial time the image can be reserved
* **project** - vcl, hpc, or vclhpc - string used to control some network configuration?
* **size** - size of the image in MB?
* **architecture** - x86 or x86_64 - architecture of image
* **description** - description of image displayed on new reservations page
* **usage** - notes on how to use image displayed on Connect page
* **basedoffrevisionid** - reference to imagerevision.id - image revision this image was based off of


### imagemeta table
This table contains additional information about some images.  It was added so that the extra information would not needed to be recorded for every image when most of them would not need it.

* **id** - id of entry
* **checkuser** - flag to tell if reservations for image should be timed out if user is disconnect for &gt; 15 minutes - 0 not to do timeout, 1 to do timeout
* **subimages** - flag to tell if subimages are associated with image
* **sysprep** - flat to tell if sysprep should be used on this image (bare metal images only, sysprep is always disabled for VMs)
* **postoption** - ??
* **architecture** - ??
* **rootaccess** - flag to tell if users should have root access on reservations for image - 1 to have it, 0 not to
* **sethostname** - flag to determine if vcld should set the hostname of the computer after an image is deployed to the computer.hostname entry for the computer; default value is NULL; default behaviour for windows is not to set it; default behaviour for linux is to set it


### imagerevision table
This table contains an entry for every revision (including the initial one) of each image.

* **id** - id of entry
* **imageid** - reference to image.id
* **revision** - number of this revision
* **userid** - reference to user.id - user that created the revision
* **datecreated** - date/time revision was created
* **deleted** - flag to tell if revision has been deleted - 1 for deleted, 0 otherwise
* **datedeleted** - date/time revision was set to deleted
* **production** - flag to tell if this revision is the production one - 1 for production, 0 otherwise
* **comments** - comments entered when revision was created for keeping track of what was done to the image
* **imagename** - system name of revision
* **autocaptured** - flag to tell if this was an auto-captured revision - 1 if it was, 0 otherwise


### imagerevisioninfo
* **imagerevisionid** - reference to imagerevision.id
* **usernames** - 
* **firewallenabled** - 
* **timestamp** - 


### imagetype
This table is a list of all of the types of images VCL can handle.  As of 2.4.2, these values are kickstart, lab, none, partimage, partimage-ng, qcow2, vdi, and vmdk.

* **id** - id of entry
* **name** - name of entry


### IMtype table
This table never really got used.  The idea was the people could be notified via IM in addition to or instead of via email.

* **id** - id of entry
* **name** - name of entry


### localauth table

This table contains password hashes for local accounts.

* **userid** - reference to user.id
* **passhash** - sha1 hash of password and salt
* **salt** - 8 character salt to be hashed with the password
* **lastupdated** - date/time entry was last updated
* **lockedout** - (unused) flag to tell if this account is locked out - 1 if locked out, 0 otherwise


### log table

This table contains an entry for every reservation made in VCL except for those made by the special account 'vclreload'.

* **id** - id of entry
* **userid** - reference to user.id
* **nowfuture** - now or future - whether the reservation was for 'now' or a future date/time
* **start** - start time of the reservation
* **loaded** - date/time the image was ready for user connection
* **initialend** - scheduled end time of reservation
* **finalend** - date/time reservation actually ended
* **wasavailable** - flag to tell if requested reservation was actually available - somewhat deprecated because users get feedback that a selection is not available without actually submitting it
* **ending** - deleted, released, failed, failedtest, noack, nologin, timeout, EOR, or none - how the reservation ended
* **requestid** - reference to request.id - useful for looking through vcld logs
* **computerid** - reference to computer.id
* **remoteIP** - IP address of user's machine
* **imageid** - reference to image.id
* **size** - ??


### loginlog table

This table contains a log of every authentication attempt.

* **user** - user id entered on login page
* **authmech** - authentication method selected
* **affiliationid** - affiliation used to authenticate user
* **timestamp** - date/time authentication attempt occurred
* **passfail** - 0 for fail, 1 for pass
* **remoteIP** - IP address of user's machine
* **code** - either "none" or "invalid credentials" - used for recording when an LDAP server responds with "invalid credentials" when attempting to validate a username/password combination


### managementnode table
This table contains information about each management node.

* **id** - id of entry
* **IPaddress** - IP of management node
* **hostname** - hostname of management node
* **ownerid** - reference to user.id - owner of management node
* **stateid** - reference to state.id - current state of management node
* **lastcheckin** - date/time of last check in by management node
* **checkininterval** - how often in seconds the management node should be checking in
* **installpath** - path to root of image library
* **imagelibenable** - 1 to enable sharing images among management nodes, 0 otherwise
* **imagelibgroupid** - reference to resourcegroup.id - resource group that contains other management nodes from which this one can get images
* **imagelibuser** - user to use when fetching images from other management nodes
* **imagelibkey** - ssh identity key to use when fetching images from other management nodes
* **keys** - comman delimited list of ssh identity keys to use when sshing to compute nodes
* **sshport** - ssh port to listen on
* **publicIPconfiguration** - how compute nodes managed by this node obtain their public IP
* **publicSubnetMask** - if publicIPconfiguration is 'static', enter the subnet mask to be used when configuring the compute nodes addresses
* **publicDefaultGateway** - if publicIPconfiguration is 'static', enter the gateway to be used when configuring the compute nodes addresses
* **publicDNSserver** - if publicIPconfiguration is 'static', enter the DNS server to be used when configuring the compute nodes addresses
* **sysadminEmailAddress** - email address to use when sending problem reports
* **sharedMailBox** - email address to use for sending shadow emails of user emails
NOT_STANDALONE - list of affiliations for which federated authentication is used for Linux images, meaning vcld does not need to set a password for users when creating their reservations because the image will handle it via federated authentication
* **availablenetworks** - list of networks for which the management node is capable of configuring fixed (static) addresses for server reservations


### module table

This table contains information about the various perl modules that are part of vcld.

* **id** - id of module
* **name** - name of module
* **prettyname** - more descriptive name of module
* **description** - description of module
* **perlpackage** - string to use when including this module in perl scripts


### nathost
This table tracks which nodes are configured to be used as NAT hosts.

* **id** - id of entry
* **resourceid** - reference to resource.id - which resource is being used as a NAT host (can be either a computer or management node)
* **publicIPaddress** - IP address on node that faces the public Internet
* **internalIPaddress** - IP address on node that faces the internal network


### nathostcomputermap
This table maps compute nodes to nodes being used as a NAT host for them.

* **nathostid** - reference to nathost.id
* **computerid** - reference to computer.id


### natlog
This table records relevant information about how NAT was configured for a reservation.

* **sublogid** - reference to sublog.id - sublog entry for reservation
* **nathostresourceid** - reference to resource.id - resource id of host doing NAT at time of reservation
* **publicIPaddress** - public facing IP address on NAT host at time of reservation
* **publicport** - public port forwarded to internal node on NAT host at time of reservation
* **internalIPaddress** - internal facing IP address on NAT host at time of reservation
* **internalport** - internal port on reserved node to which forwarding was done on NAT host at time of reservation
* **protocol** - protocol (TCP or UDP) of port that was forwarded at time of reservation
* **timestamp** - timestamp at which the port forward was set up


### natport
This table tracks which ports are actively being forwarded on NAT hosts for which reservations.

* **reservationid** - reference to reservation.id - reservation for which port is forwarded
* **nathostid** - reference to nathost.id - node on which port is forwarded
* **publicport** - public port being forwarded on NAT host
* **connectmethodportid** - reference to connectmethodport.id


### openstackcomputermap
* **instanceid** - 
* **computerid** - 


### openstackimagerevision
* **imagerevisionid** - 
* **imagedetails** - 
* **flavordetails** - 


### OS table

This table contains information about OSes VCL knows about.

* **id** - id of entry
* **name** - name of entry
* **prettyname** - more descriptive name of OS
* **type** - reference to OStype.name - windows, linux, unix, etc
* **installtype** - reference to OSinstalltype.name - none, partimage, kickstart, etc
* **minram** - minimum RAM required by this OS
* **sourcepath** - ??
* **moduleid** - reference to module.id - module that handles this OS


### OSinstalltype table
This table is a list of the ways an image can be installed.

* **id** - id of entry
* **name** - name of entry


### OStype table
This table contains a list of OS types VCL knows about - linux, unix, windows, etc.

* **id** - id of entry
* **name** - name of entry


### platform table
This table contains a list of platforms VCL knows about - i386, i386_lab (special case for lab machines), and ultrasparc.

* **id** - id of entry
* **name** - name of entry

### privnode table
This table contains all of the nodes that make up the Privilege Tree on the Privileges page.

* **id** - id of entry
* **parent** - reference to privnode.id - parent of this node
* **name** - name of entry


### provisioning table
This table contains all of the provisioning modules that are part of vcld.

* **id** - id of entry
* **name** - name of entry
* **prettyname** - more descriptive name of provisioning method
* **moduleid** - reference to module.id - id of module that handles this provisioning method


### provisioningOSinstalltype table
This table is a mapping of which provisioning methods can handle which OS install types.

* **provisioningid** - reference to provisioning.id
* **OSinstalltypeid** - reference to OSinstalltype.id


### querylog table
This table contains an entry for every query performed by the frontend that modifies the database (i.e. everything but SELECT statements).

* **userid** - reference to user.id
* **timestamp** - date/time of query
* **mode** - mode of site when query performed
* **query** - string of query


### request table
This table contains information about every current or future reservation.  Only a single entry exists in this table for cluster reservations.

* **id** - id of entry
* **stateid** - reference to state.id - current state of reservation
* **userid** - reference to user.id
* **laststateid** - reference to state.id - last state of reservation
* **logid** - reference to log.id - log entry for reservation
* **forimaging** - 0 for normal reservation, 1 for imaging
* **test** - ??
* **preload** - ??
* **start** - date/time for start of reservation
* **end** - date/time for end of reservation
* **daterequested** - date/time reservation submitted
* **datemodified** - date/time reservation modified
* **checkuser** - flag to tell if reservation should be timed out if user is disconnect for &gt; 15 minutes - 0 not to do timeout, 1 to do timeout


### reservation table
This table contains information about every current or future reservation.  There will be one entry in this table corresponding to each entry in the request table for normal reservations, and multiple entries (one for each node) in this one for each entry in the request table for cluster reservations.

* **id** - id of entry
* **requestid** - reference to request.id - corresponding entry in request table
* **computerid** - reference to computer.id - computer assigned to this reservation
* **imageid** - reference to image.id - image deployed on computer
* **imagerevisionid** - reference to imagerevision.id - image revision to be deployed on computer
* **managementnodeid** - reference to managementnode.id - management node handling this reservation
* **remoteIP** - IP address of user's machine
* **lastcheck** - date/time reservation last checked by vcld
* **pw** - user's password for reservation - leave empty to signify user should use enterprise authentication password
* **connectIP** - (unused)
* **connectport** - (unused)


### reservationaccounts table
This table contains userids and passwords for additional accounts for server reservations.  There is not an entry for the owner of the reservation.  These correspond to the admin and login user groups.

* **reservationid** - reference to reservation.id
* **userid** - reference to user.id
* **password** - user's password for this reservation


### resource table
This table contains an entry for every resource VCL knows about.  Every resource has a unique id from this table, and a sub id from a resource specific table (computer, image, management node, etc).

* **id** - id of entry
* **resourcetypeid** - reference to resourcetype.id - type of this resource
* **subid** - reference to id from specific resource table (computer.id, image.id, managementnode.id, etc)


### resourcegroup table
This table contains all of the resource groups.

* **id** - id of entry
* **name** - name of entry
* **ownerusergroupid** - reference to usergroup.id - user group that owns this resource group
* **resourcetypeid** - reference to resourcetype.id - type of this resource group


### resourcegroupmembers table
This table contains a list of which resources are in which resource groups.

* **resourceid** - reference to resource.id
* **resourcegroupid** - reference to resourcegroup.id


### resourcemap table
This table contains which resource groups map to other resource groups.

resourcegroupid1 - reference to resourcegroup.id
resourcetypeid1 - reference to resourcetype.id
resourcegroupid2 - reference to resourcegroup.id
resourcetypeid2 - reference to resourcetype.id


### resourcepriv table
This table contains the attributes that can be granted to resource groups.

* **id** - id of entry
* **resourcegroupid** - reference to resourcegroup.id - resource group being assigned attribute
* **privnodeid** - reference to privnode.id - node where attribute being assigned
* **type** - block, cascade, available, administer, manageGroup, or manageMapping - attribute being assigned at node


### resourcetype table
This table contains a list of all the resource types.

* **id** - id of entry
* **name** - name of entry


### schedule table
This table contains all of the schedules available.

* **id** - id of entry
* **name** - name of entry
* **ownerid** - reference to user.id - owner of schedule


### scheduletimes table

This table contains all of the starts/ends of the time slots for each schedule.  Schedules are what times during a week that computers are available.  They run from midnight Sunday morning (0) to midnight Sunday morning one week later (10080).

* **scheduleid** - reference to schedule.id
* **start** - start of time slot in minutes since midnight Sunday morning
* **end** - end of time slot in minutes since midnight Sunday morning


### semaphone table
This table is used by the frontend to manage semaphores for computers being considered for reservations. During normal network and CPU loads, entries in this table should only exist for fractions of a second.

* **computerid** - reference to computer.id - computer being locked
* **imageid** - reference to image.id - image to be deployed on computer
* **imagerevisionid** - reference to imagerevision.id - revision of image to be deployed on computer
* **managementnodeid** - reference to managementnode.id - management node to handle reservation
* **expires** - timestamp after which the semaphore is considered to be expired; can be configured by setting SEMTIMEOUT in conf.php, defaults to 45 seconds after insertion
* **procid** - unique id for process that obtained the lock (combination of hostname and process id)


### serverprofile table
This table contains all of the server profiles.

* **id** - id of entry
* **name** - name of entry
* **description** - info about profile
* **imageid** - reference to image.id
* **ownerid** - reference to user.id - owner of this profile
* **ending** - specified or indefinite - how reservations for this profile will typically end
* **fixedIP** - IP address reservations for this profile will typically use
* **fixedMAC** - MAC address reservations for this profile will typically use
* **admingroupid** - reference to usergroup.id
* **logingroupid** - reference to usergroup.id
* **monitored** - (unused)


### serverrequest table
This table contains an entry for each server reservation.

* **id** - id of entry
* **name** - name of server reservation
* **serverprofileid** - reference to serverprofile.id - 0 if no profile used or too many items changed from profile
* **requestid** - reference to request.id - main request entry associated with this server reservation
* **fixedIP** - IP address to use on deployed machine
* **fixedMAC** - MAC address to use on deployed machine
* **admingroupid** - reference to usergroup.id - user group containing users that should be able to control this reservation and have admin access to the machine
* **logingroupid** - reference to usergroup.id - user group containing users that should be only be able to log in to this machine (will see reservation, but only the Connect button)
* **monitored** - 1 to have this reservation monitored, 0 otherwise (unused)


### shibauth table
This table contains authentication information related to shibboleth logins.

* **id** - id of entry
* **userid** - reference to user.id - user entry associated with
* **ts** - date/time entry was inserted
* **sessid** - shib session id
* **data** - various shibboleth related data passed in from httpd


### sitemaintenance table
This table contains an entry for any active or upcoming scheduled site maintenance windows.

* **id** - id of entry
* **start** - date/time for start of maintenance window
* **end** - date/time for end of maintenance window
* **ownerid** - reference to user.id - owner of this entry
* **created** - date/time entry created
* **reason** - info about why maintenance is scheduled
* **usermessage** - message that will be displayed to users about the maintenance
* **informhoursahead** - hours before the start time that a warning should be displayed on the VCL site about upcoming maintenance
* **allowreservations** - 1 to allow reservations to be scheduled ahead of time that overlap with the window, 0 to keep overlapping future reservations from being scheduled

### state table
This table contains all of the states used in VCL.  Not all states are used any place where states are used.  For example, there are states used in the request table that are not used in the computer table.

* **id** - id of entry
* **name** - name of entry


### statgraphcache table
This table contains cached values for the stat graphs.  Some of the data points take enough computation time that it is prohibitive to calculate them for really long periods of time.  This table allows historical points to computed once and then saved forever.

* **graphtype** - totalres, concurres, concurblade, or concurvm - type of graph for this entry
* **statdate** - date for this entry
* **affiliationid** - reference to affiliation.id; affiliation for this entry or NULL
* **value** - data point value for this entry
* **provisioningid** - reference to provisioning.id; provisioning id for this entry or NULL


### subimages table
This table contains a list of sub images associated with any clusters.

* **imagemetaid** - reference to imagemeta.id
* **imageid** - reference to image.id - subimage associated with imagemetaid


### sublog table
This table contains an entry for each computer that was part of a log table entry.  For normal reservations, this is a single entry; for cluster reservations, it is one entry for each subimage.

* **id** - id of entry
* **logid** - reference to log.id - corresponding entry in log table
* **imageid** - reference to image.id - image deployed for this reservation
* **imagerevisionid** - reference to imagerevision.id - image revision deployed for this reservation
* **computerid** - reference to computer.id - computer deployed for this reservation
* **IPaddress** - IP address of computer during this deploy
* **managementnodeid** - reference to managementnode.id - management node that handled this deploy
* **predictivemoduleid** - reference to module.id - prediction module used to load image when this reservation finished ??
* **hostcomputerid** - reference to computer.id - for VMs, this was the host the VM was deployed to
* **blockRequestid** - reference to blockRequest.id (if reservation was part of a block allocation)
* **blockStart** - start time of blockTime (if reservation was part of a block allocation)
* **blockEnd** - end time of blockTime (if reservation was part of a block allocation)


### user table
This table contains an entry for every user that has every logged in to VCL.

* **id** - id of entry
* **uid** - numeric id of user for accounts on deployed reservations
* **unityid** - normal user id for user
* **affiliationid** - reference to affiliation.id - affiliation of user
* **firstname** - first name of user
* **lastname** - last name of user
* **preferredname** - preferred name of user
* **email** - email address of user
* **emailnotices** - 1 to get email notices, 0 otherwise
* **IMtypeid** - reference to IMtype.id - type of IM address in IMid
* **IMid** - IM account for user
* **adminlevelid** - reference to adminlevel.id - deprecated
* **width** - screen width for RDP files
* **height** - screen height for RDP files
* **bpp** - color depth for RDP files
* **audiomode** - audio mode for RDP files
* **mapdrives** - drive mapping status for RDP files
* **mapprinters** - printer mapping status for RDP files
* **mapserial** - serial mapping status for RDP files
* **showallgroups** - 1 to show user groups from all affiliations where user groups can be selected, 0 to only show user groups matching user's affiliation
* **lastupdated** - date/time user's info was last updated
* **validated** - 0 or 1; if shibboleth authentication is configured and ALLOWADDSHIBUSERS is set to 1 in conf.php, users can be added to the site (i.e. adding to a user group) without validating that the entered user name is valid, in which case this would be set to 0 until the user actually logs in, at which point it is updated to 1; always 1 for other types of authentication
* **usepublickeys** - 0 or 1; whether or not user wants to use public key authentication for linux reservations
* **sshpublickeys** - data to be put in ~/.ssh/authorized_keys within linux reservations if usepublickeys is set to 1


### usergroup table
This table contains all of the user groups.

* **id** - id of entry
* **name** - name of entry
* **affiliationid** - reference to affiliation.id - affiliation of user group
* **ownerid** - reference to user.id - owner of user group
* **editusergroupid** - reference to usergroup.id - user group that can edit membership of this one
* **custom** - 1 for groups created on user groups page, 0 otherwise
* **courseroll** - 1 for user group created by courseroll scripts, 0 otherwise
* **initialmaxtime** - max time allowed for initial reservation creation for user group
* **totalmaxtime** - total time allowed for reservations created by users in this group
* **maxextendtime** - max time allowed per extension for users in this group
* **overlapResCount** - number of allowed overlapping reservations for users in this group (note that 1 is invalid as it doesn't make sense)

### usergroupmembers table
This table tracks which users are members of which user groups.

* **userid** - reference to user.id
* **usergroupid** - reference to usergroup.id


### usergrouppriv table
This table is a list of which additional user group privileges have been assigned to which user groups.

* **usergroupid** - reference to usergroup.id
* **userprivtypeid** - reference to usergroupprivtype.id - it probably should have been named usergroupprivtypeid


### usergroupprivtype table
This table contains additional privileges that can be associated with user groups that don't make sense to have at any particular privilege node.

* **id** - id of entry
* **name** - name of entry
* **help** - explaination of privilege type


### userpriv table
This table contains the user and user group privileges assigned in the privilege tree.

* **id** - id of entry
* **userid** - reference to user.id
* **usergroupid** - reference to usergroup.id
* **privnodeid** - reference to privnode.id - node where user privilege being granted
* **userprivtypeid** - reference to userprivtype.id - user privilege being granted


### userprivtype table
This table contains all of the available user privileges.

* **id** - id of entry
* **name** - name of entry


### variable table
This table is a place to store any generic data.  It can be settings that stay around forever, or things that only need to be temporarily stored.  It also provides for a place for the frontend and backend to share less structured information that what is in other tables.

* **id** - id of entry
* **name** - name of entry
* **serialization** - serialization method used for storing data
* **value** - data stored
* **setby** - what set the entry - perl module, web code, etc
* **timestamp** - date/time entry set


### vmhost table

This table contains an entry for each virtual host.

* **id** - id of entry
* **computerid** - reference to computer.id - physical machine entry refers to
* **vmlimit** - max number of VMs that can be on this host
* **vmprofileid** - reference to vmprofile.id - profile being used on this host


### vmprofile table
This table contains an entry for each virtual host profile.

* **id** - id of entry
* **profilename** - name of the profile
* **imageid** - reference to image.id - image deployed on host
* **resourcepath** - only used with vCenter, location where VMs will be created in the vCenter inventory tree
* **folderpath** - only used with vCenter, location where VMs will reside according to the vSphere Client's 'VMs and Templates' inventory view
* **repositorypath** - path where master copies of images are stored which are used to transfer images to VM host datastores or to other repositories
* **repositoryimagetypeid** - virtual disk type of the images stored in the repository
* **datastorepath** - location where master copies of images are stored which are used by running VMs
* **datastoreimagetypeid** - virtual disk type of the images stored in the datastore
* **vmpath** - path on VM host where VM working directories will reside
* **virtualswitch0** - name of virtual switch0
* **virtualswitch1** - name of virtual switch1
* **virtualswitch2** - name of virtual switch2
* **virtualswitch3** - name of virtual switch3
* **vmdisk** - whether the Virtual Disk Path storage is dedicated to a single host or shared among multiple hosts
* **username** - name of the administrative or root user residing on the VM host
* **password** - password of the administrative or root user residing on the VM host
* **eth0generated** - 0 or 1, whether the mac address for eth0 should be generated by the hypervisor or not
* **eth1generated** - 0 or 1, whether the mac address for eth1 should be generated by the hypervisor or not
* **rsapub** - public key used to encrypt password for VM host and store it in encryptedpasswd
* **rsakey** - path to private key on management nodes that is used to decrypt password for VM host
* **encryptedpasswd** - encrypted password of the administrative or root user residing on the VM host, if encrypted, the "password" field will be NULL

### vmtype table
This table contains all of the virtual machine types.

* **id** - id of entry
* **name** - name of entry


### winKMS table
This table contains Windows KMS licensing information.

* **affiliationid** - reference to affiliation.id
* **address** - IP address of KMS server
* **port** - port KMS server is listening on


### winProductKey table
This table contains Windows product key information.

* **affiliationid** - reference to affiliation.id
* **productname** - ??
* **productkey** - ??


### xmlrpcLog table
This table logs each XML RPC API call.

* **xmlrpcKeyid** - reference to user.id - user that made API call (originally, every user got their own key, and this was a reference to another table)
* **timestamp** - date/time API call was made
* **IPaddress** - IP address from which API call was made
* **method** - function called through API
* **apiversion** - API version used
* **comments** - serialization of arguments passed to API method