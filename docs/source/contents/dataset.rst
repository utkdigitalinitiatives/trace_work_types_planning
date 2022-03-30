Dataset Work Type
=================

About
-----

This work type represents datasets from our institutional repository.  Datasets have :code:`1-n` files and each may
be open or restricted from public access.

Datasets are different from other works and deserve there own worktype in order to be included in
`Google's Dataset Search <https://datasetsearch.research.google.com/>`_.

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

Suggested Actions
-----------------

1. If an object in Digital Commons refers to a object on trace.utk.edu that is not an ETD, we will migrate the object into the new repository as a dataset. It cannot stay at trace.utk.edu for security reasons.
2. If an object is in Trace Deposit and not an ETD, we will migrate it to the new system as a dataset.
2. We will provide the vendor for migration pages with front matter but without the coverpage.
3. The vendor will build a feature to add the appropriate cover page.
4. The vendor will build a feature for front matter going forward.

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
