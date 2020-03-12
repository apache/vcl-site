---
title: VCL 2.3 - Adding LDAP Authentication
---

<a name="VCL2.3-AddingLDAPAuthentication-*AddingLDAPAuthenciation*"></a>
## *Adding LDAP Authenciation*

<a name="VCL2.3-AddingLDAPAuthentication-PrerequisitesforyourLDAPserver:"></a>
### Prerequisites for your LDAP server:

* SSL should be enabled on your LDAP server
* An LDAP account that can look up a user's first and last names, user id,
and email address (email address is optional) - this will be referred to as
'vcllookup' on this page. You can skip this step if anonymous binds are
enabled on your LDAP server and an anonymous bind will be able to look up
userids, names, and email addresses.
* If your LDAP server is behind a firewall, you will need to allow your VCL
web server to access tcp port 636 on your LDAP server

<a name="VCL2.3-AddingLDAPAuthentication-PrerequisitesforyourVCLwebserver:"></a>
### Prerequisites for your VCL web server:

* *php-ldap* needs to be installed
* If your LDAP server's SSL certificate is self-signed, your VCL web server
needs to have the root CA certificate that was used to sign the LDAP server
certificate installed. The PEM formatted certificate needs to be added to
the ca-bundle.crt file. On CentOS, the file is located at
/etc/pki/tls/certs/ca-bundle.crt. The hostname in the certificate must
match the hostname entered in the conf.php file further down. If your
certificate does not have the correct hostname in it, you can put an entry
in /etc/hosts for the hostname in the certificate.
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


<a name="VCL2.3-AddingLDAPAuthentication-AddingLDAPAuthenticationtotheWebCode"></a>
### Adding LDAP Authentication to the Web Code

* You will need to manually add an entry to the affiliation table in the
VCL database. Choose a name for the affiliation. This will be appended to
all userids for the affiliation to distinguish them from other affiliations
you may configure later. *Do not* use the Global affiliation for this.
Initials or a short name of your organization are a good idea. The
affiliation name cannot contain spaces. Use the following to add the
affiliation, replacing 'EXAMPLE' with the name you chose. Take note of the
id from the 2nd SQL statement as you will need it later. It is the
numerical id for this affiliation.
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
* Uncomment the "EXAMPLE1 LDAP" section by removing the '/\*' before it and
the '\*/' at the end of 'to use this login mechanism'
* Change 'EXAMPLE1 LDAP' to something to match your location, for example
at NCSU, it is 'NCSU LDAP'. This string is what users will see where they
select the authentication mechanism to use when logging in.
* Modify the following fields:
** *server* \- this is the hostname of your LDAP server - this must match
the hostname in the certificate.
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
** *lookupuserbeforeauth* \- Some LDAP servers will only allow the full DN
of a user to be used when authenticating. If this is the case, you will
need to set this to 1 and set a value for *lookupuserfield*. You can
probably start out with this set to 0. If your LDAP server has users in
multiple containers, you will probably need to set this to 1. 
** *lookupuserfield* \- If you need to set *lookupuserbeforeauth* to 1, set
this to the attribute to use to search for the user in ldap. Typical values
are 'cn', 'uid', and 'samaccountname'.
** *help* \- this is some text that will show up on the page where users
select the authentication method explaining why they would select this
option
* Uncomment the *require_once* line for *ldapauth.php* toward the bottom of
the file
