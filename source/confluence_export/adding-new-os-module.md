---
title: Adding New OS Module
---

This is a short guide on how to set up development environment for a OS
Module.

# Install VCL {#installvcl}

* Follow the install guide linked to from the [download](/downloads/download.cgi)
page.

# Setting up a new OS Module {#settingupanewosmodule}

* Start by creating a Module/OS/...pm file.
    * See the other OS Module for examples.
    * Set the package path in the file<br>
package VCL::Module::OS::...;
* Add an entry to the module table pointing to your new module with the
package path mentioned above.
* Add an entry to the OS table pointing to the entry you add to the module
table.
* Add entries to the image and imagerevision table for a base new image,
with image.OSid pointing to the entry you add to the OS table.
* Enter the computer information for a loaded new machine into VCL and make
sure that the management node can access this machine via SSH.
* Insert the code you want to test at the
beginning of the process() subroutine in new.pm, followed by a call to
exit:

    ```perl
    sub process {
    my $self = shift;

    my $request_data = $self->data->get_request_data();
    ...
    my $imagerevision_id = $self->data->get_imagerevision_id();

    print "\n\n---\n\n";

    my $ip = $self->os->get_public_ip_address();
    print "IP: $ip\n";

    print "\n\n---\n\n";
    exit;
    ...
    ```

* To test things over and over again, run a script which inserts entries
into the request and reservation tables with the request state and
laststate set to 'new'.  vcld picks up the reservation, configures
everything as it would for a normal reservation, calls new.pm::process(),
test code is executed, then the process exits.
* Once this is set up, it should be pretty efficient to test all of the
subroutines in OS module.