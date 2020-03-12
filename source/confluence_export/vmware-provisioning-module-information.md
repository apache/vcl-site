---
title: VMware Provisioning Module Information
---

<a name="VMwareProvisioningModuleInformation-VMwareProvisioningModule"></a>
## VMware Provisioning Module

* Source file: managementnode/lib/VCL/Module/Provisioning/VMware/VMware.pm

<a name="VMwareProvisioningModuleInformation-SupportedVMwareProducts"></a>
#### Supported VMware Products

* VMware Server 2.0
* VMware ESX/ESXi 3.5
* VMware ESX/ESXi 4.0

<a name="VMwareProvisioningModuleInformation-SupportedVMware&nbsp;APIs,SDKs,&CLIs"></a>
#### Supported VMware&nbsp;APIs, SDKs, & CLIs

There are several different methods to control VMware hosts and virtual
machines.&nbsp; The main VMware.pm module should remain as
SDK/API/CLI-agnostic as possible.&nbsp; All code which interacts with a
VMware remote control method should reside in utility modules located in
the lib/VCL/Module/Provisioning/VMware directory.
* vSphere SDK - lib/VCL/Module/Provisioning/VMware/vSphere_SDK.pm
** Provides full VM and VM host remote access functionality
** Provides VM host datastore file access
** Can only be used if the VMware&nbsp;host is not running with a
restricted license
** SSH access is not required to the VM host
** Installed by default on ESX/ESXi hosts
** Can be installed on Server 2.0 hosts
* -VIX API - lib/VCL/Module/Provisioning/VMware/VIX_API.pm-
_Although a utility module has been written to use the VIX API, it is not
supported and will not be maintained.&nbsp; Everything that the VIX API can
do can be done by the vim-cmd CLI and SSH access to the VM host is required
for both methods.&nbsp; Therefore, there is no benefit to maintain&nbsp;the
VIX API module._
** -Provides basic VM control functions-
** -Does not provide any file access-
** -SSH access is required to the VM host in order to manipulate the file
system-
** -Can only be used if the VMware&nbsp;host is not running with a
restricted license-
** -Installed by default on Server 2.0 hosts-
* vim-cmd CLI via SSH - lib/VCL/Module/Provisioning/VMware/VIM_SSH.pm
** Provides full VM host remote access functionality
** Does not provide file access
** SSH access is required to the VM host in order to manipulate the file
system
** Can be used if the the VMware host is running with a restricted license

<a name="VMwareProvisioningModuleInformation-RequiredUtilityModuleSubroutines"></a>
### Required Utility Module Subroutines

* get_registered_vms
* vm_register
* vm_unregister
* get_vm_power_state
* vm_power_on
* vm_power_off
* copy_virtual_disk
* move_virtual_disk
* get_virtual_disk_controller_type
* get_virtual_disk_hardware_version
* get_virtual_disk_type

<a name="VMwareProvisioningModuleInformation-RequiredOSModuleSubroutines"></a>
### Required OS Module Subroutines

* find_files
* copy_file
* copy_file_to
* copy_file_from
* delete_file
* move_file
* file_exists
* get_available_space
* create_directory
* get_file_contents
* get_file_size
