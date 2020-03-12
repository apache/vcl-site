---
title: LDAP Authentication
---

{{% toc %}}

## Why LDAP Authentication?

Authenticating your users to VCL via LDAP allows you to use your enterprise managed
accounts to log in to the VCL web site. Additionally, you can mirror certain user
groups from your LDAP system into VCL so that you do not need to manage the user
group memberships both in your enterprise system and in VCL.

## Overview

First, you need an LDAP server with SSL enabled. You already have this if you have
an Active Directory system set up. Next, you (probably) need to add an affiliation
to VCL so that users logging in via the new LDAP connection will all be associated
together. Finally, you need to modify the web code conf.php file to have information
about how to connect to the LDAP server. You will also need to make sure your web
server can trust the SSL certificate and access it through any firewalls.

## Prerequisites for your LDAP server:

* SSL must be enabled on your LDAP server
* An LDAP account that can look up these items for users:
    * first name
    * last name
    * user id
    * email (optional)

    This will be referred to as 'vcllookup' on 
this page. You can skip this step if anonymous binds are enabled on your LDAP server 
and an anonymous bind will be able to look up the listed items.

* If your LDAP server is behind a firewall, you will need to allow your VCL web 
server to access tcp port 636 on your LDAP server

## Prerequisites for your VCL web server:

* **php-ldap** needs to be installed
* **SSL certificate** - If your LDAP server's SSL certificate is self-signed, your VCL web server needs 
to have the root CA certificate that was used to sign the LDAP server certificate 
installed. The PEM formatted certificate needs to be added to the ca-bundle.crt file. 
On CentOS, the file is located at /etc/pki/tls/certs/ca-bundle.crt 
([example](/docs/ldap-ca-bundle-ex.html)). The hostname in 
the certificate must match the hostname entered in the conf.php file further down. 
If your certificate does not have the correct hostname in it, you must put an entry 
in /etc/hosts for the hostname in the certificate ([viewing the hostname in the 
certificate](/docs/ldap-showhostname.html)).

* After adding the certificate, restart httpd:

    service httpd restart

* You can verify that the certificate is properly installed using this command:

    openssl s_client -showcerts -CAfile /etc/pki/tls/certs/ca-bundle.crt -connect 
your.ldap.server.here:636

    If you see "Verify return code: 0 (ok)" at the end of the output then it is 
installed correctly. If you see a different return code, then you'll need to 
troubleshoot the problem.

* You may need to add a line to **/etc/openldap/ldap.conf** to point to the 
ca-bundle.crt file. If so, add the following:

    TLS_CACERT /etc/pki/tls/certs/ca-bundle.crt

## Adding LDAP Authentication to the Web Code

* You will need to manually add an entry to the affiliation table in the VCL 
database. Choose a name for the affiliation. This will be appended to all userids 
for the affiliation to distinguish them from other affiliations you may configure 
later. **Do not** use the Global affiliation for this. Initials or a short name of 
your organization are a good idea. The affiliation name cannot contain spaces. Use 
the following to add the affiliation, replacing 'EXAMPLE' with the name you chose. 
Take note of the id from the 2nd SQL statement as you will need it later. It is the 
numerical id for this affiliation.

    mysql vcl

    INSERT INTO affiliation (name) VALUES ('EXAMPLE');

    SELECT id FROM affiliation WHERE name = 'EXAMPLE';

    exit

* Edit *conf.php* and search for "EXAMPLE1 LDAP"
* Uncomment the "EXAMPLE1 LDAP" section by removing the '/\*' before it and the '\*/' 
at the end of 'to use this login mechanism'
* Change 'EXAMPLE1 LDAP' to something to match your location, for example at NCSU, 
it is 'NCSU LDAP'. This string is what users will see where they select the 
authentication mechanism to use when logging in.
* Modify the following fields:
    * **server** - this is the hostname of your LDAP server - this must match the 
hostname in the certificate.
    * **binddn** - typically, you'll want to use the base DN of your LDAP server; for 
Active Directory, this is usually dc= for each of your domain name components. For 
example, your your domain name was ad.example.org, it would be 
"dc=ad,dc=example,dc=org"
    * **userid** - this is a string that is added to the userid a user enters on the 
login page. Place a '%s' where the entered userid should go. Some examples are:
        * %s@example.org
        * %s@ad.example.org
        * uid=%s,ou=accounts,dc=example,dc=org'
    * **unityid** \- this is the ldap field that contains a user's login id (for Active 
Directory, this is usually sAMAccountName)
    * **firstname** \- this is the ldap field that contains a user's first name
    * **lastname** \- this is the ldap field that contains a user's last name
    * **email** \- this is the ldap field that contains a user's email address
    * **defaultemail** \- if an email address is not provided by the ldap server, this 
will be appended to the end of the userid to create an email address. In this case, 
email notifications will be disabled by default.
    * **masterlogin** \- this is the vcllookup account referred to in the "Prerequisites 
for your LDAP server" section - comment out this line if using anonymous binds
    * **masterpwd** \- password for the masterlogin account - comment out this line if 
using anonymous binds
    * **affiliationid** \- this is the id from the SELECT statement in the first step
    * **lookupuserbeforeauth** \- Some LDAP servers will only allow the full DN of a 
user to be used when authenticating. If this is the case, you will need to set this 
to 1 and set a value for *lookupuserfield*. You can probably start out with this set 
to 0. If your LDAP server has users in multiple containers, you will probably need 
to set this to 1. 
    * **lookupuserfield** \- If you need to set *lookupuserbeforeauth* to 1, set 
