---
title: Viewing the hostname in an SSL certificate
---

The hostname in an SSL certificate used for LDAP must match the hostname entered in 
the conf.php file (this is the SSL certificate actually installed on the LDAP server,
not the CA certificate). If you have no control over making it match, you can just put
an entry in /etc/hosts with the IP of the LDAP server and the hostname that is in
the certificate. To view the hostname in the certificate, you need a file containing
the certificate (mycert.pem is used in the example). Run the following command to see
the hostname that is set in the certificate:

<pre>
openssl x509 -in /tmp/mycert.pem -subject -noout
</pre>

You should see something like:

<pre>
subject= /OU=Domain Control Validated/CN=ldap.example.edu
</pre>

The hostname is after the **CN=** part. So, **ldap.example.edu** is the hostname in
this example.