---
title: KVM Configuration
---

<a name="KVMConfiguration-InstallPackages"></a>
#### Install Packages

The following commands will install the Linux packages required for VCL to
manage a KVM host:

{panel}yum install libvirt virt-manager dejavu-lgc-sans-fonts bridge-utils
libguestfs-tools \-y
/sbin/chkconfig libvirtd on

echo "Starting the libvirtd service..."
/sbin/chkconfig libvirtd on
/sbin/service libvirtd start{panel}
The virt-manager package is optional.&nbsp; It is a graphical utility which
is used to manage KVM and other hypervisors controlled via libvirt.&nbsp;
The dejavu-lgc-sans-fonts package is usually necessary in order for
virt-manager to render fonts correctly.


<a name="KVMConfiguration-ConfigureNetworking"></a>
#### Configure Networking

The following commands will configure networking to allow KVM guests to
communicate.&nbsp; It configures a bridge named br0 on eth0, and br1 on
eth1.&nbsp; When configured this way, the network names in the VM host
profile should be set to br0 and br1.
{panel}echo "Stopping the NetworkManager service..."
chkconfig NetworkManager off 2>/dev/null
service NetworkManager stop 2>/dev/null
yum erase NetworkManager \-y


cat > /etc/sysconfig/network-scripts/ifcfg-eth0 <<EOF
DEVICE=eth0
ONBOOT=yes
BRIDGE=br0
NM_CONTROLLED=no
EOF
echo "Configured ifcfg-eth0:"
cat /etc/sysconfig/network-scripts/ifcfg-eth0

cat > /etc/sysconfig/network-scripts/ifcfg-br0 <<EOF
DEVICE=br0
TYPE=Bridge
BOOTPROTO=dhcp
ONBOOT=yes
DELAY=0
NM_CONTROLLED=no
EOF
echo "Configured ifcfg-br0:"
cat /etc/sysconfig/network-scripts/ifcfg-br0

cat > /etc/sysconfig/network-scripts/ifcfg-eth1 <<EOF
DEVICE=eth1
ONBOOT=yes
BRIDGE=br1
NM_CONTROLLED=no
EOF
echo "Configured ifcfg-eth1:"
cat /etc/sysconfig/network-scripts/ifcfg-eth1
  
  

cat > /etc/sysconfig/network-scripts/ifcfg-br1 <<EOF
DEVICE=br1
TYPE=Bridge
BOOTPROTO=dhcp
ONBOOT=yes
DELAY=0
NM_CONTROLLED=no
EOF
echo "Configured ifcfg-br1:"
cat /etc/sysconfig/network-scripts/ifcfg-br1

echo "Configuring eth0 bridge..."
ifdown br0 2>/dev/null
brctl delbr br0 2>/dev/null
brctl addbr br0
brctl addif br0 eth0

echo "Configuring eth1 bridge..."
ifdown br1 2>/dev/null
brctl delbr br1 2>/dev/null
brctl addbr br1
brctl addif br1 eth1

/sbin/chkconfig network on
/sbin/service network restart{panel}

<a name="KVMConfiguration-AddaNetworkStoragePool"></a>
#### Add a Network Storage Pool

The following commands will add an NFS storage pool named images to the KVM
host.&nbsp; The */images* directory is exported via NFS from host
*10.10.10.1*.&nbsp; This directory is mounted as */mnt/kvm1* on the KVM
host.&nbsp; An entry is added to /etc/fstab to ensure the directory is
mounted if the KVM host is rebooted.

{panel}echo "Adding the images pool..."
virsh pool-destroy images 2>/dev/null
virsh pool-undefine images 2>/dev/null
umount /images 2>/dev/null
mkdir /images&nbsp; 2>/dev/null
chmod \-R 0755 /images
echo '10.10.10.1:/mnt/kvm1 /images nfs
vers=3,rsize=32768,wsize=32768,intr,rw,soft,bg 0 0' >> /etc/fstab
mount \-a

virsh pool-define-as \--name images \--type dir \--target /images
virsh pool-autostart \--pool images
virsh pool-start images{panel}

<a name="KVMConfiguration-AddaLocalStoragePool"></a>
#### Add a Local Storage Pool

The following commands will define a storage pool named *local-vms*
pointing to the */vms* directory on the local disk:

{panel}echo "Adding the local-vms pool..."
virsh pool-destroy local-vms 2>/dev/null
virsh pool-undefine local-vms 2>/dev/null
mkdir /vms 2>/dev/null
chmod \-R 755 /vms
virsh pool-define-as \--name local-vms \--type dir \--target /vms
virsh pool-autostart \--pool local-vms
virsh pool-start local-vms{panel}
