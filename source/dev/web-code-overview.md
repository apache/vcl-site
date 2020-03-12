---
title: Web Code Overview
---

## General Overview

The code is broken up into multiple files, based on sections of the site (as divided up by the navigation area). There are also several general purpose files:

* index.php -  This is the only file used in any URLs. It includes other files based on the passed in "mode".
* states.php - builds an array of modes, which function should be called for each mode, and the part of the site each mode belongs to
* utils.php - contains many functions that are common to several sections
* errors.php - contains an array of all errors that can be reported by the site. I'm not sure how useful it was do set it up this way, but it's where things currently are. errors.php also contains the debug function that is used if the current user has an adminlevel of ADMIN_DEVELOPER in the user table.
* secrets.php - contains all passwords/passphrases and secret and shared keys
* conf.php - contains all configuration variables that might need to be modified for each install base
* php5extras.php - anything that needs to be done differently when using php5 vs php4



## Site Security

The initial handling of form data within the code was quite insecure, and several areas of the site are still this way. After learning more about web security, I developed a security model based on "continuations". All of the pages have been converted to using continuations.

Deep linking into the site is only allowed for modes in the $actions['entry'] array in states.php. Anything else requires the submission of a continuation. For the most part, access to different parts of the site is controlled by what privileges you have in the Privileges section of the site. However, there are a few things controlled by a user's adminlevel field in the user table. The very earliest form of authorization was handled by the user's adminlevel field, and it has continued to be useful in a few situations.

All form data passed in to the site should be verified very strictly. Unfortunately, that is not currently the case. All of the main pages available to the average user should have been updated to have strict validation, though other parts of the site have not made it yet. Most sections of the site have a single function (or a very small number of similar functions) that handle the processing of form data. This will make it easier to add better checks throughout the site as the number of locations needing to be modified is fairly small.

## General Processing Flow

