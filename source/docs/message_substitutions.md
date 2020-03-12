---
title: Site Configuration Message Substitutions
---

# Message Substitutions

Messages sent to users and admins can be configured via the VCL web 
site under Site Configuration as of version 2.5. There are many 
variables that can be substituted into the messages by the backend 
before a message is sent to a user. Variables are included in 
square brackets ( [ ] ). For example:

    Your reservation for [image_name] is now available.

The list of variables that can be substituted is quite large. So, 
listing all of them out results in a list that can easily become 
difficult to maintain and quickly out of date. The best place to 
look for a list of variables that could be used is in the 
[Datastructure.pm][1] module of the backend code in the 
$SUBROUTINE_MAPPINGS hash (though, not all of those make sense in 
some of the messages and may not be available).

After saving a message, the backend will analyze it for any invalid
variables. If any are found, a notice will be displayed about which
messages have invalid variables, and which variables are invalid.

As of VCL 2.5, here is the list of variables included in the default
set of messages:

<pre>
[IMAGE_CAPTURE_TYPE]
[IMAGE_SIZE_OLD]
[NOTICE_INTERVAL]
[PID]
[computer_id]
[computer_provisioning_module_perl_package]
[computer_provisioning_name]
[computer_provisioning_pretty_name]
[computer_short_name]
[image_id]
[image_name]
[image_os_module_perl_package]
[image_prettyname]
[image_size]
[imagemeta_sysprep]
[imagerevision_id]
[imagerevision_revision]
[management_node_short_name]
[request_id]
[reservation_id]
[user_affiliation_helpaddress]
[user_affiliation_name]
[user_affiliation_sitewwwaddress]
[user_firstname]
[user_id]
[user_lastname]
[user_login_id]
[vmhost_computer_id]
[vmhost_id]
[vmhost_profile_id]
[vmhost_profile_name]
[vmhost_short_name]
</pre>

  [1]: http://svn.apache.org/viewvc/vcl/trunk/managementnode/lib/VCL/DataStructure.pm?view=markup