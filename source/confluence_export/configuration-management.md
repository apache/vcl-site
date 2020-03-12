---
title: Configuration Management
---

This page describes a new configuration system that will be added to VCL
that  can be used to dynamically configure deployed systems.

<a name="ConfigurationManagement-DatabaseSchema"></a>
## Database Schema

!config_schema.jpg|thumbnail,border=1!
config:
* id - id of record
* name - name of record
* ownerid - owner of this record (reference to user.id)
* configtypeid - type of record (reference to configtype.id)
* data - any data associated with this (ex. puppet manifest)
* optional - 0/1 - when this config is mapped to something, can the user 
specify to apply it or not

configtype:
* id - id of record
* name - name of record
* moduleid - id of module that handles this type of record (reference to 
module.id)initial types: puppet, subimage, shellcommand, perlfunction, 
software
configvariable:
* id - id of record
* name - name of record
* configid - config this is associated with (reference to config.id)
* value - default value of this variable
* required - 0/1 - when mapped to something, is this variable always 
applied
* ask - 0/1 - will the user be prompted for a value for this variable, or
will  the default value always be used
* key - string in config.data to replace with the value of this variable
* datatype - enum(int, multiint, string) - type of this variable so that
the  frontend knows how to validate it
  
  
There are some initial, special names:
** subimage - used for clusters, specifies a subimage to be deployed; when 
deployed, configinstancevariable.value will be reservation.id of the 
subimage
** min - used in conjunction with subimage to specify a minimum number of
those  subimages
** max - used in conjunction with subimage to specify a maximum number of
those  subimages
** runbefore - used to relate to other configs to specify that this should
be  run before the ones specified in 'value'
** runafter - used to relate to other configs to specify that this should
be  run after the ones specified in 'value'
** getdata - ??

configinstance:This is similar to the config table, but is for deployed 
systems.\* id - id of record
* reservationid - reservation this is associated with (references 
reservation.id)
* configid - config entry being applied (references config.id)
* status - new/processing/completed??

configinstancevariable:This is similar to the configvariable table, but is
for deployed  systems.\* configinstanceid - config instance this is
associated with (references  configinstance.id)
* configvariableid - config variable being applied (references 
configvariable.id)
* value - similar to configvariable.value, but can be set by user to
different  value if configvariable.ask is set to 1

configmap:This is for mapping configs to various resources or other items
in  VCL.\* configid - config being mapped (references config.id)
* subid - id from specific resource table (ex. image.id)
* configmaptypeid - type of resource or other item in VCL this is mapped to
 (references configmaptype.id)
* affiliationid - allows configs to only be mapped for a specific
affiliation,  use the Global affilation to map to all (references
affiliation.id)
* disabled - 0/1 (a little complicated, normally 0) allows exceptions to a 
config being applied; set to 1 if a config would be mapped due to a general
 mapping, but want to disable for a specific instance (ex. if a config is
applied  for everything deployed by a certain provisioning module, but you
don't want it  applied for a certain image, you would have an entry in this
table mapping it to  the provisioning module with disabled set to 0, then
you would also have an	entry for the image with disabled set to 1)
* stage - start_load/post_load/(others?) which stage in the provisioning 
process where this record should be applied

configmaptype:
* id - id of this record
* name - name of this record
  
  
Initial types:
** image
** OStype
** provisioning

<a name="ConfigurationManagement-Examples"></a>
## Examples


<a name="ConfigurationManagement-AssigningaVLANtoanimage"></a>
### Assigning a VLAN to an image

This example shows how to assign a VLAN to an image.

For this example, we'll use the following values from other tables:
* module.id for handling VLAN config type: 67
* image.id for the image in this example: 524
* affiliation.id for the desired affiliation: 6
* reservation.id for the image: 2748
* user.id that owns the configs: 54

