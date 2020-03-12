---
title: Granting Access to a New Image
---

<a name="GrantingAccesstoaNewImage-Overview"></a>
## Overview

Once you have created a new image, there are a few things you have to do to
allow other people to use it.&nbsp; If you don't have access to do any of
the following steps, you will need to get a VCL administrator to do them
for you.

When you create a new image, it is only available to you, and it is only
allowed to be run on a few computers that have been set aside for the
testing of new images.

*NOTE*: After you have been through these steps one time, if you are
granting the same set of users access to a new image, you may only have to
perform step 1.1 for subsequent images.


<a name="GrantingAccesstoaNewImage-Step1:ImageMapping"></a>
## Step 1: Image Mapping

Images are mapped to be run on a set of computers. See the documentation on [Resource Mapping](for-vcl-users#resourcemapping.html)
 to learn more about why this is done. For your new image to be able to run
on more computers than just those designated for testing, you need to map
it to a set of computers. There are a few steps to this process:
1. You need to make your image a member of an image group
1. * Select {color:#0000ff}Manage Images{color}\->{color:#0000ff}Edit Image
Grouping{color}
1. * Select your image from the drop down box and click {color:#0000ff}Get
Groups{color}
1. * Choose one or more image groups to which you would like to add the image
from the box on the right
1. * Click {color:#0000ff}<-Add{color} to make the image a member of the
group(s)
1. You need to map the image group(s) you selected in #1 to one or more
computer groups (if they are not already mapped)
1. * Select {color:#0000ff}Manage Images{color}\->{color:#0000ff}Edit Image
Mapping{color}
1. * Do the following for each group from #1:
1. ** Select the image group from the drop down box and click
{color:#0000ff}Get Computer Groups{color}
1. ** Choose one or more computer groups to which you would like to map the
image group from the box on the right
1. ** click {color:#0000ff}<-Add{color} to map the image group to the
computer group(s)
1. * *Note*: there is an assumption here that the computer groups you
selected already have computers that are in those groups

<a name="GrantingAccesstoaNewImage-Step2:Privileges"></a>
## Step 2: Privileges

Now, you need to grant access to use the image to a user or group of users
under the Privileges section of the site.&nbsp; Here are the steps
involved:
1. Select {color:#0000ff}Privileges{color}
1. Choose an existing node or create a new node in the tree structure in the
upper portion of the page where you would like to assign the user(s) access
1. Now, you need to grant the user {color:#0000ff}imageCheckOut{color} at
the node.&nbsp; You can do this for an individual user or a group of users.
1. * Individual User:
1. ** Click {color:#0000ff}Add User{color}
1. ** Enter the user's id (you may need to include the user's affiliation) in
the text box and select the {color:#0000ff}imageCheckOut{color} checkbox
1. ** Click {color:#0000ff}Submit New User{color}
1. * User Group:
1. ** Click {color:#0000ff}Add Group{color}
1. ** Select the user group from the drop-down box and select the
{color:#0000ff}imageCheckOut{color} checkbox
1. ** Click {color:#0000ff}Submit New User Group{color}
1. Next, you need to make sure the image group in which you placed the image
in #1 of *Image Mapping* is available at this node. If it is, go on to the
next step, if not:
1. * Click {color:#0000ff}Add Resource Group{color}
1. * Select the image group from the drop-down box and select the
{color:#0000ff}available{color} checkbox
1. * Click {color:#0000ff}Submit New Resource Group{color}
1. Finally, you need to make sure the computer group(s) selected in #2 of
*Image Mapping* are also available here. If so, you are finished.&nbsp; If
not:
1. * Click {color:#0000ff}Add Resource Group{color}
1. * Select the computer group from the drop-down box and select the
{color:#0000ff}available{color} checkbox
1. * Click {color:#0000ff}Submit New Resource Group{color}

Now, the user or user groups you have added to this node will be able to
make reservations for the new image.
