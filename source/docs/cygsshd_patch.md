---
title: Cygwin SSHD Service Name Change Patch for VCL 2.5.1
---

When Microsoft made openssh available as an installable package on Windows, they
used the same service name (sshd) that cygwin had been using for many years. This
caused the Cygwin project to change the name of the sshd service they install from
sshd to cygsshd. VCL 2.5.1 needs a patch applied to handle the service name change.

# Download Patch

The patch is available from the ASF distribution servers.

[Download patch](https://dist.apache.org/repos/dist/release/vcl/patches/cygwin_sshd_to_cygsshd/cygwin_sshd_for_2.5.1.patch) 
[ [GPG](https://dist.apache.org/repos/dist/release/vcl/patches/cygwin_sshd_to_cygsshd/cygwin_sshd_for_2.5.1.patch.asc) ] 
[ [SHA512](https://dist.apache.org/repos/dist/release/vcl/patches/cygwin_sshd_to_cygsshd/cygwin_sshd_for_2.5.1.patch.sha512) ] 

# Validate Patch

It is essential that you verify the integrity of the patch file using the GPG and 
SHA signatures. By verifying the integrity of the patch, you ensure it has not
been tainted.

Run the following command to verify the SHA512 sum. You should get output 
similar to "cygwin_sshd_for_2.5.1.patch: OK":</p>

```bash
sha512sum -c cygwin_sshd_for_2.5.1.patch.sha512
```

To verify the GPG signature (you'll need to have [GnuPG](http://www.gnupg.org/) installed):

1. download and import the [VCL KEYS file](https://www.apache.org/dist/vcl/KEYS) (if you've imported the KEYS file for previously,
you do not need to import it again):

    ```bash
    gpg --import KEYS
    ```

1. download the GPG Signature to the same location as the patch file
1. from the directory containing both the release file and the GPG signature, run

    ```bash
    gpg --verify cygwin_sshd_for_2.5.1.patch.asc

# Apply Patch
The patch is applied to the management node code, which is typically installed to /usr/local/vcl.
The following example assumes the patch was downloaded to /tmp.

```bash
cd /usr/local/vcl
patch -p2 < /tmp/cygwin_sshd_for_2.5.1.patch
```

If it applies correctly, you should see a message similar to

```bash
patching file bin/cygwin-sshd-config.sh
patching file bin/gen-node-key.sh
patching file lib/VCL/Module/OS/Windows/Version_6/8.pm
patching file lib/VCL/Module/OS/Windows.pm
patching file tools/Windows/Scripts/update_cygwin.cmd
```
