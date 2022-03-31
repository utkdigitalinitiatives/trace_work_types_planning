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

.. code-block:: json

    {
      "results": [
        {
          "pid": "info:fedora/utk.ir.fg:7",
          "label": "Data from Tasmanian Eucalyptus Plant Functional Trait and Herbivory Data"
        },
        {
          "pid": "info:fedora/utk.ir.fg:14",
          "label": "Data from The State of Social Media Policies in Higher Education"
        },
        {
          "pid": "info:fedora/utk.ir.fg:18",
          "label": "Data from Public Progress, Data Management and the Land Grant Mission"
        },
        {
          "pid": "info:fedora/utk.ir.fg:27",
          "label": "Data Used in Carter et al., Exotic Plants and Thermal Regimes, Functional Ecology"
        },
        {
          "pid": "info:fedora/utk.ir.fg:29",
          "label": "Data from NSF Award #1155339: Governance of International Labor Migration: Scalar Politics and Network Relations"
        },
        {
          "pid": "info:fedora/utk.ir.fg:101",
          "label": "Data from Interpretations of NASA’s MSL Dynamic Albedo of Neutrons Passive Mode Data"
        },
        {
          "pid": "info:fedora/utk.ir.fg:2090",
          "label": "Voices of Diversity"
        },
        {
          "pid": "info:fedora/utk.ir.fg:2099",
          "label": "Data from New Age Estimates and Microscopic Charcoal Data for the 1976-B Core from Anderson Pond, Tennessee, USA"
        },
        {
          "pid": "info:fedora/utk.ir.fg:2110",
          "label": "Data for Investigating the effect of metal powder recycling in Electron beam Powder Bed Fusion using process log data"
        },
        {
          "pid": "info:fedora/utk.ir.fg:2112",
          "label": "Data for Investigating the effect of metal powder recycling in Electron beam Powder Bed Fusion using process log data"
        },
        {
          "pid": "info:fedora/utk.ir.fg:2129",
          "label": "Data from Near-field infrared spectroscopy of monolayer MnPS3 (OBJ file)"
        },
        {
          "pid": "info:fedora/utk.ir.fg:2132",
          "label": "Spectroscopic studies of size-dependent optical properties of oxide nanomaterials, molecule-based materials in extreme condition"
        },
        {
          "pid": "info:fedora/utk.ir.fg:2162",
          "label": "Data from Host density and habitat structure influence host contact rates and Batrachochytrium salamandrivorans transmission"
        },
        {
          "pid": "info:fedora/utk.ir.fg:2176",
          "label": "Data from Mental Health, Weather Extremes, and Race study"
        },
        {
          "pid": "info:fedora/utk.ir.fg:2179",
          "label": "Data from American Astronomical Society Survey"
        },
        {
          "pid": "info:fedora/utk.ir.fg:2188",
          "label": "Data from The National Electronic Library - User questionnaire for universities 2007 (Finland)"
        },
        {
          "pid": "info:fedora/utk.ir.fg:2193",
          "label": "Data for Database Use Patterns in Academic and Public Libraries"
        },
        {
          "pid": "info:fedora/utk.ir.fg:2198",
          "label": "Data from Database Marketplace Survey 2000"
        },
        {
          "pid": "info:fedora/utk.ir.fg:2215",
          "label": "Data Fitness for Use - INTERVIEWS"
        },
        {
          "pid": "info:fedora/utk.ir.fg:2239",
          "label": "Data for Soil nematode functional diversity, successional patterns, and indicator taxa associated with vertebrate decomposition"
        },
        {
          "pid": "info:fedora/utk.ir.fg:2245",
          "label": "Data from Business Journals Data Sharing"
        },
        {
          "pid": "info:fedora/utk.ir.fg:2248",
          "label": "Job analyses of earth science data librarians and data managers"
        },
        {
          "pid": "info:fedora/utk.ir.fg:2263",
          "label": "Data from \"Traditional rural values and posttraumatic stress among rural and urban undergraduates\""
        },
        {
          "pid": "info:fedora/utk.ir.fg:2268",
          "label": "Experimental methodologies can affect pathogenicity of Batrachochytrium salamandrivorans infections."
        },
        {
          "pid": "info:fedora/utk.ir.fg:2273",
          "label": "Data Management Plan Compliance and Evaluation"
        },
        {
          "pid": "info:fedora/utk.ir.fg:2287",
          "label": "Data Fitness for Use - SURVEYS"
        },
        {
          "pid": "info:fedora/utk.ir.fg:2290",
          "label": "Data Services Librarians"
        },
        {
          "pid": "info:fedora/utk.ir.fg:2303",
          "label": "GSSE Water Quality 2020"
        },
        {
          "pid": "info:fedora/utk.ir.fg:2307",
          "label": "Influence of Flocculant on Flow Behavior and Undrained Shear Strength of Fine Coal Refuse"
        },
        {
          "pid": "info:fedora/utk.ir.fg:2311",
          "label": "Winter is Coming – Temperature Affects Immune Defenses and Susceptibility to Batrachochytrium salamandrivorans"
        },
        {
          "pid": "info:fedora/utk.ir.fg:2341",
          "label": "Frequency-dependent transmission of Batrachochytrium salamandrivorans in eastern newts"
        },
        {
          "pid": "info:fedora/utk.ir.fg:2355",
          "label": "Nitrogen-cycle genes and transcripts abundances under agricultural management practices in a long-term continuous cotton field"
        },
        {
          "pid": "info:fedora/utk.ir.fg:2360",
          "label": "Data for Broad host susceptibility of North American amphibian species to Batrachochytrium salamandrivorans"
        },
        {
          "pid": "info:fedora/utk.ir.fg:2381",
          "label": "Survey Validation of Job Analyses for Science Data Managers"
        },
        {
          "pid": "info:fedora/utk.ir.fg:2384",
          "label": "Alabama Taxation and Changing Discourse from Reconstruction to Redemption"
        },
        {
          "pid": "info:fedora/utk.ir.fg:2385",
          "label": "Alabama Taxation and Changing Discourse from Reconstruction to Redemption"
        }
      ]
    }

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

