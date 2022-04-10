==============
Google Scholar
==============

-----
About
-----

This page describes things needed to ensure appropriate objects are available in Google Scholar.

----------------------
Inclusion Requirements
----------------------

In order to index objects, Google Scholar needs:

1. Access to crawl the site
2. A way to find all urls for articles: sitemap or browse by date
3. Bibliographic information in the form of machine readable metatags

The metatags include bibliographic information and tell Google Scholar which file to associate with the metatag data.

For articles, theses, and dissertations, the file should end in PDF and inside the PDF should be:

* the title of the paper in a large font on top of the first page
* the authors of the paper are listed right below the title on a separate line
* there's a bibliography section titled, e.g., "References" or "Bibliography" at the end


--------
Metatags
--------

Google Scholar's inclusion guidelines state that

.. epigraph::

    Google Scholar supports Highwire Press tags (e.g., citation_title), Eprints tags (e.g., eprints.title), BE Press
    tags (e.g., bepress_citation_title), and PRISM tags (e.g., prism.title). Use Dublin Core tags (e.g., DC.title) as a
    last resort - they work poorly for journal papers because Dublin Core doesn't have unambiguous fields for journal
    title, volume, issue, and page numbers.

    -- Google Scholar Inclusion Guidelines

According to `DSPACE documentation <https://wiki.lyrasis.org/display/DSDOC7x/Google+Scholar+Metadata+Mappings>`_, Google
Scholar prefers Highwire Press metatags.

Until DSPACE 7.x, metatags were configurable using files like `this <https://github.com/DSpace/DSpace/blob/dspace-6_x/dspace/config/crosswalks/google-metadata.properties>`_.
This may be a good place to start to define our own.

Other resources worth reviewing:

* `Invisible institutional repositories: addressing the low indexing ratios of IRs in Google Scholar <https://scholarworks.montana.edu/xmlui/handle/1/3193>`_
* `Mendeley's Information for Publishers <https://www.mendeley.com/guides/information-for-publishers>`_
* `Google Scholar Indexing for Institutional Repositories <https://www.carl-abrc.ca/wp-content/uploads/2021/01/Google_Scholar_webinar_Jan2021.pdf>`_

