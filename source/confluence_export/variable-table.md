---
title: Variable Table
---

<a name="VariableTable-Overview"></a>
## Overview

This page describes the _variable_ table in the database.&nbsp; The purpose
of this table is to allow pieces of data to be easily stored in the
database&nbsp;without having to&nbsp;manipulate the schema.&nbsp; The need
for such a table has grown over time as more and more features are added to
VCL.&nbsp; This table will become very useful as VCL becomes increasingly
modularized.&nbsp; This table will allow any VCL component to access the
variable data without having to interact directly with the database.

<a name="VariableTable-VariableNames"></a>
### Variable Names

A variable stored in this table can be thought&nbsp;just like any other
programatic variable \-\- it has a unique name and value.&nbsp; The name
can be any string and is chosen by the developer utilizing the table.&nbsp;
Since the name must be unique and the variable&nbsp;table is shared by all
facets of VCL (frontend, backend, modules), the developer should choose a
name that isn't too general.&nbsp; It is advisable to include something
like the module name in the variable name in order to prevent other
components from overwriting the variable.

<a name="VariableTable-VariableValues&Serialization"></a>
### Variable Values & Serialization

The variable value is completely flexible. &nbsp;It can be a
simple&nbsp;integer or a complex data structure.&nbsp; This is accomplished
by [serializing](http://en.wikipedia.org/wiki/Serialization)
 the value before saving it to the database.&nbsp; [YAML|http://en.wikipedia.org/wiki/Yaml]
 is used to serialize the data.&nbsp; YAML is a human friendly data
serialization standard for all programming languages
([http://yaml.org/]).&nbsp; YAML modules are available for Perl, PHP, and
many other languages:
* Perl: [http://search.cpan.org/~ingy/YAML-0.68/lib/YAML.pm](http://search.cpan.org/~ingy/YAML-0.68/lib/YAML.pm)
* PHP: [http://code.google.com/p/spyc](http://code.google.com/p/spyc)

Because the data is serialized into a highly compatible format, the backend
and frontend can utilize common variables.&nbsp; It will be easy for the
frontend to provide a means to configure variables by capturing the data
entered into a web page, constructing a data structure, serializing it via
a PHP YAML module,&nbsp;and then saving&nbsp;the data structure in the
variable table.&nbsp; The backend can then access the identical data
structure using a Perl YAML module to deserialize the data.

<a name="VariableTable-BackendInterface"></a>
### Backend Interface

The variable table&nbsp;is utilized by backend code via functions provided
by the DataStructure.pm module:
* get_variable($name)
* set_variable($name, $value)

<a name="VariableTable-DatabaseTableStructure"></a>
## Database Table Structure

The variable has the following columns:
<table>
<tr><th> id </th><th> name </th><th> value </th><th> setby </th><th> timestamp </th></tr>
  
  
  
  
  
  
  
  
unique | longtext | varchar(40) | timestamp |
* id
** variable.id contains a unique&nbsp;auto-incremented unsigned integer
value
** The id column is consistent with most other columns in the VCL database
* name
** variable.name contains a string
** variable.name values must be unique
** variable.name provides a human-friendly means of identifying a variable
* value
** variable.value contains an encoded&nbsp;string which is a YAML
serialized representation of the data
** The string stored in variable.value is programatically serialized before
it is stored and programatically deserialized when it is retrieved
* setby
** variable.setby contains a string which indicates who/where last set the
data
** variable.setby is mainly used for debugging purposes
** variable.setby can be NULL but should be set whenever a row is altered
* timestamp
** variable.timestamp contains the date and time when the variable was last
set
** variable.timestamp&nbsp;is automatically&nbsp;updated whenever a row is
inserted or altered because the "ON UPDATE CURRENT_TIMESTAMP" column
attribute is set
</table>

<a name="VariableTable-SQLtabledefinition"></a>
### SQL table definition


    CREATE TABLE `variable` (
    � `id` smallint(5) unsigned NOT NULL auto_increment,
    � `name` varchar(128) NOT NULL,
    � `value` longtext NOT NULL,
    � `setby` varchar(128) default NULL,
    � `timestamp` datetime NOT NULL,
    � PRIMARY KEY� (`id`),
    � UNIQUE KEY `name` (`name`)
    ) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;


<a name="VariableTable-Examples"></a>
## Examples


<a name="VariableTable-Example1:"></a>
### Example 1:

The following hash is created in Perl:

    my %kms_configuration = (
    �"ECU" => "192.168.22.33:1688",
    �"NCSU" => "kms-server.ncsu.edu",
    );
    $self->data->set_variable("kms-configuration", \%kms_configuration);

The keys correspond to the affiliation.name column in the database.&nbsp;
The values represent the addresses (phony) of Windows Vista/2008 KMS
activation servers.

This hash is serialized by DataStructure.pm::set_variable() using the YAML
module's Dump function which transforms the hash into:

    ---
    ECU: 192.168.22.33:1688
    NCSU: kms-server.ncsu.edu

The following&nbsp;row is saved in the variable table by the
DataStructure.pm::set_variable() subroutine:
<table>
<tr><th> id </th><th> name </th><th> value </th><th> setby </th><th> timestamp </th></tr>
  
  
  
  
NCSU: kms-server.ncsu.edu | new.pm:139 | 2009-05-26 11:35:36 |
To retrieve the data:

    my $kms_configuration = $self->data->get_variable("kms-configuration");
    my $kms_address = $kms_configuration->{$affiliation_id};


<a name="VariableTable-Example2:"></a>
### Example 2:

A more elaborate data structure is created in Perl containing an array of
hashes. One of the hash values (email) can be multivalued because the value
is an anonymous array:

    my @contacts = (
     {
      "firstname" => "Joe",
      "lastname" => "Doe",
      "email" => ["joe@somewhere.org", "jdoe22@unity.ncsu.edu"]
,
      "employee_id" => 3342
     },
     {
      "firstname" => "Jane",
      "lastname" => "Doe",
      "email" => ["jane@somewhere.org"]
,
      "employee_id" => 7865
     }
    );��
    $self->data->set_variable("contacts", \@contacts);

DataStructure.pm::set_variable() uses YAML::Dump to transform this data
structure into:

    ---
    - email:
    ��� - joe@somewhere.org
    ��� - jdoe22@unity.ncsu.edu
    � employee_id: 3342
    � firstname: Joe
    � lastname: Doe
    - email:
    ��� - jane@somewhere.org
    � employee_id: 7865
    � firstname: Jane
    � lastname: Doe

The following row is then added to the variable table:
<table>
<tr><th> id </th><th> name </th><th> value </th><th> setby </th><th> timestamp </th></tr>
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
&nbsp; lastname: Doe | DataStructure.pm:554 | 2009-05-26 12:35:36 |
To retrieve the data:

    my @returned_contacts = @{$self->data->get_variable('contacts')};
    for my $contact (@returned_contacts) {
       print "Name: $contact->{firstname} $contact->{lastname}\n";
       for my $email_address (@{$contact->{email}}) {
          print "Email: $email_address\n";
       }
       print "---\n";
    }