The name property is modeled as `Text <https://schema.org/Text>`_.

-----------
description
-----------

A short summary describing the dataset.

The summary must be between 50 and 5000 characters long and may include Markdown syntax. Embedded images need to use
absolute path URLs.

The description property is modeled as `Text <https://schema.org/Text>`_.

-----------------------
distribution.contentUrl
-----------------------

The link for the download.

The distribution.contentUrl is modeled as a `URL <https://schema.org/URL>`_.

======================
Recommended Properties
======================

-------------
alternateName
-------------

Alternative names that have been used to refer to this dataset, such as aliases or abbreviations.

The property is modeled as `Text <https://schema.org/Text>`_.

-------
creator
-------

The creator or author of this dataset.

If the creator is a person, it should be modelled as a `Person <https://schema.org/Person>`_. If it is an
organization, it should be modelled as a `Organization <https://schema.org/Organization>`_.

To uniquely identify individuals, use ORCID ID as the value of the sameAs property of the Person type.

To uniquely identify institutions and organizations, use ROR ID (`UT Example <https://ror.org/020f3ap87>`_).

--------
citation
--------

Identifies academic articles that are recommended by the data provider be cited in addition to the dataset itself.

Provide the citation for the dataset itself with other properties, such as name, identifier, creator, and publisher
properties. For example, this property can uniquely identify a related academic publication such as a data descriptor,
data paper, or an article for which this dataset is supplementary material for.

Don't use this property to provide citation information for the dataset itself. It is intended to identify related
academic articles, not the dataset itself. To provide information necessary to cite the dataset itself use name,
identifier, creator, and publisher properties instead.

The property is modeled as `Text <https://schema.org/Text>`_ or `CreativeWork <https://schema.org/CreativeWork>`_.

------------
distribution
------------

The description of the location for download of the dataset and the file format for download.

The property is modelled as `DataDownload <https://schema.org/DataDownload>`_.

---------------------------
distribution.encodingFormat
---------------------------

The file format of the distribution.

The property is modeled as `Text <https://schema.org/Text>`_ or `URL <https://schema.org/URL>`_.