+-----------------------------------+------------------------------------------------------------------------------------------------------------------------------------------+----------+-----------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------+------------------------------------------------+
| Metatag                           | Definition                                                                                                                               | Status   | Expectation                                                                                               | Example                                                                                             | Notes                                                                                                                                                                                                                                                  | Worktype                                                                 | Property                                       |
+===================================+==========================================================================================================================================+==========+===========================================================================================================+=====================================================================================================+========================================================================================================================================================================================================================================================+==========================================================================+================================================+
| citation_pdf_url                  | The URL of the PDF version of an academic paper.  Should not point at supplemental files.                                                | Proposal | This metatag should map to the file that is the primary PDF of the work.                                  | <meta name="citation_pdf_url" content="https://trace.tennessee.edu/path/to/the/primary/pdf/file" /> |                                                                                                                                                                                                                                                        | Article, Book, Citation, Conference Proceeding, Thesis, Technical Report | N/A                                            |
+-----------------------------------+------------------------------------------------------------------------------------------------------------------------------------------+----------+-----------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------+------------------------------------------------+
| citation_abstract_html_url        | The URL that contains the metadata that describes the file. Should be the full results page that a user navigates to from search results | N/A      | This metatag should map to the work page with metadata that describes the attached PDF.                   | <meta name="citation_abstract_html_url" content="https://trace.tennessee.edu/path/to/the/work" />   | This isn't registered, but it's the tag that DSPACE uses out of the box.                                                                                                                                                                               | Article, Book, Citation, Conference Proceeding, Thesis, Technical Report | N/A                                            |
+-----------------------------------+------------------------------------------------------------------------------------------------------------------------------------------+----------+-----------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------+------------------------------------------------+
| citation_abstract                 | A summary of the resource.                                                                                                               | N/A      | The metatag should be populated by the value of the matching RDF property if it exists.                   | <meta name="citation_abstract" content="The value of the associated property." />                   | This isn't a registered metatag but is used by some repositories including CDL.  For that reason, also map this information to the registered dcterms.abstract field.                                                                                  | Article, Book, Citation, Conference Proceeding, Thesis, Technical Report | http://purl.org/dc/terms/abstract              |
+-----------------------------------+------------------------------------------------------------------------------------------------------------------------------------------+----------+-----------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------+------------------------------------------------+
| dcterms.abstract                  | A summary of the resource.                                                                                                               | Proposal | The metatag should be populated by the value of the matching RDF property if it exists.                   | <meta name="dcterms.abstract" content="The value of the associated property." />                    | This is duplicated from citation_abstract.                                                                                                                                                                                                             | Article, Book, Citation, Conference Proceeding, Thesis, Technical Report | http://purl.org/dc/terms/abstract              |
+-----------------------------------+------------------------------------------------------------------------------------------------------------------------------------------+----------+-----------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------+------------------------------------------------+
| citation_author                   | The name of an author of an academic paper.  We use this for related objects like books and theses as well.                              | Proposal | The metatag should be populated by the value of the matching RDF property if it exists.                   | <meta name="citation_author" content="The value of the associated property." />                     | The format should match the order of the authors on the first page of the attached PDF according to Michelle Westin at Google Scholar. See more information at: https://www.carl-abrc.ca/wp-content/uploads/2021/01/Google_Scholar_webinar_Jan2021.pdf | Thesis, Article, Book, Citation, Technical Report, Conference Proceeding | http://id.loc.gov/vocabulary/relators/aut      |
+-----------------------------------+------------------------------------------------------------------------------------------------------------------------------------------+----------+-----------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------+------------------------------------------------+
| citation_date                     | The publication date of an academic paper                                                                                                | Proposal | The metatag should be populated by the value of the matching RDF property if it exists.                   | <meta name="citation_date" content="The value of the associated property." />                       | The date should correspond to the value on the first page of the PDF according to Monica Westin.  See more at: https://www.carl-abrc.ca/wp-content/uploads/2021/01/Google_Scholar_webinar_Jan2021.pdf                                                  | Thesis                                                                   | http://purl.org/cerif/frapo/hasMilestone       |
+-----------------------------------+------------------------------------------------------------------------------------------------------------------------------------------+----------+-----------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------+------------------------------------------------+
| citation_keywords                 | A semicolon-separated list of keywords associated with an academic paper                                                                 | Proposal | The metatag should be populated as semicolon separated values of all PDF properties that map to this tag. | <meta name="citation_keywords" content="value; value; value; value" />                              |                                                                                                                                                                                                                                                        | Article, Book, Citation, Conference Proceeding, Thesis, Technical Report | http://dbpedia.org/ontology/academicDiscipline |
+-----------------------------------+------------------------------------------------------------------------------------------------------------------------------------------+----------+-----------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------+------------------------------------------------+
| citation_doi                      | The Digital Object Identifier of an academic paper                                                                                       | Proposal | The metatag should be populated by the value of the matching RDF property if it exists.                   | <meta name="citation_doi" content="The value of the associated property." />                        |                                                                                                                                                                                                                                                        | Article, Book, Citation, Conference Proceeding, Thesis, Technical Report | http://purl.org/ontology/bibo/doi              |
+-----------------------------------+------------------------------------------------------------------------------------------------------------------------------------------+----------+-----------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------+------------------------------------------------+
| citation_dissertation_institution | The name of the institution which published an academic dissertation                                                                     | Proposal | The metatag should be populated by the value of the matching RDF property if it exists.                   | <meta name="citation_dissertation_institution" content="The value of the associated property." />   |                                                                                                                                                                                                                                                        | Thesis                                                                   | http://id.loc.gov/vocabulary/relators/dgg      |
+-----------------------------------+------------------------------------------------------------------------------------------------------------------------------------------+----------+-----------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------+------------------------------------------------+
| citation_author_institution       | The name of an institution to which the preceding author (identified using citation_author) of an academic paper is affiliated           | Proposal | The metatag should be populated by the value of the matching RDF property if it exists.                   | <meta name="citation_author_institution" content="The value of the associated property." />         |                                                                                                                                                                                                                                                        | Thesis                                                                   | http://id.loc.gov/vocabulary/relators/dgg      |
+-----------------------------------+------------------------------------------------------------------------------------------------------------------------------------------+----------+-----------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------+------------------------------------------------+
| citation_issue                    | The issue of the journal in which an academic paper is published                                                                         | Proposal | The metatag should be populated by the value of the matching RDF property if it exists.                   | <meta name="citation_issue" content="The value of the associated property." />                      |                                                                                                                                                                                                                                                        | Article, Citation                                                        | http://purl.org/ontology/bibo/issue            |
+-----------------------------------+------------------------------------------------------------------------------------------------------------------------------------------+----------+-----------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------+------------------------------------------------+
| citation_lastpage                 | The last page of the journal in which an academic paper is published                                                                     | Proposal | The metatag should be populated by the value of the matching RDF property if it exists.                   | <meta name="citation_lastpage" content="1009" />                                                    |                                                                                                                                                                                                                                                        | Article, Citation                                                        | http://purl.org/ontology/bibo/pageEnd          |
+-----------------------------------+------------------------------------------------------------------------------------------------------------------------------------------+----------+-----------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------+------------------------------------------------+
| citation_firstpage                | The first page of the journal in which an academic paper is published                                                                    | Proposal | The metatag should be populated by the value of the matching RDF property if it exists.                   | <meta name="citation_firstpage" content="1001" />                                                   |                                                                                                                                                                                                                                                        | Article, Citation                                                        | http://purl.org/ontology/bibo/pageStart        |
+-----------------------------------+------------------------------------------------------------------------------------------------------------------------------------------+----------+-----------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------+------------------------------------------------+
| citation_journal_title            | The title of the journal in which an academic paper is published                                                                         | Proposal | The metatag should be populated by the value of the matching RDF property if it exists.                   | <meta name="citation_journal_title" content="Property value" />                                     |                                                                                                                                                                                                                                                        | Article, Citation                                                        | http://purl.org/dc/terms/isPartOf              |
+-----------------------------------+------------------------------------------------------------------------------------------------------------------------------------------+----------+-----------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------+------------------------------------------------+
| citation_volume                   | The volume of the journal in which an academic paper is published                                                                        | Proposal | The metatag should be populated by the value of the matching RDF property if it exists.                   | <meta name="citation_volume" content="Property value" />                                            |                                                                                                                                                                                                                                                        | Article, Citation                                                        | http://purl.org/ontology/bibo/volume           |
+-----------------------------------+------------------------------------------------------------------------------------------------------------------------------------------+----------+-----------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------+------------------------------------------------+
| citation_keywords                 | A semicolon-separated list of keywords associated with an academic paper                                                                 | Proposal | The metatag should be populated as semicolon separated values of all PDF properties that map to this tag. | <meta name="citation_keywords" content="value; value; value; value" />                              |                                                                                                                                                                                                                                                        | Article, Book, Citation, Conference Proceeding, Thesis, Technical Report | https://w3id.org/idsa/core/keyword             |
+-----------------------------------+------------------------------------------------------------------------------------------------------------------------------------------+----------+-----------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------+------------------------------------------------+
| citation_author_orcid             | An ORCID identifier (not the URL) of a researcher                                                                                        | N/A      | The metatag should be populated by the value of the matching RDF property if it exists.                   | <meta name="citation_author_orcid" content="Property value" />                                      | Mark questions whether we should even use this.  It's used by Zotero, but not popular in practice by publishers.                                                                                                                                       | Article, Book, Citation, Conference Proceeding, Thesis, Technical Report | http://purl.org/cerif/frapo/hasORCID           |
+-----------------------------------+------------------------------------------------------------------------------------------------------------------------------------------+----------+-----------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------+------------------------------------------------+
| citation_date                     | The publication date of an academic paper                                                                                                | Proposal | The metatag should be populated by the value of the matching RDF property if it exists.                   | <meta name="citation_date" content="The value of the associated property." />                       | The date should correspond to the value on the first page of the PDF according to Monica Westin.  See more at: https://www.carl-abrc.ca/wp-content/uploads/2021/01/Google_Scholar_webinar_Jan2021.pdf                                                  | Thesis, Article, Book, Citation, Technical Report, Conference Proceeding | http://purl.org/dc/terms/issued                |
+-----------------------------------+------------------------------------------------------------------------------------------------------------------------------------------+----------+-----------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------+------------------------------------------------+
| citation_publication_date         | The publication date of an academic paper                                                                                                | Proposal | The metatag should be populated by the value of the matching RDF property if it exists.                   | <meta name="citation_publication_date" content="The value of the associated property." />           | The date should correspond to the value on the first page of the PDF according to Monica Westin.  See more at: https://www.carl-abrc.ca/wp-content/uploads/2021/01/Google_Scholar_webinar_Jan2021.pdf                                                  | Thesis, Article, Book, Citation, Technical Report, Conference Proceeding | http://purl.org/dc/terms/issued                |
+-----------------------------------+------------------------------------------------------------------------------------------------------------------------------------------+----------+-----------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------+------------------------------------------------+
| citation_publisher                | The name of the publisher of an academic paper                                                                                           | Proposal | The metatag should be populated by the value of the matching RDF property if it exists.                   | <meta name="citation_publisher" content="The value of the associated property." />                  |                                                                                                                                                                                                                                                        | Book, Conference Proceeding, Citation                                    | http://id.loc.gov/vocabulary/relators/pbl      |
+-----------------------------------+------------------------------------------------------------------------------------------------------------------------------------------+----------+-----------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------+------------------------------------------------+
| dcterms.type                      | The nature or genre of the resource.                                                                                                     | Proposal | The metatag should be populated by the value of the matching RDF property if it exists.                   | <meta name="dcterms.type" content="The value of the associated property." />                        |                                                                                                                                                                                                                                                        | Article, Book, Citation, Conference Proceeding, Thesis, Technical Report | http://purl.org/dc/terms/type                  |
+-----------------------------------+------------------------------------------------------------------------------------------------------------------------------------------+----------+-----------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------+------------------------------------------------+
| citation_keywords                 | A semicolon-separated list of keywords associated with an academic paper                                                                 | Proposal | The metatag should be populated as semicolon separated values of all PDF properties that map to this tag. | <meta name="citation_keywords" content="value; value; value; value" />                              |                                                                                                                                                                                                                                                        | Article, Book, Citation, Conference Proceeding, Thesis, Technical Report | http://purl.org/dc/terms/subject               |
+-----------------------------------+------------------------------------------------------------------------------------------------------------------------------------------+----------+-----------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------+------------------------------------------------+
| citation_title                    | The title of an academic paper                                                                                                           | Proposal | The title of the object as it appears in the PDF.                                                         | <meta name="citation_title" content="The value of the associated property." />                      | Accordining to Monica Westin, this value needs to match the title exactly to avoid inclusion issues.                                                                                                                                                   | Article, Book, Citation, Conference Proceeding, Thesis, Technical Report | http://purl.org/dc/terms/title                 |
+-----------------------------------+------------------------------------------------------------------------------------------------------------------------------------------+----------+-----------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------+------------------------------------------------+
| citation_editor                   | The editor of a book.                                                                                                                    | N/A      | The metatag should be populated by the value of the matching RDF property if it exists.                   | <meta name="citation_editor" content="The value of the associated property." />                     | This is a Zotero translator but is questionably used if at all by Google Scholar.                                                                                                                                                                      | Conference Proceeding, Book                                              | http://id.loc.gov/vocabulary/relators/edt      |
+-----------------------------------+------------------------------------------------------------------------------------------------------------------------------------------+----------+-----------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------+------------------------------------------------+
| citation_language                 | The language in which an academic paper is written, as an ISO 639-1 two-letter code                                                      | Proposal | The metadata should be a ISO 639-1 code.  We should use a vocab to ensure this.                           | <meta name="citation_language" content="en" />                                                      | Monica Westin's presentation actually shows an example of a three letter language code being used: https://www.carl-abrc.ca/wp-content/uploads/2021/01/Google_Scholar_webinar_Jan2021.pdf                                                              | Article, Book, Citation, Conference Proceeding, Thesis, Technical Report | http://purl.org/dc/terms/language              |
+-----------------------------------+------------------------------------------------------------------------------------------------------------------------------------------+----------+-----------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------+------------------------------------------------+
| citation_fulltext_html_url        | The URL of the full text HTML version of an academic paper                                                                               | Proposal | For citations, use this to point at the document since we don't control the PDFs.                         | <meta name="citation_fulltext_html_url" content="http://somevalue" />                               |                                                                                                                                                                                                                                                        | Citation                                                                 | https://schema.org/url                         |
+-----------------------------------+------------------------------------------------------------------------------------------------------------------------------------------+----------+-----------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------+------------------------------------------------+
| citation_isbn                     | The ISBN of the book in which an academic paper is published                                                                             | Proposal | The metatag should be populated by the value of the matching RDF property if it exists.                   | <meta name="citation_isbn" content="The value of the associated property." />                       |                                                                                                                                                                                                                                                        | Book, Conference Proceeding                                              | http://purl.org/ontology/bibo/isbn             |
+-----------------------------------+------------------------------------------------------------------------------------------------------------------------------------------+----------+-----------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------+------------------------------------------------+
| citation_conference_title         | The title of the conference where the resource was presented.                                                                            | Proposal | The metatag should be populated by the value of the matching RDF property if it exists.                   | <meta name="citation_conference_title" content="The value of the associated property." />           |                                                                                                                                                                                                                                                        | Conference Proceeding                                                    | http://purl.org/ontology/bibo/presentedAt      |
+-----------------------------------+------------------------------------------------------------------------------------------------------------------------------------------+----------+-----------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------+------------------------------------------------+

