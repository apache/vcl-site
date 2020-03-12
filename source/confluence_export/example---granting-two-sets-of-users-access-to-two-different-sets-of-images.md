---
title: Example - Granting Two Sets of Users Access to Two Different Sets of Images
---

This page explains how to grant one groups of users access to one set of
images, and another set of users access to a separate set of images.

After looking over these steps, you can [watch a video](video---granting-two-sets-of-users-access-to-two-different-sets-of-images.html)
 of the steps being performed.

<a name="Example-GrantingTwoSetsofUsersAccesstoTwoDifferentSetsofImages-1.CreateaUserGroupforEachSetofUsers"></a>
## 1. Create a User Group for Each Set of Users
First, you need to create two user groups - one for each set of users.
1. Click Manage Groups
1. Under the User Groups section (at the top):
1. # Enter a name for the group (it can include spaces)
1. # (Optionally, if it shows up) select an affiliation for the group
1. # Enter an owner of the group - probably yourself
1. # Select a group allowed to edit the user group
1. # The rest of the fields can be left as defaults
1. Click Add
1. Repeat the steps for the second group

For the rest of the page, I'll call the groups *faculty* and *student*

<a name="Example-GrantingTwoSetsofUsersAccesstoTwoDifferentSetsofImages-2.AddUserstoEachGroup"></a>
## 2. Add Users to Each Group
You need to add users to each of the groups.
1. Click Manage Groups if you're not still on that page
1. Click Edit next to the *faculty* group
1. Enter a userid in the box next to the Add button (NOTE: if you are not
using LDAP authentication, the users' accounts will already need to exist
in VCL)
1. Click Add
1. Repeat for all users you wish to add to the *faculty* group
1. Repeat these steps for the *student* group

<a name="Example-GrantingTwoSetsofUsersAccesstoTwoDifferentSetsofImages-3.CreateanImageGroupforEachSetofImages"></a>
## 3. Create an Image Group for Each Set of Images

Next, you need to create an image group for each set of images.
1. Click Manage Groups if you're not still on that page
1. Under the Resource Groups section (further down the page):
1. # Select Image as the type
1. # Enter a name for the group (it can contain spaces)
1. # Select a user group that will own the resource group (this user group
will have access to manage some aspects of the resource group)
1. Click Add
1. Repeat the steps for the second group

For the rest of the page, I'll call the groups *faculty images* and
*student images*

<a name="Example-GrantingTwoSetsofUsersAccesstoTwoDifferentSetsofImages-4.AddImagestoEachGroup"></a>
## 4. Add Images to Each Group
Now, you need to add the desired images to each group.
1. Click Manage Images
1. Select the Edit Image Grouping radio button
1. Click Submit
1. Click the *By Group* tab
1. Select *faculty images*
1. Click Get Images
1. Select any images you want to be available to the *faculty* user group in
the list on the right (Ctrl+click to select multiple images)
1. Click the <-Add button
1. Repeat steps for the *student images* group

<a name="Example-GrantingTwoSetsofUsersAccesstoTwoDifferentSetsofImages-5.MaptheImageGroupstoComputerGroups"></a>
## 5. Map the Image Groups to Computer Groups
In order for VCL to know on which computers the images can run, you must
map the image groups to computer groups. I'll assume you already have one
or more computer groups that contain computers.
1. Click Manage Images
1. Select the Edit Image Mapping radio button
1. Click Submit
1. Select the *faculty images* group
1. Click Get Computer Groups
1. Select at least one computer group to map it to from the list on the
right
1. Click the <-Add button
1. Repeat for the *student images* group (NOTE: It is okay to map both image
groups to the same computer group. That will not affect what images the
users have access to.)

<a name="Example-GrantingTwoSetsofUsersAccesstoTwoDifferentSetsofImages-6.CreateaTwoPrivilegeNodes"></a>
## 6. Create a Two Privilege Nodes
Now, you need to create one node for each user group to separate their
access.
1. Click Privileges
1. In the tree at the top of the page, click a node under which you'll
create the two new nodes
1. Click the Add Child button
1. Enter a name for the new node (spaces are allowed)
1. Click Create Child
1. Repeat for the second node for the other user group

I'll refer to these nodes as *faculty access* and *student access*

<a name="Example-GrantingTwoSetsofUsersAccesstoTwoDifferentSetsofImages-7.AssignRightsatEachNode"></a>
## 7. Assign Rights at Each Node
Finally, you need to give each user group the *imageCheckOut* privilege at
their respective nodes, and give each image group the *available* attribute
at their respective nodes.
1. Click on the *faculty access* node
1. Under User Groups, click Add Group
1. Select the *faculty* group
1. Select the checkbox for the *imageCheckOut* privilege
1. Click Submit New User Group
1. Scroll down to the Resources section and click Add Resource Group
1. Select the *image/faculty images* group
1. Select the checkbox for the *available* attribute
1. Click Submit New Resource Group
1. Click on the *student access* node
1. Under User Groups, click Add Group
1. Select the *student* group
1. Select the checkbox for the *imageCheckOut* privilege
1. Click Submit New User Group
1. Scroll down to the Resources section and click Add Resource Group
1. Select the *image/student images* group
1. Select the checkbox for the *available* attribute
1. Click Submit New Resource Group

<a name="Example-GrantingTwoSetsofUsersAccesstoTwoDifferentSetsofImages-Summary"></a>
## Summary
Now, users in the *faculty* user group will have access to check out images
in the *faculty images* image group, and users in the *student* user group
will have access to check out images in the *student images* image group.
