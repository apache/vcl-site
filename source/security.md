---
title:     Apache VCL Security
---

# Security Issues
The Apache Software Foundation takes security issues seriously and has a 
[security team](https://www.apache.org/security/) that helps Apache projects work through security 
issues. If you discover any potential vulnerabilities in Apache VCL, please report them to
[security@apache.org](mailto:security@apache.org).

## Known Security Issues
Here is a list of known security issues with Apache VCL along with the versions affected, versions
in which they were fixed, and information on patching vulnerable versions.

### CVE-2018-11772
* Announced: July 29th, 2019
* Affected versions: versions 2.1 through 2.5
* Fixed in version: 2.5.1
* [Installing patches](/patches/patching-CVE-2018.html)
* Problem type: SQL injection
* Description:

    Apache VCL versions 2.1 through 2.5 do not properly validate cookie input when determining what 
    node (if any) was previously selected in the privilege tree. The cookie data is then used in an 
    SQL statement. This allows for an SQL injection attack. Access to this portion of a VCL system 
    requires admin level rights.  Other layers of security seem to protect against malicious attack. 
    However, all VCL systems running versions earlier than 2.5.1 should be upgraded or patched. 
    This vulnerability was found and reported to the Apache VCL project by ADLab of Venustech.

### CVE-2018-11773
* Announced: July 29th, 2019
* Affected versions: versions 2.1 through 2.5
* Fixed in version: 2.5.1
* [Installing patches](/patches/patching-CVE-2018.html)
* Problem type: improper form validation
* Description:

    Apache VCL versions 2.1 through 2.5 do not properly validate form input when processing a 
    submitted block allocation. The form data is then used as an argument to the php built in 
    function strtotime. This allows for an attack against the underlying implementation of that 
    function. The implementation of strtotime at the time the issue was discovered appeared to be 
    resistant to a malicious attack. However, all VCL systems running versions earlier than 2.5.1 
    should be upgraded or patched. This vulnerability was found and reported to the Apache VCL 
    project by ADLab of Venustech.

### CVE-2018-11774
* Announced: July 29th, 2019
* Affected versions: versions 2.1 through 2.5
* Fixed in version: 2.5.1
* [Installing patches](/patches/patching-CVE-2018.html)
* Problem type: SQL Injection
* Description:

    Apache VCL versions 2.1 through 2.5 do not properly validate form input when adding and 
    removing VMs to and from hosts. The form data is then used in SQL statements. This allows for 
    an SQL injection attack. Access to this portion of a VCL system requires admin level rights.  
    Other layers of security seem to protect against malicious attack. However, all VCL systems 
    running versions earlier than 2.5.1 should be upgraded or patched. This vulnerability was 
    found and reported to the Apache VCL project by ADLab of Venustech.

### CVE-2013-0267
* Announced: May 6th, 2013
* Affected versions: versions 2.1, 2.2, 2.2.1, 2.3, 2.3.1
* Fixed in version: 2.2.2, 2.3.2
* Problem type: improper input validation
* Description:

    Some parts of VCL did not properly validate input data. This problem was present both in the 
    Privileges portion of the web GUI and in the XMLRPC API.

    A malicious user having a minimal level of administrative rights could 
    manipulate the data submitted by the web GUI or submit non-standard data to 
    the API to gain additional administrative rights.

    The API functions that are vulnerable were introduced in 2.3.1.  Some of those 
    API functions can also be exploited to perform a DOS attack on the site to 
    remove access from other users and to perform an XSS attack to gain elevated 
    privileges.

    The vulnerabilities were found by an Apache VCL developer doing a code review.