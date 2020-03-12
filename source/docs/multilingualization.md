---
title: Adding a New Locale to the VCL Web Frontend
---

## Introduction

VCL 2.3 has the first step in multilingualization by allowing the parts of the site 
that the basic user sees to be presented in different languages. The initial work was 
done and contributed by Toru Yokoyama in JIRA-485.

More work will be done in future releases to add multilingualization to all parts of 
the site. Also, there are currently several sections where a paragraph may be 
translated in portions instead of as a whole. This does not provide for optimal 
translations. This should be addressed if future releases.

There are three places where translation work needs to happen to add a new language: 
a gettext translation file (.po or portable object file), a javascript translation 
file, and a few database entries.

## Places to translate

There are two files to work with - a php translation file and a javascript translation 
file. Also, there are entries that need to be added to the database in the connect
method table.

    vcl/locale/po_files/vcl.po.template
    vcl/js/nls/messages.js.template

## Creating a gettext translation file
vcl/locale/po_files/vcl.po.template is a base translation file. You need to create 
two new directories under vcl/locale for your new locale (using es_PR as an example):

    vcl/locale/es_PR/LC_MESSAGES
    vcl/locale/po_files/es_PR

Next, create a file named language in the new locale directory (vcl/locale/es_PR) 
with the name you would like displayed in the drop-down box for selecting the locale:

    echo 'Spanish (PR)' > vcl/locale/es_PR/language

Next, copy vcl/locale/po_files/vcl.po.template under the new po path:

    cp vcl/locale/po_files/vcl.po.template vcl/locale/po_files/es_PR/vcl.po

You need to translate each string in your new vcl.po file in to the new language. The 
file has pairs of lines like

    msgid "<H2>Welcome to the Virtual Computing Lab</H2>\n"
    msgstr ""

You must translate the string listed after msgid and place the translation on the 
msgstr line. There is a program under Linux named poedit from the gettext suite that 
makes this easier. Make sure you incorporate any HTML in the string into your 
translated string.

After you have translated everything, you need to compile the .po file into a .mo 
file using msgfmt, also from the gettext suite, placing the .mo file under the 
vcl/locale/es_PR/LC_MESSAGES/ path:

    msgfmt --output=vcl/locale/es_PR/LC_MESSAGES/vcl.mo vcl/locale/po_files/es_PR/vcl.po

## Creating a javascript translation file

There is a base translation file at vcl/js/nls/messages.js.template. You need to create a new directory under vcl/js/nls (using es_PR as an example):

    vcl/js/nls/es_PR

Next, copy vcl/js/nls/messages.js.template under the new nls path:

    cp vcl/js/nls/messages.js.template vcl/js/nls/messages.js

You need to translate each string in your new messages.js file in to the new 
language. The file has an English string and a translation string on each line line:

    'Times cannot be suggested for cluster reservations': '',

You must translate the string in the first set of quotes and place the translation 
in the second set of quotes for each string in the file.

## Adding entries to connectmethod table in database

VCL 2.3 also introduced Connection Methods. This actually introduced a problem with 
multilingualization because most of the text for the Connect page is now in the 
database. Each connect method has a description and the text to be displayed on the 
Connect page. These are in the connectmethod.description and connectmethod.connecttext 
fields. If you will only need a single language for your site, you can just change the 
text in those fields to be in your desired language. If you will need multiple 
languages, you can add additional fields to the table for each locale. You need to 
add two fields for each locale (using es_PR as an example):

    connectmethod.description_es_PR
    connectmethod.connecttext_es_PR

You can add as many of the pairs of fields to the database as needed. The VCL code 
will check for the existance of fields with names like the above, and automatically 
display the text from the correct one if it exists. If it does not, the content of 
connectmethod.description and connectmethod.connecttext will be used.