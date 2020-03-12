---
title: Example - Granting Two Sets of Users Access to Two Different Sets of Images
---

This page explains how to grant one groups of users access to one set of images, 
and another set of users access to a separate set of images.

After looking over these steps, you can watch a [video](example2users2images-video.html) of the steps being performed.

{{% toc %}}

## Create a User Group for Each Set of Users

First, you need to create two user groups - one for each set of users.

1. Click Manage Groups
2. Under the User Groups section (at the top):
    <ol type="a">
    <li>Enter a name for the group (it can include spaces)
    <li>(Optionally, if it shows up) select an affiliation for the group
    <li>Enter an owner of the group - probably yourself
    <li>Select a group allowed to edit the user group
    <li>The rest of the fields can be left as defaults
    </ol>
3. Click Add
4. Repeat the steps for the second group

For the rest of the page, I'll call the groups **faculty** and **student**

## Add Users to Each Group

You need to add users to each of the groups.

1. Click Manage Groups if you're not still on that page
2. Click Edit next to the **faculty** group
3. Enter a userid in the box next to the Add button (NOTE: if you are not using 
LDAP authentication, the users' accounts will already need to exist in VCL)
4. Click Add
5. Repeat for all users you wish to add to the **faculty** group
6. Repeat these steps for the **student** group

## Create an Image Group for Each Set of Images

Next, you need to create an image group for each set of images.

1. Click Manage Groups if you're not still on that page
2. Under the Resource Groups section (further down the page):
    <ol type="a">
    <li>Select Image as the type
    <li>Enter a name for the group (it can contain spaces)
    <li>Select a user group that will own the resource group (this user group 
will have access to manage some aspects of the resource group)
    </ol>
3. Click Add
4. Repeat the steps for the second group

For the rest of the page, I'll call the groups **faculty images** and **student images**

## Add Images to Each Group

Now, you need to add the desired images to each group.

1. Click Manage Images
2. Select the Edit Image Grouping radio button
3. Click Submit
4. Click the **By Group** tab
5. Select **faculty images**
6. Click Get Images
7. Select any images you want to be available to the **faculty** user group 
in the list on the right (Ctrl+click to select multiple images)
8. Click the <-Add button
9. Repeat steps for the **student images** group

## Map the Image Groups to Computer Groups

In order for VCL to know on which computers the images can run, you must map 
the image groups to computer groups. I'll assume you already have one or more 
computer groups that contain computers.

1. Click Manage Images
2. Select the Edit Image Mapping radio button
3. Click Submit
4. Select the **faculty images** group
5. Click Get Computer Groups
6. Select at least one computer group to map it to from the list on the right
7. Click the <-Add button
8. Repeat for the **student images** group (NOTE: It is okay to map both image 
groups to the same computer group. That will not affect what images the users 
have access to.)

## Create a Two Privilege Nodes

Now, you need to create one node for each user group to separate their access.

1. Click Privileges
2. In the tree at the top of the page, click a node under which you'll create 
the two new nodes
3. Click the Add Child button
4. Enter a name for the new node (spaces are allowed)
5. Click Create Child
6. Repeat for the second node for the other user group

I'll refer to these nodes as **faculty access** and **student access**

## Assign Rights at Each Node

Finally, you need to give each user group the **imageCheckOut** privilege at 
their respective nodes, and give each image group the **available** attribute 
at their respective nodes.

1. Click on the **faculty access** node
* Under User Groups, click Add Group
* Select the **faculty** group
* Select the checkbox for the **imageCheckOut** privilege
* Click Submit New User Group
* Scroll down to the Resources section and click Add Resource Group
* Select the **image/faculty images** group
* Select the checkbox for the **available** attribute
* Click Submit New Resource Group
* Click on the **student access** node
* Under User Groups, click Add Group
* Select the **student** group
* Select the checkbox for the **imageCheckOut** privilege
* Click Submit New User Group
* Scroll down to the Resources section and click Add Resource Group
* Select the **image/student images** group
* Select the checkbox for the **available** attribute
* Click Submit New Resource Group

## Summary

Now, users in the **faculty** user group will have access to check out images 
in the **faculty images** image group, and users in the **student** user group 
will have access to check out images in the **student images** image group.
