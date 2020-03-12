---
title:     Customization of Email messages with HTML content
---

Email messages sent out to VCL users can be customized under the Site Configuration part of the
site. However, HTML content is not allowed to be entered via the web form for security reasons. 
VCL 2.5.1 introduced a method of including HTML content in the email messages using a command 
line script run from a management node. The script is in the bin directory of the management node 
code. The same substitution available in plain text messages can be used in the HTML messages.

Usage:

```bash
vclmessages.pl --getmessagenames
vclmessages.pl --dumpmessage '<name of message>'
vclmessages.pl --setmessage '<name of message>' --htmlfile <filename> --subject <message subject>
vclmessages.pl --resetmessage '<name of message>'

vclmessages.pl --help|-?
```

Where

--**getmessagenames** displays a list of all available names that can be used<br>
--**dumpmessage** displays the current value of a message<br>
--**setmessage** sets the value of a message to the contents of the specified file<br>
--**resetmessage** sets the value of a message back to the original value as distributed with VCL<br>

&lt;**name of message**&gt; = the name of the message from the database (enclose in single quotes)<br>
<span style="margin-left:40px;">(use --getmessagenames to get a list of message names)</span>

&lt;**filename**&gt; = filename (including path) of file containing html contents for email message

&lt;**message subject**&gt; = subject for email message (enclose in single quotes)

So, use --**getmessagenames** to get a list of all of the messages that can be set.  Use 
--**dumpmessage** to see the current contents of a message.

To set a new message, create a file containing the HTML that you would like used as the message. 
Then, use --**setmessage** to set the contents of the message, specifying both a message subject and 
the file containing the contents of the HTML message.  To reset a message back to the stock message 
supplied at VCL installation, use --**resetmessage**.  Only the "Global" messages can be reset.

To set a new message for a specific affiliation, an affiliation specific message, plain text 
message needs to be created through the web UI first. Then, that message can be converted to HTML 
using the script.