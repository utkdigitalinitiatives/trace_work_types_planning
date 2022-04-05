Conference Proceedings Work Type
================================

About
-----

This work type represents conference proceeding.  The object may include additional files including PDFs that are only
portions of the entire object.

This is a separate work type primarily because stakeholders felt that people would not know whether this should go to
book or other.

Migration Scope
---------------

Only PDF like objects whould get this work type and items will be hand selected to get this work type. One specific collection
in scope is:

.. code-block:: text

    utk_sasproceed

Suggested Actions
-----------------

1. Only objects whose primary file type :code:`PDF` should be migrated as this work type.
2. We may need a cover page for these.
3. We will keep all associated supplemental files.
4. We will hand select these for migration.

Example
-------

For this example, let's use the contents of :code:`https://trace.tennessee.edu/utk_sasproceed/8`:

.. code-block:: text

    Ethnocentrism_NFP_30March2021.pdf
    metadata.xml


This object includes a descriptive metadata file and the original file uploaded to the repository.

PCDM Model for Fedora
---------------------

==============
The Whole Work
==============

The object should be a :code:`pcdmworks:Work` and describe its relationship to its files along with its descriptive
metadata elements.


.. code-block:: turtle

    @prefix pcdm: <http://pcdm.org/models#> .
    @prefix pcdmuse: <http://pcdm.org/2015/05/12/use> .
    @prefix pcdmworks: <http://pcdm.org/2016/02/16/works> .
    @prefix : <https://location-of-future-repository/extra/paths/> .

    :sample-conference_proceedings a pcdmworks:Work ;
        <http://purl.org/dc/terms/title> "Ethnocentrism in Its Many Guises" ;
        pcdm:hasFile :sample_conference_proceeding_file_1, :sample_conference_proceeding_file_2 .

==========================
The Original Uploaded File
==========================

The original uploaded file representing this work should be a :code:`pcdmuse:OriginalFile`.

.. code-block:: turtle

    @prefix pcdm: <http://pcdm.org/models#> .
    @prefix pcdmuse: <http://pcdm.org/2015/05/12/use> .
    @prefix pcdmworks: <http://pcdm.org/2016/02/16/works> .
    @prefix : <https://location-of-future-repository/extra/paths/> .

    :sample_conference_proceeding_file_1 a pcdmuse:OriginalFile ;
        rdfs:label "Ethnocentrism_NFP_30March2021.pdf" ;
        pcdm:fileOf :sample-conference-proceedings .

======================
Original Metadata File
======================

We want to keep the original metadata in case there are questions about the migration or something that originally existed
but not appearing in the metadata here.

Ideally, this would not be available to users (at least in the GUI).

.. code-block:: turtle

    @prefix pcdm: <http://pcdm.org/models#> .
    @prefix pcdmuse: <http://pcdm.org/2015/05/12/use> .
    @prefix pcdmworks: <http://pcdm.org/2016/02/16/works> .
    @prefix : <https://location-of-future-repository/extra/paths/> .

    :sample_conference_proceeding_file_2 a pcdm:File ;
        rdfs:label "metadata.xml" ;
        pcdm:fileOf :sample-conference-proceedings .

==================
Supplemental Files
==================

Books can have supplemental files that we want to make available to users.

While this object does not have one, we would model it like this if it did:

.. code-block:: turtle

    @prefix pcdm: <http://pcdm.org/models#> .
    @prefix pcdmuse: <http://pcdm.org/2015/05/12/use> .
    @prefix pcdmworks: <http://pcdm.org/2016/02/16/works> .
    @prefix dcterms: <http://purl.org/dc/terms/> .
    @prefix fabio: <http://purl.org/spar/fabio/> .
    @prefix : <https://location-of-future-repository/extra/paths/> .

    :sample_conference_proceeding_file_3 a pcdmuse:OriginalFile, fabio:SupplementaryInformation  ;
        rdfs:label "Supplemental_File_1.fasta" ;
        dcterms:description "JCVI-CMR Catalase Database (FASTA format)" ;
        dcterms:format "text/plain" ;
        pcdm:fileOf <http://localhost/sample-conference-proceedings> .