configtype:
<table>
<tr><th> id </th><th> name </th><th> moduleid </th></tr>
<tr><td> 5 </td><td> VLAN </td><td> 67 </td></tr>
config:
<tr><th> id </th><th> name </th><th> ownerid </th><th> configtypeid </th><th> data </th><th> optional </th></tr>
<tr><td> 77 </td><td> VLAN 30 </td><td> 54 </td><td> 5 </td><td> 30 </td><td> 0 </td></tr>
configvariable:
<tr><th> id </th><th> name </th><th> configid </th><th> value </th><th> required </th><th> ask </th><th> key </th><th> datatype </th></tr>
<tr><td> 486 </td><td> VLAN </td><td> 77 </td><td> 30 </td><td> 1 </td><td> 0 </td><td> (empty) </td><td> int </td></tr>
configmaptype:
<tr><th> id </th><th> name </th></tr>
<tr><td> 1 </td><td> image </td></tr>
configmap:
<tr><th> configid </th><th> subid </th><th> configmaptypeid </th><th> affiliationid </th><th> disabled </th><th>
stage </th></tr>
<tr><td> 77 </td><td> 524 </td><td> 1 </td><td> 6 </td><td> 0 </td><td> post_load </td></tr>
configinstance:
<tr><th> id </th><th> reservationid </th><th> configid </th><th> status </th></tr>
<tr><td> 6854 </td><td> 2748 </td><td> 77 </td><td> new </td></tr>
configinstancevariable:
<tr><th> configinstanceid </th><th> configvariableid </th><th> value </th></tr>
<tr><td> 6854 </td><td> 486 </td><td> 30 </td></tr>
</table>

<a name="ConfigurationManagement-Hadoopclusterwithvariableamountofslavenodes"></a>
### Hadoop cluster with variable amount of slave nodes

This example shows how a hadoop cluster can be requested with 5-10 slave 
nodes. It can be useful to have the variable amount because 10 nodes may be
 desired, but you may want to cluster anyway if only 5 nodes are available
or if  10 are requested, but 2 of them fail at deploy time.

For this example, we'll use the following values from other tables:
* module.id for handling subimage config type: 58
* image.id for the Hadoop master image: 453
* image.id for the Hadoop slave image: 454
* affiliation.id for the desired affiliation: 5
* reservation.id for the Hadoop master image: 2351
* reservation.id for the Hadoop slave images: 2352-2361
* user.id that owns the configs: 9

configtype:
<table>
<tr><th> id </th><th> name </th><th> moduleid </th></tr>
<tr><td> 2 </td><td> subimage </td><td> 58 </td></tr>
config:
<tr><th> id </th><th> name </th><th> ownerid </th><th> configtypeid </th><th> data </th><th> optional </th></tr>
<tr><td> 59 </td><td> hadoop cluster </td><td> 9 </td><td> 2 </td><td> (empty) </td><td> 0 </td></tr>
configvariable:
<tr><th> id </th><th> name </th><th> configid </th><th> value </th><th> required </th><th> ask </th><th> key </th><th> datatype </th></tr>
<tr><td> 146 </td><td> subimage </td><td> 59 </td><td> 454 </td><td> 1 </td><td> 0 </td><td> (empty) </td><td> int </td></tr>
<tr><td> 147 </td><td> min </td><td> 59 </td><td> 1 </td><td> 1 </td><td> 1 </td><td> (empty) </td><td> int </td></tr>
<tr><td> 148 </td><td> max </td><td> 59 </td><td> 50 </td><td> 1 </td><td> 1 </td><td> (empty) </td><td> int </td></tr>
configmaptype:
<tr><th> id </th><th> name </th></tr>
<tr><td> 1 </td><td> image </td></tr>
configmap:
<tr><th> configid </th><th> subid </th><th> configmaptypeid </th><th> affiliationid </th><th> disabled </th><th>
stage </th></tr>
<tr><td> 59 </td><td> 453 </td><td> 1 </td><td> 5 </td><td> 0 </td><td> start_load </td></tr>
configinstance:
<tr><th> id </th><th> reservationid </th><th> configid </th><th> status </th></tr>
<tr><td> 5023 </td><td> 2351 </td><td> 59 </td><td> new </td></tr>
configinstancevariable:
<tr><th> configinstanceid </th><th> configvariableid </th><th> value </th></tr>
<tr><td> 5023 </td><td> 146 </td><td> 2352 </td></tr>
<tr><td> 5023 </td><td> 146 </td><td> 2353 </td></tr>
<tr><td> 5023 </td><td> 146 </td><td> 2354 </td></tr>
<tr><td> 5023 </td><td> 146 </td><td> 2355 </td></tr>
<tr><td> 5023 </td><td> 146 </td><td> 2356 </td></tr>
<tr><td> 5023 </td><td> 146 </td><td> 2357 </td></tr>
<tr><td> 5023 </td><td> 146 </td><td> 2358 </td></tr>
<tr><td> 5023 </td><td> 146 </td><td> 2359 </td></tr>
<tr><td> 5023 </td><td> 146 </td><td> 2360 </td></tr>
<tr><td> 5023 </td><td> 146 </td><td> 2361 </td></tr>
<tr><td> 5023 </td><td> 147 </td><td> 5 </td></tr>
<tr><td> 5023 </td><td> 148 </td><td> 10 </td></tr>
</table>

