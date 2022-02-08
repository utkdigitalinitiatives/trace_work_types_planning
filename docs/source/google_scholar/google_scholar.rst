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

