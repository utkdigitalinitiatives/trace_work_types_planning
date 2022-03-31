Dataset Work Type
=================

About
-----

This work type represents datasets from our institutional repository.  Datasets have :code:`1-n` files and each may
be open or restricted from public access.

Datasets are different from other works and deserve there own worktype in order to be included in
`Google's Dataset Search <https://datasetsearch.research.google.com/>`_.

Should datasets be in there own tenant?
---------------------------------------

Arguably, yes.  The primary purpose of treating datasets as its own worktype is to enable dataset sharing in Google
Dataset Search.  Google Dataset Search has a different inclusion methodolgy than Google Scholar that more resembles standard
indexing practices. In addition to requirements for :code:`JSON-LD` or :code:`rdfa`, this requires a sitemap with proper
canonical tagging, and the sitemap should describe only the datasets. Therefore, having a separate tenant makes things easier.

That being said, it is important to remember that we have very few datasets, and we don't have clear direction or policies
for our approach to taking datasets in the future.

A potential workaround for including datasets in our planned tenant then is to simply create a small feature that queries
our instance for dataset works and generate a separate sitemap around those. The works described in the sitemap should
all have proper :code:`JSON-LD` or :code:`rdfa`.

Migration Scope
---------------

Datasets in Digital Commons are currently metadata only objects that reference `Trace Deposit <https://trace.utk.edu>`_.

Datasets are in two series (collections):

.. code-block:: text

    utk_datasets
    utk_geogpubs

Currently, these are our list of datasets:

.. code-block:: text

    utk_datasets/14/metadata.xml
    utk_datasets/15/metadata.xml
    utk_datasets/16/metadata.xml
    utk_datasets/17/metadata.xml
    utk_datasets/18/metadata.xml
    utk_datasets/19/metadata.xml
    utk_datasets/20/metadata.xml
    utk_datasets/21/metadata.xml
    utk_datasets/23/metadata.xml
    utk_datasets/24/metadata.xml
    utk_datasets/25/metadata.xml
    utk_datasets/26/metadata.xml
    utk_datasets/27/metadata.xml
    utk_datasets/28/metadata.xml
    utk_datasets/29/metadata.xml
    utk_datasets/30/metadata.xml
    utk_geogpubs/30/metadata.xml

Using a bit of sparql, we can determine what our list of datasets in Digital Commons should be:

.. code-block:: sparql

    PREFIX rels-ext: <info:fedora/fedora-system:def/relations-external#>
    PREFIX model: <info:fedora/fedora-system:def/model#>
    SELECT $pid FROM <#ri> WHERE {{
    ?pid rels-ext:isMemberOfCollection <info:fedora/utk.ir:fg>;
    model:hasModel <info:fedora/islandora:compoundCModel> . }}

That returns these results:

.. code-block:: text

    info:fedora/utk.ir.fg:7
    info:fedora/utk.ir.fg:14
    info:fedora/utk.ir.fg:18
    info:fedora/utk.ir.fg:27
    info:fedora/utk.ir.fg:29
    info:fedora/utk.ir.fg:101
    info:fedora/utk.ir.fg:2090
    info:fedora/utk.ir.fg:2099
    info:fedora/utk.ir.fg:2110
    info:fedora/utk.ir.fg:2112
    info:fedora/utk.ir.fg:2129
    info:fedora/utk.ir.fg:2132
    info:fedora/utk.ir.fg:2162
    info:fedora/utk.ir.fg:2176
    info:fedora/utk.ir.fg:2179
    info:fedora/utk.ir.fg:2188
    info:fedora/utk.ir.fg:2193
    info:fedora/utk.ir.fg:2198
    info:fedora/utk.ir.fg:2215
    info:fedora/utk.ir.fg:2239
    info:fedora/utk.ir.fg:2245
    info:fedora/utk.ir.fg:2248
    info:fedora/utk.ir.fg:2263
    info:fedora/utk.ir.fg:2268
    info:fedora/utk.ir.fg:2273
    info:fedora/utk.ir.fg:2287
    info:fedora/utk.ir.fg:2290
    info:fedora/utk.ir.fg:2303
    info:fedora/utk.ir.fg:2307
    info:fedora/utk.ir.fg:2311
    info:fedora/utk.ir.fg:2341
    info:fedora/utk.ir.fg:2355
    info:fedora/utk.ir.fg:2360
    info:fedora/utk.ir.fg:2381
    info:fedora/utk.ir.fg:2384
    info:fedora/utk.ir.fg:2385