this to the attribute to use to search for the user in ldap. Typical values are 'cn', 
'uid', and 'samaccountname'.
    * **help** \- this is some text that will show up on the page where users select the 
authentication method explaining why they would select this option
* Uncomment the **require_once** line for **ldapauth.php** toward the bottom of the file

## Mirroring LDAP User Groups
This part is a little more complicated because it actually requires modifying some
of the VCL code. Before modifying VCL, you first need to create user groups in your
LDAP system and configure things so that a lookup of a user in your LDAP system will
list the groups of which the user is a member. Doing these items is beyond the scope
of this document.

In the vcl/.ht-inc/authmethods/ldapauth.php file, there is an example function at 
the end named **updateEXAMPLE1Groups**. In a previous step, you modified conf.php 
and changed **EXAMPLE1 LDAP** to something to match your location. **NCSU LDAP** 
was used as an example. We'll continue using that here.

You need to change the name of **updateEXAMPLE1Groups** to match your location. 
We'll change it to **updateNCSUGroups** for our example. Next, on the 2nd line of
the function, change **EXAMPLE1 LDAP** to match your location (ex. **NCSU LDAP**).
Next, you need to determine what attribute is used when looking up users in your 
LDAP system to reference user group memberships. For Active Directory, this is typically
**memberof**. Now, if needed, change the two references in the function from **memberof**
to the attribute used in your LDAP system. Finally, there are three example regular
expressions in the **for** loop at the bottom of the function that match various 
example names of user groups. You'll need to modify these to match the OU structure
of your LDAP system.

These are the three example rules in VCL 2.3:

    ^CN=(.+),OU=CourseRolls,DC=example1,DC=com
    ^CN=(Students_Enrolled),OU=Students,DC=example1,DC=com$
    ^CN=(Staff),OU=IT,DC=example1,DC=com$

The first one matches any groups under the CourseRolls OU. The second one specifically
matches the **Students_Enrolled** group under the Students OU. The third one matches
the **Staff** group under the IT OU. If you need help creating regular expressions
to match your LDAP system, please feel free to ask on our user email list or via IRC.

Finally, you'll also need to modify the updateLDAPUser function in the same file. 
Toward the end of the function is a **switch** statement based on affiliation names. 
Change the **EXAMPLE1** entry to the affiliation you created for your site. Then, 
change the name of the function called for that affiliation to your new name for the
**updateEXAMPLE1Groups** function. Here is an example of that part of the function:

    switch(getAffiliationName($affilid)) {
       case 'NCSU':
          updateNCSUGroups($user);
          break;
       default:
          //TODO possibly add to a default group
    }



Here is an example function using NCSU instead of EXAMPLE1, and using an Active 
Directory LDAP system:

    function updateNCSUGroups($user) {
       global $authMechs;
       $auth = $authMechs['NCSU LDAP'];
       $ds = ldap_connect("ldaps://{$auth['server']}/");
       if(! $ds)
          return 0;
       ldap_set_option($ds, LDAP_OPT_PROTOCOL_VERSION, 3);
       ldap_set_option($ds, LDAP_OPT_REFERRALS, 0);
    
       $res = ldap_bind($ds, $auth['masterlogin'],
                         $auth['masterpwd']);
       if(! $res)
          return 0;
    
       $search = ldap_search($ds,
                             $auth['binddn'],
                             "{$auth['unityid']}={$user['unityid']}",
                             array('memberof'), 0, 10, 15);
       if(! $search)
          return 0;
    
       $data = ldap_get_entries($ds, $search);
       $newusergroups = array();
       if(! array_key_exists('memberof', $data[0]))
          return;
       for($i = 0; $i < $data[0]['memberof']['count']; $i++) {
          if(preg_match('/^CN=(.+),OU=VCLGroups,DC=ad,DC=ncsu,DC=edu/', $data[0]['memberof'][$i], $match))
             array_push($newusergroups, getUserGroupID($match[1], $user['affiliationid']));
       }
       $newusergroups = array_unique($newusergroups);
       updateGroups($newusergroups, $user["id"]);
    }

If you add other affiliations that need to be tied in with LDAP, you can copy this
function and rename things in a similar fashion to match the new LDAP system.

### Some things to be aware of with mirrored groups
There are a few things to be aware of when working with mirrored groups in VCL. A 
group isn't mirrored in to VCL until someone that is a member of the group logs in 
to VCL, or a user with the membership is looked up using the **User Lookup** page. 
So, what is generally suggest is to create an LDAP user that you make a member of
all user groups. Then, when you need to get a new group in to VCL, you can force
a lookup of that user on the **User Lookup** page. 

The second gotcha is that VCL 
caches a user's LDAP information for up to 24 hours. So, if you log in to VCL, then add 
yourself to a group on your LDAP server, you will have to wait for up to 24 hours 
before VCL looks up your LDAP information again. Alternatively, you can
force a lookup on the **User Lookup** page.

### Debugging LDAP Configuration
If you run in to problems getting an LDAP configuration to work,
you can download a [LDAP Debug Script](/docs/generic.php.txt) and save it as generic.php (remove .txt
from the name) somewhere you can access it on you web server. There
are 5 variables at the top of the script that need to be set
according to your site's configuration. There is a comment in the
file explaining what each variable needs to be set to. Once you get
the script to show you search results, you should have a good idea
what you need to set the variables to in conf.php.