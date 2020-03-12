---
title: Patch to remove mcrypt dependency
---

This page explains how to use a php package called [phpseclib](http://phpseclib.sourceforge.net/)
 to remove the requirement of mcrypt. phpseclib will use mcrypt functions
if it is installed but will use native php to implement the encryption if
it is not installed.

Here are the steps to remove the dependency:
* Download [phpseclib](http://sourceforge.net/projects/phpseclib/files/phpseclib0.2.2.zip/download)
 to /tmp (version 0.2.2 was used for testing)
{tip}
cd /tmp
wget
{nolink:http://downloads.sourceforge.net/project/phpseclib/phpseclib0.2.2.zip}
{tip}
* Create a directory named phpseclib in your .ht-inc directory
{tip}
mkdir /var/www/html/vcl/.ht-inc/phpseclib
{tip}
* unzip phpseclib in the phpseclib directory
{tip}
cd /var/www/html/vcl/.ht-inc/phpseclib
unzip /tmp/phpseclib0.2.2.zip
{tip}
* Download [no_mcrypt.patch](http://people.apache.org/~jfthomps/no_mcrypt.patch)
 to your .ht-inc directory
{tip}
cd /var/www/html/vcl/.ht-inc
wget {nolink:http://people.apache.org/~jfthomps/no_mcrypt.patch}
{tip}
* Apply the patch
{tip}
patch < no_mcrypt.patch
{tip}