Suggested Actions
-----------------

1. If an object in Digital Commons refers to a object on trace.utk.edu that is not an ETD, we will migrate the object into the new repository as a dataset. It cannot stay at trace.utk.edu for security reasons.
2. If an object is in Trace Deposit and not an ETD, we will migrate it to the new system as a dataset.
3. We will provide the vendor for migration pages with front matter but without the coverpage.
4. The vendor will build a feature to add the appropriate cover page.
5. The vendor will build a feature for front matter going forward.

Example Dataset
---------------

For this example, let's use :code:`https://trace.tennessee.edu/utk_datasets/1`.

In Digital Commons, no files are currently managed, but in Trace Deposit there are several files and an original metadata.
Datasets in Trace Deposit are compound objects with the metadata record attached to the compound object and 1 to many binary
objects that belong the the compound object. In this instance:

* Compound object: https://trace.utk.edu/islandora/object/utk.ir.fg%3A18
* Binary object: https://trace.utk.edu/islandora/object/utk.ir.fg%3A15
* Binary object: https://trace.utk.edu/islandora/object/utk.ir.fg%3A16
* Binary object: https://trace.utk.edu/islandora/object/utk.ir.fg%3A17

For migration, we want to move the metadata from the compound object and each binary object.

Suggested PCDM Model for Fedora
-------------------------------

Google Dataset Inclusion
------------------------

Datasets should not go to Google Scholar, but should go to Google Dataset Search.

Unlike Google Scholar, Google Dataset Search relies on a structured body via a Schema.org mapping in a :code:`script`
tag in the :code:`head` of the document.

Our metadata mapping will include this conversion for this worktype.

===================
Required Properties
===================

----
name
----

A descriptive name of the dataset. For example, "Snow depth in the Northern Hemisphere".

The name property is modeled as `Schema.org Text <https://schema.org/Text>`_.

-----------
description
-----------

A short summary describing the dataset.

The summary must be between 50 and 5000 characters long and may include Markdown syntax. Embedded images need to use
absolute path URLs.

The description property is modeled as `Schema.org Text <https://schema.org/Text>`_.

-----------------------
distribution.contentUrl
-----------------------

======================
Recommended Properties
======================

-------------
alternateName
-------------

-------
creator
-------

The creator or author of this dataset.

If the creator is a person, it should be modelled as a `Schema.org Person <https://schema.org/Person>`_. If it is an
organization, it should be modelled as a `Schema.org Organization <https://schema.org/Organization>`_.

To uniquely identify individuals, use ORCID ID as the value of the sameAs property of the Person type.

To uniquely identify institutions and organizations, use ROR ID (`UT Example <https://ror.org/020f3ap87>`_).

--------
citation
--------

------------
distribution
------------

---------------------------
distribution.encodingFormat
---------------------------

------
funder
------

-------------------
hasPart or isPartOf
-------------------

----------
identifier
----------

---------------------
includedInDataCatalog
---------------------

-------------------
isAccessibleForFree
-------------------

--------
keywords
--------

-------
license
-------

--------------------
measurementTechnique
--------------------

------
sameAs
------

---------------
spatialCoverage
---------------

----------------
temporalCoverage
----------------

----------------
variableMeasured
----------------

-------
version
-------

---
url
---

