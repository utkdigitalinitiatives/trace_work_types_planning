Book Work Type
==============

About
-----

This work type represents book like objects.  The object may include additional files including PDFs that are only
portions of the entire object.

This is a separate work type primarily because we want different metatags than the standard article type for Google
Scholar inclusion.

Migration Scope
---------------

Only PDF like objects whould get this work type.  Is there a PDF with Polk?

Here are the series with at least one item with some sort of ISBN value in its metadata record:

.. code-block:: text

    tcwp_news
    utk_agannual
    utk_agbulletin
    utk_arthistory
    utk_blackfacultyreports
    utk_blackinfo
    utk_blackmisccommunications
    utk_blackmiscreports
    utk_blacktaskissues
    utk_blacktaskmeetings
    utk_chempubs
    utk_compmedpubs
    utk_early-american
    utk_ecolpubs
    utk_ewing
    utk_forepubs
    utk_graddiss
    utk_gradthes
    utk_harlan
    utk_IACE-browseall
    utk_infosciepubs
    utk_jackson
    utk_lawalumniheadnotes
    utk_lawbulletins
    utk_libdevel
    utk_libpub
    utk_mtasdir
    utk_mtaspubs
    utk_mtastech
    utk_newfound-ebooks
    utk_nurspubs
    utk_polk
    utk_presrep
    utk_sasproceed
    utk_socopubs
    utk_socstim
    utk_tome
    utk_trustexh
    utk_utpress
    utk_wommin
    utk_womrepor

Current objects with the string :code:`ISBN`?

.. code-block:: text

    utk_chempubs/63/metadata.xml:116:&lt;p&gt;ISBN: 978-9934-588-82-2 (print)&lt;/p&gt;</abstract>
    utk_ewing/16/metadata.xml:48:&lt;p&gt;ISBN: 978-0-9761633-6-8&lt;/p&gt;
    utk_ewing/17/metadata.xml:46:&lt;p&gt;ISBN: 978-0-9761663-9-9&lt;/p&gt;
    utk_ewing/19/metadata.xml:40:&lt;p&gt;ISBN: 978-0-976-1663-0-6&lt;/p&gt;
    utk_ewing/28/metadata.xml:41:&lt;p&gt;ISBN: 978-0-9761663-4-4&lt;/p&gt;</value>
    utk_ewing/3/metadata.xml:51:&lt;p&gt;ISBN: 0-9761663-1-3&lt;/p&gt;
    utk_ewing/9/metadata.xml:45:&lt;p&gt;ISBN: 978-0-9761663-5-1&lt;/p&gt;
    utk_infosciepubs/59/metadata.xml:36:<value>Peiling Wang (2017). Developing an ePortfolio as a capstone experience for graduate studies in information science: a process-to-product model and its implementation. In Proceedings of EDULEARN17 Conference (3rd-5th July, 2017, Barcelona, SPAIN) Pages: 3861-3870 (ISBN: 978-84-697-3777-4)</value>
    utk_nurspubs/117/metadata.xml:3:<title>A Review of: “The Past in the Present” by Faith Gibson Baltimore, MD: Health Professions Press ISBN: 1-878812-87-4 Copyright: 2004</title>
    utk_nurspubs/117/metadata.xml:28:<value>Bonnie Callen. &quot;A Review of: “The Past in the Present” by Faith Gibson Baltimore, MD: Health Professions Press ISBN: 1-878812-87-4 Copyright: 2004&quot; Issues in Mental Health Nursing 26.7 (2005): 795-797.</value>
    utk_nurspubs/119/metadata.xml:3:<title>A Review of: “The Mindful Brain” W. W. Norton, New York, 2007 ISBN-0-393-70470-X</title>
    utk_nurspubs/119/metadata.xml:33:<value>Bonnie Callen and Daniel J. Siegel. &quot;A Review of: “The Mindful Brain” W. W. Norton, New York, 2007 ISBN-0-393-70470-X&quot; Issues in Mental Health Nursing 29.6 (2008): 675-676.</value>

Items with a :code:`978-` string.

.. code-block:: text

    tcwp_news/74/metadata.xml:4:<publication-date>1978-01-06T00:00:00-08:00</publication-date>
    tcwp_news/74/metadata.xml:23:<value>1978-01-06T00:00:00-08:00</value>
    tcwp_news/75/metadata.xml:4:<publication-date>1978-02-27T00:00:00-08:00</publication-date>
    tcwp_news/75/metadata.xml:23:<value>1978-02-27T00:00:00-08:00</value>
    tcwp_news/76/metadata.xml:4:<publication-date>1978-04-20T00:00:00-08:00</publication-date>
    tcwp_news/76/metadata.xml:23:<value>1978-04-20T00:00:00-08:00</value>
    tcwp_news/77/metadata.xml:4:<publication-date>1978-06-26T00:00:00-07:00</publication-date>
    tcwp_news/77/metadata.xml:23:<value>1978-06-26T00:00:00-07:00</value>
    tcwp_news/78/metadata.xml:4:<publication-date>1978-08-21T00:00:00-07:00</publication-date>
    tcwp_news/78/metadata.xml:23:<value>1978-08-21T00:00:00-07:00</value>
    tcwp_news/79/metadata.xml:4:<publication-date>1978-10-30T00:00:00-08:00</publication-date>
    tcwp_news/79/metadata.xml:23:<value>1978-10-30T00:00:00-08:00</value>
    utk_agannual/14/metadata.xml:4:<publication-date>1978-01-01T00:00:00-08:00</publication-date>
    utk_agannual/14/metadata.xml:31:<value>1978-01-01T00:00:00-08:00</value>
    utk_agbulletin/411/metadata.xml:4:<publication-date>1978-11-01T00:00:00-08:00</publication-date>
    utk_agbulletin/411/metadata.xml:40:<value>1978-11-01T00:00:00-08:00</value>
    utk_agbulletin/413/metadata.xml:4:<publication-date>1978-09-01T00:00:00-07:00</publication-date>
    utk_agbulletin/413/metadata.xml:46:<value>1978-09-01T00:00:00-07:00</value>
    utk_agbulletin/414/metadata.xml:4:<publication-date>1978-06-01T00:00:00-07:00</publication-date>
    utk_agbulletin/414/metadata.xml:46:<value>1978-06-01T00:00:00-07:00</value>
    utk_agbulletin/415/metadata.xml:4:<publication-date>1978-06-01T00:00:00-07:00</publication-date>
    utk_agbulletin/415/metadata.xml:41:<value>1978-06-01T00:00:00-07:00</value>
    utk_agbulletin/416/metadata.xml:4:<publication-date>1978-06-01T00:00:00-07:00</publication-date>
    utk_agbulletin/416/metadata.xml:45:<value>1978-06-01T00:00:00-07:00</value>
    utk_agbulletin/417/metadata.xml:4:<publication-date>1978-06-01T00:00:00-07:00</publication-date>
    utk_agbulletin/417/metadata.xml:41:<value>1978-06-01T00:00:00-07:00</value>
    utk_arthistory/45/metadata.xml:4:<publication-date>1978-01-01T00:00:00-08:00</publication-date>
    utk_arthistory/45/metadata.xml:39:<value>1978-01-01T00:00:00-08:00</value>
    utk_blackfacultyreports/74/metadata.xml:4:<publication-date>1978-01-01T00:00:00-08:00</publication-date>
    utk_blackfacultyreports/74/metadata.xml:26:<value>1978-01-01T00:00:00-08:00</value>
    utk_blackfacultyreports/75/metadata.xml:4:<publication-date>1978-01-01T00:00:00-08:00</publication-date>
    utk_blackfacultyreports/75/metadata.xml:26:<value>1978-01-01T00:00:00-08:00</value>
    utk_blackfacultyreports/76/metadata.xml:4:<publication-date>1978-02-13T00:00:00-08:00</publication-date>
    utk_blackfacultyreports/76/metadata.xml:26:<value>1978-02-13T00:00:00-08:00</value>
    utk_blackinfo/80/metadata.xml:4:<publication-date>1978-01-01T00:00:00-08:00</publication-date>
    utk_blackinfo/80/metadata.xml:26:<value>1978-01-01T00:00:00-08:00</value>
    utk_blackinfo/81/metadata.xml:4:<publication-date>1978-01-01T00:00:00-08:00</publication-date>
    utk_blackinfo/81/metadata.xml:26:<value>1978-01-01T00:00:00-08:00</value>
    utk_blackinfo/82/metadata.xml:4:<publication-date>1978-01-01T00:00:00-08:00</publication-date>
    utk_blackinfo/82/metadata.xml:26:<value>1978-01-01T00:00:00-08:00</value>
    utk_blackinfo/86/metadata.xml:4:<publication-date>1978-01-01T00:00:00-08:00</publication-date>
    utk_blackinfo/86/metadata.xml:26:<value>1978-01-01T00:00:00-08:00</value>
    utk_blackmisccommunications/14/metadata.xml:4:<publication-date>1978-03-15T00:00:00-08:00</publication-date>
    utk_blackmisccommunications/14/metadata.xml:26:<value>1978-03-15T00:00:00-08:00</value>
    utk_blackmisccommunications/32/metadata.xml:4:<publication-date>1978-05-27T00:00:00-07:00</publication-date>
    utk_blackmisccommunications/32/metadata.xml:26:<value>1978-05-27T00:00:00-07:00</value>
    utk_blackmisccommunications/33/metadata.xml:4:<publication-date>1978-04-27T00:00:00-08:00</publication-date>
    utk_blackmisccommunications/33/metadata.xml:26:<value>1978-04-27T00:00:00-08:00</value>
    utk_blackmisccommunications/34/metadata.xml:4:<publication-date>1978-05-26T00:00:00-07:00</publication-date>
    utk_blackmisccommunications/34/metadata.xml:26:<value>1978-05-26T00:00:00-07:00</value>
    utk_blackmisccommunications/35/metadata.xml:4:<publication-date>1978-05-26T00:00:00-07:00</publication-date>
    utk_blackmisccommunications/35/metadata.xml:26:<value>1978-05-26T00:00:00-07:00</value>
    utk_blackmisccommunications/36/metadata.xml:4:<publication-date>1978-04-07T00:00:00-08:00</publication-date>
    utk_blackmisccommunications/36/metadata.xml:26:<value>1978-04-07T00:00:00-08:00</value>
    utk_blackmisccommunications/37/metadata.xml:4:<publication-date>1978-02-02T00:00:00-08:00</publication-date>
    utk_blackmisccommunications/37/metadata.xml:26:<value>1978-02-02T00:00:00-08:00</value>
    utk_blackmiscreports/34/metadata.xml:4:<publication-date>1978-01-01T00:00:00-08:00</publication-date>
    utk_blackmiscreports/34/metadata.xml:26:<value>1978-01-01T00:00:00-08:00</value>
    utk_blackmiscreports/35/metadata.xml:4:<publication-date>1978-01-01T00:00:00-08:00</publication-date>
    utk_blackmiscreports/35/metadata.xml:26:<value>1978-01-01T00:00:00-08:00</value>
    utk_blackmiscreports/36/metadata.xml:4:<publication-date>1978-02-01T00:00:00-08:00</publication-date>
    utk_blackmiscreports/36/metadata.xml:26:<value>1978-02-01T00:00:00-08:00</value>
    utk_blacktaskissues/26/metadata.xml:4:<publication-date>1978-03-06T00:00:00-08:00</publication-date>
    utk_blacktaskissues/26/metadata.xml:26:<value>1978-03-06T00:00:00-08:00</value>
    utk_blacktaskissues/27/metadata.xml:4:<publication-date>1978-04-03T00:00:00-08:00</publication-date>
    utk_blacktaskissues/27/metadata.xml:26:<value>1978-04-03T00:00:00-08:00</value>
    utk_blacktaskissues/28/metadata.xml:4:<publication-date>1978-03-02T00:00:00-08:00</publication-date>
    utk_blacktaskissues/28/metadata.xml:26:<value>1978-03-02T00:00:00-08:00</value>
    utk_blacktaskmeetings/100/metadata.xml:4:<publication-date>1978-03-02T00:00:00-08:00</publication-date>
    utk_blacktaskmeetings/100/metadata.xml:26:<value>1978-03-02T00:00:00-08:00</value>
    utk_blacktaskmeetings/101/metadata.xml:4:<publication-date>1978-02-28T00:00:00-08:00</publication-date>
    utk_blacktaskmeetings/101/metadata.xml:26:<value>1978-02-28T00:00:00-08:00</value>
    utk_blacktaskmeetings/102/metadata.xml:4:<publication-date>1978-02-27T00:00:00-08:00</publication-date>
    utk_blacktaskmeetings/102/metadata.xml:26:<value>1978-02-27T00:00:00-08:00</value>
    utk_blacktaskmeetings/103/metadata.xml:4:<publication-date>1978-02-02T00:00:00-08:00</publication-date>
    utk_blacktaskmeetings/103/metadata.xml:26:<value>1978-02-02T00:00:00-08:00</value>
    utk_blacktaskmeetings/104/metadata.xml:4:<publication-date>1978-02-02T00:00:00-08:00</publication-date>
    utk_blacktaskmeetings/104/metadata.xml:26:<value>1978-02-02T00:00:00-08:00</value>
    utk_blacktaskmeetings/105/metadata.xml:4:<publication-date>1978-01-30T00:00:00-08:00</publication-date>
    utk_blacktaskmeetings/105/metadata.xml:26:<value>1978-01-30T00:00:00-08:00</value>
    utk_blacktaskmeetings/106/metadata.xml:4:<publication-date>1978-01-30T00:00:00-08:00</publication-date>
    utk_blacktaskmeetings/106/metadata.xml:26:<value>1978-01-30T00:00:00-08:00</value>
    utk_blacktaskmeetings/107/metadata.xml:4:<publication-date>1978-01-30T00:00:00-08:00</publication-date>
    utk_blacktaskmeetings/107/metadata.xml:26:<value>1978-01-30T00:00:00-08:00</value>
    utk_blacktaskmeetings/108/metadata.xml:4:<publication-date>1978-01-27T00:00:00-08:00</publication-date>
    utk_blacktaskmeetings/108/metadata.xml:26:<value>1978-01-27T00:00:00-08:00</value>
    utk_blacktaskmeetings/109/metadata.xml:4:<publication-date>1978-11-09T00:00:00-08:00</publication-date>
    utk_blacktaskmeetings/109/metadata.xml:26:<value>1978-11-09T00:00:00-08:00</value>
    utk_blacktaskmeetings/110/metadata.xml:4:<publication-date>1978-05-24T00:00:00-07:00</publication-date>
    utk_blacktaskmeetings/110/metadata.xml:26:<value>1978-05-24T00:00:00-07:00</value>
    utk_blacktaskmeetings/111/metadata.xml:4:<publication-date>1978-05-08T00:00:00-07:00</publication-date>
    utk_blacktaskmeetings/111/metadata.xml:26:<value>1978-05-08T00:00:00-07:00</value>
    utk_blacktaskmeetings/112/metadata.xml:4:<publication-date>1978-04-26T00:00:00-08:00</publication-date>
    utk_blacktaskmeetings/112/metadata.xml:26:<value>1978-04-26T00:00:00-08:00</value>
    utk_blacktaskmeetings/113/metadata.xml:4:<publication-date>1978-04-12T00:00:00-08:00</publication-date>
    utk_blacktaskmeetings/113/metadata.xml:26:<value>1978-04-12T00:00:00-08:00</value>
    utk_blacktaskmeetings/114/metadata.xml:4:<publication-date>1978-04-05T00:00:00-08:00</publication-date>
    utk_blacktaskmeetings/114/metadata.xml:26:<value>1978-04-05T00:00:00-08:00</value>
    utk_blacktaskmeetings/115/metadata.xml:4:<publication-date>1978-03-14T00:00:00-08:00</publication-date>
    utk_blacktaskmeetings/115/metadata.xml:26:<value>1978-03-14T00:00:00-08:00</value>
    utk_blacktaskmeetings/116/metadata.xml:4:<publication-date>1978-03-08T00:00:00-08:00</publication-date>
    utk_blacktaskmeetings/116/metadata.xml:26:<value>1978-03-08T00:00:00-08:00</value>
    utk_blacktaskmeetings/117/metadata.xml:4:<publication-date>1978-02-22T00:00:00-08:00</publication-date>
    utk_blacktaskmeetings/117/metadata.xml:26:<value>1978-02-22T00:00:00-08:00</value>
    utk_blacktaskmeetings/118/metadata.xml:4:<publication-date>1978-02-08T00:00:00-08:00</publication-date>
    utk_blacktaskmeetings/118/metadata.xml:26:<value>1978-02-08T00:00:00-08:00</value>
    utk_blacktaskmeetings/119/metadata.xml:4:<publication-date>1978-01-26T00:00:00-08:00</publication-date>
    utk_blacktaskmeetings/119/metadata.xml:26:<value>1978-01-26T00:00:00-08:00</value>
    utk_blacktaskmeetings/120/metadata.xml:4:<publication-date>1978-01-25T00:00:00-08:00</publication-date>
    utk_blacktaskmeetings/120/metadata.xml:26:<value>1978-01-25T00:00:00-08:00</value>
    utk_blacktaskmeetings/121/metadata.xml:4:<publication-date>1978-01-11T00:00:00-08:00</publication-date>
    utk_blacktaskmeetings/121/metadata.xml:26:<value>1978-01-11T00:00:00-08:00</value>
    utk_blacktaskmeetings/95/metadata.xml:4:<publication-date>1978-09-06T00:00:00-07:00</publication-date>
    utk_blacktaskmeetings/95/metadata.xml:26:<value>1978-09-06T00:00:00-07:00</value>
    utk_blacktaskmeetings/96/metadata.xml:4:<publication-date>1978-05-19T00:00:00-07:00</publication-date>
    utk_blacktaskmeetings/96/metadata.xml:26:<value>1978-05-19T00:00:00-07:00</value>
    utk_blacktaskmeetings/97/metadata.xml:4:<publication-date>1978-05-16T00:00:00-07:00</publication-date>
    utk_blacktaskmeetings/97/metadata.xml:26:<value>1978-05-16T00:00:00-07:00</value>
    utk_blacktaskmeetings/98/metadata.xml:4:<publication-date>1978-05-16T00:00:00-07:00</publication-date>
    utk_blacktaskmeetings/98/metadata.xml:26:<value>1978-05-16T00:00:00-07:00</value>
    utk_blacktaskmeetings/99/metadata.xml:4:<publication-date>1978-05-10T00:00:00-07:00</publication-date>
    utk_blacktaskmeetings/99/metadata.xml:26:<value>1978-05-10T00:00:00-07:00</value>
    utk_chempubs/63/metadata.xml:116:&lt;p&gt;ISBN: 978-9934-588-82-2 (print)&lt;/p&gt;</abstract>
    utk_compmedpubs/126/metadata.xml:59:<value>https://doi.org/10.1186/s12917-019-1978-6</value>
    utk_early-american/10/metadata.xml:4:<publication-date>1978-01-01T00:00:00-08:00</publication-date>
    utk_early-american/10/metadata.xml:41:<value>1978-01-01T00:00:00-08:00</value>
    utk_early-american/13/metadata.xml:44:<value>978-1-57233-844-9</value>
    utk_early-american/16/metadata.xml:4:<publication-date>1978-01-01T00:00:00-08:00</publication-date>
    utk_early-american/16/metadata.xml:41:<value>1978-01-01T00:00:00-08:00</value>
    utk_early-american/17/metadata.xml:4:<publication-date>1978-01-01T00:00:00-08:00</publication-date>
    utk_early-american/17/metadata.xml:41:<value>1978-01-01T00:00:00-08:00</value>
    utk_ecolpubs/17/metadata.xml:4:<publication-date>1978-01-01T00:00:00-08:00</publication-date>
    utk_ecolpubs/17/metadata.xml:35:<value>1978-01-01T00:00:00-08:00</value>
    utk_ewing/16/metadata.xml:48:&lt;p&gt;ISBN: 978-0-9761633-6-8&lt;/p&gt;
    utk_ewing/17/metadata.xml:46:&lt;p&gt;ISBN: 978-0-9761663-9-9&lt;/p&gt;
    utk_ewing/19/metadata.xml:40:&lt;p&gt;ISBN: 978-0-976-1663-0-6&lt;/p&gt;
    utk_ewing/28/metadata.xml:41:&lt;p&gt;ISBN: 978-0-9761663-4-4&lt;/p&gt;</value>
    utk_ewing/9/metadata.xml:45:&lt;p&gt;ISBN: 978-0-9761663-5-1&lt;/p&gt;
    utk_forepubs/24/metadata.xml:50:<value>Gray, Matthew J. and V. Gregory Chinchar. Ranaviruses: Lethal Pathogens of Ectothermic Vertebrates. Switzerland: Springer International Publishing, 2015. http://dx.doi.org/10.1007/978-3-319-13755-1.</value>
    utk_forepubs/24/metadata.xml:53:<value>http://dx.doi.org/10.1007/978-3-319-13755-1</value>
    utk_forepubs/25/metadata.xml:49:<value>Gray, Matthew J. and V. Gregory Chinchar. Ranaviruses: Lethal Pathogens of Ectothermic Vertebrates. Switzerland: Springer International Publishing, 2015. http://dx.doi.org/10.1007/978-3-319-13755-1.</value>
    utk_forepubs/25/metadata.xml:52:<value>http://dx.doi.org/10.1007/978-3-319-13755-1</value>
    utk_forepubs/26/metadata.xml:37:<value>Gray, Matthew J. and V. Gregory Chinchar. Ranaviruses: Lethal Pathogens of Ectothermic Vertebrates. Switzerland: Springer International Publishing, 2015. http://dx.doi.org/10.1007/978-3-319-13755-1.</value>
    utk_forepubs/26/metadata.xml:40:<value>http://dx.doi.org/10.1007/978-3-319-13755-1</value>
    utk_graddiss/1247/metadata.xml:4:<publication-date>1978-03-01T00:00:00-08:00</publication-date>
    utk_graddiss/1247/metadata.xml:36:<value>1978-03-01T00:00:00-08:00</value>
    utk_graddiss/1247/metadata.xml:39:<value>1978-03-01T00:00:00-08:00</value>
    utk_graddiss/1248/metadata.xml:41:<value>1978-06-01T00:00:00-07:00</value>
    utk_graddiss/1607/metadata.xml:4:<publication-date>1978-06-01T00:00:00-07:00</publication-date>
    utk_graddiss/1607/metadata.xml:44:<value>1978-06-01T00:00:00-07:00</value>
    utk_graddiss/1607/metadata.xml:47:<value>1978-06-01T00:00:00-07:00</value>
    utk_graddiss/2542/metadata.xml:4:<publication-date>1978-08-01T00:00:00-07:00</publication-date>
    utk_graddiss/2542/metadata.xml:50:<value>1978-08-01T00:00:00-07:00</value>
    utk_graddiss/2542/metadata.xml:53:<value>1978-08-01T00:00:00-07:00</value>
    utk_graddiss/2636/metadata.xml:4:<publication-date>1978-06-01T00:00:00-07:00</publication-date>
    utk_graddiss/2636/metadata.xml:51:<value>1978-06-01T00:00:00-07:00</value>
    utk_graddiss/2636/metadata.xml:54:<value>1978-06-01T00:00:00-07:00</value>
    utk_graddiss/2639/metadata.xml:4:<publication-date>1978-06-01T00:00:00-07:00</publication-date>
    utk_graddiss/2639/metadata.xml:41:<value>1978-06-01T00:00:00-07:00</value>
    utk_graddiss/2639/metadata.xml:44:<value>1978-06-01T00:00:00-07:00</value>
    utk_graddiss/2641/metadata.xml:4:<publication-date>1978-08-01T00:00:00-07:00</publication-date>
    utk_graddiss/2641/metadata.xml:41:<value>1978-08-01T00:00:00-07:00</value>
    utk_graddiss/2641/metadata.xml:44:<value>1978-08-01T00:00:00-07:00</value>
    utk_graddiss/2667/metadata.xml:4:<publication-date>1978-08-01T00:00:00-07:00</publication-date>
    utk_graddiss/2667/metadata.xml:48:<value>1978-08-01T00:00:00-07:00</value>
    utk_graddiss/2667/metadata.xml:51:<value>1978-08-01T00:00:00-07:00</value>
    utk_graddiss/2839/metadata.xml:22:</disciplines><abstract>&lt;p&gt;Small businesses and the entrepreneurial spirit are among the driving forces in economic growth and development in the United States. The US governments (both federal and state) have long been aware of the importance of entrepreneurship, and many policies are directed toward helping small businesses. However, whether such policies give rise to expected behavioral responses from small businesses remains inconclusive. This dissertation looks into the behavioral response of self-employed filers to individual income tax and the impact of state and federal tax policies on entrepreneurship. In the first chapter, we examine taxpayers’ behavioral response to the Alternative Minimum Tax (AMT). We find strong evidence that taxpayers, especially self-employed individuals, appear to manipulate their incomes to avoid the AMT. We also find suggestive evidence that the notch created by the AMT generates both a real response and an evasion response. These results have important policy implications for the AMT design and for the evaluation of the welfare loss from taxation of small businesses. The second chapter examines the effect of state tax policies on entrepreneurial activity. This paper contributes to the literature in several important ways: first, we explore dynamic specifications to capture inherent time trends among entrepreneurial performance. Second, we consider a number of intensive-margin measures of state nonfarm proprietors’ success. Our paper is the first to use nonfarm proprietors’ income as a direct measure of entrepreneurial success at the state level. We investigate several measures of small business performance derived from nonfarm proprietors’ income and employment data. Third, we extend the earlier research by including a longer panel (1978-2009) of state data. Despite these innovations, our empirical results echo the recent studies in this area and suggest that most of the highly-visible state tax policies do not have statistically significant impacts on entrepreneurial performance. The last chapter uses time series analysis to explore the effect of federal tax policies on entrepreneurial performance and whether the effect is heterogeneous across different stages of the business cycle. We do not find that tax policy affects the small businesses sector differently between economic ups and downs.&lt;/p&gt;</abstract>
    utk_graddiss/3051/metadata.xml:4:<publication-date>1978-06-01T00:00:00-07:00</publication-date>
    utk_graddiss/3051/metadata.xml:45:<value>1978-06-01T00:00:00-07:00</value>
    utk_graddiss/3051/metadata.xml:48:<value>1978-06-01T00:00:00-07:00</value>
    utk_graddiss/3812/metadata.xml:4:<publication-date>1978-08-01T00:00:00-07:00</publication-date>
    utk_graddiss/3812/metadata.xml:40:<value>1978-08-01T00:00:00-07:00</value>
    utk_graddiss/3812/metadata.xml:43:<value>1978-08-01T00:00:00-07:00</value>
    utk_graddiss/3820/metadata.xml:4:<publication-date>1978-08-01T00:00:00-07:00</publication-date>
    utk_graddiss/3820/metadata.xml:45:<value>1978-08-01T00:00:00-07:00</value>
    utk_graddiss/3820/metadata.xml:48:<value>1978-08-01T00:00:00-07:00</value>
    utk_graddiss/3840/metadata.xml:4:<publication-date>1978-03-01T00:00:00-08:00</publication-date>
    utk_graddiss/3840/metadata.xml:44:<value>1978-03-01T00:00:00-08:00</value>
    utk_graddiss/3840/metadata.xml:47:<value>1978-03-01T00:00:00-08:00</value>
    utk_graddiss/3854/metadata.xml:4:<publication-date>1978-08-01T00:00:00-07:00</publication-date>
    utk_graddiss/3854/metadata.xml:46:<value>1978-08-01T00:00:00-07:00</value>
    utk_graddiss/3854/metadata.xml:49:<value>1978-08-01T00:00:00-07:00</value>
    utk_graddiss/4017/metadata.xml:4:<publication-date>1978-08-01T00:00:00-07:00</publication-date>
    utk_graddiss/4017/metadata.xml:43:<value>1978-08-01T00:00:00-07:00</value>
    utk_graddiss/4017/metadata.xml:46:<value>1978-08-01T00:00:00-07:00</value>
    utk_graddiss/4069/metadata.xml:4:<publication-date>1978-12-01T00:00:00-08:00</publication-date>
    utk_graddiss/4069/metadata.xml:49:<value>1978-12-01T00:00:00-08:00</value>
    utk_graddiss/4069/metadata.xml:52:<value>1978-12-01T00:00:00-08:00</value>
    utk_graddiss/4317/metadata.xml:16:&lt;p&gt;Two hundred-twenty articles listed under the multicultural education heading in the Education Index from 1977-1987 were used as data for this study. Sixty-two articles that appeared in journals in 1977 were used to identify the early common themes of multicultural education. The remaining years covered in this study, 1978-1987, were divided into two periods: Period I: 1977-1983 and Period II: 1983-1987. The writings taken from the articles from both periods, I and II, were used for interpretation and analysis of the evolution of the themes identified from the 1977/78 index.&lt;/p&gt;
    utk_gradthes/1050/metadata.xml:4:<publication-date>1978-06-01T00:00:00-07:00</publication-date>
    utk_gradthes/1050/metadata.xml:43:<value>1978-06-01T00:00:00-07:00</value>
    utk_gradthes/1050/metadata.xml:46:<value>1978-06-01T00:00:00-07:00</value>
    utk_gradthes/1354/metadata.xml:4:<publication-date>1978-12-01T00:00:00-08:00</publication-date>
    utk_gradthes/1354/metadata.xml:45:<value>1978-12-01T00:00:00-08:00</value>
    utk_gradthes/1354/metadata.xml:48:<value>1978-12-01T00:00:00-08:00</value>
    utk_gradthes/1425/metadata.xml:4:<publication-date>1978-08-01T00:00:00-07:00</publication-date>
    utk_gradthes/1425/metadata.xml:40:<value>1978-08-01T00:00:00-07:00</value>
    utk_gradthes/1425/metadata.xml:43:<value>1978-08-01T00:00:00-07:00</value>
    utk_gradthes/1428/metadata.xml:4:<publication-date>1978-08-01T00:00:00-07:00</publication-date>
    utk_gradthes/1428/metadata.xml:42:<value>1978-08-01T00:00:00-07:00</value>
    utk_gradthes/1428/metadata.xml:45:<value>1978-08-01T00:00:00-07:00</value>
    utk_gradthes/1449/metadata.xml:4:<publication-date>1978-12-01T00:00:00-08:00</publication-date>
    utk_gradthes/1449/metadata.xml:47:<value>1978-12-01T00:00:00-08:00</value>
    utk_gradthes/1449/metadata.xml:50:<value>1978-12-01T00:00:00-08:00</value>
    utk_gradthes/1473/metadata.xml:4:<publication-date>1978-06-01T00:00:00-07:00</publication-date>
    utk_gradthes/1473/metadata.xml:43:<value>1978-06-01T00:00:00-07:00</value>
    utk_gradthes/1473/metadata.xml:46:<value>1978-06-01T00:00:00-07:00</value>
    utk_gradthes/1480/metadata.xml:4:<publication-date>1978-08-01T00:00:00-07:00</publication-date>
    utk_gradthes/1480/metadata.xml:44:<value>1978-08-01T00:00:00-07:00</value>
    utk_gradthes/1480/metadata.xml:47:<value>1978-08-01T00:00:00-07:00</value>
    utk_gradthes/2339/metadata.xml:3:<title>An Assessment of Responses in the British Press to Muslim Immigrants 1978-1989</title>
    utk_gradthes/2498/metadata.xml:4:<publication-date>1978-03-01T00:00:00-08:00</publication-date>
    utk_gradthes/2498/metadata.xml:42:<value>1978-03-01T00:00:00-08:00</value>
    utk_gradthes/2498/metadata.xml:45:<value>1978-03-01T00:00:00-08:00</value>
    utk_gradthes/2504/metadata.xml:20:&lt;p&gt;One hundred seventy-eight bears were tested serologically for canine distemper virus.  Fifty-two reactors (29.2%) were determined for 1978-79 but no reactors were found in 1977 (n=47).&lt;/p&gt;
    utk_gradthes/2504/metadata.xml:22:&lt;p&gt;Sixty-seven sera samples were submitted for antibody titers to infectious bovine rhinotracheitis, swine parvovirus, and pseudorabies.  All specimens were collected during the 1978-79 period.  No reactors were found.  Sixty samples were negative for canine parvovirus titers.&lt;/p&gt;
    utk_gradthes/2512/metadata.xml:15:</disciplines><abstract>&lt;p&gt;Black bear reproduction, winter dormancy and denning physiology were studied during June 1984 to May 1986 in the northwest quadrant of Great Smoky Mountains National Park, Tennessee.  Information was obtained from 30 individual females captured 35 times.  Additional information on mast indices, lactation and den utilization were summarized from within the study area for the period from 1978-1988.&lt;/p&gt;
    utk_gradthes/2579/metadata.xml:18:&lt;p&gt;Using den records from 1978-1991, I calculated litter size, sex ratio, and cub survival. The average size of 74 litters was 2.24 with a sex ratio of 102♂:100♀.  Overall cub survival was 61.3% with females and cubs from intermediate-size litters exhibiting slightly higher survival rates.&lt;/p&gt;
    utk_gradthes/2643/metadata.xml:24:</disciplines><abstract>&lt;p&gt;Gold Mine (16RI13) is a Troyville ossuary mound site (circa CE 825) in northeastern Louisiana. Approximately 10-20% of the primary mound (Mound A) was excavated over the course of three field seasons (1978-1980), yielding a host of human skeletal remains. Extensively commingled secondary burials make up the majority of interments. The number of individuals represented within the collection (&lt;em&gt;N&lt;/em&gt;) has been estimated at 150+ (McGimsey 2004:214), but attempts to quantitatively determine &lt;em&gt;N&lt;/em&gt; have produced varied results. Formal analysis of the skeletal collection is complicated by the loss of provenience for many remains as well as additional post-excavation fragmentation and commingling.&lt;/p&gt;
    utk_gradthes/2686/metadata.xml:4:<publication-date>1978-08-01T00:00:00-07:00</publication-date>
    utk_gradthes/2686/metadata.xml:45:<value>1978-08-01T00:00:00-07:00</value>
    utk_gradthes/2686/metadata.xml:48:<value>1978-08-01T00:00:00-07:00</value>
    utk_gradthes/3007/metadata.xml:4:<publication-date>1978-08-01T00:00:00-07:00</publication-date>
    utk_gradthes/3007/metadata.xml:42:<value>1978-08-01T00:00:00-07:00</value>
    utk_gradthes/3007/metadata.xml:45:<value>1978-08-01T00:00:00-07:00</value>
    utk_gradthes/3222/metadata.xml:4:<publication-date>1978-08-01T00:00:00-07:00</publication-date>
    utk_gradthes/3222/metadata.xml:43:<value>1978-08-01T00:00:00-07:00</value>
    utk_gradthes/3222/metadata.xml:46:<value>1978-08-01T00:00:00-07:00</value>
    utk_gradthes/3321/metadata.xml:4:<publication-date>1978-06-01T00:00:00-07:00</publication-date>
    utk_gradthes/3321/metadata.xml:47:<value>1978-06-01T00:00:00-07:00</value>
    utk_gradthes/3321/metadata.xml:50:<value>1978-06-01T00:00:00-07:00</value>
    utk_gradthes/3437/metadata.xml:4:<publication-date>1978-06-01T00:00:00-07:00</publication-date>
    utk_gradthes/3437/metadata.xml:42:<value>1978-06-01T00:00:00-07:00</value>
    utk_gradthes/3437/metadata.xml:45:<value>1978-06-01T00:00:00-07:00</value>
    utk_gradthes/3834/metadata.xml:4:<publication-date>1978-12-01T00:00:00-08:00</publication-date>
    utk_gradthes/3834/metadata.xml:43:<value>1978-12-01T00:00:00-08:00</value>
    utk_gradthes/3834/metadata.xml:46:<value>1978-12-01T00:00:00-08:00</value>
    utk_gradthes/3969/metadata.xml:4:<publication-date>1978-08-01T00:00:00-07:00</publication-date>
    utk_gradthes/3969/metadata.xml:40:<value>1978-08-01T00:00:00-07:00</value>
    utk_gradthes/3969/metadata.xml:43:<value>1978-08-01T00:00:00-07:00</value>
    utk_gradthes/4167/metadata.xml:4:<publication-date>1978-06-01T00:00:00-07:00</publication-date>
    utk_gradthes/4167/metadata.xml:41:<value>1978-06-01T00:00:00-07:00</value>
    utk_gradthes/4167/metadata.xml:44:<value>1978-06-01T00:00:00-07:00</value>
    utk_gradthes/4197/metadata.xml:4:<publication-date>1978-12-01T00:00:00-08:00</publication-date>
    utk_gradthes/4197/metadata.xml:44:<value>1978-12-01T00:00:00-08:00</value>
    utk_gradthes/4197/metadata.xml:47:<value>1978-12-01T00:00:00-08:00</value>
    utk_gradthes/4207/metadata.xml:4:<publication-date>1978-06-01T00:00:00-07:00</publication-date>
    utk_gradthes/4207/metadata.xml:44:<value>1978-06-01T00:00:00-07:00</value>
    utk_gradthes/4207/metadata.xml:47:<value>1978-06-01T00:00:00-07:00</value>
    utk_gradthes/4245/metadata.xml:4:<publication-date>1978-12-01T00:00:00-08:00</publication-date>
    utk_gradthes/4245/metadata.xml:40:<value>1978-12-01T00:00:00-08:00</value>
    utk_gradthes/4245/metadata.xml:43:<value>1978-12-01T00:00:00-08:00</value>
    utk_gradthes/4246/metadata.xml:4:<publication-date>1978-12-01T00:00:00-08:00</publication-date>
    utk_gradthes/4246/metadata.xml:42:<value>1978-12-01T00:00:00-08:00</value>
    utk_gradthes/4246/metadata.xml:45:<value>1978-12-01T00:00:00-08:00</value>
    utk_gradthes/4249/metadata.xml:4:<publication-date>1978-06-01T00:00:00-07:00</publication-date>
    utk_gradthes/4249/metadata.xml:43:<value>1978-06-01T00:00:00-07:00</value>
    utk_gradthes/4249/metadata.xml:46:<value>1978-06-01T00:00:00-07:00</value>
    utk_gradthes/5799/metadata.xml:4:<publication-date>1978-08-01T00:00:00-07:00</publication-date>
    utk_gradthes/5799/metadata.xml:36:<value>1978-08-01T00:00:00-07:00</value>
    utk_gradthes/6347/metadata.xml:4:<publication-date>1978-06-01T00:00:00-07:00</publication-date>
    utk_gradthes/6347/metadata.xml:38:<value>1978-06-01T00:00:00-07:00</value>
    utk_gradthes/852/metadata.xml:4:<publication-date>1978-08-01T00:00:00-07:00</publication-date>
    utk_gradthes/852/metadata.xml:48:<value>1978-08-01T00:00:00-07:00</value>
    utk_harlan/101/metadata.xml:4:<publication-date>1978-12-05T00:00:00-08:00</publication-date>
    utk_harlan/101/metadata.xml:31:<value>1978-12-05T00:00:00-08:00</value>
    utk_harlan/137/metadata.xml:4:<publication-date>1978-08-15T00:00:00-07:00</publication-date>
    utk_harlan/137/metadata.xml:31:<value>1978-08-15T00:00:00-07:00</value>
    utk_harlan/169/metadata.xml:4:<publication-date>1978-04-27T00:00:00-08:00</publication-date>
    utk_harlan/169/metadata.xml:31:<value>1978-04-27T00:00:00-08:00</value>
    utk_harlan/244/metadata.xml:4:<publication-date>1978-08-11T00:00:00-07:00</publication-date>
    utk_harlan/244/metadata.xml:31:<value>1978-08-11T00:00:00-07:00</value>
    utk_harlan/276/metadata.xml:4:<publication-date>1978-05-04T00:00:00-07:00</publication-date>
    utk_harlan/276/metadata.xml:31:<value>1978-05-04T00:00:00-07:00</value>
    utk_harlan/350/metadata.xml:4:<publication-date>1978-01-01T00:00:00-08:00</publication-date>
    utk_harlan/350/metadata.xml:31:<value>1978-01-01T00:00:00-08:00</value>
    utk_harlan/411/metadata.xml:4:<publication-date>1978-01-01T00:00:00-08:00</publication-date>
    utk_harlan/411/metadata.xml:31:<value>1978-01-01T00:00:00-08:00</value>
    utk_harlan/436/metadata.xml:4:<publication-date>1978-01-01T00:00:00-08:00</publication-date>
    utk_harlan/436/metadata.xml:31:<value>1978-01-01T00:00:00-08:00</value>
    utk_harlan/63/metadata.xml:4:<publication-date>1978-03-17T00:00:00-08:00</publication-date>
    utk_harlan/63/metadata.xml:31:<value>1978-03-17T00:00:00-08:00</value>
    utk_harlan/64/metadata.xml:4:<publication-date>1978-10-02T00:00:00-07:00</publication-date>
    utk_harlan/64/metadata.xml:31:<value>1978-10-02T00:00:00-07:00</value>
    utk_IACE-browseall/354/metadata.xml:4:<publication-date>1978-01-01T00:00:00-08:00</publication-date>
    utk_IACE-browseall/354/metadata.xml:56:<value>1978-01-01T00:00:00-08:00</value>
    utk_IACE-browseall/387/metadata.xml:65:<value>10.4018/978-1-4666-6260-5.ch020</value>
    utk_IACE-browseall/388/metadata.xml:66:<value>10.4018/978-1-4666-5872-1.ch008</value>
    utk_IACE-browseall/389/metadata.xml:65:<value>10.4018/978-1-4666-6046-5.ch010</value>
    utk_IACE-browseall/391/metadata.xml:53:<value>10.4018/978-1-4666-4249-2.ch021</value>
    utk_IACE-browseall/392/metadata.xml:65:<value>10.4018/978-1-4666-4249-2.ch049</value>
    utk_IACE-browseall/478/metadata.xml:4:<publication-date>1978-01-01T00:00:00-08:00</publication-date>
    utk_IACE-browseall/478/metadata.xml:61:<value>1978-01-01T00:00:00-08:00</value>
    utk_IACE-browseall/546/metadata.xml:59:<value>978-1-119-05101-5</value>
    utk_infosciepubs/229/metadata.xml:4:<publication-date>1978-06-01T00:00:00-07:00</publication-date>
    utk_infosciepubs/229/metadata.xml:43:<value>1978-06-01T00:00:00-07:00</value>
    utk_infosciepubs/24/metadata.xml:4:<publication-date>1978-06-01T00:00:00-07:00</publication-date>
    utk_infosciepubs/24/metadata.xml:31:<value>1978-06-01T00:00:00-07:00</value>
    utk_infosciepubs/44/metadata.xml:4:<publication-date>1978-05-01T00:00:00-07:00</publication-date>
    utk_infosciepubs/44/metadata.xml:27:<value>1978-05-01T00:00:00-07:00</value>
    utk_infosciepubs/450/metadata.xml:44:<value>&lt;p&gt;This short paper is published in the Information in Contemporary Society, 14th International Conference, iConference 2019, Washington, DC, USA, March 31–April 3, 2019, Proceedings, See https://link.springer.com/chapter/10.1007/978-3-030-15742-5_22.&lt;/p&gt;</value>
    utk_infosciepubs/450/metadata.xml:47:<value>Potnis, D. &amp; Gala, B. (2019). Proposing “mobile, finance, and information” toolkit for financial inclusion of the poor in developing countries. In Taylor, N., Christian-Lamb, C., Martin M., &amp; Nardi, B. (Eds.), Lecture notes in computer science: Vol. 11420. Information in Contemporary Society (pp. 228-235). Springer. https://link.springer.com/chapter/10.1007/978-3-030-15742-5_22</value>
    utk_infosciepubs/450/metadata.xml:50:<value>https://link.springer.com/chapter/10.1007/978-3-030-15742-5_22</value>
    utk_infosciepubs/59/metadata.xml:36:<value>Peiling Wang (2017). Developing an ePortfolio as a capstone experience for graduate studies in information science: a process-to-product model and its implementation. In Proceedings of EDULEARN17 Conference (3rd-5th July, 2017, Barcelona, SPAIN) Pages: 3861-3870 (ISBN: 978-84-697-3777-4)</value>
    utk_jackson/11/metadata.xml:48:<value>978-1-57233-593-6</value>
    utk_jackson/13/metadata.xml:49:<value>978-1-62190-538-7</value>
    utk_jackson/6/metadata.xml:47:<value>978-1-62190-267-6</value>
    utk_jackson/8/metadata.xml:49:<value>978-1-62190-004-7</value>
    utk_jackson/9/metadata.xml:47:<value>978-1-57233-715-2</value>
    utk_lawalumniheadnotes/1/metadata.xml:4:<publication-date>1978-01-01T00:00:00-08:00</publication-date>
    utk_lawalumniheadnotes/1/metadata.xml:27:<value>1978-01-01T00:00:00-08:00</value>
    utk_lawbulletins/16/metadata.xml:3:<title>Bulletin (1978-1979)</title>
    utk_lawbulletins/17/metadata.xml:4:<publication-date>1978-01-01T00:00:00-08:00</publication-date>
    utk_lawbulletins/17/metadata.xml:27:<value>1978-01-01T00:00:00-08:00</value>
    utk_libdevel/32/metadata.xml:4:<publication-date>1978-09-01T00:00:00-07:00</publication-date>
    utk_libdevel/32/metadata.xml:25:<value>1978-09-01T00:00:00-07:00</value>
    utk_libdevel/33/metadata.xml:3:<title>The Library Development Program Report 1978-79</title>
    utk_libdevel/71/metadata.xml:4:<publication-date>1978-09-01T00:00:00-07:00</publication-date>
    utk_libdevel/71/metadata.xml:34:<value>1978-09-01T00:00:00-07:00</value>
    utk_libdevel/72/metadata.xml:3:<title>The Library Development Program Report 1978-79</title>
    utk_libpub/15/metadata.xml:50:<value>Maynor, Ashley R. &quot;Response to the Unthinkable: Collecting and Archiving Condolence and Temporary Memorial Materials following Public Tragedies.&quot; In Handbook of Research on Disaster Management and Contingency Planning in Modern Libraries, ed. Emy Nelson Decker and Jennifer A. Townes, 582-624 (2016). doi:10.4018/978-1-4666-8624-3.ch025</value>
    utk_libpub/15/metadata.xml:53:<value>10.4018/978-1-4666-8624-3.ch025</value>
    utk_mtasdir/47/metadata.xml:3:<title>Directory of Tennessee Municipal Officials 1978-79</title>
    utk_mtasdir/47/metadata.xml:4:<publication-date>1978-01-01T00:00:00-08:00</publication-date>
    utk_mtasdir/47/metadata.xml:17:</disciplines><abstract>&lt;p&gt;A directory of Tennessee cities that includes personnel and municipal data, such as number of employees, population, charter form, size in square miles, and election date, for 1978-79.&lt;/p&gt;</abstract>
    utk_mtasdir/47/metadata.xml:36:<value>1978-01-01T00:00:00-08:00</value>
    utk_mtaspubs/13/metadata.xml:4:<publication-date>1978-03-01T00:00:00-08:00</publication-date>
    utk_mtaspubs/13/metadata.xml:31:<value>1978-03-01T00:00:00-08:00</value>
    utk_mtaspubs/14/metadata.xml:4:<publication-date>1978-07-01T00:00:00-07:00</publication-date>
    utk_mtaspubs/14/metadata.xml:34:<value>1978-07-01T00:00:00-07:00</value>
    utk_mtastech/261/metadata.xml:4:<publication-date>1978-04-05T00:00:00-08:00</publication-date>
    utk_mtastech/261/metadata.xml:37:<value>1978-04-05T00:00:00-08:00</value>
    utk_mtastech/262/metadata.xml:4:<publication-date>1978-03-06T00:00:00-08:00</publication-date>
    utk_mtastech/262/metadata.xml:35:<value>1978-03-06T00:00:00-08:00</value>
    utk_mtastech/263/metadata.xml:4:<publication-date>1978-02-24T00:00:00-08:00</publication-date>
    utk_mtastech/263/metadata.xml:36:<value>1978-02-24T00:00:00-08:00</value>
    utk_mtastech/264/metadata.xml:4:<publication-date>1978-02-17T00:00:00-08:00</publication-date>
    utk_mtastech/264/metadata.xml:37:<value>1978-02-17T00:00:00-08:00</value>
    utk_mtastech/265/metadata.xml:4:<publication-date>1978-01-10T00:00:00-08:00</publication-date>
    utk_mtastech/265/metadata.xml:38:<value>1978-01-10T00:00:00-08:00</value>
    utk_mtastech/266/metadata.xml:4:<publication-date>1978-01-05T00:00:00-08:00</publication-date>
    utk_mtastech/266/metadata.xml:39:<value>1978-01-05T00:00:00-08:00</value>
    utk_mtastech/267/metadata.xml:4:<publication-date>1978-11-13T00:00:00-08:00</publication-date>
    utk_mtastech/267/metadata.xml:37:<value>1978-11-13T00:00:00-08:00</value>
    utk_mtastech/268/metadata.xml:4:<publication-date>1978-11-01T00:00:00-08:00</publication-date>
    utk_mtastech/268/metadata.xml:35:<value>1978-11-01T00:00:00-08:00</value>
    utk_mtastech/269/metadata.xml:4:<publication-date>1978-10-16T00:00:00-07:00</publication-date>
    utk_mtastech/269/metadata.xml:37:<value>1978-10-16T00:00:00-07:00</value>
    utk_mtastech/270/metadata.xml:4:<publication-date>1978-08-17T00:00:00-07:00</publication-date>
    utk_mtastech/270/metadata.xml:38:<value>1978-08-17T00:00:00-07:00</value>
    utk_mtastech/271/metadata.xml:4:<publication-date>1978-06-27T00:00:00-07:00</publication-date>
    utk_mtastech/271/metadata.xml:37:<value>1978-06-27T00:00:00-07:00</value>
    utk_mtastech/272/metadata.xml:4:<publication-date>1978-06-23T00:00:00-07:00</publication-date>
    utk_mtastech/272/metadata.xml:39:<value>1978-06-23T00:00:00-07:00</value>
    utk_mtastech/273/metadata.xml:4:<publication-date>1978-06-15T00:00:00-07:00</publication-date>
    utk_mtastech/273/metadata.xml:37:<value>1978-06-15T00:00:00-07:00</value>
    utk_mtastech/274/metadata.xml:4:<publication-date>1978-05-15T00:00:00-07:00</publication-date>
    utk_mtastech/274/metadata.xml:38:<value>1978-05-15T00:00:00-07:00</value>
    utk_mtastech/275/metadata.xml:4:<publication-date>1978-04-20T00:00:00-08:00</publication-date>
    utk_mtastech/275/metadata.xml:39:<value>1978-04-20T00:00:00-08:00</value>
    utk_mtastech/276/metadata.xml:4:<publication-date>1978-04-10T00:00:00-08:00</publication-date>
    utk_mtastech/276/metadata.xml:36:<value>1978-04-10T00:00:00-08:00</value>
    utk_mtastech/277/metadata.xml:4:<publication-date>1978-04-07T00:00:00-08:00</publication-date>
    utk_mtastech/277/metadata.xml:37:<value>1978-04-07T00:00:00-08:00</value>
    utk_newfound-ebooks/10/metadata.xml:52:<value>978-0-9797292-1-8</value>
    utk_newfound-ebooks/11/metadata.xml:57:<value>978-0-9797292-4-9</value>
    utk_newfound-ebooks/12/metadata.xml:54:<value>978-0-9846445-0-6</value>
    utk_newfound-ebooks/13/metadata.xml:49:<value>978-0-9846445-1-3</value>
    utk_newfound-ebooks/14/metadata.xml:39:<value>978-0-9797292-9-4</value>
    utk_newfound-ebooks/16/metadata.xml:82:<value>978-0-9860803-109</value>
    utk_newfound-ebooks/17/metadata.xml:77:<value>978-0-9860803-3-3</value>
    utk_newfound-ebooks/18/metadata.xml:69:<value>978-0-9860803-5-7</value>
    utk_newfound-ebooks/1/metadata.xml:46:<value>978-0-9797292-8-7</value>
    utk_newfound-ebooks/2/metadata.xml:48:<value>978-0-9846445-5-1</value>
    utk_newfound-ebooks/3/metadata.xml:65:<value>978-0-9846445-9-9</value>
    utk_newfound-ebooks/5/metadata.xml:47:<value>978-0-9797292-7-0</value>
    utk_newfound-ebooks/6/metadata.xml:69:<value>978-0-9846445-8-2</value>
    utk_newfound-ebooks/7/metadata.xml:46:<value>978-0-9797292-2-5</value>
    utk_newfound-ebooks/8/metadata.xml:53:<value>978-0-9797292-6-3</value>
    utk_newfound-ebooks/9/metadata.xml:53:<value>978-0-9846445-7-5</value>
    utk_nurspubs/100/metadata.xml:29:</disciplines><abstract>&lt;p&gt;Although health is a key element in one&#39;s experience of middle adulthood as a time of productivity and personal fulfillment, research on psychosocial factors predictive of mid-life health is sparse, especially for women. Psychosocial variables are not only highly salient to health, but also are potentially modifiable by women themselves. This study employed a multivariate, multitheoretical approach to the study of health, examining a variety of psychosocial predictors (locus of control/mastery, psychological well-being, role quality, social network ties, optimism, and demographic variables) in a secondary analysis of data collected by Baruch and Barnett on 238 women. Subjects were divided into four groups: never married (N=50), married without children (N=54), married with children (N=88), and divorced with children (N=46) and were interviewed in their homes (Brookline, Massachusetts), 1978-79. It was found that 27% of the variance in self-reported health of mothers (whether married or divorced) was accounted for by stress, optimism, employment outside the home, occupational prestige, and quality of experience in the maternal role. Twenty-two percent of the variance in health of married women was explained by stress, quality of experience in the wife role, employment, and occupational prestige. A comparison of the healthiest and the least healthy women revealed that women in better health in middle adulthood had fewer concerns regarding their work, marital roles, and child-rearing roles as compared to their less healthy counterparts. Contains approximately 120 references.&lt;/p&gt;</abstract>
    utk_polk/14/metadata.xml:47:<value>978-1-62190-275-1</value>
    utk_polk/3/metadata.xml:57:<value>978-1-57233-952-1</value>
    utk_presrep/14/metadata.xml:3:<title>Annual Report of the President, the University of Tennessee to the Board of Trustees, 1978-1979:  Review and Preview</title>
    utk_presrep/15/metadata.xml:4:<publication-date>1978-06-15T00:00:00-07:00</publication-date>
    utk_presrep/15/metadata.xml:35:<value>1978-06-15T00:00:00-07:00</value>
    utk_sasproceed/1/metadata.xml:62:<value>978-0-9860803-0-2</value>
    utk_sasproceed/2/metadata.xml:68:<value>978-0-9846445-6-8</value>
    utk_sasproceed/3/metadata.xml:54:<value>978-0-9846445-4-4</value>
    utk_sasproceed/4/metadata.xml:50:<value>978-0-9846445-3-7</value>
    utk_sasproceed/5/metadata.xml:53:<value>978-0-9846445-2-0</value>
    utk_sasproceed/6/metadata.xml:55:<value>978-0-9860803-7-1</value>
    utk_sasproceed/7/metadata.xml:52:<value>978-0-9860803-9-5</value>
    utk_socopubs/38/metadata.xml:4:<publication-date>1978-09-01T00:00:00-07:00</publication-date>
    utk_socopubs/38/metadata.xml:46:<value>1978-09-01T00:00:00-07:00</value>
    utk_socopubs/55/metadata.xml:4:<publication-date>1978-01-01T00:00:00-08:00</publication-date>
    utk_socopubs/55/metadata.xml:41:<value>1978-01-01T00:00:00-08:00</value>
    utk_socstim/83/metadata.xml:4:<publication-date>1978-09-01T00:00:00-07:00</publication-date>
    utk_socstim/83/metadata.xml:27:<value>1978-09-01T00:00:00-07:00</value>
    utk_socstim/84/metadata.xml:4:<publication-date>1978-03-01T00:00:00-08:00</publication-date>
    utk_socstim/84/metadata.xml:27:<value>1978-03-01T00:00:00-08:00</value>
    utk_socstim/85/metadata.xml:4:<publication-date>1978-06-01T00:00:00-07:00</publication-date>
    utk_socstim/85/metadata.xml:27:<value>1978-06-01T00:00:00-07:00</value>
    utk_socstim/86/metadata.xml:4:<publication-date>1978-12-01T00:00:00-08:00</publication-date>
    utk_socstim/86/metadata.xml:27:<value>1978-12-01T00:00:00-08:00</value>
    utk_tome/1/metadata.xml:48:<value>978-0-8101-4213-8 ; 978-0-8101-4211-4 ; 978-0-8101-4212-1</value>
    utk_trustexh/380/metadata.xml:4:<publication-date>1978-02-24T00:00:00-08:00</publication-date>
    utk_trustexh/380/metadata.xml:29:<value>1978-02-24T00:00:00-08:00</value>
    utk_trustexh/381/metadata.xml:4:<publication-date>1978-05-31T00:00:00-07:00</publication-date>
    utk_trustexh/381/metadata.xml:29:<value>1978-05-31T00:00:00-07:00</value>
    utk_trustexh/382/metadata.xml:4:<publication-date>1978-06-14T00:00:00-07:00</publication-date>
    utk_trustexh/382/metadata.xml:29:<value>1978-06-14T00:00:00-07:00</value>
    utk_trustexh/383/metadata.xml:4:<publication-date>1978-06-15T00:00:00-07:00</publication-date>
    utk_trustexh/383/metadata.xml:29:<value>1978-06-15T00:00:00-07:00</value>
    utk_trustexh/384/metadata.xml:4:<publication-date>1978-08-02T00:00:00-07:00</publication-date>
    utk_trustexh/384/metadata.xml:29:<value>1978-08-02T00:00:00-07:00</value>
    utk_trustexh/385/metadata.xml:4:<publication-date>1978-08-31T00:00:00-07:00</publication-date>
    utk_trustexh/385/metadata.xml:29:<value>1978-08-31T00:00:00-07:00</value>
    utk_trustexh/386/metadata.xml:4:<publication-date>1978-10-20T00:00:00-07:00</publication-date>
    utk_trustexh/386/metadata.xml:29:<value>1978-10-20T00:00:00-07:00</value>
    utk_utpress/1/metadata.xml:44:<value>978-1-57233-617-9</value>
    utk_wommin/1/metadata.xml:4:<publication-date>1978-01-01T00:00:00-08:00</publication-date>
    utk_wommin/1/metadata.xml:30:<value>1978-01-01T00:00:00-08:00</value>
    utk_womrepor/4/metadata.xml:4:<publication-date>1978-01-01T00:00:00-08:00</publication-date>
    utk_womrepor/4/metadata.xml:30:<value>1978-01-01T00:00:00-08:00</value>

**Note**: not all Newfound Press collections have ISBNs.  Why?

.. code-block:: text

    utk_appalachian-echoes

Suggested Actions
-----------------

1. Only objects whose primary file type :code:`PDF` should be migrated as this work type.
2. We may need a cover page for these.
3. We will keep all associated supplemental files.