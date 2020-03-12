---
title: Libvirt Provisioning Module
---

**(this page is probably beyond repair and should be recreated - it would probably
be best to separate the manually created part from the auto generated part and
just directly check in the manually created part as a plain html file instead of
a .mdtext file)**


[Libvirt ](http://libvirt.org/)
is an open source toolkit which can interact with KVM, Xen, and several
other virtualization architectures.


### libvirt.pm {#libvirtpm}

* libvirt.pm is the main provisioning module
* Computers should have their provisioningID attributes set to point to
this module in order to utilize it
* Implements the required provisioning module subroutines: **load, capture,
node_status, power_status, power_on, power_off, power_reset...**
* Implements the functions provided by libvirt: **define, start, destroy...**
* Does not contain code specific to any of the hypervisors supported by
libvirt (KVM, Xen, etc)
* File location: **lib/VCL/Module/Provisioning/Libvirt.pm**
* Automatically determines which hypervisor driver object to use upon
initialization by examining the host

### Hypervisor Driver Modules {#hypervisordrivermodules}

Libvirt hypervisor drivers allow it to interact with and control various
types of hypervisors. The drivers are listed at [http://libvirt.org/drivers.html](http://libvirt.org/drivers.html).
A hypervisor driver module must be written in order for VCL to support
any of the hypervisors supported by libvirt. These driver modules
only contain code specific to the driver in order to perform functions not
handled by libvirt.pm.


* Hypervisor driver directory: **lib/VCL/Module/Provisioning/libvirt/**
* Example: lib/VCL/Module/Provisioning/libvirt/KVM.pm
    * Contains code which only applies to KVM
    * Calls qemu-img to perform image file operations

!Libvirt UML Diagram.gif!


#### Virtual Machine Disks {#virtualmachinedisks}

A master disk image is stored in the location specified by the datastore
path in the VM host profile. A copy on write virtual disk image is
created for each virtual machine when it is loaded. The master disk
image is used as a read-only backing file for the copy on write disk
images. Each VM writes to its own copy on write disk image. 
Using copy on write virtual disks allows VMs to be loaded without having to
create a complete copy of the master disk image.
!Copy on Write.gif|width=367,height=448!
  
  
# libvirt.pm {#libvirtpm2}

<p><a name="__index__"></a></p>
<!-- INDEX BEGIN -->

<ul>

	<li><a href="#name">NAME</a></li>
	<li><a href="#synopsis">SYNOPSIS</a></li>
	<li><a href="#description">DESCRIPTION</a></li>
	<li><a href="#object_methods">OBJECT METHODS</a></li>
	<ul>

		<li><a href="#initialize">initialize</a></li>
		<li><a href="#load">load</a></li>
		<li><a href="#capture">capture</a></li>
		<li><a href="#node_status">node_status</a></li>
		<li><a href="#does_image_exist">does_image_exist</a></li>
		<li><a href="#get_image_size">get_image_size</a></li>
		<li><a
href="#get_image_repository_search_paths">get_image_repository_search_paths</a></li>
		<li><a href="#power_status">power_status</a></li>
		<li><a href="#power_on">power_on</a></li>
		<li><a href="#power_off">power_off</a></li>
		<li><a href="#power_reset">power_reset</a></li>
		<li><a
href="#post_maintenance_action">post_maintenance_action</a></li>
	</ul>

	<li><a href="#private_methods">PRIVATE METHODS</a></li>
	<ul>

		<li><a href="#driver">driver</a></li>
		<li><a href="#get_driver_name">get_driver_name</a></li>
		<li><a href="#get_domain_name">get_domain_name</a></li>
		<li><a
href="#get_domain_file_base_name">get_domain_file_base_name</a></li>
		<li><a
href="#get_domain_xml_directory_path">get_domain_xml_directory_path</a></li>
		<li><a
href="#get_domain_xml_file_path">get_domain_xml_file_path</a></li>
		<li><a
href="#get_master_image_directory_path">get_master_image_directory_path</a></li>
		<li><a
href="#get_master_image_file_path">get_master_image_file_path</a></li>
		<li><a
href="#get_copy_on_write_file_path">get_copy_on_write_file_path</a></li>
		<li><a
href="#delete_existing_domains">delete_existing_domains</a></li>
		<li><a href="#delete_domain">delete_domain</a></li>
		<li><a
href="#generate_domain_xml">generate_domain_xml</a></li>
		<li><a href="#get_domain_info">get_domain_info</a></li>
		<li><a href="#get_domain_xml">get_domain_xml</a></li>
		<li><a href="#domain_exists">domain_exists</a></li>
		<li><a href="#get_snapshot_info">get_snapshot_info</a></li>
		<li><a href="#create_snapshot">create_snapshot</a></li>
		<li><a href="#delete_snapshot">delete_snapshot</a></li>
		<li><a
href="#get_image_size_bytes">get_image_size_bytes</a></li>
		<li><a
href="#find_repository_image_file_paths">find_repository_image_file_paths</a></li>
	</ul>

	<li><a href="#see_also">SEE ALSO</a></li>
</ul>
<!-- INDEX END -->

<hr />
<p>
</p>
<h1><a name="name">NAME</a></h1>
<p>VCL::Provisioning::libvirt - VCL provisioning module to support the
libvirt toolkit</p>
<p>
</p>
<hr />
<h1><a name="synopsis">SYNOPSIS</a></h1>
<pre>
 use VCL::Module::Provisioning::libvirt;
 my $provisioner =
(VCL::Module::Provisioning::libvirt)-&gt;new({data_structure =&gt; $self-&gt;data});</pre>
<p>
</p>
<hr />
<h1><a name="description">DESCRIPTION</a></h1>
<pre>
 Provides support allowing VCL to provisioning resources supported by the
 libvirt toolkit.
 <a href="http://libvirt.org">http://libvirt.org</a></pre>
<p>
</p>
<hr />
<h1><a name="object_methods">OBJECT METHODS</a></h1>
<p>
</p>
<h2><a name="initialize">initialize</a></h2>
<pre>
 Parameters  : none
 Returns     : boolean
 Description : Enumerates the libvirt driver modules directory:
	       lib/VCL/Module/Provisioning/libvirt/

	       Attempts to create and initialize an object for each hypervisor
	       driver module found in this directory. The first driver module
	       object successfully initialized is used. This object is made
	       accessible within this module via $self-&gt;driver. This allows
	       libvirt support driver modules to be added without having to
	       alter the code in libvirt.pm.</pre>
<p>
</p>
<h2><a name="load">load</a></h2>
<pre>
 Parameters  : none
 Returns     : boolean
 Description : Loads the requested image on the domain:</pre>
<ul>
<li>
<p>Destroy and delete any domains have already been defined for the
computer
assigned to this reservation.</p>
</li>
<li>
<p>Construct the default libvirt XML definition for the domain.</p>
</li>
<li>
<p>Call the libvirt driver module's 'extend_domain_xml' subroutine if it is
implemented. Pass the default domain XML definition hash reference as an
argument. The 'extend_domain_xml' subroutine may add or modify XML values.
This
allows the driver module to customize the XML specific to that driver.</p>
</li>
<li>
<p>Call the driver module's 'pre_define' subroutine if it is implemented.
This
subroutine completes any necessary tasks which are specific to the driver
being
used prior to defining the domain.</p>
</li>
<li>
<p>Create a text file on the node containing the domain XML definition.</p>
</li>
<li>
<p>Define the domain on the node by calling 'virsh define &lt;XML
file&gt;'.</p>
</li>
<li>
<p>Power on the domain.</p>
</li>
<li>
<p>Call the domain guest OS module's 'post_load' subroutine if
implemented.</p>
</li>
</ul>
<p>
</p>
<h2><a name="capture">capture</a></h2>
<pre>
 Parameters  : none
 Returns     : boolean
 Description : Captures the image currently loaded on the computer.</pre>
<p>
</p>
<h2><a name="node_status">node_status</a></h2>
<pre>
 Parameters  : $computer_id (optional)
 Returns     : string
 Description : Checks the status of the computer in order to determine if the
	       computer is ready to be reserved or needs to be reloaded. A
	       string is returned depending on the status of the computer:
	       'READY':
		  * Computer is ready to be reserved
		  * It is accessible
		  * It is loaded with the correct image
		  * OS module's post-load tasks have run
	       'POST_LOAD':
		  * Computer is loaded with the correct image
		  * OS module's post-load tasks have not run
	       'RELOAD':
		  * Computer is not accessible or not loaded with the correct
		    image</pre>
<p>
</p>
<h2><a name="does_image_exist">does_image_exist</a></h2>
<pre>
 Parameters  : $image_name (optional)
 Returns     : array (boolean)
 Description : Checks if the requested image exists on the node or in the
	       repository. If the image exists, an array containing the image
	       file paths is returned. A boolean evaluation can be done on the
	       return value to simply determine if an image exists.</pre>
<p>
</p>
<h2><a name="get_image_size">get_image_size</a></h2>
<pre>
 Parameters  : $image_name (optional)
 Returns     : integer
 Description : Returns the size of the image in megabytes.</pre>
<p>
</p>
<h2><a
name="get_image_repository_search_paths">get_image_repository_search_paths</a></h2>
<pre>
 Parameters  : $management_node_identifier (optional)
 Returns     : array
 Description : Returns an array containing paths on the management node where an
	       image may reside. The paths may contain wildcards. This is used
	       to attempt to locate an image on another managment node in order
	       to retrieve it.</pre>
<p>
</p>
<h2><a name="power_status">power_status</a></h2>
<pre>
 Parameters  : $domain_name (optional)
 Returns     : string
 Description : Determines the power state of the domain. A string is returned
	       containing one of the following values:
		  * 'on'
		  * 'off'
		  * 'suspended'</pre>
<p>
</p>
<h2><a name="power_on">power_on</a></h2>
<pre>
 Parameters  : $domain_name (optional)
 Returns     : boolean
 Description : Powers on the domain. Returns true if the domain was successfully
	       powered on or was already powered on.</pre>
<p>
</p>
<h2><a name="power_off">power_off</a></h2>
<pre>
 Parameters  : $domain_name
 Returns     : boolean
 Description : Powers off the domain. Returns true if the domain was
	       successfully powered off or was already powered off.</pre>
<p>
</p>
<h2><a name="power_reset">power_reset</a></h2>
<pre>
 Parameters  : $domain_name (optional)
 Returns     : boolean
 Description : Resets the power of the domain by powering it off and then back
	       on.</pre>
<p>
</p>
<h2><a name="post_maintenance_action">post_maintenance_action</a></h2>
<pre>
 Parameters  : none
 Returns     : boolean
 Description : Performs tasks to the computer after it has been put into
	       maintenance mode.</pre>
<p>
</p>
<hr />
<h1><a name="private_methods">PRIVATE METHODS</a></h1>
<p>
</p>
<h2><a name="driver">driver</a></h2>
<pre>
 Parameters  : none
 Returns     : Libvirt driver object
 Description : Returns a reference to the libvirt driver object which is created
	       when this libvirt.pm module is initialized.</pre>
<p>
</p>
<h2><a name="get_driver_name">get_driver_name</a></h2>
<pre>
 Parameters  : none
 Returns     : string
 Description : Returns the name of the libvirt driver being used to control the
	       node. Example: 'KVM'</pre>
<p>
</p>
<h2><a name="get_domain_name">get_domain_name</a></h2>
<pre>
 Parameters  : none
 Returns     : string
 Description : Returns the name of the domain. This name is passed to various
	       virsh commands. It is also the name displayed in virt-manager.
	       Example: 'vclv99-197:vmwarewin7-Windows764bit1846-v3'</pre>
<p>
</p>
<h2><a name="get_domain_file_base_name">get_domain_file_base_name</a></h2>
<pre>
 Parameters  : none
 Returns     : string
 Description : Returns the base name for files created for the current
	       reservation. A file extension is not included. This file name is
	       used for the domain's XML definition file and it's copy on write
	       image file. Example: 'vclv99-37_234-v23'</pre>
<p>
</p>
<h2><a
name="get_domain_xml_directory_path">get_domain_xml_directory_path</a></h2>
<pre>
 Parameters  : none
 Returns     : string
 Description : Returns the directory path on the node where domain definition
	       XML files reside. The directory used is: '/tmp/vcl'</pre>
<p>
</p>
<h2><a name="get_domain_xml_file_path">get_domain_xml_file_path</a></h2>
<pre>
 Parameters  : none
 Returns     : string
 Description : Returns the domain XML definition file path on the node.
	       Example: '/tmp/vcl/vclv99-37_234-v23.xml'</pre>
<p>
</p>
<h2><a
name="get_master_image_directory_path">get_master_image_directory_path</a></h2>
<pre>
 Parameters  : none
 Returns     : string
 Description : Returns the directory path on the node where the master image
	       files reside. Example: '/var/lib/libvirt/images'</pre>
<p>
</p>
<h2><a
name="get_master_image_file_path">get_master_image_file_path</a></h2>
<pre>
 Parameters  : $image_name (optional)
 Returns     : string
 Description : Returns the path on the node where the master image file resides.
	       Example:
	       '/var/lib/libvirt/images/vmwarelinux-RHEL54Small2251-v1.qcow2'</pre>
<p>
</p>
<h2><a
name="get_copy_on_write_file_path">get_copy_on_write_file_path</a></h2>
<pre>
 Parameters  : none
 Returns     : string
 Description : Returns the path on the node where the copy on write file for the
	       domain resides. Example:
	       '/var/lib/libvirt/images/vclv99-197_2251-v1.qcow2'</pre>
<p>
</p>
<h2><a name="delete_existing_domains">delete_existing_domains</a></h2>
<pre>
 Parameters  : none
 Returns     : boolean
 Description : Deletes existing domains which were previously created for the
	       computer assigned to the current reservation.</pre>
<p>
</p>
<h2><a name="delete_domain">delete_domain</a></h2>
<pre>
 Parameters  : $domain_name
 Returns     : boolean
 Description : Deletes a domain from the node.</pre>
<p>
</p>
<h2><a name="generate_domain_xml">generate_domain_xml</a></h2>
<pre>
 Parameters  : none
 Returns     : string
 Description : Generates a string containing the XML definition for the domain.

</pre>
<p>
</p>
<h2><a name="get_domain_info">get_domain_info</a></h2>
<pre>
 Parameters  : none
 Returns     : hash reference
 Description : Retrieves information about all of the domains defined on the
	       node and constructs a hash containing the information. Example:
		  &quot;vclv99-197:vmwarewin7-Windows764bit1846-v3&quot; =&gt; {
		     &quot;id&quot; =&gt; 135,
		     &quot;state&quot; =&gt; &quot;paused&quot;
		  },
		  &quot;vclv99-37:vmwarewinxp-base234-v23&quot; =&gt; {
		     &quot;state&quot; =&gt; &quot;shut off&quot;
		  }

</pre>
<p>
</p>
<h2><a name="get_domain_xml">get_domain_xml</a></h2>
<pre>
 Parameters  : $domain_name
 Returns     : hash reference
 Description : Retrieves the XML definition of a domain already defined on the
	       node. Generates a hash using XML::Simple::XMLin.

</pre>
<p>
</p>
<h2><a name="domain_exists">domain_exists</a></h2>
<pre>
 Parameters  : $domain_name
 Returns     : boolean
 Description : Determines if the domain is defined on the node.

</pre>
<p>
</p>
<h2><a name="get_snapshot_info">get_snapshot_info</a></h2>
<pre>
 Parameters  : $domain_name
 Returns     : hash reference
 Description : Retrieves snapshot information for the domain specified by the
	       argument and constructs a hash. The hash keys are the snapshot
	       names. Example:
		  &quot;VCL snapshot&quot; =&gt; {
		     &quot;creation_time&quot; =&gt; &quot;2011-12-07 16:05:50 -0500&quot;,
		     &quot;state&quot; =&gt; &quot;shutoff&quot;
		  }

</pre>
<p>
</p>
<h2><a name="create_snapshot">create_snapshot</a></h2>
<pre>
 Parameters  : $domain_name, $description
 Returns     : boolean
 Description : Creates a snapshot of the domain specified by the argument.

</pre>
<p>
</p>
<h2><a name="delete_snapshot">delete_snapshot</a></h2>
<pre>
 Parameters  : $domain_name, $snapshot
 Returns     : boolean
 Description : Deletes a snapshot created of the domain specified by the
	       argument.

</pre>
<p>
</p>
<h2><a name="get_image_size_bytes">get_image_size_bytes</a></h2>
<pre>
 Parameters  : $image_name (optional)
 Returns     : integer
 Description : Returns the size of the image in bytes.

</pre>
<p>
</p>
<h2><a
name="find_repository_image_file_paths">find_repository_image_file_paths</a></h2>
<pre>
 Parameters  : $image_name (optional)
 Returns     : array
 Description : Locates valid image files stored in the image repository.
	       Searches for all files beginning with the image name and then
	       checks the results to remove any files which should not be
	       included. File extensions which are excluded: vmx, txt, xml
	       If multiple vmdk files are found it is assumed that the image is
	       one of the split vmdk formats and the &lt;image name&gt;.vmdk contains
	       the descriptor information. This file is excluded because it
	       causes qemu-img to fail.

</pre>
<p>
</p>
<hr>
<a name="LibvirtProvisioningModule-"></a>

# KVM.pm {#kvmpm}


<p><a name="__index__"></a></p>

<ul>

	<li><a href="#name">NAME</a></li>
	<li><a href="#description">DESCRIPTION</a></li>
	<li><a href="#object_methods">OBJECT METHODS</a></li>
	<ul>

		<li><a href="#initialize">initialize</a></li>
		<li><a href="#get_domain_type">get_domain_type</a></li>
		<li><a
href="#get_disk_driver_name">get_disk_driver_name</a></li>
		<li><a href="#get_disk_format">get_disk_format</a></li>
		<li><a
href="#get_disk_file_extension">get_disk_file_extension</a></li>
		<li><a href="#pre_define">pre_define</a></li>
	</ul>

	<li><a href="#private_methods">PRIVATE METHODS</a></li>
	<ul>

		<li><a
href="#get_virtual_disk_file_info">get_virtual_disk_file_info</a></li>
		<li><a
href="#get_virtual_disk_size_bytes">get_virtual_disk_size_bytes</a></li>
		<li><a href="#copy_virtual_disk">copy_virtual_disk</a></li>
		<li><a
href="#create_copy_on_write_image">create_copy_on_write_image</a></li>
		<li><a
href="#update_windows_image">update_windows_image</a></li>
	</ul>

	<li><a href="#see_also">SEE ALSO</a></li>
</ul>
<!-- INDEX END -->

<hr />
<p>
</p>
<h1><a name="name">NAME</a></h1>
<p>VCL::Provisioning::libvirt::KVM - Libvirt hypervisor driver module to
allow support for the KVM hypervisor</p>
<p>
</p>
<hr />
<h1><a name="description">DESCRIPTION</a></h1>
<pre>
 This is a driver module to allow the main libvirt.pm provisioning module to
 support KVM hosts. It performs the KVM-specific tasks not handled by libvirt
 itself.</pre>
<p>
</p>
<hr />
<h1><a name="object_methods">OBJECT METHODS</a></h1>
<p>
</p>
<h2><a name="initialize">initialize</a></h2>
<pre>
 Parameters  : none
 Returns     : boolean
 Description : Checks if the node has KVM installed by checking if /usr/bin/qemu
	       exists. Returns true if the file exists, false otherwise.</pre>
<p>
</p>
<h2><a name="get_domain_type">get_domain_type</a></h2>
<pre>
 Parameters  : none
 Returns     : string
 Description : Returns 'kvm'. This is specified in the domain XML definition:
		  &lt;domain type='kvm'&gt;</pre>
<h2><a name="get_disk_driver_name">get_disk_driver_name</a></h2>
<pre>
 Parameters  : none
 Returns     : string
 Description : Returns 'qemu'. The disk driver name is specified in the domain
	       XML definition:
		  &lt;domain ...&gt;
		     &lt;devices&gt;
			&lt;disk ...&gt;
			   &lt;driver name='qemu' ...&gt;</pre>
<p>
</p>
<h2><a name="get_disk_format">get_disk_format</a></h2>
<pre>
 Parameters  : none
 Returns     : string
 Description : Returns 'qcow2'. The disk format is specified in the domain XML
	       definition:
		  &lt;domain ...&gt;
		     &lt;devices&gt;
			&lt;disk ...&gt;
			   &lt;driver type='qcow2' ...&gt;</pre>
<p>
</p>
<h2><a name="get_disk_file_extension">get_disk_file_extension</a></h2>
<pre>
 Parameters  : none
 Returns     : string
 Description : Returns 'qcow2'. This is used by libvirt.pm as the file extension
	       of the virtual disk file paths.</pre>
<p>
</p>
<h2><a name="pre_define">pre_define</a></h2>
<pre>
 Parameters  : none
 Returns     : boolean
 Description : Performs the KVM-specific steps prior to defining a domain:
	       * Checks if the master image file exists on the node, If it does
	    	 not exist, attempts to copy image from repository to the node
	       * Creates a copy on write image which will be used by the domain
	    	 being loaded</pre>
<p>
</p>
<hr />
<h1><a name="private_methods">PRIVATE METHODS</a></h1>
<p>
</p>
<h2><a
name="get_virtual_disk_file_info">get_virtual_disk_file_info</a></h2>
<pre>
 Parameters  : $virtual_disk_file_path
 Returns     : hash reference
 Description : Calls 'qemu-img info' to retrieve the virtual disk information.
	       Builds a hash based on the output. Example:
		  &quot;backing_file&quot; =&gt; &quot;/var/lib/libvirt/images/vmwarewinxp-base234-v23.qcow2 (actual path:
/var/lib/libvirt/images/vmwarewinxp-base234-v23.qcow2)&quot;, 
		  &quot;backing_file_actual_path&quot; =&gt; &quot;/var/lib/libvirt/images/vmwarewinxp-base234-v23.qcow2&quot;,
		  &quot;cluster_size&quot; =&gt; 65536,
		  &quot;disk_size&quot; =&gt; &quot;423M&quot;,
		  &quot;disk_size_bytes&quot; =&gt; 443547648,
		  &quot;file_format&quot; =&gt; &quot;qcow2&quot;,
		  &quot;image&quot; =&gt; &quot;/var/lib/libvirt/images/vclv99-37_234-v23.qcow2&quot;,
		  &quot;snapshot&quot; =&gt; {
		    1 =&gt; {
		      &quot;date&quot; =&gt; &quot;2011-12-07 14:43:12&quot;,
		      &quot;tag&quot; =&gt; &quot;snap1&quot;,
		      &quot;vm_clock&quot; =&gt; &quot;00:00:00.000&quot;,
		      &quot;vm_size&quot; =&gt; 0
		    }
		  },
		  &quot;virtual_size&quot; =&gt; &quot;20G (21474836480 bytes)&quot;,
		  &quot;virtual_size_bytes&quot; =&gt; &quot;21474836480&quot;</pre>
<p>
</p>
<h2><a
name="get_virtual_disk_size_bytes">get_virtual_disk_size_bytes</a></h2>
<pre>
 Parameters  : $image_name (optional)
 Returns     : integer
 Description : Returns the size of the virtual disk in bytes.</pre>
<p>
</p>
<h2><a name="copy_virtual_disk">copy_virtual_disk</a></h2>
<pre>
 Parameters  : $source_file_paths, $destination_file_path, $disk_format (optional)
 Returns     : boolean
 Description : Calls qemu-img to copy a virtual disk image. The destination disk
	       format can be specified as an argument. If omitted, qcow2 is
	       used.</pre>
<p>
</p>
<h2><a
name="create_copy_on_write_image">create_copy_on_write_image</a></h2>
<pre>
 Parameters  : $master_image_file_path, $copy_on_write_file_path
 Returns     : boolean
 Description : Calls qemu-img to create a copy on write virtual disk image based
	       on the master image. The resulting image is written to by the VM
	       when it makes changes to its hard disk. Multiple VMs may utilize
	       the master image file. Each writes to its own copy on write image
	       file. The master image file is not altered.</pre>
<p>
</p>
<h2><a name="update_windows_image">update_windows_image</a></h2>
<pre>
 Parameters  : $virtual_disk_file_path
 Returns     : boolean
 Description : Runs virt-win-reg to update the registry of the image specified
	       by the $virtual_disk_file_path argument. The virt-win-reg utility
	       is provided by libguestfs-tools. This subroutine returns true if
	       virt-win-reg isn't installed.

	       Adds registry keys to disable VMware services. If the image is
	       Windows 5.x, registry keys are added to enable the builtin IDE
	       drivers. This allows Windows images converted from VMware using a
	       SCSI virtual disk to be loaded on KVM.</pre>
