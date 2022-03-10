Migration Rules
===============

About
-----

This page contains decisions that apply to all migrations for TRACE collections.  It exists so that we have one reference
point detailing how we approach building migration spreadsheets.

Notes and Decisions
-------------------

This section includes notes and decisions about various rules regarding migration.

====================================================================
Rule 1: Only Migrate Supplemental Files that Are in the metadata.xml
====================================================================

The s3 bucket includes supplemental files that have been deleted and are no longer associated with the work that it was
originally attached to.  An example of this is `ce_reports/2 <https://trace.tennessee.edu/ce_reports/2/>`_.

In order to not copy over files that have been intentionally deleted, we must follow what's identified in the metadata.xml
and not the bucket on its own.

=========================================================================================================
Rule 2: If the object points at a non-website on the streaming server, manage the files in the new system
=========================================================================================================

We have many objects that point at files on trace.lib.utk.edu or stream.lib.utk.edu.

Migrate these as works with the files managed in the new IR.

Items that point at stream:

* https://trace.tennessee.edu/utk_rothrock11/1/
* https://trace.tennessee.edu/utk_libfpubs/62/

Series that point at trace.lib.utk.edu:

.. code-block:: python

    ['utk_studfr06',
     'democracy',
     'utk_interstp3',
     'utk_chanhonoproj',
     'utk_studfr09',
     'utk_studfr13',
     'utk_studrecy',
     'utk_studfr08',
     'utk_compmatdata',
     'utk_chembiopubs',
     'utk_molecularsimulation',
     'utk_studfr11',
     'utk_interstp2',
     'utk_studfr07',
     'utk_marcspeak',
     'utk_black',
     'utk_mccarthy',
     'utk_interstp4',
     'utk_4hrfilmfest',
     'masmc2012',
     'utvswsummit',
     'utk_lawlibhist',
     'omsaconference',
     'v-pac',
     'ccisymposium']
