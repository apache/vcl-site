---
title: VCL 2.3 Configure Frontend Authentication
---

{excerpt:hidden=true}
How to configure authentication for the frontend VCL web code using LDAP
and Local accounts.{excerpt}

<a name="VCL2.3ConfigureFrontendAuthentication-ConfigureFrontendAuthentication"></a>
# Configure Frontend Authentication

<a name="VCL2.3ConfigureFrontendAuthentication-*AddingLocalVCLAccounts*"></a>
## *Adding Local VCL Accounts*

Local VCL accounts are contained within the VCL database. The *admin*
account is a local VCL account. Additional local accounts can be added via
the backend management node code. After you have finished the backend
management node installation, run:
{tip}
vcld \-setup
{tip}
1. Select *VCL Base Module*
1. Select *Add Local VCL User Account*
1. Enter the requested information

{include:VCL 2.3 - Adding LDAP Authentication}
