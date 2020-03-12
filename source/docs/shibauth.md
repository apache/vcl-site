---
title: Shibboleth Authentication
---

The VCL is designed to support Shibboleth authentication for one or more affiliations. Using Shibboleth
does not preclude the use of LDAP for other affiliations in the same VCL infrastructure. The principal
advantage of using Shibboleth with the VCL is the ability to completely externalize authentication
 (and, to a certain degree, authorization) decisions. That is, by using Shibboleth authentication, a user's
password will never pass through the VCL system.

Configure Apache
---------------

The first step is to configure Apache by protecting the `/shibauth` directory on your webserver.
If the VCL is installed in the webserver root, the configuration will look like this:

    <Location /shibauth>
        AuthType shibboleth
        ShibRequestSetting requireSession 1
        require valid-user
    </Location>

Test Shibboleth Attributes
----------------------

Before proceeding, it is generally a good idea to test that the shibboleth attributes are being correctly sent
from the Identity Provider (IdP) to the Service Provider (SP). To do that, create a PHP file in your 
`/shibauth` directory (e.g. <code>test.php</code>):

    <!DOCTYPE html>
    <html lang="en">
    <head>
      <title>Shibboleth Test</title>
    </head>
    <body>
        <h1>Shibboleth Test</h1>
    <?php
    // Include the Shibboleth attributes you intend to test here
    $attributes = array('displayName', 'mail', 'eppn',
                        'givenName', 'sn', 'affiliation', 'unscoped-affiliation');
    foreach($attributes as $a){
        print "<p>";
        print "<strong>$a</strong> = ";
        print isset($_SERVER[$a]) ? $_SERVER[$a] : "<em>Undefined</em>";
        print "</p>";
    }
    ?>
    </body>
    </html>

Then visit this page at `https://vcl.yourdomain.edu/shibauth/test.php`

The only attribute that is absolutely required is `eppn`, but the VCL also expects 
the following attributes to be defined:

  - either `displayName` or both `givenName` and `sn`
  - `mail`
  - `affiliation`

If these attributes are not present or not correct, then you may need to fix the configuration of
Shibboleth on your system. Either the SP is not mapping the attributes properly or the IdP is not 
releasing them. Some good places to start include inspecting the full contents of the 
`$_SERVER` array or write a script that calls `phpinfo();`.

Configure the VCL for Shibboleth authentication
----------------------------------------

Open the `.ht-inc/conf.php` file in a text editor

Define your institution in the `$authMechs` array like so:

    $authMechs = array(
        "My Institution" => array(
                "type" => "redirect",
                "URL" => "/Shibboleth.sso/Login?target=/shibauth&entityID={the URL-encoded location of your IdP}",
                "affiliationid" => 0,
                "help" => "..."),
        ....
    );

Notice that affiliationid is set to 0.

If you wish to be able to manually add users to groups through the web interface (that is, Shibboleth users who
have not previously logged in), then you will need to have this line in the configuration:

    define("ALLOWADDSHIBUSERS", 1);

By default this is set as 0.

Finallly, uncomment this line at the bottom of the configuration file:

    require_once(".ht-inc/authmethods/shibauth.php");

Test the login process
------------------

At this point, you should be able to login via shibboleth. A user account will be created for you
and if there is an `affiliation` attribute sent from the IdP, you will be placed into any groups listed
there: for instance, if the `affiliation` attribute is `faculty;staff`, then the user will be placed in the
`shib-faculty@AFFILIATION` and `shib-staff@AFFILIATION` groups. You should confirm that this works.
Please also note that Shibboleth uses the word affiliation to refer to groups that a user is associated with; 
for example, "employee" or "student". The VCL uses the word affiliation to refer to an institution that uses
the system. This can be confusing.

Further configuration
------------------

If you wish to further customize how Shibboleth works, you can edit the `shibauth/index.php` file.
If, for instance, you wish to add all users to an `All users@AFFILIATION` group, then add this line of
code (after the `$affilid` variable has been defined):

    updateGroups(array(getUserGroupID('All users', $affilid)), $usernid);

