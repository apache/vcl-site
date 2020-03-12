---
title: VCL 2.2.1 - Adding LDAP Authentication
---

<a name="VCL2.2.1-AddingLDAPAuthentication-PrerequisitesforyourLDAPserver:"></a>
### Prerequisites for your LDAP server:

* SSL should be enabled on your LDAP server
* An LDAP&nbsp;account that can look up a user's first and last names, user
id, and email address (email address is optional) - this will be referred
to as 'vcllookup' on this page. You can skip this step if anonymous binds
are enabled on your LDAP server and an anonymous bind will be able to look
up userids, names, and email addresses.
* If your LDAP server is behind a&nbsp;firewall, you will need to allow
your VCL web server to access tcp port 636 on your LDAP server

<a name="VCL2.2.1-AddingLDAPAuthentication-PrerequisitesforyourVCLwebserver:"></a>
### Prerequisites for your VCL web server:

* *php-ldap* needs to be installed
* If your LDAP server's SSL certificate is self-signed, your VCL web server
needs to have the root CA certificate that was used to sign the LDAP server
certificate installed. On CentOS, information about the certificate needs
to be added to /etc/pki/tls/certs/ca-bundle.crt - this [script](adding-ldap-authentication^convert_crt_for_ldapssl.html)
 will take as input a file containing the base64 encoded certificate and
generate the lines that need to be added to the ca-bundle.crt file.
* After adding the certificate, restart httpd:
{tip}
service httpd restart
{tip}
* You can verify that the certificate is properly installed using this
command:
{tip}
openssl s_client \-showcerts \-CAfile /etc/pki/tls/certs/ca-bundle.crt
\-connect your.ldap.server.here:636
{tip}
If you see "Verify return code: 0 (ok)" at the end of the output then it is
installed correctly. If you see a different return code, then you'll need
to troubleshoot the problem.
* You may need to add a line to */etc/openldap/ldap.conf* to point to the
ca-bundle.crt file. If so, add the following:

    TLS_CACERT /etc/pki/tls/certs/ca-bundle.crt


<a name="VCL2.2.1-AddingLDAPAuthentication-AddingLDAPAuthenticationtotheWebCode"></a>
### Adding LDAP Authentication to the Web Code

* You will need to manually add an entry to the affiliation table in the
VCL database. Choose a name for the affiliation. This will be appended to
all userids for the affiliation to distinguish them from other affiliations
you may configure later. Initials or a short name of your organization are
a good idea. The affiliation name&nbsp;cannot contain spaces. Use the
following to add the affiliation, replacing 'EXAMPLE' with the name you
chose. Take note of the id from the 2nd SQL statement as you will need it
later. It is the numerical id for this affiliation.
{tip}
mysql vcl
{tip}
{tip}
INSERT INTO affiliation (name) VALUES ('EXAMPLE');
{tip}
{tip}
SELECT id FROM affiliation WHERE name = 'EXAMPLE';
{tip}
{tip}
exit
{tip}
* Edit *conf.php* and search for "EXAMPLE1 LDAP"
* Uncomment the "EXAMPLE1 LDAP" section by removing the '/*' before it and
the '*/' at the end of 'to use this login mechanism'
* Change 'EXAMPLE1 LDAP' to something to match your location, for example
at NCSU, it is 'NCSU LDAP'. This string is what users will see where they
select the authentication mechanism to use when logging in.
* Modify the following fields:
** *server* \- this is the hostname of your LDAP server
** *binddn* \- typically, you'll want to use the base DN of your LDAP
server; for Active Directory, this is usually dc= for each of your domain
name components. For example, your your domain name was ad.example.org, it
would be "dc=ad,dc=example,dc=org"
** *userid* \- this is a string that is added to the userid a user enters
on the login page. Place a '%s' where the entered userid should go. Some
examples are:
*** %s@example.org
*** %s@ad.example.org
*** uid=%s,ou=accounts,dc=example,dc=org'
** *unityid* \- this is the ldap field that contains a user's login id (for
Active Directory, this is usually sAMAccountName)
** *firstname* \- this is the ldap field that contains a user's first name
** *lastname* \- this is the ldap field that contains a user's last name
** *email* \- this is the ldap field that contains a user's email address
** *defaultemail* \- if an email address is not provided by the ldap
server, this will be appended to the end of the userid to create an email
address. In this case, email notifications will be disabled by default.
** *masterlogin* \- this is the vcllookup account referred to in the
"Prerequisites for your LDAP server" section - comment out this line if
using anonymous binds
** *masterpwd* \- password for the masterlogin account - comment out this
line if using anonymous binds
** *affiliationid* \- this is the id from the SELECT statement in the first
step
** *help* \- this is some text that will show up on the page where users
select the authentication method explaining why they would select this
option
* Uncomment the *require_once* line for *ldapauth.php* toward the bottom of
the file

<a name="VCL2.2.1-AddingLDAPAuthentication-TweakifyourLDAPserverhasusersinmultiplecontainers"></a>
### Tweak if your LDAP server has users in multiple containers

If your LDAP server has users in multiple containers, then the full DN for
each user must be looked up before doing a bind to the LDAP server to
authenticate the user. In this case, you'll need to modify
authentication.php.
* Edit *authenciation.php*
* Search for "ldapLogin"
* Search for "EXAMPLE1 LDAP" in the function
* Uncomment the block of code it is contained in by removing the '/*' at the beginning of the line containing 'EXAMPLE1 LDAP', and removing the '*/' at the end of the else that is before '$ldapuser = sprintf($authMechs\[\](\.html)
['userid'], $userid);'
* change 'EXAMPLE1 LDAP' to match what you changed it to in step 3
* Look for the line containing 'cn=$userid'. If you use 'cn' to look up
userids in your LDAP server, the line is fine as is. If you use something
else, such as 'uid', change 'cn' to 'uid' or whatever is used on your LDAP
server.
* Save the file