<a name="ConfigurationManagement-SAScluster"></a>
### SAS cluster

This example shows how to configure a SAS cluster of 3 nodes: meta,
midtier,  and apps so that they are all deployed and then started in the
correct  order.

For this example, we'll use the following values from other tables:
* module.id for handling puppet config type: 57
* module.id for handling subimage config type: 58
* module.id for handling shellcommand config type: 59
* image.id for the SAS meta image: 728
* image.id for the SAS midtier image: 729
* image.id for the SAS apps image: 730
* affiliation.id for the desired affiliation: 7
* reservation.id for the SAS meta image: 2466
* reservation.id for the SAS midtier image: 2467
* reservation.id for the SAS apps image: 2468
* user.id that owns the configs: 15

configtype:
<table>
<tr><th> id </th><th> name </th><th> moduleid </th></tr>
<tr><td> 1 </td><td> puppet </td><td> 57 </td></tr>
<tr><td> 2 </td><td> subimage </td><td> 58 </td></tr>
<tr><td> 3 </td><td> shellcommand </td><td> 59 </td></tr>
config:
<tr><th> id </th><th> name </th><th> ownerid </th><th> configtypeid </th><th> data </th><th> optional </th></tr>
<tr><td> 76 </td><td> SAS apps </td><td> 15 </td><td> 2 </td><td> (empty) </td><td> 0 </td></tr>
<tr><td> 77 </td><td> SAS midtier </td><td> 15 </td><td> 2 </td><td> (empty) </td><td> 0 </td></tr>
<tr><td> 78 </td><td> SAS meta config </td><td> 15 </td><td> 1 </td><td> (puppet manifest) </td><td> 0 </td></tr>
<tr><td> 79 </td><td> SAS apps config </td><td> 15 </td><td> 1 </td><td> (puppet manifest) </td><td> 0 </td></tr>
<tr><td> 80 </td><td> SAS midtier config </td><td> 15 </td><td> 1 </td><td> (puppet manifest) </td><td> 0 </td></tr>
<tr><td> 81 </td><td> SAS meta start </td><td> 15 </td><td> 3 </td><td> (startup commands) </td><td> 0 </td></tr>
<tr><td> 82 </td><td> SAS apps start </td><td> 15 </td><td> 3 </td><td> (startup commands) </td><td> 0 </td></tr>
<tr><td> 83 </td><td> SAS midtier start </td><td> 15 </td><td> 3 </td><td> (startup commands) </td><td> 0 </td></tr>
configvariable:
<tr><th> id </th><th> name </th><th> configid </th><th> value </th><th> required </th><th> ask </th><th> key </th><th> datatype </th></tr>
<tr><td> 268 </td><td> subimage </td><td> 76 </td><td> 729 </td><td> 1 </td><td> 0 </td><td> (empty) </td><td> int </td></tr>
<tr><td> 269 </td><td> subimage </td><td> 77 </td><td> 730 </td><td> 1 </td><td> 0 </td><td> (empty) </td><td> int </td></tr>
<tr><td> 270 </td><td> runafter </td><td> 78 </td><td> 268,269 </td><td> 1 </td><td> 0 </td><td> (empty) </td><td> int </td></tr>
<tr><td> 271 </td><td> runafter </td><td> 79 </td><td> 270 </td><td> 1 </td><td> 0 </td><td> (empty) </td><td> int </td></tr>
<tr><td> 272 </td><td> runafter </td><td> 80 </td><td> 271 </td><td> 1 </td><td> 0 </td><td> (empty) </td><td> int </td></tr>
<tr><td> 273 </td><td> runafter </td><td> 81 </td><td> 272 </td><td> 1 </td><td> 0 </td><td> (empty) </td><td> int </td></tr>
<tr><td> 274 </td><td> runafter </td><td> 82 </td><td> 273 </td><td> 1 </td><td> 0 </td><td> (empty) </td><td> int </td></tr>
<tr><td> 275 </td><td> runafter </td><td> 83 </td><td> 274 </td><td> 1 </td><td> 0 </td><td> (empty) </td><td> int </td></tr>
configmaptype:
<tr><th> id </th><th> name </th></tr>
<tr><td> 1 </td><td> image </td></tr>
configmap:
<tr><th> configid </th><th> subid </th><th> configmaptypeid </th><th> affiliationid </th><th> disabled </th><th>
stage </th></tr>
<tr><td> 76 </td><td> 728 </td><td> 1 </td><td> 7 </td><td> 0 </td><td> start_load </td></tr>
<tr><td> 77 </td><td> 728 </td><td> 1 </td><td> 7 </td><td> 0 </td><td> start_load </td></tr>
<tr><td> 78 </td><td> 728 </td><td> 1 </td><td> 7 </td><td> 0 </td><td> post_load </td></tr>
<tr><td> 79 </td><td> 728 </td><td> 1 </td><td> 7 </td><td> 0 </td><td> post_load </td></tr>
<tr><td> 80 </td><td> 728 </td><td> 1 </td><td> 7 </td><td> 0 </td><td> post_load </td></tr>
<tr><td> 81 </td><td> 728 </td><td> 1 </td><td> 7 </td><td> 0 </td><td> post_load </td></tr>
<tr><td> 82 </td><td> 728 </td><td> 1 </td><td> 7 </td><td> 0 </td><td> post_load </td></tr>
<tr><td> 83 </td><td> 728 </td><td> 1 </td><td> 7 </td><td> 0 </td><td> post_load </td></tr>
configinstance:
<tr><th> id </th><th> reservationid </th><th> configid </th><th> status </th></tr>
<tr><td> 6005 </td><td> 2466 </td><td> 76 </td><td> new </td></tr>
<tr><td> 6006 </td><td> 2466 </td><td> 77 </td><td> new </td></tr>
<tr><td> 6007 </td><td> 2466 </td><td> 78 </td><td> new </td></tr>
<tr><td> 6008 </td><td> 2466 </td><td> 79 </td><td> new </td></tr>
<tr><td> 6009 </td><td> 2466 </td><td> 80 </td><td> new </td></tr>
<tr><td> 6010 </td><td> 2466 </td><td> 81 </td><td> new </td></tr>
<tr><td> 6011 </td><td> 2466 </td><td> 82 </td><td> new </td></tr>
<tr><td> 6012 </td><td> 2466 </td><td> 83 </td><td> new </td></tr>
configinstancevariable:
<tr><th> configinstanceid </th><th> configvariableid </th><th> value </th></tr>
<tr><td> 6005 </td><td> 268 </td><td> 2467 </td></tr>
<tr><td> 6006 </td><td> 269 </td><td> 2468 </td></tr>
<tr><td> 6007 </td><td> 270 </td><td> 6005,6006 </td></tr>
<tr><td> 6008 </td><td> 271 </td><td> 6007 </td></tr>
<tr><td> 6009 </td><td> 272 </td><td> 6008 </td></tr>
<tr><td> 6010 </td><td> 273 </td><td> 6009 </td></tr>
<tr><td> 6011 </td><td> 274 </td><td> 6010 </td></tr>
<tr><td> 6012 </td><td> 275 </td><td> 6011 </td></tr>