----------------------------------
Notes from Highwire Press Homework
----------------------------------

Investigating ETDs
==================

`This ETD <https://escholarship.org/uc/item/1zz6h16w>`_ from UCLA is indexed.

It has these highwire press metatags:

.. code-block:: python

    {
     'citation_title': 'Production of positron emission tomography (PET) radiotracers with electrowetting-on-dielectric (EWOD) digital microfluidics',
     'citation_abstract': 'There is currently a need to improve production of radiotracers for positron emission tomography (PET) imaging because although thousands of radiotracers have been developed in research settings, only a few are readily available, severely limiting the biological problems that can be studied in vivo via PET. An electrowetting-on-dielectric (EWOD) digital microfluidic chip was designed with multifunctional electrodes (for heating, temperature sensing, and EWOD driving) to synthesize a variety of 18F-labeled tracers targeting a range of biological processes. A single EWOD radiosynthesizer device design was used for complete synthesis of four radiotracers (a sugar, a DNA nucleoside, a protein-labelling compound, and a neurotransmitter). All of the key synthesis steps for radiochemistry have been demonstrated on chip: concentration of fluoride ion, solvent exchange, chemical reaction, and purification. A mirrored configuration of valve metal oxide was also investigated for use as a cost effective and high electrical performance dielectric in EWOD.',
     'citation_author': 'Chen, Supin',
     'citation_publication_date': '2014',
     'citation_dissertation_institution': 'UCLA',
     'citation_online_date': '2015-07-21',
     'citation_pdf_url': 'https://escholarship.org/content/qt1zz6h16w/qt1zz6h16w.pdf?t=nru1ii'
    }