This file would also be a good place to define a `Shib-logouturl` and a `Shib-IdP-Logout` value in the
`$shibdata` array. More about that below.

Logging out
----------

Logging out is very complicated when it comes to Shibboleth. The best way to log out is to completely
close (i.e. quit) your browser. However, if you would like the "logout" link to work as users will generally
expect, these instructions will explain how to set that up.

**Please note**: these instructions do not describe the so-called "global logout". That is, these examples
only provide a means for logging the user out of the VCL. If a user is also logged into another shibbolized
application, he or she will continue (depending to some degree on the server settings) to be logged in to
that application, even after logging out of the VCL.

The main thing to realize is that for any shib-enabled VCL session, there are (at least) three session cookies,
and for a user to truly "logout", all three of them must be destroyed. The first cookie is the VCL application
cookie, "VCLAUTH". That can be destroyed by overwriting it from within the VCL application -- this typically
happens automatically. 

The next cookie is the for the SP session. If that cookie continues to exist, then when a browser lands on
the `/shibauth` directory, the previous SP session will be used and the user will be immediately back in the
application. To destroy the SP session, you need to issue a GET request to `/Shibboleth.sso/Logout`.

The third cookie exists on the IdP. If that cookie isn't destroyed (and hasn't timed out), then the next time a
user is redirected to the IdP, she or he will be immediately be sent back to the SP with a valid session -- and then
on to the application with a valid session. To destroy the cookie on the IdP, you will need to have code placed
there to destroy the cookie. If the IdP cookie is named _idp_session, then you could, for instance, have a script
on the IdP that looks like this:

    https://idp.yourinstitution.edu/logout.php

    <?php
    setcookie(_idp_session", 0, 0, "/idp", "", TRUE);
    header("Content-type: text/html");
    ?>
    <!DOCTYPE html>
    <html lang="en">
    <head><title>Session Logout</title></head>
    <body>
      <h1>Session Logout</h1>
      <p>You have logged out of your application session.</p>
    </body>
    </html>

The way the VCL handles logout is that it loads a page that overwrites the application cookie and which loads
two hidden iframes -- the first one destroys the SP cookie, and the second one tries to destroy the IdP cookie.
The problem is just that it assumes your IdP logout script is located at this address:

    https://MYIDP/idp/logout.jsp

The best way to override this behavior is to modify the `shibauth/index.php` script and set a `Shib-logouturl`
value in the `$shibdata` array. You may also want to define a value for `Shib-IdP-Logout` so that it is
available to your script. This is useful if there are multiple institutions using your VCL system.

That should be a path to a file within the VCL web directory, such as `/logout.php`.

You can then customize this new file to display whatever you like; here is a bare-bones example:

    <?php
    require_once(".ht-inc/conf.php");
    require_once(".ht-inc/utils.php");
    require_once(".ht-inc/states.php");
    dbConnect();
    initGlobals();
    
    $shibdata = getShibauthData($shibauthed);
    
    setcookie("VCLAUTH", "", time() - 10, "/", COOKIEDOMAIN);
    
    doQuery("DELETE FROM shibauth WHERE id = $shibauthed", 101);
    stopSession();
    dbDisconnect();
    ?>
    <!DOCTYPE html>
    <html lang="en">
    <head>
      <title>Virtual Computing Lab</title>
      <style type="text/css">
        iframe { display: none; }
        article { text-align: center; }
      </style>
    </head>
    <body>
      <header>
        <h1><a href="https://vcl.MYINSTITUTION.edu">Virtual Computing Lab</a></h1>
      </header>
      <article>
        <h2>Logging out of the VCL...</h2>
        <p>In order to completely log out of this application, please quit your browser.</p>
      </article>
      <iframe src="https://<?php print $_SERVER['SERVER_NAME']; ?>/Shibboleth.sso/Logout">
      </iframe>
    <?php
    if(array_key_exists('Shib-IdP-Logout', $shibdata) &&
            ! empty($shibdata['Shib-IdP-Logout'])) {
        print "<iframe src=\"{$shibdata['Shib-IdP-Logout']}\">\n";
        print "</iframe>\n";
    }
    ?>
    </body>
    </html>