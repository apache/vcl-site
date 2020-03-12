---
title: Add entries to /etc/hosts
---

For vcld to probably communicate with the nodes on the private network, you need to add entries for your nodes to /etc/hosts on the management node(s).
To do go to your vcl portal and follow these steps.

 1. Click Manage Computers
 2. Select the allComputers group in the list at the top
 3. Select the Computer Utilities radio button
 4. Click Submit
 5. Click the Check All link at the bottom of the table
 6. Next to "For selected computers, generate computer data for", select /etc/hosts
 7. Click Generate Data
 8. Copy/Paste the data to your /etc/hosts file
 9. Click Close


The data generated will include a list of your short hostnames and the private IP addresses stored in the vcl database.