The PDF in `the viewer <https://escholarship.org/uc/item/1zz6h16w>`_ is different from :download:`the PDF in the metatag <https://escholarship.org/content/qt1zz6h16w/qt1zz6h16w.pdf?t=nru1ii>`.

Here is an ETD from Cornell:

.. code-block:: python
    :emphasize-lines: 5-7

    {'citation_keywords': 'transistor; poly(3-hexylthiophene) P3HT; poly(3-hexylthiophene) (P3HT); TPD; dissertation or thesis',
     'citation_title': 'Fluctuations Near Thin Films Of Polymers, Organic Photovoltaics, And Organic Semiconductors Probed By Electric Force Microscopy',
     'citation_language': 'en_US',
     'citation_author': 'Hoepker, Nikolas',
     'citation_pdf_url': 'https://ecommons.cornell.edu/bitstream/1813/33910/1/nch28.pdf',
     'citation_date': '2013-01-28',
     'citation_abstract_html_url': 'https://ecommons.cornell.edu/handle/1813/33910'}

This is a modern DSPACE site.  The ETD does not have a cover page.  It's :code:`citation_date` is not four digit.  They
share abstract via :code:`citation_abstract_html_url` which is a link to the view with a clearly displayed abstract.

Another example from the University of Minnesota is `this <https://conservancy.umn.edu/handle/11299/53398>`_.  It appears in Google Scholar with these tags:

.. code-block:: python

    {'citation_keywords': 'Affinity Tensor; Iterative Sampling; Motion Segmentation; Multiway Spectral Clustering; Perturbation Analysis; Polar Curvature; Mathematics; Thesis or Dissertation',
     'citation_title': 'Spectral curvature clustering for hybrid linear modeling.',
     'citation_language': 'en_US',
     'citation_author': 'Chen, Guangliang',
     'citation_pdf_url': 'http://conservancy.umn.edu/bitstream/11299/53398/1/Chen_umn_0130E_10496.pdf',
     'citation_date': '2009-07',
     'citation_abstract_html_url': 'http://conservancy.umn.edu/handle/11299/53398'}

It is nearly identical to Cornell (they both use modern DSPACE). Also, they do not use cover pages.

Based on these examples, I think we should have:

* :code:`citation_title`
* :code:`citation_abstract`
* :code:`citation_author`
* :code:`citation_date` and :code:`citation_publication_date` (why not both?)
* :code:`citation_online_date`
* :code:`citation_dissertation_institution`
* :code:`citation_pdf_url`

Investigating Books
===================

Google Scholar lists this object as `a book <https://ui.adsabs.harvard.edu/abs/1994emta.book.....F/abstract>`_

I'm not sure it is. I think it should be a citation.

