---
title: Using VCL to Broker Access to Pre-installed Machines
---

The Lab.pm provisioning module is used to broker access to standalone
pre-installed Linux or Solaris machines. These machines could be in an
existing walk-in computer lab or racked in a server room.

There are four main parts needed to setup a standalone machine to use with
the Lab.pm module.

1. a non-root account called vclstaff on the target machines
1. ssh idenitity key for vclstaff account, this key is used by the vcld
process on the management node
1. ssh service running on port 24 of the target machines
1. vclclientd running on the target machines, vclclientd in the bin
directory of the vcld release

For distribution to a large set of machines, an rpm or package could be
created to distribute vclclientd and related files.

# How it works {#howitworks}
The Lab.pm module confirms an assigned node or lab machine is accessible
using the ssh identity key on port 24. If this succeeds, then a small
configuration file with the state, user's id and the users' remote IP
address is sent to the node along with a flag to trigger the vclclientd
process to either open or close the remote access port. Currently this
module only supports Linux and Solaris lab machines. 

# How to setup: {#howtosetup}

All commands are run as root.


1. Create the non-root vclstaff account on target machine

    ```bash
    on linux: useradd -d /home/vclstaff -m vclstaff
    ```

2. Generate ssh identity keys for vclstaff account. Do not enter a passphrase for 
the key, just hit enter when prompted.

    ```bash
    su - vclstaff
    ssh-keygen -t rsa
    Generating public/private rsa key pair.
    Enter file in which to save the key (/home/vclstaff/.ssh/id_rsa):
    Created directory '/home/vclstaff/.ssh'.
    Enter passphrase (empty for no passphrase):
    Enter same passphrase again:
    Your identification has been saved in /home/vclstaff/.ssh/id_rsa.
    Your public key has been saved in /home/vclstaff/.ssh/id_rsa.pub.
    The key fingerprint is:
    ```

    At this point we have created a private key /home/vclstaff/.ssh/id_rsa and
    the public key /home/vclstaff/.ssh/id_rsa.pub.

1. Copy the public key to /home/vclstaff/.ssh/authorized_keys file

    ```bash
    cat /home/vclstaff/.ssh/id_rsa.pub > /home/vclstaff/.ssh/authorized_keys
    ```

1. Copy the private key to the management node. This can be stored in
/etc/vcl/lab.key. This private key is used by vcld to remotely log into the
the lab machine.

1. Edit /etc/vcld.conf
Set the variables IDENTITY_linux_lab and IDENTITY_solaris_lab to use this new key.
It should look like:

    ```bash
    IDENTITY_solaris_lab=/etc/vcl/lab.key
    IDENTITY_linux_lab=/etc/vcl/lab.key
    ```

1. Test out the newly created key from the vcl management node:

    ```bash
    ssh -i /etc/vcl/lab.key vclstaff@target_lab_machine
    ```

1. Set ssh server on target machine to listen on port 24. Edit
/etc/ssh/sshd_config on target lab machine(s).

    ```bash
    echo "Port 24" >> /etc/ssh/sshd_config
    ```

    For advanced ssh configurations one may need to also add vclstaff to the
    AllowUsers directive or some other group which would work with ones
    existing campus ssh login restrictions, if any.

1. restart sshd

    ```bash
    /etc/init.d/sshd restart
    ```

1. retest to make sure sshd is accessible on port 24

    ```bash
    ssh -p24 -i /etc/vcl/lab.key vclstaff@target_lab_machine
    ```

1. Copy vclclientd and vclclientd init script to target_lab_machine, from
managenment node:

    ```bash
    scp -P24 /usr/local/vcl/bin/vclclientd vclstaff@target_lab_machine:/home/vclstaff
    scp -P24 /usr/local/vcl/bin/S99vclclient.linux target_lab_machine:/etc/init.d/S99vclclient.linux
    ```

    add this start up script to the appropriate run time levels

1. Start vclclientd:

    ```bash
    /etc/init.d/S99vclclient.linux start
    ```

1. Add computers to the VCL database as one normally would. Make sure to set the 
type of the computer to **lab** and the Provisioning Engine to **Computing Lab**

1. Insert an image into the image table for this lab machine. You can set name and
prettyname to whatever you want. We'll use "lab-machine-image1" and "Lab Machine image"
in the example SQL:

    ```sql
    INSERT INTO `vcl`.`image`
    (`name`,
    `prettyname`,
    `ownerid`,
    `imagetypeid`,
    `platformid`,
    `OSid`,
    `lastupdate`,
    `forcheckout`)
    VALUES
    ('lab-machine-image1',
    'Lab Machine image',
    '1',
    (SELECT id FROM imagetype WHERE name = 'lab'),
    '1',
    (SELECT id FROM OS WHERE name = 'centos5'),
    NOW(),
    '1');
    ```

1. Insert a record into the imagerevision table. Note 'Lab Machine image'
can be what ever you want.

    ```sql
    INSERT INTO `vcl`.`imagerevision` (
    `imageid` ,
    `revision` ,
    `userid` ,
    `datecreated` ,
    `deleted` ,
    `production` ,
    `imagename`)
    VALUES (
    (SELECT id FROM image WHERE name = 'lab-machine-image1'),
    0,
    1,
    NOW(),
    0,
    1,
    'lab-machine-image1')
    ```

1. Insert a record into the resource table.

    ```sql
    INSERT INTO `vcl`.`resource` (
    `resourcetypeid` ,
    `subid`
    )
    VALUES (
    13,
    (SELECT id FROM image WHERE name = "lab-machine-image1")
    )
    ```

1. Set up the image to computer group mappings and grant access.

    These next steps will be done using the VCL web interface

    1. Create a new Image group

        Manage Groups->Add New Resource Group
    1. Create a new Computer group

        Manage Groups->Add New Resource Group
    1. Add new image (inserted above) to the image group just created in step 1.

        Manage Images->Edit Image Grouping
    1. Add machines that have vclclientd to the computer group created in step 2

        Manage Computers->Edit Computer Grouping
    1. Assign new computer group to be controlled by management node

        Management Nodes->Edit Management Node Mapping
    1. Grant access to the new lab image and computer group in the privilege tree.
