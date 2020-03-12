---
title: Apache Derby Database
---

# Using Apache Derby Database

<big><font color="red">**NOTE: The current code in the trunk does not support Derby
(21 Aug 2009)**</font></big>

## Prerequisites

You should have installed:

* JDK (it is maybe possible to work with jre only)

## Downloading and Setting Up the Database for VCL

1. Download Apache Derby and install it.

    ```bash
    cd ~
    wget http://apache.g5searchmarketing.com/db/derby/db-derby-10.5.1.1/db-derby-10.5.1.1-bin.tar.gz
    tar -xzf db-derby-10.5.1.1-bin.tar.gz
    mkdir /opt/Apache
    mv db-derby-10.5.1.1-bin /opt/Apache/derby
    export DERBY_HOME="/opt/Apache/derby"
    export CLASSPATH="${DERBY_HOME}/lib/derby.jar:${DERBY_HOME}/lib/derbytools.jar:${CLASSPATH}"
    PATH="$DERBY_HOME/bin:$PATH"
    ```

1. Create a database in Apache Derby. The database has to be placed in the
path */opt/*.
  Replace *'vcluser'* and *'vcluserpassword'* with the user and password
you want.

    ```bash
    cd /opt/
    ij
    connect 'jdbc:derby:vcl1;create=true;user='vcluser';password='vcluserpassword';';
    exit;
    ```

1. Download [vcl.sql](https://svn.apache.org/repos/asf/vcl/trunk/mysql/vcl.sql)
and the
[derby-parser.pl](/comm/commprojects/derby-parser.pl).
 Edit the file *'derby-parser.pl'*. The variables 
*'$user'* and *'$pw'* should match your database.

    ```bash
    svn export https://svn.apache.org/repos/asf/vcl/trunk/mysql/vcl.sql
    wget http://vcl.apache.org/comm/commprojects/derby-parser.pl
    chmod a+x derby-parser.pl
    ./derby-parser.pl
    ```

1. Import vcl-derby.sql file into database. It is a good idea to direct the
output to file and check if there were any errors.

    ```bash
    ij vcl-derby.sql > import.log
    ```

## Setting up the dbd_jdbc Server
1. Install log4j

    ```bash
    cd ~
    wget http://www.apache.org/dyn/closer.cgi/logging/log4j/1.2.15/apache-log4j-1.2.15.tar.gz
    tar -zxf apache-log4j-1.2.15.tar.gz
    mv apache-log4j-1.2.15 /opt/Apache/derby/lib/
    ```

1. When installing the perl modules using the *'install_perl_libs.pl'*
(*/usr/local/vcl/bin/install_perl_libs.pl*) two extra modules need to the
installed for Derby. Open the file *'install_perl_libs.pl'* and in the list
of modules to download add the following two modules.

    ```text
    http://search.cpan.org/CPAN/authors/id/G/GB/GBARR/Convert-BER-1.3101.tar.gz
    http://search.cpan.org/CPAN/authors/id/V/VI/VIZDOM/DBD-JDBC-0.71.tar.gz
    ```

1. Run the scrips as normal

    ```bash
    perl /usr/local/vcl/bin/install_perl_libs.pl
    ```

1. Copy some file from the modules to Derby directory

    ```bash
    cp /tmp/perl-modules/DBD-JDBC-0.71/dbd_jdbc.jar /opt/Apache/derby/lib/
    cp /tmp/perl-modules/DBD-JDBC-0.71/log4j.properties /opt/Apache/derby/lib/apache-log4j-1.2.15
    ```

1. Create a script file which will launch the dbd_jdbc Server. Save it under
any name and directory (e.g. /opt/server.sh), only remember that this
scrips needs to be executed every time you start up the server. The file
should contain

    ```bash
    #!/bin/bash
    java -Djdbc.drivers=org.apache.derby.EmbeddedDriver -Ddbd.port=12345 -classpath /opt/Apache/derby/lib/derby.jar:/opt/Apache/derby/lib/dbd_jdbc.jar:/opt/Apache/derby/lib/apache-log4j-1.2.15/log4j-1.2.15.jar:/opt/Apache/derby/lib/apache-log4j-1.2.15/  com.vizdom.dbd.jdbc.Server &
    ```

    Note1: if some of your paths are different you need make the changes in
    this scrips file as well

    Note2: currently port 12345 is used for connecting to Derby, this is hard
    coded. Can be changed on a later stage.

1. Make the script executable

    ```bash
    chmod a+x /opt/server
    ```

1. Start the Server

    ```bash
    /opt/server
    ```
