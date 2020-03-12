---
title: Image Capture Sequence
---

## Modularization Example

The following diagram shows how the image capture sequence
differs if different provisioning modules are used -- xCAT and
VMWare.

Take note of the following:

* The calls made by image.pm to the xCAT and VMWare capture()
subroutines are **identical**.  The image.pm state module does not
care which provisioning engine is being used. All it knows is that a
provisioning engine object has been created before image.pm::process() was
called, the object can be accessed via $self->provisioner, and the
name of the subroutine to call is capture().
* The calls made by xCAT and VMWare's capture() subroutine to the
Windows.pm pre_capture() subroutine are **identical**. All a
provisioning engine module needs to know is that an OS object has been
created, the object can be accessed via $self->os, and the name of the
subroutine to call is pre_capture().
* Provisioning engine modules do not not need to know any of the operating
system details. They assume the OS module's pre_capture()
subroutine will perform all the steps necessary for the particular OS to be
captured and that the computer will be shut down (or left in the state
specified by the end_state argument) when pre_capture() returns.
* The OS module's pre_capture() subroutine does not care which
provisioning engine is being used.  The steps it performs are
identical.
* A very similar example could be made using the same provisioning engine
module and different OS modules.

<img src="image_capture_sequence_xcat.png">