------
funder
------

A person or organization that provided financial support for this dataset.

To uniquely identify individuals, use ORCID ID as the value of the sameAs property of the Person type.

To uniquely identify institutions and organizations, use ROR ID.

If the funder is a person, it should be modelled as a `Person <https://schema.org/Person>`_. If it is an
organization, it should be modelled as a `Organization <https://schema.org/Organization>`_.

-------------------
hasPart or isPartOf
-------------------

If the dataset is a collection of smaller datasets, use the hasPart property to denote such relationship.

Conversly, if the dataset is part of a larger dataset, use isPartOf. Both properties can take the form of a URL or a
Dataset instance. In case Dataset is used as a value it has to include all of the properties required for a standalone
Dataset.

The property is modeled as `URL <https://schema.org/URL>`_ or `Dataset <https://schema.org/Dataset>`_.

----------
identifier
----------

An identifier, such as a DOI or a Compact Identifier. When JSON-LD, this is represented using JSON list syntax.

The property is modeled as `URL <https://schema.org/URL>`_, `Text <https://schema.org/Text>`_, or
`PropertyValue <https://schema.org/PropertyValue>`_.

---------------------
includedInDataCatalog
---------------------

The catalog to which the dataset belongs.

The full definition of DataCatalog is available at schema.org/DataCatalog.

Datasets are often published in repositories that contain many other datasets. The same dataset can be included in more than one such repository. You can refer to a data catalog that this dataset belongs to by referencing it directly.

The property is modelled as `DataCatalog <https://schema.org/DataCatalog>`_.

-------------------
isAccessibleForFree
-------------------

Is the dataset is accessible without payment.

The property is modeled as `Boolean <https://schema.org/Boolean>`_.

--------
keywords
--------

Keywords summarizing the dataset.

The property is modelled as `Text <https://schema.org/Text>`_.

-------
license
-------

A license under which the dataset is distributed.

The property can be modelled as `Text <https://schema.org/Text>`_ or `Creative Work <https://schema.org/CreativeWork>`_.

--------------------
measurementTechnique
--------------------

**Note**:  This property is pending standardization.

The technique, technology, or methodology used in a dataset, which can correspond to the variable(s) described in
:code:`variableMeasured`.

The property can be modelled as `Text <https://schema.org/Text>`_ or `URL <https://schema.org/URL>`_.

------
sameAs
------

The URL of a reference web page that unambiguously indicates the dataset's identity.

The property is modelled as `URL <https://schema.org/URL>`_.

---------------
spatialCoverage
---------------

A single point that describes the spatial aspect of the dataset. Only include this property if the dataset has a spatial
dimension. For example, a single point where all the measurements were collected, or the coordinates of a bounding box
for an area.

This property is modelled as `Text <https://schema.org/Text>`_  or `Place <https://schema.org/Place>`_.

----------------
temporalCoverage
----------------

If the data in the dataset covers a specific time interval, it can be modelled here.

Only include this property if the dataset has a temporal dimension. Use ISO 8601 standard to describe time intervals
and time points. You can describe dates differently depending upon the dataset interval. Indicate open-ended intervals
with two decimal points (..).

The property is modelled as `Text <https://schema.org/Text>`_.

Examples:

.. code-block:: text
    :caption: Single Date

    "temporalCoverage" : "2008"

.. code-block:: text
    :caption: Time Period

    "temporalCoverage" : "1950-01-01/2013-12-18"

.. code-block:: text
    :caption: Open-ended Time Period

    "temporalCoverage" : "2013-12-19/.."

----------------
variableMeasured
----------------

**Note**:  This property is pending standardization.

The variable that this dataset measures. For example, temperature or pressure.

The property can be modelled as `Text <https://schema.org/Text>`_ or `PropertyValue <https://schema.org/PropertyValue>`_.

-------
version
-------

The version number for the dataset.

The property can be modelled as `Text <https://schema.org/Text>`_ or `Number <https://schema.org/Number>`_.

---
url
---

Location of a page describing the dataset.

The property can be modelled as `URL <https://schema.org/URL>`_.
