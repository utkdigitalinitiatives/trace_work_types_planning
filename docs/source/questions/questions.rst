Questions about Work Types
--------------------------

1. Work Types We've Defined
===========================

We have defined 8 work types for the IR.  2 of them are exactly the same, but we created them separately to avoid confusion.
Each are described by a document here, but this is the TLDR:

1. Article: a PDF object that may have supplemental files and may be embargoed that should appear in Google Scholar. Has own set of metatags.
2. Book: a PDF object that may have supplemental files and should appear as a book in Google Scholar. It has its own set of metatags to aid this.
3. Citation: A metadata only object (does not have supplemental files or a PDF) that should appear in Google Scholar as a citation. Has own metatags to aid this.
4. Conference Proceeding: Exactly the same as book.
5. Dataset: A dataset that relates to research.  May be embargoed. Some files may be restricted from view unless they are an admin or depositor. Should appear in Google Datasets search but not in Google Scholar. Does not have metatags for Google Scholar but has a JSON-LD body for Google Datasets Search.
6. Thesis: Our most complex type. This is a work uploaded by the user for degree completion. There is a complex workflow that includes generating a cover page and some preformatted material from the gradschool.  Has its own metatags because of need for Google Scholar inclusion. Can be embargoed by the grad school for a set period of time. Would love to be able to have metadata on the fileset to aid in the differences between files.
7. Other: A work with files of any mimetype that should not be in Google Scholar.  Thus, has no metatag mapping.
8. Technical report: A work that is a PDF that should appear in Google Scholar as a technical report.  To aid in this, has its own Google Scholar mapping.

The question:  do the expectations for metatags / JSON-LD bodies, fileset metadata, and separately labeled works make
sense for unique worktypes.  Is there anything you see here that is problematic?

2. Structural Metadata
======================

All work type definitions have a section about structural metadata.  After our talk last week, I think it makes sense
to just handle this all with fileset metadata.  For instance, we'd like certain files to have specific :code:`pcdmuse`
types.

For instance, the primary file of an ETD that was uploaded by a student would be a :code:`pcdmuse:OriginalFile` and a
file that included frontmatter from the graduat school would be a :code:`pcdmuse:IntermediateFile`.  Other files uploaded
by the student would be :code:`fabio:SupplementaryInformation`.

I think we just handle all this with metadata on the fileset.  Do you disagree?

Also, if we did this, how can we state this for the work so that theses that are uploaded get the same data?

To help think about this, here is an example thesis.  We want to keep the original PDF, but we want to point at the one
with cover materials in Google Scholar.  Also, we want to know that the supplemental files are just that.

-------------
Original File
-------------

The original file may have some metadata like this.

.. code-block:: turtle

    @prefix : <https://utk-future-repo/some/path/>
    @prefix pcdm: <http://pcdm.org/models#> .
    @prefix pcdmuse: <http://pcdm.org/2015/05/12/use> .
    @prefix pcdmworks: <http://pcdm.org/2016/02/16/works> .

    :etd_file_1 a pcdmuse:OriginalFile ;
        rdfs:label "MorrisJames_May2011_dissertation.pdf" ;
        pcdm:fileOf :sample-etd .

-----------------------------------------
Final File with Generated Cover Materials
-----------------------------------------

.. code-block:: turtle

    @prefix : <https://utk-future-repo/some/path/>
    @prefix pcdm: <http://pcdm.org/models#> .
    @prefix pcdmuse: <http://pcdm.org/2015/05/12/use> .
    @prefix pcdmworks: <http://pcdm.org/2016/02/16/works> .

    :etd_file_2 a pcdmuse:PreservationFile, pcdmuse:IntermediateFile ;
        rdfs:label "final_etd.pdf" ;
        pcdm:fileOf :sample-etd .

--------------------
Supplemental File(s)
--------------------

.. code-block:: turtle

    @prefix : <https://utk-future-repo/some/path/>
    @prefix pcdm: <http://pcdm.org/models#> .
    @prefix pcdmuse: <http://pcdm.org/2015/05/12/use> .
    @prefix pcdmworks: <http://pcdm.org/2016/02/16/works> .
    @prefix dcterms: <http://purl.org/dc/terms/> .
    @prefix fabio: <http://purl.org/spar/fabio/> .

    :etd_file_suppl_1 a fabio:SupplementaryInformation  ;
        rdfs:label "Supplemental_File_1.fasta" ;
        dcterms:description "JCVI-CMR Catalase Database (FASTA format)" ;
        dcterms:format "text/plain" ;
        pcdm:fileOf :sample-etd .

    :etd_file_suppl_2 fabio:SupplementaryInformation ;
        rdfs:label "Supplemental_File_2.fasta" ;
        dcterms:description "JCVI-CMR rpsL Database (FASTA format)" ;
        dcterms:format "text/plain" ;
        pcdm:fileOf :sample-etd .

    :etd_file_suppl_3 a fabio:SupplementaryInformation ;
        rdfs:label "Supplemental_File_3.csv" ;
        dcterms:description "Taxonomy of GOS catalase/rpsL hits" ;
        dcterms:format "application/vnd.ms-excel" ;
        pcdm:fileOf :sample-etd .

    :etd_file_suppl_4 a fabio:SupplementaryInformation ;
        rdfs:label "Supplemental_File_4.csv" ;
        dcterms:description "GOS catalase hits with metadata (CSV format)" ;
        dcterms:format "text/plain" ;
        pcdm:fileOf :sample-etd .

    :etd_file_suppl_5 a fabio:SupplementaryInformation ;
        rdfs:label "Supplemental_File_5.csv" ;
        dcterms:description "GOS rpsL hits with metadata (CSV format)" ;
        dcterms:format "text/plain" ;
        pcdm:fileOf :sample-etd .

-----------------
Original Metadata
-----------------

We want to keep the original metadata, but restrict it. How do we apply WEBAC or describe that?

.. code-block:: turtle

    @prefix : <https://utk-future-repo/some/path/>
    @prefix pcdm: <http://pcdm.org/models#> .
    @prefix pcdmuse: <http://pcdm.org/2015/05/12/use> .
    @prefix pcdmworks: <http://pcdm.org/2016/02/16/works> .

    :etd_file_3 a pcdm:File ;
        rdfs:label "metadata.xml" ;
        pcdm:fileOf :sample-etd .

3. Specifying Restriction on Access Embargoing for Batch Upload
===============================================================

All work types have a need for restriction on access.  Restriction of files will be simple:  admin of the repostiory.
How can we specify this?  Is this needed for worktype?

Similarly, how do we do embargo migration?

4. Worktypes and Admin Sets
===========================

How do work types and administrative sets (I think this is what they are called work together?