Here are its highwire press metatags:

.. code-block:: python
    :emphasize-lines: 1, 4, 6, 10

    {'citation_journal_title': 'Engineering Materials and Their Applications',
     'citation_authors': 'Flinn, Richard A.;Trojan, Paul K.',
     'citation_title': 'Engineering Materials and Their Applications, 4th Edition',
     'citation_date': '12/1994',
     'citation_firstpage': '1056',
     'citation_isbn': '0471125083',
     'citation_language': 'en',
     'citation_keywords': 'General Materials Science',
     'citation_abstract_html_url': 'https://ui.adsabs.harvard.edu/abs/1994emta.book.....F/abstract',
     'citation_publication_date': '12/1994'}

Some things to note:

* It has a :code:`citation_journal_title`
* It has a :code:`citation_date`
* It has a :code:`citation_publication_date`
* It has a :code:`citation_isbn`
* Its authors are in a field called :code:`citation_authors`

This is `another book <https://entrospace.nilebasin.org/handle/20.500.12351/421>`_ available in Google Scholar.

.. code-block:: python
    :emphasize-lines: 2, 4

    {'citation_keywords': 'Book',
     'citation_isbn': '0072424117, 9780072424119',
     'citation_title': 'Introduction to environmental engineering',
     'citation_publisher': 'McGraw-Hill',
     'citation_language': 'en',
     'citation_author': 'Mackenzie L. Davis; David A Cornwell',
     'citation_date': '2008',
     'citation_abstract_html_url': 'https://entrospace.nilebasin.org/handle/20.500.12351/421'}

