---
title: Creating a Cluster environment
---

Cluster environments are created from existing VCL images.

The terms **parent** and **child** are used in this document and with the VCL
provisioning:

**parent** - the primary image or selectable image through the VCL New
Reservation menu

**child** - the second image or images that are also loaded and are the sub
images associated with the parent image


### To Create a cluster image

1. Select **Manage Images -> Edit Image Profiles**
1. Select **Edit** beside the parent image
1. Click on **Advanced Options** to expand that section
1. Select **Manage Subimages**
1. In the window, select a child image
    * The child image can be the same as the parent image or another.
1. Repeat adding as many subimages as needed (or have nodes for).
