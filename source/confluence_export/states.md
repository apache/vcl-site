---
title: States
---

<a name="States-RequestStates"></a>
## Request States

<table>
<tr><th> Request State </th><th> Processed by Module </th><th> Description </th></tr>
<tr><td> new </td><td> new.pm </td><td> * Normal reservation initiated by user
</tr>
* Computer is reloaded if image specified for reservation is not preloaded
* User account is added to computer |
<tr><td> reload </td><td> new.pm </td><td> * Reservation only reloads computer
</tr>
* Computer is reloaded if image specified for reservation is not preloaded
|
<tr><td> tomaintenance </td><td> new.pm </td><td> * Simply changes the computer state to
maintenance
</tr>
* Initiated from Manage Computers page when computer state is changed to
maintenance |
<tr><td> tovmhostinuse </td><td> new.pm </td><td> * Computer is reloaded with image specified in
the VM profile. If using xCAT or some other physical provisioning engine. 
</tr>
* Computer state is set to vmhostinuse after it has been reloaded |
<tr><td> reserved </td><td> reserved.pm </td><td> * User account is added to computer
</tr>
* Computer state is set to reserved
* Computer is polled for user connection for approximately 15 minutes |
<tr><td> inuse </td><td> inuse.pm </td><td> * Request enters inuse state after&nbsp;user
connection has been detected
</tr>
* Periodically polls computer for user connection
* If user connection isn't detected for approximately 15 minutes, request
state is changed to timeout
* Notifies user when reservation end time is approaching |
<tr><td> timeout </td><td> reclaim.pm </td><td> * Occurs if user never connects to computer or if
inuse state detected that the user was disconnected for approximately 15
minutes
</tr>
* Computer is reloaded if the user ever connected
* Computer is sanitized if the user did not connect (user account removed
from computer) |
<tr><td> deleted </td><td> reclaim.pm </td><td> * Occurs when a user clicks the End button
</tr>
* Computer is reloaded if the user ever connected
* Computer is sanitized if the user did not connect (user account removed
from computer) |
<tr><td> image </td><td> image.pm </td><td> * Occurs when a user makes an imaging reservation and
clicks Create Image
</tr>
* Image is captured |
<tr><td> makeproduction </td><td> makeproduction.pm </td><td> * Occurs when a user is the owner of
an image and changes the production revision
</tr>
* At the current time, simply changes the production revision in the
database (could potentially reload computers which have been loaded with
the previous production revision in the future) |
<tr><td> complete </td><td> vcld </td><td> * Occurs after another state is done but before a
reservation is actually deleted from the database
</tr>
* Allows reservations to remain in the database until the end time is
reached under certain conditions
* If a reservation times out, it remains in the database until the end time
is reached so that it is displayed on the user's Current Reservations page
in order to notify that it timed out
* Reservation is deleted from the database by vcld when its end time is
reached |
<tr><td> failed </td><td> None </td><td> * Occurs when a problem occurs with a reservation which
wasn't in the image state </td></tr>
<tr><td> maintenance </td><td> None </td><td> * Occurs when a problem occurs with a reservation
which is in the image state capturing an image 
</tr>
* Used to place computers into a maintenance state, the system will not
assign any resources in the maintenance state.
* Also applies to management nodes. When a management node is in the
maintenance state, the web schedule system will not assign any resources
soley under that management node to end-user requests.|
<tr><td>pending </td><td> none </td><td> * Used as a transition or processing state. Set when a
management node starts working on the request.
</tr>