Based on these examples, I feel that a book should have these tags:

* :code:`citation_title`
* :code:`citation_isbn`
* :code:`citation_publisher`
* :code:`citation_language`
* :code:`citation_author`
* :code:`citation_date` and * :code:`citation_publication_date` -- why not both?  Also, format doesn't seem to matter.
* A link to the abstract somehow.  Both of these link to an HTML page with the abstract on it, but I think we could do this in a different way like :code:`citation_abstract`.
* A link to the book like :code:`citation_pdf_url`

Investigating Articles
======================

One of our questions was how modern DSPACE may use :code:`citation_publisher` and :code:`citation_journal_title`.

Here are some examples.

This is an `article for Cornell Hospitality Quarterly <>`_ that is in Google Scholar.  It has these tags:

.. code-block:: python

    {'citation_keywords': 'gambling; childhood memory elicitation; cross-cultural studies; Las Vegas; Macao; article',
     'citation_title': 'Cracking the Cultural Code of Gambling',
     'citation_language': 'en_US',
     'citation_author': ['LaTour, Kathryn A.',
      'Sarrazit, Franck',
      'Hendler, Rom',
      'LaTour, Michael S.'],
     'citation_pdf_url': 'https://ecommons.cornell.edu/bitstream/1813/71767/1/LaTour9_Cracking_the_Cultural_Code_of_Gambling.pdf',
     'citation_date': '2009-09-01',
     'citation_abstract_html_url': 'https://ecommons.cornell.edu/handle/1813/71767'}

Notice, there is no :code:`citation_publisher` or :code:`citation_journal_title`.

Investigating Technical Reports
===============================

I did a little work here.

First, I went to some sites and looked for places that specify technical reports to see if they use specific metatags.

An example from Cornell is `this <https://ecommons.cornell.edu/handle/1813/7060>`_. Cornell lists it as a technical report, but
it has no special tags:

.. code-block:: python

    {'citation_keywords': 'computer science; technical report; technical report',
     'citation_title': 'Abstract Semantics for a Higher order Functional Language with Logic Variables',
     'citation_publisher': 'Cornell University',
     'citation_language': 'en_US',
     'citation_author': ['Jagadeesan, Radhakrishnan', 'Pingali, Keshav'],
     'citation_pdf_url': 'https://ecommons.cornell.edu/bitstream/1813/7060/1/91-1220.pdf',
     'citation_date': '1991-07',
     'citation_abstract_html_url': 'https://ecommons.cornell.edu/handle/1813/7060'}

Oddly, this work type populates :code:`citation_publisher` but others do not.  This appears in Google Scholar but generically.

Here is `another example from Minnesota <https://conservancy.umn.edu/handle/11299/199664>`_. It's in Google Scholar (but
notably as PDF). Its tags are:

