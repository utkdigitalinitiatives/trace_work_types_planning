============================
Orcid Integration User Story
============================

-----
About
-----

This page describes the University of Tennessee's expectations for integration between Orcid and our institutional
repository service, TRACE.

This page also serves as a guide for us thinking about the intersection of ORCID, name authorities, Google Scholar
inclusion, and the values that are stored as part of descriptive metadata in SOLR, Fedora, etc.

-------------------------------
Reviewing Other Implementations
-------------------------------

The University of Virginia
==========================

The University of Virginia maintains a `UVA-ORCID Connector <https://www.library.virginia.edu/services/orcid-at-uva/>`_
that allows researchers to create or connect an ORCiD iD, verify their UVA affiliation, and display and use the iD in
the University of Virginia’s systems.  This system insures:

* an iD can be connected to an institution only via direct permission.
* a user can remove the institution connection to your iD at any time.
* the user can change visibility, share, or remove information, such as scholarship works in their ORCID record at any time.
* a user can add more identifying information to their ORCID record at any time.

Once a researcher connects their ORCID iD to UVA, the Library’s Libra scholarly repository shows their ORCID iD on each
LibraETD or LibraOpen work for which you are an author or co-author and adds citations of the work to the ORCID profile.

Advancing Hyku: Hyrax / ORCID Integration
=========================================


Describe how this works

.. literalinclude:: ../literals/delete.json
   :language: json
   :lines: 187-196
   :linenos:
