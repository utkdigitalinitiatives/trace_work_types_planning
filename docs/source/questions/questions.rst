Questions about Work Types
--------------------------

Worktypes We've Defined
=======================

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

Structural Metadata
===================

All work type definitions have a section about structural metadata.  After our talk last week, I think it makes sense
to just handle this all with fileset metadata.  For instance, we'd like certain files to have specific :code:`pcdmuse`
types.

For instance, the primary file of an ETD that was uploaded by a student would be a :code:`pcdmuse:OriginalFile` and a
file that included frontmatter from the graduat school would be a :code:`pcdmuse:IntermediateFile`.  Other files uploaded
by the student would be :code:`fabio:SupplementaryInformation`.

I think we just handle all this with metadata on the fileset.  Do you disagree?

Also, if we did this, how can we state this for the work so that theses that are uploaded get the same data?

