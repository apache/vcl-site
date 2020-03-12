---
title: Granting Access to a New Image
---

## Overview

Once you have created a new image, there are a few things you have to do to allow 
other people to use it.  If you don't have access to do any of the following steps, 
you will need to get a VCL administrator to do them for you.

When you create a new image, it is only available to you, and it is only allowed 
to be run on a few computers that have been set aside for the testing of new images.

**NOTE**: After you have been through these steps one time, if you are granting the same 
set of users access to a new image, you may only have to perform step 1.1 for subsequent 
images.

## Step 1: Image Mapping

Images are mapped to be run on a set of computers. See the documentation on 
[Resource Mapping](administrationconcepts.html#resource-mapping) to learn 
more about why this is done. For your new image to be able to run 
on more computers than just those designated for testing, you need to map it to a 
set of computers. There are a few steps to this process:

1. You need to make your image a member of an image group
    * Select **Manage Images->Edit Image Grouping**
    * Select your image from the drop down box and click **Get Groups**
    * Choose one or more image groups to which you would like to add the image from the box on the right
    * Click **<-Add** to make the image a member of the group(s)
2. You need to map the image group(s) you selected in #1 to one or more computer groups (if they are not already mapped)
    * Select **Manage Images->Edit Image Mapping**
    * Do the following for each group from #1:
        * Select the image group from the drop down box and click **Get Computer Groups**
        * Choose one or more computer groups to which you would like to map the image group from the box on the right
        * click **<-Add** to map the image group to the computer group(s)
    * **Note**: there is an assumption here that the computer groups you selected 
already have computers that are in those groups

## Step 2: Privileges

Now, you need to grant access to use the image to a user or group of users under the Privileges section of the site.  Here are the steps involved:

1. Select **Privileges**
2. Choose an existing node or create a new node in the tree structure in the upper portion of the page where you would like to assign the user(s) access
3. Now, you need to grant the user **imageCheckOut** at the node.  You can do this for an individual user or a group of users.
    * Individual User:
        * Click **Add User**
        * Enter the user's id (you may need to include the user's affiliation) in the text box and select the **imageCheckOut** checkbox
        * Click **Submit New User**
    * User Group:
        * Click **Add Group**
        * Select the user group from the drop-down box and select the **imageCheckOut** checkbox
        * Click **Submit New User Group**
4. Next, you need to make sure the image group in which you placed the image in #1 of **Image Mapping** is available at this node. If it is, go on to the next step, if not:
    * Click **Add Resource Group**
    * Select the image group from the drop-down box and select the **available** checkbox
    * Click **Submit New Resource Group**
5. Finally, you need to make sure the computer group(s) selected in #2 of **Image Mapping** are also available here. If so, you are finished.  If not:
    * Click **Add Resource Group**
    * Select the computer group from the drop-down box and select the **available** checkbox
    * Click **Submit New Resource Group**

Now, the user or user groups you have added to this node will be able to make reservations for the new image.
