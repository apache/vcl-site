---
title: Adding Local VCL Accounts
---

Local VCL accounts are contained within the VCL database. The admin 
account is a local VCL account. Additional local accounts can be added 
after the backend management node component has been installed by 
executing the vcld file with the -setup argument:

```bash
/usr/local/vcl/bin/vcld --setup
```

<pre class="docnote">
It is safe to run vcld --setup while the normal vcld daemon process 
is running on a management node. Running vcld --setup will not 
affect it.
</pre>

You will see a menu. Enter the number next to the VCL Base Module entry:

```text
[root@mgt-node]# /usr/local/vcl/bin/vcld -setup
VCL Management Node Setup
----------------------------------------------------------------------------
Check Configuration
   1: Check Windows OS Module

Image Management
   2: Capture a Base Image

Management Node Configuration
   3: Test RPC-XML Access

Management Node Operations
   4: Check private IP addresses

User Accounts
   5: Add Local VCL User Account
   6: Set Local VCL User Account Password

VMware Provisioning Module
   7: VM Host Operations

Windows Image Configuration
   Activation
      8: Configure Key Management Service (KMS) Activation
      9: Configure Multiple Activation Key (MAK) Activation

[vcld]
Make a selection (1-9, 'c' to cancel):
```

Enter the number next to the Add Local VCL User Account entry:

```text
Make a selection (1-9, 'c' to cancel): 5
```

Enter the requested information:

```text
Enter the user login name ('c' to cancel):
localuser

Enter the first name ('c' to cancel):
Local

Enter the last name ('c' to cancel):
User

Enter the email address [not set]:
localuser@example.com

Enter the password ('c' to cancel):
somepassword
```

After adding the local user account, you can continue to navigate the 
menus or press Ctrl-C to exit.
