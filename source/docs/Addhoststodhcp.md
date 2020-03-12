---
title: Add entries to dhcpd.conf
---

#### Generate dhcpd.conf entries

You need to add entries for your VMs to your dhcpd.conf file so that
they will correctly be assigned their private addresses at boot.

1. Click Manage Computers
2. Select the All VM Computers group in the list at the top
3. Select the Computer Utilities radio button
4. Click Submit
5. Click the Check All link at the bottom of the table  
6. Next to "For selected computers, generate computer data for", select "dhcpd"
7. Click Generate Data
8. Enter the private IP address for your management node
9. Click Generate Data
10. Copy/Paste the data for dhcpd.conf to the dhcpd.conf file on
      your management node (ignore the part for dhcpd.leases)
11. Restart dhcpd:
   
       service dhcpd restart
   
12. Scroll to the bottom and click Close

#### Add entries to /etc/hosts

You need to add entries for your VM hosts and VMs to /etc/hosts

1. Click Manage Computers
2. Select the All VM Computers and the allComputers groups in the
               list at the top
3. Select the Computer Utilities radio button
4. Click Submit
5. Click the Check All link at the bottom of the table
6. Next to "For selected computers, generate computer data for",
               select /etc/hosts
7. Click Generate Data
8. Copy/Paste the data to your /etc/hosts file
9. Click Close

