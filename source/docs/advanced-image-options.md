---
title: Advanced Image Options
---

There are several advanced options for each image that can be modified.
Normally, they can be left alone. However, there are times where it is
useful to set them. These are the advanced options and their descriptions.
They are listed in the same order they appear on the Edit Image page.

The following advanced options are compared directly to corresponding
computer attributes of the VCL computers. Configuring these fields
restricts which computers can be assigned to run the image based on
computer specs.
<table>
<tr>
<th>Minimum RAM (MB)</th>
<td>This is the minimum RAM required for the image to
function and is specified in MB. This is useful if the image has software
installed that will not function without at least some specific amount of
RAM. The VCL scheduler will not assign a user a computer to run the image
that has less RAM than what is specified here.</td>
</tr>
<tr>
<th>Minimum Num of Processors</th>
<td>This is the minimum number of processors
required for the image to function. This is useful if the image has
software installed that will not function without at least some specific
number of processors. The VCL scheduler will not assign a user a computer
to run the image that has fewer processors than what is specified here.
**NOTE**: It is up to the VCL site administrators to determine if this field
and the corresponding **No. Processors** computer field mean actual
processors or processor cores. Most often, it makes the most sense to have
it mean processor cores.</td>
</tr>
<tr>
<th>Minimum Processor Speed (MHz)</th>
<td>This is the minimum processor speed
required for the image to function and is specified in MHz. This is useful
if the image has software installed that will not function without at least
a specific processor speed. The VCL scheduler will not assign a user a
computer to run the image that has a slower processor speed than what is
specified here.</td>
</tr>
<tr>
<th>Minimum Network Speed (Mbps)</th>
<td>This is the minimum network speed required
for the image to function and is specified in Mbps. This is useful if the
image has software installed that will not function without at least a
specific network speed. The VCL scheduler will not assign a user a computer
to run the image that has a slower network speed than what is specified
here. This only refers to the speed at which the VCL computer is connected
to the network. It is not related to the end user's network connection.</td>
</tr>
</table>
<br/>
These advanced options are only related to the image itself.<br/>
<br/>
<table>
<tr>
<th>Maximum Concurrent Usage</th>
<td>This field allows the concurrent usage of the
image to be limited. It is very useful if you only have a fixed number of
licenses for an application installed in the image, but no network license
manager to limit concurrent use. Leave the field empty for unlimited use.
Enter a number to limit concurrent use of the image to that number.</td>
</tr>
<tr>
<th>Estimated Reload Time (min)</th>
<td>This is the estimated amount of time it will
take the image to be loaded. It is only relevant for the first few
reservations of an image. After that, historical data is used to estimate
the load time.</td>
</tr>
<tr>
<th>Available for checkout</td>
<td>This field controls whether this image can show up
on the New Reservations page (if set to yes, the appropriate permissions
still need to be set for it to show up). The intended use of this field is
for cluster environments where an image will have several sub images. In
some of those cases, it doesn't make sense for end users to be able to make
a reservation for the sub  images directly. In those cases, set this field
to **No**. Otherwise, you should leave it as **Yes**.</td>
</tr>
<tr>
<th>Check for logged in user</th>
<td>If set to **yes**, VCL will perform checks to see
if a user is connected to a reservation for this image. If a user has
connected, but disconnects and stays disconnected for 15 minutes, then VCL
will consider the reservation to be inactive. It will time out the
reservation and reclaim the machine for someone else to use. Setting this
option to **no** disables this check, causing the reservation to exist until
its end time, even if no one is connected to it.</td>
</tr>
<tr>
<th>User group allowed to log in</th>
<td>This options is antiquated and should be
left as **Any**.</td>
</tr>
<tr>
<th>Subimages</th>
<td>This is used to create [Cluster Environments](creating-a-cluster-enviroment.html)
. Any subimages listed here will be checked out in addition to this image
when a reservation is made for this image.</td>
</tr>
</table>