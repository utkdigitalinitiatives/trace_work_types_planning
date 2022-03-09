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