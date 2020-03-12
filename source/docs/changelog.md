---
title: Apache VCL Change Log
---

## 2.5.1 Changes {#2.5.1}

###        Bug

* [<a href='https://issues.apache.org/jira/browse/VCL-1079'>VCL-1079</a>] -         Virtual Hosts page references Computer Utilities
* [<a href='https://issues.apache.org/jira/browse/VCL-1080'>VCL-1080</a>] -         Wrong port can be delivered in RDP file
* [<a href='https://issues.apache.org/jira/browse/VCL-1081'>VCL-1081</a>] -         UID conflict for admin user
* [<a href='https://issues.apache.org/jira/browse/VCL-1082'>VCL-1082</a>] -         monitor_vcld.pl throws incorrect lastcheckin time exception after Daylight Savings Time Roles Back
* [<a href='https://issues.apache.org/jira/browse/VCL-1083'>VCL-1083</a>] -         Data in shares mounted under Linux home directories may be deleted
* [<a href='https://issues.apache.org/jira/browse/VCL-1093'>VCL-1093</a>] -         vSphere_SDK.pm:vm_unregister - failed to unregister VM:
* [<a href='https://issues.apache.org/jira/browse/VCL-1100'>VCL-1100</a>] -         block allocation usage graph does not work correctly for allocations with a single time slot
* [<a href='https://issues.apache.org/jira/browse/VCL-1103'>VCL-1103</a>] -         change vcldsemaphore.pid from smallint to mediumint
* [<a href='https://issues.apache.org/jira/browse/VCL-1105'>VCL-1105</a>] -         Shibboleth authentication broken due to bug in getCryptKeyID
* [<a href='https://issues.apache.org/jira/browse/VCL-1111'>VCL-1111</a>] -         statgraphcache table not correctly being used
* [<a href='https://issues.apache.org/jira/browse/VCL-1113'>VCL-1113</a>] -         image capture for Windows system configured as domain controller fails
* [<a href='https://issues.apache.org/jira/browse/VCL-1116'>VCL-1116</a>] -         use database hostnames for ad joined computers
* [<a href='https://issues.apache.org/jira/browse/VCL-1117'>VCL-1117</a>] -         vcld fails to set fixed IP address for Linux server reservations if management node not set to static
* [<a href='https://issues.apache.org/jira/browse/VCL-1119'>VCL-1119</a>] -         wrong day submitted for future reservations made in the evening
* [<a href='https://issues.apache.org/jira/browse/VCL-1120'>VCL-1120</a>] -         image conversion from vmdk to qcow2 always done twice

###        New Feature

* [<a href='https://issues.apache.org/jira/browse/VCL-1112'>VCL-1112</a>] -         SSL Offload

###        Improvement

* [<a href='https://issues.apache.org/jira/browse/VCL-1041'>VCL-1041</a>] -         Customer facing email notifications are ugly
* [<a href='https://issues.apache.org/jira/browse/VCL-1084'>VCL-1084</a>] -         set cache mode for libvirt VMs
* [<a href='https://issues.apache.org/jira/browse/VCL-1085'>VCL-1085</a>] -         Configuring VCL Website to use custom port
* [<a href='https://issues.apache.org/jira/browse/VCL-1089'>VCL-1089</a>] -         Change ping module to use Net::Ping::External
* [<a href='https://issues.apache.org/jira/browse/VCL-1092'>VCL-1092</a>] -         Change installation script to install these RPM Perl Modules
* [<a href='https://issues.apache.org/jira/browse/VCL-1094'>VCL-1094</a>] -         add .\ to windows user login to prevent automatic use of Microsoft accounts
* [<a href='https://issues.apache.org/jira/browse/VCL-1095'>VCL-1095</a>] -         Move unjoining of Windows VMs from Active Directory to earlier in the deprovision process
* [<a href='https://issues.apache.org/jira/browse/VCL-1096'>VCL-1096</a>] -         Add ability to automatically mount NFS shares under Windows
* [<a href='https://issues.apache.org/jira/browse/VCL-1101'>VCL-1101</a>] -         Change chmod mode from string to octal number value
* [<a href='https://issues.apache.org/jira/browse/VCL-1104'>VCL-1104</a>] -         set cpu topology for libvirt VMs
* [<a href='https://issues.apache.org/jira/browse/VCL-1106'>VCL-1106</a>] -         make PHP code compatible with PHP 7
* [<a href='https://issues.apache.org/jira/browse/VCL-1109'>VCL-1109</a>] -         date duplicated on statistic graph labels for day after daylight saving time rolls back
* [<a href='https://issues.apache.org/jira/browse/VCL-1110'>VCL-1110</a>] -         expose maxinitial time for images in web UI
* [<a href='https://issues.apache.org/jira/browse/VCL-1114'>VCL-1114</a>] -         miscellaneous small web updates

###        Task

* [<a href='https://issues.apache.org/jira/browse/VCL-1097'>VCL-1097</a>] -         add hidden files to empty directories to force them to be included in Git repo

## 2.5 Changes {#2.5}

###        New Feature

* [<a href='https://issues.apache.org/jira/browse/VCL-253'>VCL-253</a>] -         Allow users to specify RDP port
* [<a href='https://issues.apache.org/jira/browse/VCL-277'>VCL-277</a>] -         Add support for images to join Active Directory domains
* [<a href='https://issues.apache.org/jira/browse/VCL-867'>VCL-867</a>] -         Active Directory Authentication for Windows VM&#39;s
* [<a href='https://issues.apache.org/jira/browse/VCL-889'>VCL-889</a>] -         Add vcl_post_load script support for Windows images
* [<a href='https://issues.apache.org/jira/browse/VCL-893'>VCL-893</a>] -         Add support for Windows 10 images
* [<a href='https://issues.apache.org/jira/browse/VCL-915'>VCL-915</a>] -         Add ability to automatically mount NFS share when user logs in
* [<a href='https://issues.apache.org/jira/browse/VCL-919'>VCL-919</a>] -         Allow customization of notification messages sent to users
* [<a href='https://issues.apache.org/jira/browse/VCL-971'>VCL-971</a>] -         Add support for Ubuntu&#39;s ufw firewall
* [<a href='https://issues.apache.org/jira/browse/VCL-972'>VCL-972</a>] -         Add support for firewalld
* [<a href='https://issues.apache.org/jira/browse/VCL-1000'>VCL-1000</a>] -         Run custom scripts at various stages on the management node
* [<a href='https://issues.apache.org/jira/browse/VCL-1010'>VCL-1010</a>] -         Support for Windows 10 and Windows Server 2016 images

###        Improvement