.. code-block:: python
    :emphasize-lines:

    {'citation_keywords': 'Technical Report',
     'citation_title': 'A Bayesian Scheme to Detect Changes in the Mean of a Short Run Process',
     'citation_language': 'en_US',
     'citation_author': ['Tsiamyrtzis, Pangiotis', 'Hawkins, Douglas M.'],
     'citation_pdf_url': 'http://conservancy.umn.edu/bitstream/11299/199664/1/Technical%20Report%20642%20A%20Bayesian%20Scheme%20to%20Detect%20Changes%20in%20the%20Mean%20of%20a%20Short%20Run%20Process.pdf',
     'citation_date': '2002-09',
     'citation_abstract_html_url': 'http://conservancy.umn.edu/handle/11299/199664',
     'citation_technical_report_institution': 'University of Minnesota'}

Notice that it does use :code:`citation_technical_report_institution` and is modern DSPACE.

I would say we should use this field if we plan to have these as a separate work type.

A Note About Posters
====================

It looks like some people have faked a content model for posters into Google Scholar. Don't think we should do it, but
wanted to share how they did it.  Here is `the item <https://ajs.hcommons.org/deposits/item/hc:31827/>`_. Here are the
tags:

.. code-block:: python
    :emphasize-lines: 1, 11

    {'citation_title': '[POSTER] The Digital Analysis of Syriac Handwriting (DASH) Project: Augmenting Manuscript Studies via Interactive Scriptcharts and IIIF',
     'citation_publication_date': '20 July 2020',
     'citation_author': ['Vijoy Abraham',
      'Scott Bailey',
      'Peter Broadwell',
      'Michael Penn',
      'Simon Wiles'],
     'citation_handle_id': 'https://doi.org/10.17613/qvbz-5t02',
     'citation_keyword': ['History', 'Paleography', 'Religious studies'],
     'citation_abstract_html_url': 'https://hcommons.org/deposits/item/hc:31827/',
     'citation_pdf_url': 'https://hcommons.org/deposits/download/hc:31828/CONTENT/penn_442_poster.pdf/'}

As you can see, the datatype is actually embedded in the title (isn't this a no-no for indexing) but isn't in the corresponding
pdf url.

Again, don't think we should go here, but wanted to share.

Some bad things discovered along the way
========================================

In my investigation of DSPACE sites, I got curious about work types for things that "don't fit" in Google Scholar according
to Google Scholar's Inclusion Guidelines.

Here is an example: `Roger Spanswick – Meet the Presenters <https://ecommons.cornell.edu/handle/1813/37296>`_. It is a
video. Let's look at the tags.

.. code-block:: python
    :emphasize-lines: 5

    {'citation_keywords': 'video/moving image',
     'citation_title': '0 Roger Spanswick – Meet the Presenters',
     'citation_language': 'en_US',
     'citation_author': 'Davies, Peter',
     'citation_pdf_url': 'https://ecommons.cornell.edu/bitstream/1813/37296/2/HD.mp4',
     'citation_date': '2014-06-02',
     'citation_abstract_html_url': 'https://ecommons.cornell.edu/handle/1813/37296'}

This object is in Google Scholar but appears as a Citation.  I wonder if your site is reputable and you violate the inclusion
guidelines, Google responds by marking the object as a :code:`citation`.



Getting Highwire Press Tags Quickly
===================================

In case it's useful, I wrote a simple class to get highwire press tags from a url as a dictionary quickly as a Python
dictionary. You'll need to install metadata_parser from pypi since it's not a part of the standard library.

.. code:: python

    from metadata_parser import MetadataParser

    class Page:
        def __init__(self, url):
            self.all = MetadataParser(url, search_head_only=True).metadata
            self.og = self.all['og']
            self.meta = self.all['meta']
            self.highwire_press = self.__get_highwire_press_tags()

        def __get_highwire_press_tags(self):
            highwire_press = {}
            for k, v in self.meta.items():
                if 'citation_' in k:
                    highwire_press[k] = v
            return highwire_press

    x = Page('https://ui.adsabs.harvard.edu/abs/1994emta.book.....F/abstract')
    x.highwire_press

