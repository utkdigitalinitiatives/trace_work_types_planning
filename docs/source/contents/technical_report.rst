Technical Report Work Type
==========================

About
-----

This work type represents technical report objects in our institutional repository.

Content of this work type should meet the
`Google Scholar inclusion guidelines <https://scholar.google.com/intl/en/scholar/inclusion.html>`_ and be discoverable
in Google Scholar.

These objects should always have:

1. The uploaded work
2. Descriptive metadata
3. Proper metatags for correct Google Scholar Inclusion

Example
-------

For this example, let's use the contents of :code:`https://trace.tennessee.edu/ce_reports/2`:

.. code-block:: text

    0-JonesWierschem_CEE_Report.pdf
    JonesWierschem_CEE_Report.pdf
    metadata.xml
    stamped.pdf

This object includes a descriptive metadata file, the original file uploaded, and a copy of the file with
a cover page.

Suggested PCDM / Structural Metadata
------------------------------------

==============
The Whole Work
==============

The object should be a :code:`pcdmworks:Work` and describe its relationship to its files along with its descriptive
metadata elements.


.. code-block:: turtle

    @prefix pcdm: <http://pcdm.org/models#> .
    @prefix pcdmuse: <http://pcdm.org/2015/05/12/use> .
    @prefix pcdmworks: <http://pcdm.org/2016/02/16/works> .

    <http://localhost/sample-tecnical-report> a pcdmworks:Work ;
        <http://purl.org/dc/terms/title> "Accelerated Innovation Development of Laser Metrology for Steel Bridge ..." ;
        pcdm:hasFile <http://localhost/sample_report_file_1>, <http://localhost/sample_report_file_2>, <http://localhost/sample_report_file_3> .

==========================
The Original Uploaded File
==========================

The original uploaded file representing this work should be a :code:`pcdmuse:OriginalFile`.

.. code-block:: turtle

    @prefix pcdm: <http://pcdm.org/models#> .
    @prefix pcdmuse: <http://pcdm.org/2015/05/12/use> .
    @prefix pcdmworks: <http://pcdm.org/2016/02/16/works> .

    <http://localhost/sample_report_file_1> a pcdmuse:OriginalFile ;
        rdfs:label "JonesWierschem_CEE_Report.pdf" ;
        pcdm:fileOf <http://localhost/sample-technical-report> .

This file does not need to be publicly accessible.

====================
File With Cover Page
====================

There should be a file with a cover page to aid in indexing with Google Scholar with appropriate metadata.

.. code-block:: turtle

    @prefix pcdm: <http://pcdm.org/models#> .
    @prefix pcdmuse: <http://pcdm.org/2015/05/12/use> .
    @prefix pcdmworks: <http://pcdm.org/2016/02/16/works> .

    <http://localhost/sample_report_file_2> a pcdmuse:PreservationFile, pcdmuse:IntermediateFile ;
        rdfs:label "JonesWierschem_CEE_Report.pdf" ;
        pcdm:fileOf <http://localhost/sample-technical_report> .

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

    <http://localhost/sample_report_file_3> a pcdm:File ;
        rdfs:label "metadata.xml" ;
        pcdm:fileOf <http://localhost/sample-technical-report> .

==================
Supplemental Files
==================

Technical reports can have supplemental files that we want to make available to users.

While this object does not have one, we would model it like this if it did:

.. code-block:: turtle

    @prefix pcdm: <http://pcdm.org/models#> .
    @prefix pcdmuse: <http://pcdm.org/2015/05/12/use> .
    @prefix pcdmworks: <http://pcdm.org/2016/02/16/works> .
    @prefix dcterms: <http://purl.org/dc/terms/> .
    @prefix fabio: <http://purl.org/spar/fabio/> .

    <http://localhost/sample_report_file_4> a pcdmuse:OriginalFile, fabio:SupplementaryInformation  ;
        rdfs:label "Supplemental_File_1.fasta" ;
        dcterms:description "JCVI-CMR Catalase Database (FASTA format)" ;
        dcterms:format "text/plain" ;
        pcdm:fileOf <http://localhost/sample-technical-report> .

