---
title: Network Layout
---

{excerpt}This page describes the basic network layout required in order for
VCL to function. It also describes the recommended network layout if a
blade chassis management module is used.{excerpt}

<a name="NetworkLayout-AtthesimplestformVCLusestwonetworks"></a>
# At the simplest form VCL uses two networks

1. Private - applies to provisioning modules where node is reloaded, esx,
vmware, etc.
1. * loading and boot strapping images
1. * managing reservations, adding/deleting accounts, controlling the OS on
the node
1. * opens access ports on node for user requests on public network interface
1. * image creation
1. * DHCP serves fixed-addresses over this network to the eth0 adapter of the
node
1. * DHCP is run on the management node - prerequisite
1. Public
1. * user accessible
1. * VCL can either use dhcp(preferred) or statically assign addresses to the
node on the public network

The diagram below shows the simple layout:
{gliffy:name=Simple network layout|space=VCL|page=Network
Layout|align=left|size=M}

<a name="NetworkLayout-BladeCenternetworklayout"></a>
# Blade Center network layout

The network using blade center is more involved by adding a 2nd private
network.
1. Private 1 - applies to provisioning modules, xCAT, vmware, etc.
1. Private 2
1. * allows management node to interact with blade center management module
1. * provides scaling method for adding multiple blade center's
1. Public - user access

The diagram below shows the suggested network layout when using blade
center.

{gliffy:name=Blade Center network layout|space=VCL|page=Network
Layout|align=left|size=M}