* [<a href='https://issues.apache.org/jira/browse/VCL-796'>VCL-796</a>] -         Prohibit tomainteance reservations from being created at end of indefinite server reservations
* [<a href='https://issues.apache.org/jira/browse/VCL-807'>VCL-807</a>] -         indicate timezone on schedules / reservations
* [<a href='https://issues.apache.org/jira/browse/VCL-808'>VCL-808</a>] -         vcld allows user values that contain HTML which is not cleaned on web interface
* [<a href='https://issues.apache.org/jira/browse/VCL-833'>VCL-833</a>] -         Improve consistency and grammar of website
* [<a href='https://issues.apache.org/jira/browse/VCL-843'>VCL-843</a>] -         Remove &quot;VM limit&quot;
* [<a href='https://issues.apache.org/jira/browse/VCL-851'>VCL-851</a>] -         Prevent warning in vcld.log if vSphere SDK is not installed
* [<a href='https://issues.apache.org/jira/browse/VCL-853'>VCL-853</a>] -         Reservations fail if vSphere SDK is used, host contains a resource pool and resource path is not configured in VM profile
* [<a href='https://issues.apache.org/jira/browse/VCL-860'>VCL-860</a>] -         Linux.pm&#39;s create_user silently fails if vcl group does not exist
* [<a href='https://issues.apache.org/jira/browse/VCL-862'>VCL-862</a>] -         Tag loaded image when request is reserved, inuse, or modified in any way other than a normal reload
* [<a href='https://issues.apache.org/jira/browse/VCL-865'>VCL-865</a>] -         Remove all calls to defined(@array)
* [<a href='https://issues.apache.org/jira/browse/VCL-879'>VCL-879</a>] -         Add semaphore to iptables commands
* [<a href='https://issues.apache.org/jira/browse/VCL-882'>VCL-882</a>] -         Add Portuguese translation to web UI
* [<a href='https://issues.apache.org/jira/browse/VCL-887'>VCL-887</a>] -         Clean up backend code
* [<a href='https://issues.apache.org/jira/browse/VCL-890'>VCL-890</a>] -         Add button to reload table contents on Edit Computer Profile page
* [<a href='https://issues.apache.org/jira/browse/VCL-894'>VCL-894</a>] -         Add reservation history and current reservation information to Computer Profiles page
* [<a href='https://issues.apache.org/jira/browse/VCL-896'>VCL-896</a>] -         Improve method to set Linux hostname
* [<a href='https://issues.apache.org/jira/browse/VCL-897'>VCL-897</a>] -         Simplify arguments accepted by grant_root_access subroutines
* [<a href='https://issues.apache.org/jira/browse/VCL-899'>VCL-899</a>] -         Add request ID and management node to reservation history on User Lookup page
* [<a href='https://issues.apache.org/jira/browse/VCL-905'>VCL-905</a>] -         VMware code should ignore files under .snapshot directories
* [<a href='https://issues.apache.org/jira/browse/VCL-906'>VCL-906</a>] -         VMware code fails to delete dedicated virtual disk directory for server reservations
* [<a href='https://issues.apache.org/jira/browse/VCL-907'>VCL-907</a>] -         reload reservations page content soonish after Connect is clicked when reservation is in reserved state
* [<a href='https://issues.apache.org/jira/browse/VCL-910'>VCL-910</a>] -         Improvements to vcld -setup&#39;s VMware datastore cleanup functions
* [<a href='https://issues.apache.org/jira/browse/VCL-911'>VCL-911</a>] -         Ensure qcow2 images are saved in backwards compatible format
* [<a href='https://issues.apache.org/jira/browse/VCL-920'>VCL-920</a>] -         Increase timeout in KVM.pm&#39;s copy_virtual_disk subroutine
* [<a href='https://issues.apache.org/jira/browse/VCL-923'>VCL-923</a>] -         Rework monitor_vcld.pl script to allow it to work with newer init daemons
* [<a href='https://issues.apache.org/jira/browse/VCL-930'>VCL-930</a>] -         Update phpmyadmin.sql to use double-underscores in pma__table_info table
* [<a href='https://issues.apache.org/jira/browse/VCL-934'>VCL-934</a>] -         Warnings generated in vcld.log for server requests because frontend isn&#39;t inserting &#39;initialconnecttimeout&#39; computerloadlog entry
* [<a href='https://issues.apache.org/jira/browse/VCL-935'>VCL-935</a>] -         modify layout of edit image dialog to distinguish what items are immediately changed
* [<a href='https://issues.apache.org/jira/browse/VCL-937'>VCL-937</a>] -         Increase max length of duration limited images from 45 days to 20 weeks
* [<a href='https://issues.apache.org/jira/browse/VCL-938'>VCL-938</a>] -         Add a count of computers listed in the table on the Edit Computer Profiles page
* [<a href='https://issues.apache.org/jira/browse/VCL-946'>VCL-946</a>] -         add image revision to manage computers page
* [<a href='https://issues.apache.org/jira/browse/VCL-947'>VCL-947</a>] -         for block allocation accept/reject emails change sender address from ENVELOPESENDER to HELPEMAIL
* [<a href='https://issues.apache.org/jira/browse/VCL-948'>VCL-948</a>] -         add admingroup and logingroup to reservation data displayed when looking up reservations on computers
* [<a href='https://issues.apache.org/jira/browse/VCL-949'>VCL-949</a>] -         userlookup page - add vmhost to reservation history; add list of reservations user has access to but doesn&#39;t own
* [<a href='https://issues.apache.org/jira/browse/VCL-950'>VCL-950</a>] -         use web notifications to alert when a reservation is ready
* [<a href='https://issues.apache.org/jira/browse/VCL-952'>VCL-952</a>] -         API modifications to allow interaction via &quot;VCL go&quot; iOS app
* [<a href='https://issues.apache.org/jira/browse/VCL-956'>VCL-956</a>] -         display reservation times in user&#39;s own timezone
* [<a href='https://issues.apache.org/jira/browse/VCL-957'>VCL-957</a>] -         Update Linux pre-capture tasks
* [<a href='https://issues.apache.org/jira/browse/VCL-958'>VCL-958</a>] -         Windows.pm sets currentimage.txt post_load status too early
* [<a href='https://issues.apache.org/jira/browse/VCL-961'>VCL-961</a>] -         VCL may clobber custom network configurations on Linux images
* [<a href='https://issues.apache.org/jira/browse/VCL-963'>VCL-963</a>] -         ManagementNode.pm::execute should be update to accept same hash reference argument as OS.pm::execute
* [<a href='https://issues.apache.org/jira/browse/VCL-964'>VCL-964</a>] -         Allow default &quot;from&quot; email address to be set if affiliation.helpaddress is NULL
* [<a href='https://issues.apache.org/jira/browse/VCL-965'>VCL-965</a>] -         util.pm::kill_child_processes is using outdated pgrep arguments
* [<a href='https://issues.apache.org/jira/browse/VCL-966'>VCL-966</a>] -         Ubuntu not detecting SysV-controlled services if chkconfig is not installed
* [<a href='https://issues.apache.org/jira/browse/VCL-967'>VCL-967</a>] -         Libvirt provisioning does not allow virtual network name to be specified in the VM host profile
* [<a href='https://issues.apache.org/jira/browse/VCL-969'>VCL-969</a>] -         Disable firstboot service for Linux images
* [<a href='https://issues.apache.org/jira/browse/VCL-976'>VCL-976</a>] -         user_password_length and user_password_spchar not in default schema
* [<a href='https://issues.apache.org/jira/browse/VCL-977'>VCL-977</a>] -         VMware may fail to register VM if existing invalid VM is registered
* [<a href='https://issues.apache.org/jira/browse/VCL-979'>VCL-979</a>] -         install script - prompt for timezine during installation
* [<a href='https://issues.apache.org/jira/browse/VCL-980'>VCL-980</a>] -         add KMS server configuration to Site Configuration page
* [<a href='https://issues.apache.org/jira/browse/VCL-981'>VCL-981</a>] -         Create a New Theme That Is More Responsive for Mobile Devices
* [<a href='https://issues.apache.org/jira/browse/VCL-984'>VCL-984</a>] -         Add support for vcld daemon controlled by systemd
* [<a href='https://issues.apache.org/jira/browse/VCL-987'>VCL-987</a>] -         Extend xCAT.pm to attempt to locate a suitable alternate Kickstart image repository directory
* [<a href='https://issues.apache.org/jira/browse/VCL-999'>VCL-999</a>] -         Rework UnixLab.pm
* [<a href='https://issues.apache.org/jira/browse/VCL-1005'>VCL-1005</a>] -         allow dashes in image names
* [<a href='https://issues.apache.org/jira/browse/VCL-1006'>VCL-1006</a>] -         Performance Improvements for 2.5
* [<a href='https://issues.apache.org/jira/browse/VCL-1008'>VCL-1008</a>] -         Extend libvirt/KVM modules to use device settings from captured VM
* [<a href='https://issues.apache.org/jira/browse/VCL-1009'>VCL-1009</a>] -         addition of es_CR translation
* [<a href='https://issues.apache.org/jira/browse/VCL-1013'>VCL-1013</a>] -         Modernize parts of Windows code
* [<a href='https://issues.apache.org/jira/browse/VCL-1021'>VCL-1021</a>] -         restrict deleting newimages and newvmimages computer groups
* [<a href='https://issues.apache.org/jira/browse/VCL-1025'>VCL-1025</a>] -         Update naming convention for VMware VMs
* [<a href='https://issues.apache.org/jira/browse/VCL-1026'>VCL-1026</a>] -         Improve VMware code&#39;s ability to select the proper guest OS
* [<a href='https://issues.apache.org/jira/browse/VCL-1027'>VCL-1027</a>] -         External SSH service under systemd fails to restart if several restarts are rapidly attempted
* [<a href='https://issues.apache.org/jira/browse/VCL-1029'>VCL-1029</a>] -         add a section for managing affiliations to Site Configuration
* [<a href='https://issues.apache.org/jira/browse/VCL-1030'>VCL-1030</a>] -         use sitewwwaddress from Global affiliation in user email messages if specific affiliation has a NULL value
* [<a href='https://issues.apache.org/jira/browse/VCL-1031'>VCL-1031</a>] -         Update iptables.pm to be used for all iptables configuration
* [<a href='https://issues.apache.org/jira/browse/VCL-1032'>VCL-1032</a>] -         VIM_SSH.pm::get_config_option_info very slow when using run_ssh_command
* [<a href='https://issues.apache.org/jira/browse/VCL-1033'>VCL-1033</a>] -         Add corrective attempts if Windows fails to respond or does not obtain a public IP address
* [<a href='https://issues.apache.org/jira/browse/VCL-1036'>VCL-1036</a>] -         Improve vcld.log output when transferring an image from another management node
* [<a href='https://issues.apache.org/jira/browse/VCL-1042'>VCL-1042</a>] -         add max reservation times to user lookup information
* [<a href='https://issues.apache.org/jira/browse/VCL-1045'>VCL-1045</a>] -         Method of encrypting sensitive database entries
* [<a href='https://issues.apache.org/jira/browse/VCL-1052'>VCL-1052</a>] -         Prevent captures from failing if VM disk mode is &#39;dedicated&#39; and the repository is not configured
* [<a href='https://issues.apache.org/jira/browse/VCL-1056'>VCL-1056</a>] -         Add checks/workarounds in iptables.pm if command fails because another process holds an xtables lock
* [<a href='https://issues.apache.org/jira/browse/VCL-1060'>VCL-1060</a>] -         VMware.pm generates warnings and critical message when checking for multiextent support under ESXi 6.5
* [<a href='https://issues.apache.org/jira/browse/VCL-1061'>VCL-1061</a>] -         Unnecessary warnings in vcld.log for Ubuntu 16 images when checking services
* [<a href='https://issues.apache.org/jira/browse/VCL-1062'>VCL-1062</a>] -         stop using Administrator account for Windows imaging reservations
* [<a href='https://issues.apache.org/jira/browse/VCL-1064'>VCL-1064</a>] -         Show reservations being captured or in maintenance on Reservations page
* [<a href='https://issues.apache.org/jira/browse/VCL-1069'>VCL-1069</a>] -         Allow Windows to update time regardless of skew
* [<a href='https://issues.apache.org/jira/browse/VCL-1072'>VCL-1072</a>] -         VMware may incorrectly indicate power on failed