Every time someone views the site, it is through index.php. This file defines several global variables and includes conf.php, states.php, errors.php, and utils.php. It then creates a database connection and calls initGlobals(), which among other things, determines $mode. Based on $mode, index.php determines which function needs to be called and assigns it to $actionFunction. Next, checkAccess() is called, followed by sendHeaders() and printHTMLHeader() (which doesn't actually print the header if $mode is in $noHTMLwrappers). set_error_handler is called if the current user has an adminlevel of ADMIN_DEVELOPER. Next, $actionFunction is finally called, followed by disconnecting from the database, a call to printHTMLFooter(), and a call to semUnlock() to make sure the semaphore was unlocked if it was locked somewhere in the process.

One thing worth noting that initGlobals() does is to include other files based on which mode is being processed. This helps to prevent the php script engine from having to process unnecessary files. It also adds a small layer of security because a section of code cannot be attacked if it has not been included.

## Continuations

Continuations are how the site handles sequences of pages. It also helps keep people from getting to parts of the site they aren't allowed to access or shouldn't jump in to the middle of (i.e. by using the browser's back button). Continuations are created by calling addContinuationsEntry, which accepts up to 6 arguments:

* $nextmode - the mode that should be used when the continuation is submitted
* $data - an array of any data that you would like to have available when the continuation is submitted
* $duration - how long from "now" that the continuation should be valid (in seconds)
* $deleteFromSelf - boolean - 1 if this is the start of a new sequence of pages, 0 if it will be a continuation of a sequence. If it is set to 0, then the "parent" continuation for this one is the continuation that the site is currently processing.
* $multicall - boolean - whether or not the continuation may be submitted more than once
* $repeatProtect - boolean - used in cases where a "sequence loop" can occur


addContinuationsEntry returns a long encrypted string to be used as an identifier to be submitted (either as a hidden form field or in the URL for a GET link). What gets encrypted is a salt value, the id of the continuation that was created (or updated), the user's numeric id, and a timestamp. If the string gets tampered with, it will not decrypt properly. If someone tries to submit a continuation given to another user, their user ids won't match; so, it will be considered invalid.

When a continuation is submitted, some checks are run and, if everything passes, whatever was submitted as $nextmode is the mode for which the site functions. One of those checks is that $duration has not expired; if it has, the user is given a notice that he has submitted expired data. Any data submitted as $data can be accessed by calling getContinuationsData() with a single argument being the index of the array that was passed to addContinuationsEntry. Additionally, getContinuationsData can be called with no arguments to get all of $data as a single array. If $multicall was set to 0, then the continuation is deleted. If $deleteFromSelf was also set to 0, then this continuation's parent will also be deleted. If $deleteFromSelf was set to 0 for the parent, it's parent will be deleted, and so on until a continuation is reached that had $deleteFromSelf set to 1.

## Javascript and AJAX

Efforts have been made to ensure the pages required for making and connecting to a reservation work without requiring any javascript. However, enhancements have been made to enrich those parts of the site if javascript is enabled. For some of the administrative parts of the site, javascript and AJAX have been used heavily, particularly the Privileges page. The [Dojo Toolkit](http://dojotoolkit.org) is what is being used for javascript widgets and to handle some of the AJAX.

## A Few Examples


### Adding a link to the navigation area

Here are the steps that would need to be done to add a new section of the site.

First, modify states.php to add a new mode.

1. create a new $actions['mode'] with the name of your mode set to the name of the function that should be called
1. create a new $actions['pages'] with the name of your mode set to the name of the section this mode belongs to. This is only an internal identifier used to associate modes together.

So, if your mode is named "examplemode", you could end up with these two lines being added:

```php
$actions['mode']['examplemode'] = <span class="code-quote">"exampleFunc1"</span>;
$actions['pages']['examplemode'] = <span class="code-quote">"exampleSection"</span>;
```

While we're editing states.php, lets jump to the top and add our new mode to $actions['entry'] so that it can be called directly without having to already be on the site. Just add 'examplemode' as a new item at the end of the array.

The next thing to do is to actually add the functions. Lets place them in a new file called 'examples.php' in the .ht-inc directory. Our first function can be really simple and just print out some text. So, create examples.php with this in it:

```php
<?php
function exampleFunc1() {
   print <span class="code-quote">"exampleFunc1 successfully called.<br>\n"</span>;
}
?>
```

There's one last thing we need to do before linking this in on the site. As described in the "General Processing Flow" section, initGlobals includes the required files based on the current mode's section. So, edit utils.php and scroll toward the end of it where files are included (using require_once) within a switch statement. In the switch statement, before the "default" case, add

```php
case 'exampleSection':
   require_once('.ht-inc/examples.php');
   break;
```

Now, we're ready to actually add a link for this example function to the navigation area (of course, not all modes are linked to from the navigation area, but it is an easy example). To do this, edit utils.php and find the getNavMenu function close to the bottom of the file. We'll add our new mode to the end; so, find the "logout" part which should look something like this:

```php
if($inclogout) {
   $rt .= menulistLI('authentication');
   $rt .= "<a href=\"" . BASEURL . SCRIPT . "?mode=logout\">";
   $rt .= "Logout</a></li>\n";
}
```

We'll basically duplicate that (without the if conditional), changing a few things so that we add this right below it:

```php
$rt .= menulistLI('exampleSection');
$rt .= "<a href=\"" . BASEURL . SCRIPT . "?mode=examplemode\">";
$rt .= "Example Section</a></li>\n";
```

Viewing the site should now show "Example Section" right under "Logout" in the navigation area. Clicking "Example Section" should cause "exampleFunc1 successfully called." to be displayed in the main content area of the site.

### Using continuations when submitting form data

Let's modify examplefunc1 so that it prints some form data that gets submitted with a continuation.

So, change the contents of examplefunc1 to be:

```php
$options = array(0 => "option1",
                 1 => "option2");
print "<FORM action=\"" . BASEURL . SCRIPT . "\" method=post>\n";
print "Select one of these options:";
printSelectInput("theoption", $options);
$cont = addContinuationsEntry("submitFunc1Form", $options);
print "<INPUT type=hidden name=continuation value=\"$cont\">\n";
print "<INPUT type=submit value=Submit>\n";
print "</FORM>\n";
```

Now, we have a form that gets displayed when "Example Section" is clicked.  Now, we need to add a function to process that form.  Add this function to examples.php:

```php
function submitFunc1Form() {
   $data = getContinuationVar();
   $theoption = processInputVar("theoption", ARG_NUMERIC);
   if(! array_key_exists($theoption, $data)) {
      print "invalid option submitted\n";
      return;
   }
   print "The option you selected was: ";
   print "{$data\[$theoption\]}<br>\n";
}
```

Next, we add this function to states.php:

```php
$actions['mode']['submitFunc1Form'] = "submitFunc1Form";
$actions['pages']['submitFunc1Form'] = "exampleSection";
```

Now, click the "Example Section" link, select one of the options, and click Submit to see if it works.

### Using AJAX to dynamically update a page

AJAX is very useful for dynamically updating page content.  Let's add something to examplefunc1 that can be updated with an AJAX call.

Add this to the end of examplefunc1:

```php
print "<br><br>\n";
print "<div id=examplediv>\n";
print "This will get dynamically changed.<br>\n";
print "</div>\n";
$cont = addContinuationsEntry("AJexample");
print "<a onclick=\"JS_AJexample('$cont');\">Click to ";
print "update</a><br>\n";
```php

Next, we need to add the javascript function we just referenced to code.js (in .ht-inc's parent directory) as well as a callback function that will be called when the results of the AJAX call are returned:

```php
function JS_AJexample(contid) {
   dojo.xhrPost({
      url:'index.php',
      load: JS_AJexampleCB,
      error: errorHandler,
      content: {continuation: contid},
      timeout: 15000
   });
}

function JS_AJexampleCB(data, ioArgs) {
   eval(data);
}
```

Then, we need to add a few things to states.php:

to the $actions array:

```php
$actions['mode']['AJexample'] = "exampleFunc2";
$actions['pages']['AJexample'] = "exampleSection";
```

to the $noHTMLwrappers array:

```php
'AJexample'
```

Now, we need to create exampleFunc2 (in examples.php):

```php
function exampleFunc2() {
   print "document.getElementById('examplediv').innerHTML = 'Dynamic update';";
}
```

Then, we do something we haven't seen before.  getDojoHTML (in utils.php) must be modified so that the correct dojo requires get set when we are in mode examplefunc1.  For a simple AJAX update, we only need the dojo.parser module to be loaded.  Since this is already loaded for some of the Group modes, just add another case statement under submitDeleteGroup so we have:

```php
case 'viewGroups':
case 'submitEditGroup':
case 'submitAddGroup':
case 'submitDeleteGroup':
case 'examplemode':
   $dojoRequires = array('dojo.parser');
   break;
```

We also have to add a case statement a little further down where the HTML is actually generated. Find "case 'submitDeleteGroup':" in the switch statement following the one we just modified, and add another case statement for examplemode so we have:

```php
case 'viewGroups':
case 'submitEditGroup':
case 'submitAddGroup':
case 'submitDeleteGroup':
case 'examplemode':
   $rt .= "<style type=\"text/css\">\n";
```

Since we modified code.js, to test this, you will need to hold Shift and click the reload button in your browser to force your browser to reload code.js.  "Click to update" will not show up as a normal link, but it should still be clickable.  You can use CSS to make it look like a normal link or give it an href="#"  if you want.

## A word about using tabs for code indentation

All of the code has been indented using tabs (rather than spaces) except where code wraps to more than one line, in which case a combination of tabs and spaces are used.  This allows someone editing the code to set his tab width to whatever he prefers, but still allows code that wraps to multiple lines to line up correctly.  To do this, when you want to wrap code to another line, put a newline at the end of the one you are on just as you normally would.  Next, tab over from the beginning of the line until you are even with where the initial line of code started, then use spaces to line up this line with something in the line above it that makes sense.  I'll give an example.  Almost all of the queries are written on multiple lines like this:

```php
=====------------------------------
     $query = "SELECT id, "
            .        "name, "
            .        "prettyname "
            . "FROM image "
            . "WHERE id < 400 AND "
            .       "OSid = 3";
=====------------------------------
```

In this example, whitespace indicated by the = marks should be made of tabs, whitespace indicated by the - marks should be made of spaces.

## Inline Code Documentation

Online documentation of the code is generated using Doxygen.  Each file that should be parsed to generate docs needs to have the following toward the top of it:

```php
/**
 * \file
 */
```

All functions should have a header above them that documents what it does.  The header should include the name of the function, a description of any parameters passed in, a description of anything returned, and a brief description of what the function does.  The format of the header is:

```php
/////////////////////////////////////////////////////////////////////
///
/// \fn nameOfFunction($param1, $param2)
///
/// \param $param1 - description of param1
/// \param $param2 - description of param2
///
/// \return description of datastructure returned
///
/// \brief short description of what the function does
///
/////////////////////////////////////////////////////////////////////
```

If the function doesn't receive any parameters or doesn't return anything, those sections can be omitted.

## Authentication

Authentication has been somewhat modularized.  When a user loads the site, the initGlobals function checks to see if the user is logged in.  If not, the mode in which the site should function gets set to "selectauth".  Here, the user is prompted to select an authentication method to use to log in.  Authentication methods are configured in $authMethods which is in conf.php.  There are currently three authentication types that can be handled: redirect, ldap, and local.  Redirect types send the user to another site to handle their authentication, with the expectation that a cookie will be set and that knowledge of how to interpret that cookie is handled in initGlobals.  If an ldap or local method is chosen, the user is directed to a page displayed by printLoginPageWithSkin() (in authentication.php as are most of the following functions).  This function sets up the skin for the page to match the affiliation defined in $authMethods, and then calls printLoginPage().  printLoginPage() displays a form for the user to enter a userid and password.  The form is submitted and then processed by submitLogin().  If the authentication method is ldap based, ldapLogin() is called; if it is the local system, localLogin() is called.  Each of these functions tries to validate the user.  If it succeeds, a cookie named VCLAUTH is set, and the user is redirected to the main page of the site.  If it fails, the user is redirected back to the login page. *If you enter valid credentials, but still get redirected back to the login page, the first thing to check is whether or not the setcookie() call was reached, and if so, was the cookie actually set in your browser.*