Google Scholar Metatags
-----------------------

In order to insure discoverability in Google Scholar as a technical report, :code:`highwire press meta tags` should be
used and a corresponding cover page should be generated.

.. code-block:: xml

    <meta name="citation_title" content="Accelerated Innovation Development of Laser Metrology for Steel Bridge Fabrication">
    <meta name="citation_author" content="Jones, Timothy W.">
    <meta name="citation_author" content="Wierscheim, Nicholas E.">
    <meta name="citation_technical_report_institution" content="University of Tennessee">
    <meta name="citation_abstract_html_url" content="###Link to the HTML Page the Work Appears On###">
    <meta name="citation_publication_date" content="2019" />
    <meta name="citation_language" content="en_US" />
    <meta name="citation_pdf_url" content="###Link to the PDF###" />

Descriptive Metadata
--------------------

+------------------+------------------+------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------+------------+------------+-----------+---------------+------------------------------+---------------------------+------------------------------------------+
| Name             | Display Label    | Property                                       | Description                                                                                                                                                                                                                                                                      | Required | Obligation | Admin only | Facetable | Brief Results | Vocab                        | Syntax                    | Metatags                                 |
+==================+==================+================================================+==================================================================================================================================================================================================================================================================================+==========+============+============+===========+===============+==============================+===========================+==========================================+
| abstract         | Abstract         | http://purl.org/dc/terms/abstract              | A summary of the resource.                                                                                                                                                                                                                                                       | Optional | 0-n        | no         | no        | yes           | none                         |                           | citation_abstract, dcterms.abstract      |
+------------------+------------------+------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------+------------+------------+-----------+---------------+------------------------------+---------------------------+------------------------------------------+
| author           | Author           | http://id.loc.gov/vocabulary/relators/aut      | The characters that should be displayed after a person's name                                                                                                                                                                                                                    | Required | 1-n        | no         | yes       | yes           | none                         |                           | citation_author                          |
+------------------+------------------+------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------+------------+------------+-----------+---------------+------------------------------+---------------------------+------------------------------------------+
| classification   | Classification   | https://dbpedia.org/ontology/classification    | A string representing a class or category the resource is assigned to for browsing purposes                                                                                                                                                                                      | Required | 1          | no         | yes       | no            | local yml file               |                           |                                          |
+------------------+------------------+------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------+------------+------------+-----------+---------------+------------------------------+---------------------------+------------------------------------------+
| college          | College          | https://dbpedia.org/ontology/college           | The college associated with the resource's creator.                                                                                                                                                                                                                              | Optional | 0-n        | no         | yes       | no            | local yml file               |                           |                                          |
+------------------+------------------+------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------+------------+------------+-----------+---------------+------------------------------+---------------------------+------------------------------------------+
| discipline       | Discipline       | http://dbpedia.org/ontology/academicDiscipline | A concept that identifies a field of knowledge or human activity defined in a controlled vocabulary, such as Computer Science, Biology, Economics, Cookery or Swimming.                                                                                                          | Required | 1-n        | no         | yes       | no            | local yml file               |                           | citation_keywords                        |
+------------------+------------------+------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------+------------+------------+-----------+---------------+------------------------------+---------------------------+------------------------------------------+
| doi              | DOI              | http://purl.org/ontology/bibo/doi              | A DOI (Digital Object Identifier), a unique identifier for this resource.                                                                                                                                                                                                        | Optional | 0-1        | no         | no        | no            | none                         | DOI syntax                | citation_doi                             |
+------------------+------------------+------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------+------------+------------+-----------+---------------+------------------------------+---------------------------+------------------------------------------+
| keywords         | Keyword          | https://w3id.org/idsa/core/keyword             | Keywords that describe the nature, purpose, or use of the content.                                                                                                                                                                                                               | Optional | 0-n        | no         | no        | no            | none                         |                           | citation_keywords                        |
+------------------+------------------+------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------+------------+------------+-----------+---------------+------------------------------+---------------------------+------------------------------------------+
| notes            | Note             | http://www.w3.org/2004/02/skos/core#note       | A general note, for any purpose.                                                                                                                                                                                                                                                 | Optional | 0-n        | no         | no        | no            | none                         |                           |                                          |
+------------------+------------------+------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------+------------+------------+-----------+---------------+------------------------------+---------------------------+------------------------------------------+
| orcidID          | Orcid ID         | http://purl.org/cerif/frapo/hasORCID           | An ORCID identifier (not the URL) of a researcher                                                                                                                                                                                                                                | Optional | 0-n        | no         | no        | no            | ORCID                        | ORCID URL                 | citation_author_orcid                    |
+------------------+------------------+------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------+------------+------------+-----------+---------------+------------------------------+---------------------------+------------------------------------------+
| date_publication | Publication Date | http://purl.org/dc/terms/issued                | Date of formal issuance of the resource.                                                                                                                                                                                                                                         | Required | 1          | no         | yes       | no            | none                         | ISO-8601                  | citation_date, citation_publication_date |
+------------------+------------------+------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------+------------+------------+-----------+---------------+------------------------------+---------------------------+------------------------------------------+
| subject          | Subject          | http://purl.org/dc/terms/subject               | A topic of the resource.                                                                                                                                                                                                                                                         | Optional | 0-n        | no         | yes       | no            | FAST                         |                           | citation_keywords                        |
+------------------+------------------+------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------+------------+------------+-----------+---------------+------------------------------+---------------------------+------------------------------------------+
| date_submission  | Submission Date  | http://purl.org/dc/terms/dateSubmitted         | Date of submission of the resource.                                                                                                                                                                                                                                              | Required | 1          | no         | no        | no            | none                         | ISO-8601                  |                                          |
+------------------+------------------+------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------+------------+------------+-----------+---------------+------------------------------+---------------------------+------------------------------------------+
| title            | Title            | http://purl.org/dc/terms/title                 | A name given to the resource.                                                                                                                                                                                                                                                    | Required | 1          | no         | no        | yes           | none                         |                           | citation_title                           |
+------------------+------------------+------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------+------------+------------+-----------+---------------+------------------------------+---------------------------+------------------------------------------+
| type             | Type             | http://www.europeana.eu/schemas/edm/hasType    | This property relates a resource with the concepts it belongs to in a suitabletype system such as MIME or any thesaurus that captures categories ofobjects in a given field (e.g., the “Objects” facet in Getty’s Art andArchitecture Thesaurus). It does not capture aboutness. | Required | 1-n        | no         | yes       | no            | no                           |                           |                                          |
+------------------+------------------+------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------+------------+------------+-----------+---------------+------------------------------+---------------------------+------------------------------------------+
| language         | Language         | http://purl.org/dc/terms/language              | The language of the resource.                                                                                                                                                                                                                                                    | Optional | 0-n        | no         | no        | no            | local yaml or ISO 639-1 list | ISO 639-1 two-letter code | citation_language                        |
+------------------+------------------+------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------+------------+------------+-----------+---------------+------------------------------+---------------------------+------------------------------------------+

User Expectations
-----------------

The user should see the title, files, and other pertinent metadata defined in our metadata mapping. It should look similar
to an :code:`Article` or other works.

Restricted files should be appropriately restricted.

Unrestricted files should be available.

.. image:: ../images/technical_report_view.png
    :width: 600
    :Alt: Wireframe of a Sample Technical Report


For UTK Faculty and Staff Only
------------------------------

===============
Migration Scope
===============

Items migrated like this will come from select collections.

The primary file type should be a :code:`pdf`.

=================
Suggested Actions
=================

1. Only objects whose primary file type :code:`PDF` should be migrated as this work type.
2. We need to generate a cover page for these that match our descriptive metadata.
3. We will only keep supplemental files that are mentioned