###        Task

* [<a href='https://issues.apache.org/jira/browse/VCL-968'>VCL-968</a>] -         Localization updates for 2.5
* [<a href='https://issues.apache.org/jira/browse/VCL-1024'>VCL-1024</a>] -         comment out Server Profile code

###        Sub-task

* [<a href='https://issues.apache.org/jira/browse/VCL-898'>VCL-898</a>] -         Update schema to allow NULL request.logid
* [<a href='https://issues.apache.org/jira/browse/VCL-1065'>VCL-1065</a>] -         update_cygwin.cmd script does not work correctly if computer is joined to Active Directory

###        Bug


* [<a href='https://issues.apache.org/jira/browse/VCL-809'>VCL-809</a>] -         Information disclosure when accessing page you don&#39;t have access to
* [<a href='https://issues.apache.org/jira/browse/VCL-846'>VCL-846</a>] -         Improve flow of handling nodes for deleted reservations assigned to new reservations
* [<a href='https://issues.apache.org/jira/browse/VCL-861'>VCL-861</a>] -         Web timetable endless loop
* [<a href='https://issues.apache.org/jira/browse/VCL-864'>VCL-864</a>] -         selecting the first image id from the user&#39;s set of images can give an error when the user has no access to images
* [<a href='https://issues.apache.org/jira/browse/VCL-866'>VCL-866</a>] -         makeproduction state isn&#39;t handled correctly if inuse process is running
* [<a href='https://issues.apache.org/jira/browse/VCL-868'>VCL-868</a>] -         OS.pm::wait_for_no_ping uses computer&#39;s hostname, change to use IP address
* [<a href='https://issues.apache.org/jira/browse/VCL-870'>VCL-870</a>] -         Synchronize foreign keys and other items between vcl.sql and update-vcl.sql
* [<a href='https://issues.apache.org/jira/browse/VCL-871'>VCL-871</a>] -         OS.pm::create_text_file fails if content is too long
* [<a href='https://issues.apache.org/jira/browse/VCL-872'>VCL-872</a>] -         Computer notes not saved when changing state from vmhostinuse to maintenance
* [<a href='https://issues.apache.org/jira/browse/VCL-873'>VCL-873</a>] -         Allow web UI &quot;User Preferences&quot; to handle multiple SSH identity keys
* [<a href='https://issues.apache.org/jira/browse/VCL-874'>VCL-874</a>] -         change reloading state sooner in load process
* [<a href='https://issues.apache.org/jira/browse/VCL-875'>VCL-875</a>] -         Management node loses SSH access if iptables multiport rule exists
* [<a href='https://issues.apache.org/jira/browse/VCL-877'>VCL-877</a>] -         libvirt provisioning module fails to process checkpoint state correctly
* [<a href='https://issues.apache.org/jira/browse/VCL-878'>VCL-878</a>] -         Delayed checkpoint attempts are not displayed on web UI Dashboard page
* [<a href='https://issues.apache.org/jira/browse/VCL-880'>VCL-880</a>] -         Issues with clean_iptables in Linux.pm
* [<a href='https://issues.apache.org/jira/browse/VCL-881'>VCL-881</a>] -         Schedules cannot be deleted from web UI
* [<a href='https://issues.apache.org/jira/browse/VCL-883'>VCL-883</a>] -         KVM provisioning module fails to capture Windows 8.x images
* [<a href='https://issues.apache.org/jira/browse/VCL-884'>VCL-884</a>] -         Windows.pm fails to set computer hostname
* [<a href='https://issues.apache.org/jira/browse/VCL-885'>VCL-885</a>] -         Windows.pm::sanitize_files doesn&#39;t remove password if default changed since capture
* [<a href='https://issues.apache.org/jira/browse/VCL-886'>VCL-886</a>] -         xCAT.pm generates &quot;defined(@array) is deprecated&quot; warnings
* [<a href='https://issues.apache.org/jira/browse/VCL-888'>VCL-888</a>] -         Web UI fails to handle translations containing single quotes
* [<a href='https://issues.apache.org/jira/browse/VCL-892'>VCL-892</a>] -         $authtype gets undefined when clearselection submitted to selectAuth
* [<a href='https://issues.apache.org/jira/browse/VCL-900'>VCL-900</a>] -         Empty error box displayed on computer page with private DHCP and invalid server IP
* [<a href='https://issues.apache.org/jira/browse/VCL-901'>VCL-901</a>] -         Cannot enter preferred name under user preferences if have reservation and custom RDP port set
* [<a href='https://issues.apache.org/jira/browse/VCL-908'>VCL-908</a>] -         Image owner string is not validated when creating a new image
* [<a href='https://issues.apache.org/jira/browse/VCL-909'>VCL-909</a>] -         get_random_mac_address in utils.pm may generate the same mac for VMs
* [<a href='https://issues.apache.org/jira/browse/VCL-913'>VCL-913</a>] -         VCL KVM Libvirt provisioning module does not check length of the image&#39;s name when create an new image
* [<a href='https://issues.apache.org/jira/browse/VCL-914'>VCL-914</a>] -         VCL web utils.pm may block NCCU access
* [<a href='https://issues.apache.org/jira/browse/VCL-916'>VCL-916</a>] -         Linux.pm get_total_space and get_available_space may generate undefined array reference warnings
* [<a href='https://issues.apache.org/jira/browse/VCL-918'>VCL-918</a>] -         Site Config page uses wrong variable key for nat port range
* [<a href='https://issues.apache.org/jira/browse/VCL-921'>VCL-921</a>] -         changing owner of an image can cause a duplicate key error on resourcegroupmembers
* [<a href='https://issues.apache.org/jira/browse/VCL-922'>VCL-922</a>] -         Windows.pm logoff_users may generate undefined array reference errors
* [<a href='https://issues.apache.org/jira/browse/VCL-924'>VCL-924</a>] -         Commands may hang on management node if it has an unavailable NFS share
* [<a href='https://issues.apache.org/jira/browse/VCL-928'>VCL-928</a>] -         Reference vmx file not saved during image capture if vmprofile.vmdisk = dedicated and repository is mounted on host
* [<a href='https://issues.apache.org/jira/browse/VCL-929'>VCL-929</a>] -         VMware.pm does not parse hardware version from .vmdk file correctly
* [<a href='https://issues.apache.org/jira/browse/VCL-932'>VCL-932</a>] -         delete reservation from View Time Table does not work
* [<a href='https://issues.apache.org/jira/browse/VCL-936'>VCL-936</a>] -         cannot update management node sysadmin or shadow email addresses
* [<a href='https://issues.apache.org/jira/browse/VCL-939'>VCL-939</a>] -         VMware VM may be unassigned from a host if it is still running
* [<a href='https://issues.apache.org/jira/browse/VCL-940'>VCL-940</a>] -         timing issue getting public IP
* [<a href='https://issues.apache.org/jira/browse/VCL-941'>VCL-941</a>] -         Reservation may fail and be reloaded if reboot fails
* [<a href='https://issues.apache.org/jira/browse/VCL-943'>VCL-943</a>] -         Deep recursion on subroutine VCL::utils::get_vmhost_info
* [<a href='https://issues.apache.org/jira/browse/VCL-944'>VCL-944</a>] -         typo in getUserResources prevents access to management nodes and groups
* [<a href='https://issues.apache.org/jira/browse/VCL-951'>VCL-951</a>] -         suggested times not displayed for parent image of clusters when making imaging reservation
* [<a href='https://issues.apache.org/jira/browse/VCL-953'>VCL-953</a>] -         Ubuntu.pm clobbers /etc/network/interfaces even if listed in vcl_exclude_list
* [<a href='https://issues.apache.org/jira/browse/VCL-962'>VCL-962</a>] -         Scheduled task password fails to get set for Windows 10
* [<a href='https://issues.apache.org/jira/browse/VCL-970'>VCL-970</a>] -         Linux images lose default gateway when rebooted if static public IP address is used
* [<a href='https://issues.apache.org/jira/browse/VCL-974'>VCL-974</a>] -         VMware VMs may fail to power on if host does not support nested VMs
* [<a href='https://issues.apache.org/jira/browse/VCL-975'>VCL-975</a>] -         End user notification intervals being ignored in inuse.pm
* [<a href='https://issues.apache.org/jira/browse/VCL-982'>VCL-982</a>] -         VIM_SSH.pm:_get_vm_virtual_disk_file_layout fails to parse output
* [<a href='https://issues.apache.org/jira/browse/VCL-983'>VCL-983</a>] -         Manage computers does not update &quot;Computers in table&quot; count after &quot;Refresh Computer Data&quot; is clicked
* [<a href='https://issues.apache.org/jira/browse/VCL-985'>VCL-985</a>] -         login page and change locale form use continuations when user is logged out
* [<a href='https://issues.apache.org/jira/browse/VCL-988'>VCL-988</a>] -         KVM libvirt provisioning module colon char in domain name Error starting domain: Invalid machine name
* [<a href='https://issues.apache.org/jira/browse/VCL-989'>VCL-989</a>] -         Adding ext_sshd service fails Ubuntu 16 images
* [<a href='https://issues.apache.org/jira/browse/VCL-992'>VCL-992</a>] -         ext_sshd service occasionally fails to restart under systemd
* [<a href='https://issues.apache.org/jira/browse/VCL-993'>VCL-993</a>] -         web code should handle user.IMtypeid being NULL
* [<a href='https://issues.apache.org/jira/browse/VCL-995'>VCL-995</a>] -         Unable to change server reservation name if schedule no longer available
* [<a href='https://issues.apache.org/jira/browse/VCL-996'>VCL-996</a>] -         Linux firewall subroutines do not sort rule numbers correctly
* [<a href='https://issues.apache.org/jira/browse/VCL-1001'>VCL-1001</a>] -         changing a future reservation to a now reservation doesn&#39;t properly update the reserved computer
* [<a href='https://issues.apache.org/jira/browse/VCL-1004'>VCL-1004</a>] -         Illegal division by zero VMware.pm::copy_vmdk
* [<a href='https://issues.apache.org/jira/browse/VCL-1022'>VCL-1022</a>] -         API function XMLRPCgetRequestConnectData shows Administrator account for all imaging reservations
* [<a href='https://issues.apache.org/jira/browse/VCL-1023'>VCL-1023</a>] -         Cluster reservations may fail to copy an image if assigned to multiple VM hosts sharing a datastore
* [<a href='https://issues.apache.org/jira/browse/VCL-1034'>VCL-1034</a>] -         Lab.pm does not handle preload reservations correctly
* [<a href='https://issues.apache.org/jira/browse/VCL-1035'>VCL-1035</a>] -         selecting Manage Images-&gt;Create/Update an Image doesn&#39;t work
* [<a href='https://issues.apache.org/jira/browse/VCL-1038'>VCL-1038</a>] -         Wrong OS module used if NAT host image is noimage
* [<a href='https://issues.apache.org/jira/browse/VCL-1043'>VCL-1043</a>] -         utils.pm::kill_child_processes generates warnings if ps line begins with a space
* [<a href='https://issues.apache.org/jira/browse/VCL-1044'>VCL-1044</a>] -         getVariable returns wrong value if $incparams == 1 and variable has been set in $_SESSION[&#39;variables&#39;]
* [<a href='https://issues.apache.org/jira/browse/VCL-1048'>VCL-1048</a>] -         NAT rules not always deleted when a reservation ends
* [<a href='https://issues.apache.org/jira/browse/VCL-1050'>VCL-1050</a>] -         Adding a new user group doesn&#39;t include the affiliation of the default owner
* [<a href='https://issues.apache.org/jira/browse/VCL-1051'>VCL-1051</a>] -         Backend is not checking for &#39;checkpoint&#39; state everywhere it checks for &#39;image state
* [<a href='https://issues.apache.org/jira/browse/VCL-1054'>VCL-1054</a>] -         Windows.pm user_exists may return true when user doesn&#39;t exist
* [<a href='https://issues.apache.org/jira/browse/VCL-1055'>VCL-1055</a>] -         &#39;Use of uninitialized value in lc&#39; warning may be generated from a few subroutines
* [<a href='https://issues.apache.org/jira/browse/VCL-1057'>VCL-1057</a>] -         allManagementNodes is assigned available at the initial admin node
* [<a href='https://issues.apache.org/jira/browse/VCL-1058'>VCL-1058</a>] -         User accounts not deleted on computer when removed from a server request admin or access group
* [<a href='https://issues.apache.org/jira/browse/VCL-1059'>VCL-1059</a>] -         AllowUsers lines getting removed due to sequencing issue
* [<a href='https://issues.apache.org/jira/browse/VCL-1063'>VCL-1063</a>] -         editing a future reservation to have a start time that is in the past should not be allowed
* [<a href='https://issues.apache.org/jira/browse/VCL-1066'>VCL-1066</a>] -         Checkpoint image capture fails to set request state back to reserved
* [<a href='https://issues.apache.org/jira/browse/VCL-1068'>VCL-1068</a>] -         Windows fails to update scheduled task password if password contains some special characters
* [<a href='https://issues.apache.org/jira/browse/VCL-1073'>VCL-1073</a>] -         Linux.pm::reboot may fail because it doesn't detect broken SSH connection during first attempt
* [<a href='https://issues.apache.org/jira/browse/VCL-1075'>VCL-1075</a>] -         Newlines in image description not handled properly under Manage Images
* [<a href='https://issues.apache.org/jira/browse/VCL-1076'>VCL-1076</a>] -         Unsetting Enable Image Library for a management node does not set the image library group to NULL
* [<a href='https://issues.apache.org/jira/browse/VCL-1077'>VCL-1077</a>] -         Adding an AD Domain to the privilege tree with available or manageMapping set causes it to be added with no way to remove it

## 2.4.2 Changes {#2.4.2}

###        Improvement

* [<a href='https://issues.apache.org/jira/browse/VCL-850'>VCL-850</a>] -         Prevent 3D video from being enabled by default in VMware .vmx files
* [<a href='https://issues.apache.org/jira/browse/VCL-859'>VCL-859</a>] -         disable image creation for images with root access disabled

###        Bug

* [<a href='https://issues.apache.org/jira/browse/VCL-847'>VCL-847</a>] -         Computer left in reserved state if user deletes cluster request
* [<a href='https://issues.apache.org/jira/browse/VCL-849'>VCL-849</a>] -         makeproduction state not processed correctly for cluster requests
* [<a href='https://issues.apache.org/jira/browse/VCL-855'>VCL-855</a>] -         JSON Perl module missing from install_perl_libs.pl
* [<a href='https://issues.apache.org/jira/browse/VCL-856'>VCL-856</a>] -         iptables.pm generates an error under old versions of Perl
* [<a href='https://issues.apache.org/jira/browse/VCL-857'>VCL-857</a>] -         admin access not granted if owner of server reservation in access user group
* [<a href='https://issues.apache.org/jira/browse/VCL-858'>VCL-858</a>] -         Image owner should have root access for imaging reservations

###        Task

* [<a href='https://issues.apache.org/jira/browse/VCL-845'>VCL-845</a>] -         Remove blockRequest.admingroupid column
* [<a href='https://issues.apache.org/jira/browse/VCL-848'>VCL-848</a>] -         Prepare VCL 2.4.2 release

## 2.4.1 Changes {#2.4.1}

###        Improvement

* [<a href='https://issues.apache.org/jira/browse/VCL-842'>VCL-842</a>] -         Warnings appear in vcld.log if managementnode.keys is not populated

###        Bug

* [<a href='https://issues.apache.org/jira/browse/VCL-836'>VCL-836</a>] -         Incorrect IP addresses in cluster_info file
* [<a href='https://issues.apache.org/jira/browse/VCL-839'>VCL-839</a>] -         Problems occur when &quot;localhost&quot; is used for a management node name
* [<a href='https://issues.apache.org/jira/browse/VCL-841'>VCL-841</a>] -         VMware.pm::configure_vmhost_dedicated_ssh_key may fail


## 2.4 Changes {#2.4}

###        New Feature


* [<a href='https://issues.apache.org/jira/browse/VCL-5'>VCL-5</a>] -         multiple web servers
* [<a href='https://issues.apache.org/jira/browse/VCL-170'>VCL-170</a>] -         option to power off blades after reservation - new reload module
* [<a href='https://issues.apache.org/jira/browse/VCL-174'>VCL-174</a>] -         NAT Support
* [<a href='https://issues.apache.org/jira/browse/VCL-178'>VCL-178</a>] -         enable checkuser flag for per reservation instead of image only
* [<a href='https://issues.apache.org/jira/browse/VCL-562'>VCL-562</a>] -         Automatically disable user accounts known to be insecure stored in Windows images
* [<a href='https://issues.apache.org/jira/browse/VCL-564'>VCL-564</a>] -         Run custom scripts during various reservation stages
* [<a href='https://issues.apache.org/jira/browse/VCL-580'>VCL-580</a>] -         Add support for Fedora 16
* [<a href='https://issues.apache.org/jira/browse/VCL-590'>VCL-590</a>] -         Openstack Module
* [<a href='https://issues.apache.org/jira/browse/VCL-593'>VCL-593</a>] -         Documentation Links on VCL Home Page
* [<a href='https://issues.apache.org/jira/browse/VCL-617'>VCL-617</a>] -         new XML-RPC methods
* [<a href='https://issues.apache.org/jira/browse/VCL-722'>VCL-722</a>] -         OpenNebula module
* [<a href='https://issues.apache.org/jira/browse/VCL-770'>VCL-770</a>] -         Windows 8.x and Server 2012 Support
* [<a href='https://issues.apache.org/jira/browse/VCL-771'>VCL-771</a>] -         VMware ESXi 5.5 support
* [<a href='https://issues.apache.org/jira/browse/VCL-783'>VCL-783</a>] -         Add support for 64-bit cygwin
* [<a href='https://issues.apache.org/jira/browse/VCL-810'>VCL-810</a>] -         2.4 install script

                
###        Improvement


* [<a href='https://issues.apache.org/jira/browse/VCL-16'>VCL-16</a>] -         Enhance cluster reservation process
* [<a href='https://issues.apache.org/jira/browse/VCL-50'>VCL-50</a>] -         Moving machines from  Maintenance to VMhost INuse
* [<a href='https://issues.apache.org/jira/browse/VCL-133'>VCL-133</a>] -         poor flow of pages for new reservation that&#39;s not currently available for image owner with multiple revisions
* [<a href='https://issues.apache.org/jira/browse/VCL-179'>VCL-179</a>] -         image creation - confirm node is on
* [<a href='https://issues.apache.org/jira/browse/VCL-229'>VCL-229</a>] -         add something browser specific to continuations data
* [<a href='https://issues.apache.org/jira/browse/VCL-237'>VCL-237</a>] -         improve wording in error message about extending a reservation to overlap with a concurrently limited image
* [<a href='https://issues.apache.org/jira/browse/VCL-280'>VCL-280</a>] -         only fail computers for computer related failures
* [<a href='https://issues.apache.org/jira/browse/VCL-289'>VCL-289</a>] -         Consolodate image retrieval subroutines for provisioning modules
* [<a href='https://issues.apache.org/jira/browse/VCL-291'>VCL-291</a>] -         Move OS response checking from provisioning to OS modules
* [<a href='https://issues.apache.org/jira/browse/VCL-322'>VCL-322</a>] -         Add code to check that the static public address is set for all new/reload reservations, even if computer is not reloaded
* [<a href='https://issues.apache.org/jira/browse/VCL-366'>VCL-366</a>] -         as needed add throttling to new vmware modules
* [<a href='https://issues.apache.org/jira/browse/VCL-374'>VCL-374</a>] -         Set password requirements before attempting to set passwords during image capture
* [<a href='https://issues.apache.org/jira/browse/VCL-392'>VCL-392</a>] -         Add option to rename computer separate from Sysprep
* [<a href='https://issues.apache.org/jira/browse/VCL-409'>VCL-409</a>] -         Improvements to vcld -setup
* [<a href='https://issues.apache.org/jira/browse/VCL-428'>VCL-428</a>] -         Make get_*_info() subroutines consistent and improve queries
* [<a href='https://issues.apache.org/jira/browse/VCL-430'>VCL-430</a>] -         reservation extension can allow an invalid time to be submited
* [<a href='https://issues.apache.org/jira/browse/VCL-442'>VCL-442</a>] -         Reduce time between user clicking Connect and RDP being opened
* [<a href='https://issues.apache.org/jira/browse/VCL-503'>VCL-503</a>] -         Add timeout to hung SSH processes
* [<a href='https://issues.apache.org/jira/browse/VCL-531'>VCL-531</a>] -         additions to dashboard
* [<a href='https://issues.apache.org/jira/browse/VCL-538'>VCL-538</a>] -         time server option per management node
* [<a href='https://issues.apache.org/jira/browse/VCL-552'>VCL-552</a>] -         create an easy way to view deleted computers
* [<a href='https://issues.apache.org/jira/browse/VCL-555'>VCL-555</a>] -         need a way to give users access to add management nodes
* [<a href='https://issues.apache.org/jira/browse/VCL-559'>VCL-559</a>] -         convert pages with large tables to use dojo datagrids
* [<a href='https://issues.apache.org/jira/browse/VCL-568'>VCL-568</a>] -         refresh current reservations page 15 minutes after a reservation becomes available
* [<a href='https://issues.apache.org/jira/browse/VCL-570'>VCL-570</a>] -         Ubuntu support
* [<a href='https://issues.apache.org/jira/browse/VCL-581'>VCL-581</a>] -         check for whitespace in image name during image creation
* [<a href='https://issues.apache.org/jira/browse/VCL-582'>VCL-582</a>] -         Linux.pm remove rc.local dependence  
* [<a href='https://issues.apache.org/jira/browse/VCL-584'>VCL-584</a>] -         Extend features of Server loads
* [<a href='https://issues.apache.org/jira/browse/VCL-585'>VCL-585</a>] -         Migrate time source variable to variable table
* [<a href='https://issues.apache.org/jira/browse/VCL-586'>VCL-586</a>] -         Remove code using imagemeta.usergroupid
* [<a href='https://issues.apache.org/jira/browse/VCL-592'>VCL-592</a>] -         honor user preference to only show user groups matching user&#39;s affiliation on server profile pages
* [<a href='https://issues.apache.org/jira/browse/VCL-596'>VCL-596</a>] -         privilege tree - image list bubble/pop-up shows deleted images
* [<a href='https://issues.apache.org/jira/browse/VCL-604'>VCL-604</a>] -         get_currentimage info - start using imageid and imagerevisionid instead of imagename
* [<a href='https://issues.apache.org/jira/browse/VCL-605'>VCL-605</a>] -         change labels for advanced options for VM images
* [<a href='https://issues.apache.org/jira/browse/VCL-608'>VCL-608</a>] -         XMLRPC interface inaccessible to Shibboleth-authenticated users
* [<a href='https://issues.apache.org/jira/browse/VCL-636'>VCL-636</a>] -         Allow vCenter folder to be specified in VM profile
* [<a href='https://issues.apache.org/jira/browse/VCL-637'>VCL-637</a>] -         linux updating hostname
* [<a href='https://issues.apache.org/jira/browse/VCL-638'>VCL-638</a>] -         Add support for vSphere distributed switch
* [<a href='https://issues.apache.org/jira/browse/VCL-640'>VCL-640</a>] -         block allocation fixes
* [<a href='https://issues.apache.org/jira/browse/VCL-655'>VCL-655</a>] -         Manage groups - create a default or none user group
* [<a href='https://issues.apache.org/jira/browse/VCL-669'>VCL-669</a>] -         ssh identity keys for end-users
* [<a href='https://issues.apache.org/jira/browse/VCL-678'>VCL-678</a>] -         Reduce unnecessary output written to vcld.log
* [<a href='https://issues.apache.org/jira/browse/VCL-682'>VCL-682</a>] -         Consolidate xCAT provisioning modules, retire xCAT 1.x support
* [<a href='https://issues.apache.org/jira/browse/VCL-683'>VCL-683</a>] -         Retire utils.pm::_sshd_status
* [<a href='https://issues.apache.org/jira/browse/VCL-684'>VCL-684</a>] -         Remove retrieve_user_data from DataStructure.pm
* [<a href='https://issues.apache.org/jira/browse/VCL-685'>VCL-685</a>] -         VMware improvements for VCL 2.4
* [<a href='https://issues.apache.org/jira/browse/VCL-687'>VCL-687</a>] -         Problems occur if /etc/issue.net is configured in Linux images
* [<a href='https://issues.apache.org/jira/browse/VCL-690'>VCL-690</a>] -         There is no default selection on Manage computer 
* [<a href='https://issues.apache.org/jira/browse/VCL-695'>VCL-695</a>] -         Change newimages membership if image owner is changed via website
* [<a href='https://issues.apache.org/jira/browse/VCL-696'>VCL-696</a>] -         Improve resource group deletion options and information
* [<a href='https://issues.apache.org/jira/browse/VCL-698'>VCL-698</a>] -         Linux.pm delete_user may fail to detect network mounted home directory and to clean sudoers
* [<a href='https://issues.apache.org/jira/browse/VCL-702'>VCL-702</a>] -         Rework code to use new subroutines and objects &amp; general code cleanup for VCL 2.4
* [<a href='https://issues.apache.org/jira/browse/VCL-703'>VCL-703</a>] -         Delete home directory when Linux user is deleted
* [<a href='https://issues.apache.org/jira/browse/VCL-711'>VCL-711</a>] -         Move check_image_os from State.pm to xCAT.pm
* [<a href='https://issues.apache.org/jira/browse/VCL-713'>VCL-713</a>] -         Add ability to turn off certain types of logging in the database
* [<a href='https://issues.apache.org/jira/browse/VCL-714'>VCL-714</a>] -         HTML cleanup
* [<a href='https://issues.apache.org/jira/browse/VCL-717'>VCL-717</a>] -         Prevent multiple failed image creation messages being sent to user
* [<a href='https://issues.apache.org/jira/browse/VCL-726'>VCL-726</a>] -         Child processes are not killed when a vcld state process is killed
* [<a href='https://issues.apache.org/jira/browse/VCL-727'>VCL-727</a>] -         xCAT commands may timeout - make multiple attempts
* [<a href='https://issues.apache.org/jira/browse/VCL-732'>VCL-732</a>] -         disable user_connected checks for request &gt;= 24 hr
* [<a href='https://issues.apache.org/jira/browse/VCL-734'>VCL-734</a>] -         set requests to pending state earlier when processing
* [<a href='https://issues.apache.org/jira/browse/VCL-744'>VCL-744</a>] -         image retrieval can fail in some cases to find image across different management node
* [<a href='https://issues.apache.org/jira/browse/VCL-748'>VCL-748</a>] -         Linux.pm get_firewall_configuration  /etc/services
* [<a href='https://issues.apache.org/jira/browse/VCL-751'>VCL-751</a>] -         Linux.pm reserve create_user
* [<a href='https://issues.apache.org/jira/browse/VCL-757'>VCL-757</a>] -         partimageng script fails if computer has additional USB drive
* [<a href='https://issues.apache.org/jira/browse/VCL-758'>VCL-758</a>] -         VCL timings - make various timings to be variables and edited by admin 
* [<a href='https://issues.apache.org/jira/browse/VCL-759'>VCL-759</a>] -         check user group access to image when creating block allocations
* [<a href='https://issues.apache.org/jira/browse/VCL-760'>VCL-760</a>] -         user based post reservation script
* [<a href='https://issues.apache.org/jira/browse/VCL-763'>VCL-763</a>] -         Add missing constraints to database tables
* [<a href='https://issues.apache.org/jira/browse/VCL-764'>VCL-764</a>] -         Database changes for VCL 2.4
* [<a href='https://issues.apache.org/jira/browse/VCL-766'>VCL-766</a>] -         Add message argument to image.pm&#39;s reservation_failed subroutine
* [<a href='https://issues.apache.org/jira/browse/VCL-767'>VCL-767</a>] -         Allow dynamic private IP addresses, remove /etc/hosts requirement
* [<a href='https://issues.apache.org/jira/browse/VCL-769'>VCL-769</a>] -         VMware vim-cmd fails if services fail
* [<a href='https://issues.apache.org/jira/browse/VCL-772'>VCL-772</a>] -         remove node_status from provisioning sub-modules
* [<a href='https://issues.apache.org/jira/browse/VCL-773'>VCL-773</a>] -         Dashboard View Update
* [<a href='https://issues.apache.org/jira/browse/VCL-774'>VCL-774</a>] -         _get_file_info is unnecessarily slow for vSphere provisioning
* [<a href='https://issues.apache.org/jira/browse/VCL-776'>VCL-776</a>] -         rework resource code to have a base class for all resources and inheriting classes for each resource type
* [<a href='https://issues.apache.org/jira/browse/VCL-778'>VCL-778</a>] -         add graph for seeing historical usage of block allocations
* [<a href='https://issues.apache.org/jira/browse/VCL-779'>VCL-779</a>] -         add method to dashboard for restarting failed imaging reservations
* [<a href='https://issues.apache.org/jira/browse/VCL-780'>VCL-780</a>] -         combine new reservation and current reservations pages
* [<a href='https://issues.apache.org/jira/browse/VCL-781'>VCL-781</a>] -         Add ability for provisioning modules to retrieve minimum hardware requirements for a particular OS
* [<a href='https://issues.apache.org/jira/browse/VCL-782'>VCL-782</a>] -         utils.pm update_request_state generated unnecessary critical messages
* [<a href='https://issues.apache.org/jira/browse/VCL-797'>VCL-797</a>] -         system admin setting for randomly generated passwords
* [<a href='https://issues.apache.org/jira/browse/VCL-799'>VCL-799</a>] -         cluster reservations - update OS firewall to allow nodes of cluster to communicate 
* [<a href='https://issues.apache.org/jira/browse/VCL-813'>VCL-813</a>] -         Disable Windows &quot;Select a location for the network&quot; prompt
* [<a href='https://issues.apache.org/jira/browse/VCL-814'>VCL-814</a>] -         Reservation ready email should be sent as close as possible to when the Connect button appears
* [<a href='https://issues.apache.org/jira/browse/VCL-816'>VCL-816</a>] -         Nmap is very slow due to DNS
* [<a href='https://issues.apache.org/jira/browse/VCL-817'>VCL-817</a>] -         pgrep command arguments have changed with RHEL/CentOS 7.x

                                
###        Task


* [<a href='https://issues.apache.org/jira/browse/VCL-457'>VCL-457</a>] -         VCL new provisioning module: CCMP module (Provisioning virtual machines inside IBM Cloud)
* [<a href='https://issues.apache.org/jira/browse/VCL-606'>VCL-606</a>] -         viewdocs interface removal


###        Sub-task


* [<a href='https://issues.apache.org/jira/browse/VCL-122'>VCL-122</a>] -         Reload reservations setting ending state for user request when it shouldn&#39;t
* [<a href='https://issues.apache.org/jira/browse/VCL-647'>VCL-647</a>] -         Warning generated if vmprofile.rsakey is not defined
* [<a href='https://issues.apache.org/jira/browse/VCL-677'>VCL-677</a>] -         xCAT2.pm displays &quot;Use of uninitialized value in concatenation&quot; warnings
* [<a href='https://issues.apache.org/jira/browse/VCL-686'>VCL-686</a>] -         vSphere_SDK.pm::_get_file_info slow
* [<a href='https://issues.apache.org/jira/browse/VCL-798'>VCL-798</a>] -         Password complexity

            
###        Bug


* [<a href='https://issues.apache.org/jira/browse/VCL-22'>VCL-22</a>] -         run_ssh_command may produce unexpected results if invalid identity key path is specified
* [<a href='https://issues.apache.org/jira/browse/VCL-27'>VCL-27</a>] -         SQL statement error Level_1.pm
* [<a href='https://issues.apache.org/jira/browse/VCL-60'>VCL-60</a>] -         image copy lock file for shared image library 
* [<a href='https://issues.apache.org/jira/browse/VCL-86'>VCL-86</a>] -         reserved.pm does not correctly check for user connection for Linux imaging standalone reservations
* [<a href='https://issues.apache.org/jira/browse/VCL-144'>VCL-144</a>] -         Imaging reservations may fail and not be put into maintenance if initialize() sub in State.pm fails
* [<a href='https://issues.apache.org/jira/browse/VCL-308'>VCL-308</a>] -         Computer load log does not account for images that have to be transferred to another management node
* [<a href='https://issues.apache.org/jira/browse/VCL-560'>VCL-560</a>] -         cleartext password stored in VMProfile table
* [<a href='https://issues.apache.org/jira/browse/VCL-594'>VCL-594</a>] -         xCAT changes
* [<a href='https://issues.apache.org/jira/browse/VCL-607'>VCL-607</a>] -         &#39;default&#39; skin hard-coded in initialization function when it should use the global DEFAULTTHEME
* [<a href='https://issues.apache.org/jira/browse/VCL-610'>VCL-610</a>] -         minor HTML errors 
* [<a href='https://issues.apache.org/jira/browse/VCL-613'>VCL-613</a>] -         output from init.d startup scripts are slightly amiss
* [<a href='https://issues.apache.org/jira/browse/VCL-619'>VCL-619</a>] -         usenls may be undefined in _() function in requests.js
* [<a href='https://issues.apache.org/jira/browse/VCL-623'>VCL-623</a>] -         Invalid public IP address may be presented on Connect page
* [<a href='https://issues.apache.org/jira/browse/VCL-624'>VCL-624</a>] -         getUserlistID should be passed a user&#39;s full login string, not just a unityid
* [<a href='https://issues.apache.org/jira/browse/VCL-627'>VCL-627</a>] -         image type fields on VM Host Profile page do not get updated
* [<a href='https://issues.apache.org/jira/browse/VCL-628'>VCL-628</a>] -         check for duplicate image name not correctly performed when specified name is the same as the base image
* [<a href='https://issues.apache.org/jira/browse/VCL-630'>VCL-630</a>] -         currentimage.txt name may conflict with imagerevision name, causing unnecessary reloads
* [<a href='https://issues.apache.org/jira/browse/VCL-646'>VCL-646</a>] -         Ubuntu.pm doesn&#39;t set userid when creating a user account
* [<a href='https://issues.apache.org/jira/browse/VCL-664'>VCL-664</a>] -         hard coded references to &quot;Local Account&quot;
* [<a href='https://issues.apache.org/jira/browse/VCL-665'>VCL-665</a>] -         nmap routine output missing variable
* [<a href='https://issues.apache.org/jira/browse/VCL-667'>VCL-667</a>] -         Administrator is always passed as the userid in RDP files for imaging reservations, even if it is for xRDP
* [<a href='https://issues.apache.org/jira/browse/VCL-668'>VCL-668</a>] -         VMware fails to copy image under ESXi 5.1
* [<a href='https://issues.apache.org/jira/browse/VCL-672'>VCL-672</a>] -         privilege page does not handle user groups with the same name but different affiliations correctly
* [<a href='https://issues.apache.org/jira/browse/VCL-673'>VCL-673</a>] -         imaging reservation for an image with subimages prompts for revisions for each subimage
* [<a href='https://issues.apache.org/jira/browse/VCL-676'>VCL-676</a>] -         OS.pm::remove_lines_from_file not escaping characters correctly
* [<a href='https://issues.apache.org/jira/browse/VCL-679'>VCL-679</a>] -         utils.pm:get_computer_info using image.name to retrieve imagerevision info
* [<a href='https://issues.apache.org/jira/browse/VCL-681'>VCL-681</a>] -         Failure to detect if SSH is available on VMware - timed out during banner exchange
* [<a href='https://issues.apache.org/jira/browse/VCL-688'>VCL-688</a>] -         Image retrieval may fail to detect image residing on another management node
* [<a href='https://issues.apache.org/jira/browse/VCL-691'>VCL-691</a>] -         utils.pm::get_production_imagerevision_info fails if image name argument is not the production revision
* [<a href='https://issues.apache.org/jira/browse/VCL-692'>VCL-692</a>] -         server request and vcl_post_reserve
* [<a href='https://issues.apache.org/jira/browse/VCL-693'>VCL-693</a>] -         VCL Cluster Reinstall Fails
* [<a href='https://issues.apache.org/jira/browse/VCL-694'>VCL-694</a>] -         problem with conditional in editOrAddComputer - $data[&#39;compid&#39;] can be used when adding a computer
* [<a href='https://issues.apache.org/jira/browse/VCL-697'>VCL-697</a>] -         image capture state overwritten
* [<a href='https://issues.apache.org/jira/browse/VCL-699'>VCL-699</a>] -         Process may die if $self-&gt;mn_os isn&#39;t defined and get_computer_private_ip_address is called
* [<a href='https://issues.apache.org/jira/browse/VCL-700'>VCL-700</a>] -         tovmhostinuse requests may fail if automatic VM host provisioning isn&#39;t configured
* [<a href='https://issues.apache.org/jira/browse/VCL-701'>VCL-701</a>] -         Fedora 18 support
* [<a href='https://issues.apache.org/jira/browse/VCL-704'>VCL-704</a>] -         Changes in user preferences not applied until vcld is restarted
* [<a href='https://issues.apache.org/jira/browse/VCL-707'>VCL-707</a>] -         Improve ability to parse vcld.log
* [<a href='https://issues.apache.org/jira/browse/VCL-712'>VCL-712</a>] -         Ubuntu module checks for iptables service when it should be checking for ufw
* [<a href='https://issues.apache.org/jira/browse/VCL-719'>VCL-719</a>] -         add/edit resource group when no user groups to be listed
* [<a href='https://issues.apache.org/jira/browse/VCL-723'>VCL-723</a>] -         Chrome has problems with the Virtual Hosts-&gt;VM Host Profiles page
* [<a href='https://issues.apache.org/jira/browse/VCL-725'>VCL-725</a>] -         utils.pm run_command does not consistently return exit status
* [<a href='https://issues.apache.org/jira/browse/VCL-729'>VCL-729</a>] -         utils.pm::mail will display errors if $RETURNPATH is not defined
* [<a href='https://issues.apache.org/jira/browse/VCL-730'>VCL-730</a>] -         cannot update image revision comments under Edit Image
* [<a href='https://issues.apache.org/jira/browse/VCL-731'>VCL-731</a>] -         printSelectInput should match the image name instead of the id for the $skip argument
* [<a href='https://issues.apache.org/jira/browse/VCL-733'>VCL-733</a>] -         editing a block allocation recreates past block time entries
* [<a href='https://issues.apache.org/jira/browse/VCL-735'>VCL-735</a>] -         UnixLab.pm updates
* [<a href='https://issues.apache.org/jira/browse/VCL-736'>VCL-736</a>] -         notify user on console 
* [<a href='https://issues.apache.org/jira/browse/VCL-737'>VCL-737</a>] -         reboot option can set reservation to failed
* [<a href='https://issues.apache.org/jira/browse/VCL-739'>VCL-739</a>] -         predictive module Level 1 not using computer.nextimageid
* [<a href='https://issues.apache.org/jira/browse/VCL-740'>VCL-740</a>] -         Deletion of Block allocations not removing reload reservations
* [<a href='https://issues.apache.org/jira/browse/VCL-741'>VCL-741</a>] -         a tomaintenance reservation can be created right after another tomaintenance reservation
* [<a href='https://issues.apache.org/jira/browse/VCL-742'>VCL-742</a>] -         server reservations cannot be modified if they cannot be extended
* [<a href='https://issues.apache.org/jira/browse/VCL-743'>VCL-743</a>] -         run_ssh_command fails if SSH key permissions are incorrect
* [<a href='https://issues.apache.org/jira/browse/VCL-745'>VCL-745</a>] -         Windows.pm user_logged_in does not check for imaging requests
* [<a href='https://issues.apache.org/jira/browse/VCL-746'>VCL-746</a>] -         Windows.pm get_service_configuration may hang
* [<a href='https://issues.apache.org/jira/browse/VCL-747'>VCL-747</a>] -         editOrAddGroup can have $ownerid undefined for add mode
* [<a href='https://issues.apache.org/jira/browse/VCL-752'>VCL-752</a>] -         block allocated nodes count toward max concurrent usage of image even for users in that block allocation
* [<a href='https://issues.apache.org/jira/browse/VCL-754'>VCL-754</a>] -         server reservation Admin access and User access user groups
* [<a href='https://issues.apache.org/jira/browse/VCL-755'>VCL-755</a>] -         Add &#39;if defined&#39; checks for all get_management_node_info calls
* [<a href='https://issues.apache.org/jira/browse/VCL-756'>VCL-756</a>] -         Run custom vcl_post_load scripts last
* [<a href='https://issues.apache.org/jira/browse/VCL-761'>VCL-761</a>] -         Incorrect repository path used for images retrieved from another management node for a KVM hypervisor
* [<a href='https://issues.apache.org/jira/browse/VCL-765'>VCL-765</a>] -         get_computer_ids may return deleted computers
* [<a href='https://issues.apache.org/jira/browse/VCL-768'>VCL-768</a>] -         Linux.pm&#39;s logoff_user displays a warning if the user is not logged in
* [<a href='https://issues.apache.org/jira/browse/VCL-775'>VCL-775</a>] -         Request may fail due to timing issue in computer_not_being_used and get_request_by_computerid
* [<a href='https://issues.apache.org/jira/browse/VCL-793'>VCL-793</a>] -         Repeated vcld processes are forked for &#39;deleted&#39; processes which fail to initialize
* [<a href='https://issues.apache.org/jira/browse/VCL-794'>VCL-794</a>] -         Make sure computer_not_being_used in new.pm always returns an explicit value
* [<a href='https://issues.apache.org/jira/browse/VCL-795'>VCL-795</a>] -         Request processes are continuously created after end time is reached if request state is &#39;inuse&#39; and process initialization fails
* [<a href='https://issues.apache.org/jira/browse/VCL-800'>VCL-800</a>] -         Reservations insert log.ending = failed when they shouldn&#39;t
* [<a href='https://issues.apache.org/jira/browse/VCL-811'>VCL-811</a>] -         server requests for owned user groups show up in reservation list
* [<a href='https://issues.apache.org/jira/browse/VCL-812'>VCL-812</a>] -         Windows is not always activated on load
* [<a href='https://issues.apache.org/jira/browse/VCL-815'>VCL-815</a>] -         Problems with update_cluster in OS.pm
* [<a href='https://issues.apache.org/jira/browse/VCL-834'>VCL-834</a>] -         Disable timeout for disconnected users is meaningless for imaging reservations


## 2.3.2 Changes {#2.3.2}

###        Bug


* [<a href='https://issues.apache.org/jira/browse/VCL-666'>VCL-666</a>] -         Administrator is always passed as the userid in RDP files for imaging reservations, even if it is for xRDP
* [<a href='https://issues.apache.org/jira/browse/VCL-671'>VCL-671</a>] -         VMware may delete VM assigned to another reservation when reclaiming disk space on the host
* [<a href='https://issues.apache.org/jira/browse/VCL-674'>VCL-674</a>] -         problem adding a user group to the privilege with cascade checked
* [<a href='https://issues.apache.org/jira/browse/VCL-675'>VCL-675</a>] -         deleting a hierarchy of 3 or more privilege nodes throws an error


## 2.3.1 Changes {#2.3.1}

###        Bug


* [<a href='https://issues.apache.org/jira/browse/VCL-451'>VCL-451</a>] -         Cannot add deleted computers
* [<a href='https://issues.apache.org/jira/browse/VCL-603'>VCL-603</a>] -         reboot hard does not work for hung windows machines
* [<a href='https://issues.apache.org/jira/browse/VCL-607'>VCL-607</a>] -         &#39;default&#39; skin hard-coded in initialization function when it should use the global DEFAULTTHEME
* [<a href='https://issues.apache.org/jira/browse/VCL-609'>VCL-609</a>] -         Reservations fail if cat command returns non-zero exit status when retrieving contents of /etc/hosts on management node
* [<a href='https://issues.apache.org/jira/browse/VCL-610'>VCL-610</a>] -         minor HTML errors
* [<a href='https://issues.apache.org/jira/browse/VCL-613'>VCL-613</a>] -         output from init.d startup scripts are slightly amiss
* [<a href='https://issues.apache.org/jira/browse/VCL-616'>VCL-616</a>] -         update_cygwin.cmd fails to generate keys with current version of Cygwin
* [<a href='https://issues.apache.org/jira/browse/VCL-619'>VCL-619</a>] -         usenls may be undefined in _() function in requests.js
* [<a href='https://issues.apache.org/jira/browse/VCL-620'>VCL-620</a>] -         libvirt.pm does not remove VMs when unassigned from host via website
* [<a href='https://issues.apache.org/jira/browse/VCL-621'>VCL-621</a>] -         confirm_public_ip_address does not detect public ip address correctly for reloads
* [<a href='https://issues.apache.org/jira/browse/VCL-622'>VCL-622</a>] -         reservation_failed Linux.pm Windows.pm
* [<a href='https://issues.apache.org/jira/browse/VCL-623'>VCL-623</a>] -         Invalid public IP address may be presented on Connect page
* [<a href='https://issues.apache.org/jira/browse/VCL-624'>VCL-624</a>] -         getUserlistID should be passed a user&#39;s full login string, not just a unityid
* [<a href='https://issues.apache.org/jira/browse/VCL-625'>VCL-625</a>] -         Image retrieval may attempt to copy multiple copies of the same file, does not retrieve VMware reference vmx file.
* [<a href='https://issues.apache.org/jira/browse/VCL-626'>VCL-626</a>] -         Name RDP file download after server reservation name
* [<a href='https://issues.apache.org/jira/browse/VCL-627'>VCL-627</a>] -         image type fields on VM Host Profile page do not get updated
* [<a href='https://issues.apache.org/jira/browse/VCL-628'>VCL-628</a>] -         check for duplicate image name not correctly performed when specified name is the same as the base image
* [<a href='https://issues.apache.org/jira/browse/VCL-630'>VCL-630</a>] -         currentimage.txt name may conflict with imagerevision name, causing unnecessary reloads
* [<a href='https://issues.apache.org/jira/browse/VCL-631'>VCL-631</a>] -         imagerevision.datedeleted not getting set
* [<a href='https://issues.apache.org/jira/browse/VCL-632'>VCL-632</a>] -         vSphere_SDK.pm set_file_permissions does not work
* [<a href='https://issues.apache.org/jira/browse/VCL-633'>VCL-633</a>] -         Change of vmprofile.vmdisk value can cause image capture to fail due to insufficient space
* [<a href='https://issues.apache.org/jira/browse/VCL-634'>VCL-634</a>] -         Cluster reservations fail if node_status returns POST_LOAD
* [<a href='https://issues.apache.org/jira/browse/VCL-641'>VCL-641</a>] -         VCL fails to properly trim whitespace from "virsh list --all"
* [<a href='https://issues.apache.org/jira/browse/VCL-642'>VCL-642</a>] -         colons should not be allowed in resource group names
* [<a href='https://issues.apache.org/jira/browse/VCL-643'>VCL-643</a>] -         VM Limit can be decreased to below the current number of assigned VMs
* [<a href='https://issues.apache.org/jira/browse/VCL-648'>VCL-648</a>] -         blockRequests re-processed at end time for skipped block time entries
* [<a href='https://issues.apache.org/jira/browse/VCL-649'>VCL-649</a>] -         Images may fail to load if renamed in database by VMware code
* [<a href='https://issues.apache.org/jira/browse/VCL-650'>VCL-650</a>] -         VCL breaks with PHP 5.4
* [<a href='https://issues.apache.org/jira/browse/VCL-651'>VCL-651</a>] -         libvirt to vmware entry missing from provisioningOSinstalltype table
* [<a href='https://issues.apache.org/jira/browse/VCL-652'>VCL-652</a>] -         xCAT nodeset failure
* [<a href='https://issues.apache.org/jira/browse/VCL-653'>VCL-653</a>] -         editing a federated user group sets the affiliation of the group that of the user editing the group
* [<a href='https://issues.apache.org/jira/browse/VCL-654'>VCL-654</a>] -         Sysprep fails for 32-bit Windows 7
* [<a href='https://issues.apache.org/jira/browse/VCL-656'>VCL-656</a>] -         VIM_SSH.pm times out too early when removing snapshots from a VM
* [<a href='https://issues.apache.org/jira/browse/VCL-657'>VCL-657</a>] -         Prevent benign warning messages from appearing in vcld.log


###        Improvement


* [<a href='https://issues.apache.org/jira/browse/VCL-608'>VCL-608</a>] -         XMLRPC interface inaccessible to Shibboleth-authenticated users
* [<a href='https://issues.apache.org/jira/browse/VCL-615'>VCL-615</a>] -         make default adminUsers group have the same level of access as the default admin user
* [<a href='https://issues.apache.org/jira/browse/VCL-629'>VCL-629</a>] -         update ownership of existing /home/$username
* [<a href='https://issues.apache.org/jira/browse/VCL-639'>VCL-639</a>] -         server loads - reinstall
* [<a href='https://issues.apache.org/jira/browse/VCL-640'>VCL-640</a>] -         block allocation fixes


###        New Feature


* [<a href='https://issues.apache.org/jira/browse/VCL-617'>VCL-617</a>] -         new XML-RPC methods


## 2.2.2 Changes {#2.2.2}

###        Bug


* [<a href='https://issues.apache.org/jira/browse/VCL-328'>VCL-328</a>] -         shibboleth sp logout URL not using SSL
* [<a href='https://issues.apache.org/jira/browse/VCL-342'>VCL-342</a>] -         problem selecting image revision id when making a cluster reservation with identical subimages
* [<a href='https://issues.apache.org/jira/browse/VCL-348'>VCL-348</a>] -         Setting privileges in web gui -- Slightly broken
* [<a href='https://issues.apache.org/jira/browse/VCL-400'>VCL-400</a>] -         virtual hosts page shows all unassigned vms instead of checking which ones the user can access
* [<a href='https://issues.apache.org/jira/browse/VCL-433'>VCL-433</a>] -         new revisions can be captured of kickstart images
* [<a href='https://issues.apache.org/jira/browse/VCL-447'>VCL-447</a>] -         Notice: Uninitialized string offset: 0 in .../vcl/.ht-inc/utils.php on line 3206
* [<a href='https://issues.apache.org/jira/browse/VCL-456'>VCL-456</a>] -         groupwasnone variable is not properly initialized
* [<a href='https://issues.apache.org/jira/browse/VCL-458'>VCL-458</a>] -         $virtual undefined in utils.php line 3678
* [<a href='https://issues.apache.org/jira/browse/VCL-467'>VCL-467</a>] -         Members of a group from one affiliation have access to groups with the same name from other affiliations
* [<a href='https://issues.apache.org/jira/browse/VCL-473'>VCL-473</a>] -         query in findManagementNode in utils.php doesn&#39;t have conditional to join tables
* [<a href='https://issues.apache.org/jira/browse/VCL-475'>VCL-475</a>] -         addShibUser in shibauth.php returns an array when it should be returning a user id
* [<a href='https://issues.apache.org/jira/browse/VCL-476'>VCL-476</a>] -         manage block allocation page may show incorrect next start time
* [<a href='https://issues.apache.org/jira/browse/VCL-480'>VCL-480</a>] -         XMLRPCproccessBlockTime can throw an error about VMhostCheck table already existing
* [<a href='https://issues.apache.org/jira/browse/VCL-482'>VCL-482</a>] -         scheduler does not order VMs properly when no VMs are preloaded with the selected image
* [<a href='https://issues.apache.org/jira/browse/VCL-486'>VCL-486</a>] -         Measures against cross site scripting on the Login form
* [<a href='https://issues.apache.org/jira/browse/VCL-487'>VCL-487</a>] -         Problem in screen transition after successful login authentication
* [<a href='https://issues.apache.org/jira/browse/VCL-492'>VCL-492</a>] -         edit computer info for VM in maintenance state
* [<a href='https://issues.apache.org/jira/browse/VCL-494'>VCL-494</a>] -         Typo in testsetup.php
* [<a href='https://issues.apache.org/jira/browse/VCL-507'>VCL-507</a>] -         Deleted VMs appear in the list of unassigned VMs
* [<a href='https://issues.apache.org/jira/browse/VCL-509'>VCL-509</a>] -         error when adding computer with no groups selected
* [<a href='https://issues.apache.org/jira/browse/VCL-510'>VCL-510</a>] -         insert correct architecture in image table when adding new entry
* [<a href='https://issues.apache.org/jira/browse/VCL-533'>VCL-533</a>] -         error when trying to download dhcp data when private IP address was not entered
* [<a href='https://issues.apache.org/jira/browse/VCL-547'>VCL-547</a>] -         removing site maintenance entry from .ht-inc/maintenance directory doesn&#39;t fully remove site from maintenance
* [<a href='https://issues.apache.org/jira/browse/VCL-549'>VCL-549</a>] -         AJAX error when creating a new schedule
* [<a href='https://issues.apache.org/jira/browse/VCL-556'>VCL-556</a>] -         edit schedule groups code not doing permissions correctly
* [<a href='https://issues.apache.org/jira/browse/VCL-674'>VCL-674</a>] -         problem adding a user group to the privilege with cascade checked
* [<a href='https://issues.apache.org/jira/browse/VCL-675'>VCL-675</a>] -         deleting a hierarchy of 3 or more privilege nodes throws an error
