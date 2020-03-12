---
title: Network requirements
---

For the current Apache VCL release (version 2.2.1), the system requires a
minimum of two parallel networks, i.e.:
(1) A private network, providing interconnectivity between the VCL
management node and the deployed target server(s) (the latter with the
requested software being provided to the end user, running either real or
virtual images). This private network allows the management node to manage
the pool of server resources, and to load and tear down the images (OS plus
applications/middleware) on the target server(s) that will be handed to an
end user.
(2) A public network, providing outside users access to the main VCL GUI
via the internet, to request hardware/software resources, and to then
connect them directly to the allocated server(s).

This is enabled by installing two Ethernet NICs per target server, with a
minimum bandwidth of 1 Gbs each. 
For additional details, see
https://cwiki.apache.org/confluence/display/VCL/Network+Layout

Note from above that under some possible operational modes, only one NIC is
required (e.g., when accessing the IBM Smart Cloud). Under other
circumstances (e.g., controlling blades) more than two NICs may be
recommended. 
