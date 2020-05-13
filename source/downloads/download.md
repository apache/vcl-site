---
title: Downloads
---

## Download Links
Use the links below to download Apache VCL from one of our mirrors. You **must**
[verify the integrity](download.cgi#verify) of the downloaded files using 
signatures downloaded from our main distribution directory, **not** from a mirror.

Only current recommended releases are available on the main distribution site and
its mirrors. Older releases are available from the [archive download site](http://archive.apache.org/dist/vcl/).

Stable Release - Latest Version:

* <a href="[location]?Preferred=[preferred]&action=download&filename=%2Fvcl%2F2.5.1%2Fapache-VCL-2.5.1.tar.bz2">apache-VCL-2.5.1.tar.bz2</a>
[ [GPG](https://www.apache.org/dist/vcl/2.5.1/apache-VCL-2.5.1.tar.bz2.asc) ]
[ [SHA512](https://www.apache.org/dist/vcl/2.5.1/apache-VCL-2.5.1.tar.bz2.sha512) ]
(released 2019-07-25)

Previous Releases:

* apache-VCL-2.5.tar.bz2 (released 2017-08-18)
* apache-VCL-2.4.2.tar.bz2 (released 2015-04-16)
* (Apache VCL 2.4.1 was never officially released)
* (Apache VCL 2.4 was never officially released)
* apache-VCL-2.3.2.tar.bz2 (released 2013-03-25)
* apache-VCL-2.2.2.tar.bz2 (released 2013-03-25)
* apache-VCL-2.3.1.tar.bz2 (released 2012-12-20)
* apache-VCL-2.3.tar.bz2 (released 2012-07-20)
* apache-VCL-2.2.1-incubating.tar.bz2 (released 2011-04-08)
* apache-VCL-2.2-incubating.tar.bz2 (released 2010-10-05)
* apache-VCL-2.1-incubating.tar.bz2 (released 2009-12-04)

## Mirror
The currently selected mirror is **[preferred]**. If you encounter a problem with this 
mirror, please select another mirror. If all mirrors are failing, there are backup 
mirrors (at the end of the mirrors list) that should be available.

<form name="setmirror" method="get" action="[location]">
Other mirrors: 
<select name="Preferred">
[if-any http]
  [for http]
    <option value="[http]">[http]</option>
  [end]
[end]
[if-any ftp]
  [for ftp]
    <option value="[ftp]">[ftp]</option>
  [end]
[end]
[if-any backup]
  [for backup]
    <option value="[backup]">[backup] (backup)</option>
  [end]
[end]
</select>
<input type="submit" value="Change"></input>
</form>

You may also consult the [complete list of mirrors](http://www.apache.org/mirrors/).

<a name="verify"></a>
## Verifying the integrity of the files

It is essential that you verify the integrity of the downloaded files using the GPG and 
SHA signatures. Security of the mirrors cannot be guaranteed, which means malicious code 
could be added to the downloads from the mirrors. By verifying the integrity of 
downloaded release files, you ensure they have not been tainted.

Run the following command to verify the SHA256 sum. You should get output 
similar to "apache-VCL-2.5.1.tar.bz2: OK":</p>

```bash
sha256sum -c apache-VCL-2.5.1.tar.bz2.sha256
```

Similarly, run the following command to verify the MD5 sum. It should give output similar to 
"apache-VCL-2.5.1.tar.bz2: OK":

```bash
md5sum -c apache-VCL-2.5.1.tar.bz2.md5
```

To verify the GPG signature (you'll need to have [GnuPG](http://www.gnupg.org/) installed):


1. download and import the [VCL KEYS file](https://www.apache.org/dist/vcl/KEYS) (if you've imported the KEYS file for previous 
releases, you do not need to import it again):

    ```bash
    gpg --import KEYS
    ```

1. download the GPG Signature to the same location as the release file
1. from the directory containing both the release file and the GPG signature, run

    ```bash
    gpg --verify apache-VCL-2.5.1.tar.bz2.asc
    ```

## TSU Notification - Encryption
This distribution includes cryptographic software. The country in which you
currently reside may have restrictions on the import, possession, use, and/or
re-export to another country, of encryption software. BEFORE using any
encryption software, please check your country's laws, regulations and policies
concerning the import, possession, or use, and re-export of encryption software,
to see if this is permitted. See <http://www.wassenaar.org/> for more
information.

The U.S. Government Department of Commerce, Bureau of Industry and Security
(BIS), has classified this software as Export Commodity Control Number (ECCN)
5D002.C.1, which includes information security software using or performing
cryptographic functions with asymmetric algorithms. The form and manner of this
Apache Software Foundation distribution makes it eligible for export under the
License Exception ENC Technology Software Unrestricted (TSU) exception (see the
BIS Export Administration Regulations, Section 740.13) for both object code and
source code.

The following provides more details on the included cryptographic software:

The web and backend portions of the code utilize php and perl functions to
encrypt password information stored in the database. The web code utilizes php
functions to encrypt cookie information passed to and stored in users' browsers.
The backend code uses openssh to connect to and control deployed nodes. openssh
heavily uses encryption.

Addionally, the web portion of the code includes portions of the phpseclib
library. This library is only used for PHP versions not supporting the function
"openssl_encrypt" (supported since PHP 5.3.0).

## Installation
For new installs, visit the on-line installation guide:

Latest Version:

* [Apache VCL 2.5.1 Installation Guide](/docs/VCL251InstallGuide.html)

Previous Versions:

* [Apache VCL 2.5 Installation Guide](/docs/VCL25InstallGuide.html)
* [Apache VCL 2.4.2 Installation Guide](/docs/VCL242InstallGuide.html)
* [Apache VCL 2.3.2 Installation Guide](/docs/VCL232InstallGuide.html)
* [Apache VCL 2.3.1 Installation Guide](/docs/VCL231InstallGuide.html)
* [Apache VCL 2.3 Installation Guide](/docs/VCL23Installation.html)
* [Apache VCL 2.2.1 Installation Guide](http://cwiki.apache.org/confluence/display/VCL/VCL+2.3+Installation)
* [Apache VCL 2.2 Installation Guide](http://cwiki.apache.org/confluence/display/VCL/VCL+2.3+Installation)
* [Apache VCL 2.1 Installation Guide](http://cwiki.apache.org/confluence/display/VCL/VCL+2.3+Installation)


## Upgrading
For upgrades, visit the on-line upgrade guide:

Upgrade to latest version:

* [upgrade 2.5 to 2.5.1](/docs/UpgradePreviousVersions/UpgradeFrom2.5to2.5.1.html)
* [upgrade 2.4.2 to 2.5.1](/docs/UpgradePreviousVersions/UpgradeFrom2.4.2to2.5.1.html)

Upgrade to 2.5

* [upgrade 2.4.2 to 2.5](/docs/UpgradePreviousVersions/UpgradeFrom2.4.2to2.5.html)

Upgrade to 2.4.2

* [upgrade 2.3.2 to 2.4.2](/docs/UpgradePreviousVersions/UpgradeFrom2.3.2to2.4.2.html)
* [upgrade 2.2.2 to 2.4.2](/docs/UpgradePreviousVersions/UpgradeFrom2.2.2to2.4.2.html)

Upgrade to 2.3.2

* [upgrade 2.3.1 to 2.3.2](/docs/UpgradePreviousVersions/UpgradeFrom2.3.1to2.3.2.html)
* [upgrade 2.3 to 2.3.2](/docs/UpgradePreviousVersions/UpgradeFrom2.3to2.3.2.html)
* [upgrade 2.2.1 to 2.3.2](/docs/UpgradePreviousVersions/UpgradeFrom2.2.1to2.3.2.html)
* [upgrade 2.2 to 2.3.2](/docs/UpgradePreviousVersions/UpgradeFrom2.2to2.3.2.html)

Upgrade to 2.2.2:

* [upgrade 2.2.1 to 2.2.2](/docs/UpgradePreviousVersions/UpgradeFrom2.2.1to2.2.2.html)
* [upgrade 2.2 to 2.2.2](/docs/UpgradePreviousVersions/UpgradeFrom2.2to2.2.2.html)

Upgrade really old versions to older versions:

to 2.3.1

* [upgrade 2.3 to 2.3.1](/docs/UpgradePreviousVersions/UpgradeFrom2.3to2.3.1.html)
* [upgrade 2.2.1 to 2.3.1](/docs/UpgradePreviousVersions/UpgradeFrom2.2.1to2.3.1.html)
* [upgrade 2.2 to 2.3.1](/docs/UpgradePreviousVersions/UpgradeFrom2.2to2.3.1.html)

to 2.3

* [upgrade 2.2.1 to 2.3](/docs/UpgradePreviousVersions/UpgradeFrom2.2.1to2.3)
* [upgrade 2.2 to 2.3](/docs/UpgradePreviousVersions/UpgradeFrom2.2to2.3)
* [upgrade 2.1 to 2.3](http://cwiki.apache.org/confluence/display/VCL/Upgrade+From+Previous+Version+%282.1+to+2.3%29)

to 2.2.1

* [upgrade 2.2 to 2.2.1](http://cwiki.apache.org/confluence/display/VCL/Upgrade+From+Previous+Version+%282.2+to+2.2.1%29)
* [upgrade 2.1 to 2.2.1](http://cwiki.apache.org/confluence/display/VCL/Upgrade+From+Previous+Version+%282.1+to+2.2.1%29)

to 2.2

* [upgrade 2.1 to 2.2](http://cwiki.apache.org/confluence/display/VCL/Upgrade+From+Previous+Version)

## Release Notes
See the [release notes page](/docs/releasenotes.html) for information about each release.

## Change Log
See the [change log page](/docs/changelog.html) for changes made in each release.
