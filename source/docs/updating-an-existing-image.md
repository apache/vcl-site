---
title: Updating an Existing Image
---

This is a continuation of other pages, if you did not come from [Save the Image](save-the-image.html)
, you should start at [Creating a New Image from a Base Image](creating-a-new-image-from-a-base-image.html)
.

<a name="UpdatinganExistingImage-UnderstandingImageRevisions"></a>
## Understanding Image Revisions
Each VCL image can have multiple revisions. When a VCL image is saved, all
data from the image's disk is saved in disk image files. A revision is
still a full set of disk image files, but information about each revision
allows them to be tracked as a series of updates to a VCL image. Think
about it like writing a paper. If you print a first draft, you end up with
the 1st revision of the paper. After making some changes and printing it
again, you end up with the 2nd revision of the paper.  Now, you have two
physical copies of the paper. The 2nd one is based on and very similar to
the 1st one, but it is still a separate copy of it. You could end up with
more revisions if you make more changes. When you decide to publish it, you
can choose any of the revisions, though you'll most likely choose the most
recent one.

With VCL, you can make as many revisions as you want, and you can select
which is the **production** image, that is, the one users get when they make
a reservation. You can select which revision is in production by going to
Manage Images-&gt;Edit Image Profiles, and clicking Edit next to the
desired image. Then, scroll down to the bottom of the page and select the
radio button for the revision you would like to be in production.

Only the owner of an image can create new revisions of it. If you need
someone else to update an image, simply change the owner of the image to
that person (and make sure they have access to update images).

## Steps to Finish Updating an Existing Image

1. After selecting Update Existing Image, click Submit
1. The next page will present you with an Install Agreement stating that all
software in the image is appropriately licensed
1. Click **I agree** (clicking _I do not agree_ will take you back to Current
Reservations)
1. On the next page, enter any notes for yourself and other admins about the
image. These notes are not viewable by normal users - only people with
access to manage the image.
1. Click **Create New Revision** to start the imaging process
