![](Aspose.Words.bef9e791-4ef2-43dc-ae9d-769f51fa1525.001.png)**INSPIRE**

**Infrastructure for Spatial Information in Europe**



**Technical Guidance for the implementation of INSPIRE dataset and service metadata based on ISO/TS 19139:2007**



|**Title** |Technical Guidelines for implementing dataset and service metadata based on ISO/TS 19139:2007|
| :- | :- |
|**Creator**|Temporary MIG subgroup for action MIWP-8|
|**Date of publication**|2017-08-31|
|**Subject**|Technical Guidance for INSPIRE metadata for datasets and services|
|**Status**|<p>Version 2.0.2</p><p>This document contains minor bug fixes (see release notes) of the version endorsed by the INSPIRE maintenance and implementation group (MIG) in its meeting on 30/11-1/12/2016 (see meeting minutes at <https://ies-svn.jrc.ec.europa.eu/projects/mig-p/wiki/5th_MIG-P_meeting>).</p>|
|**Publisher**|INSPIRE Maintenance and Implementation Group (MIG)|
|**Type**|Text|
|**Description**|Implementation specification for defining metadata for INSPIRE datasets and services in ISO/TS 19139 based XML format in compliance with the INSPIRE Implementing Rules for metadata.|
|**Format**|MS Word (doc)|
|**Licence**|Creative Commons Attribution (cc-by) 4.0 (<https://creativecommons.org/licenses/by/4.0/>)|
|**Identifier**|<p><http://inspire.ec.europa.eu/id/document/tg/metadata-iso19139/2.0> (latest bugfix version of v2.0)</p><p><http://inspire.ec.europa.eu/id/document/tg/metadata-iso19139/2.0.2> (this bugfix version)</p>|
|**Corrigenda**|<http://inspire.ec.europa.eu/id/document/tg/metadata-iso19139/2.0/corrigenda> |
|**Language**|EN|




|INSPIRE|Technical Guidelines for the implementation of INSPIRE dataset and service metadata based on ISO/TS 19139:2007|
| :- | :- |
|Version 2.0.2|2017-08-31|Page  PAGE V|

` `PAGE XXI

` `PAGE XXI

**Table of Contents**

` `**TOC \o "1-4" \h \z \u [Table of Contents	 PAGEREF _Toc476300502 \h II**](#_Toc476300502)**

[**Acknowledgements	 PAGEREF _Toc476300503 \h VI**](#_Toc476300503)

[**Foreword	 PAGEREF _Toc476300504 \h VII**](#_Toc476300504)

[**Foreword to this version	 PAGEREF _Toc476300505 \h IX**](#_Toc476300505)

[**Revision history	 PAGEREF _Toc476300506 \h XI**](#_Toc476300506)

[**Normative references	 PAGEREF _Toc476300507 \h XIV**](#_Toc476300507)

[**Other references	 PAGEREF _Toc476300508 \h XVI**](#_Toc476300508)

[**Terms and abbreviations	 PAGEREF _Toc476300509 \h XVII**](#_Toc476300509)

[**Verbal forms for expression of provisions	 PAGEREF _Toc476300510 \h XIX**](#_Toc476300510)

[**1**	**Overview	 PAGEREF _Toc476300511 \h 1**](#_Toc476300511)

[1.1	Introduction	 PAGEREF _Toc476300512 \h 1](#_Toc476300512)

[1.1.1	Roadmap and timelines for provisioning INSPIRE metadata	 PAGEREF _Toc476300513 \h 2](#_Toc476300513)

[1.1.2	Categories of INSPIRE Spatial Data Services	 PAGEREF _Toc476300514 \h 3](#_Toc476300514)

[1.2	XML Encoding of ISO metadata	 PAGEREF _Toc476300515 \h 4](#_Toc476300515)

[1.3	INSPIRE Validator Service	 PAGEREF _Toc476300516 \h 4](#_Toc476300516)

[1.4	Position and structure of this document	 PAGEREF _Toc476300517 \h 5](#_Toc476300517)

[1.4.1	TG Requirements, TG Recommendations and conformance	 PAGEREF _Toc476300518 \h 6](#_Toc476300518)

[**2**	**Common requirements for ISO/TC 19139:2007 based INSPIRE metadata records	 PAGEREF _Toc476300519 \h 7**](#_Toc476300519)

[2.1	Metadata structure and encoding	 PAGEREF _Toc476300520 \h 7](#_Toc476300520)

[2.1.1	Encoding of code list values	 PAGEREF _Toc476300521 \h 8](#_Toc476300521)

[2.1.2	Encoding of free text values	 PAGEREF _Toc476300522 \h 8](#_Toc476300522)

[2.2	General requirements	 PAGEREF _Toc476300523 \h 11](#_Toc476300523)

[2.2.1	File identifier	 PAGEREF _Toc476300524 \h 11](#_Toc476300524)

[2.2.2	Metadata language	 PAGEREF _Toc476300525 \h 11](#_Toc476300525)

[2.2.3	Metadata point of contact	 PAGEREF _Toc476300526 \h 12](#_Toc476300526)

[2.2.4	Metadata date	 PAGEREF _Toc476300527 \h 14](#_Toc476300527)

[2.3	Identification info section	 PAGEREF _Toc476300528 \h 14](#_Toc476300528)

[2.3.1	Resource title	 PAGEREF _Toc476300529 \h 14](#_Toc476300529)

[2.3.2	Resource abstract	 PAGEREF _Toc476300530 \h 15](#_Toc476300530)

[2.3.3	Responsible organisation and point of contact for the described resource	 PAGEREF _Toc476300531 \h 16](#_Toc476300531)

[2.3.4	Temporal references	 PAGEREF _Toc476300532 \h 17](#_Toc476300532)

[2.3.5	Using keywords	 PAGEREF _Toc476300533 \h 20](#_Toc476300533)

[2.3.6	Limitations on public access	 PAGEREF _Toc476300534 \h 23](#_Toc476300534)

[2.3.7	Conditions applying to access and use	 PAGEREF _Toc476300535 \h 25](#_Toc476300535)

[2.3.8	Geographic bounding box	 PAGEREF _Toc476300536 \h 27](#_Toc476300536)

[2.4	Data quality info section	 PAGEREF _Toc476300537 \h 29](#_Toc476300537)

[2.4.1	Conformity	 PAGEREF _Toc476300538 \h 29](#_Toc476300538)

[**3**	**Conformance Classes for data sets	 PAGEREF _Toc476300539 \h 33**](#_Toc476300539)

[3.1	Baseline metadata for data sets and data set series	 PAGEREF _Toc476300540 \h 33](#_Toc476300540)

[3.1.1	Direct properties of MD_Metadata element	 PAGEREF _Toc476300541 \h 33](#_Toc476300541)

[3.1.1.1	Resource type	 PAGEREF _Toc476300542 \h 33](#_Toc476300542)

[3.1.2	Identification info section	 PAGEREF _Toc476300543 \h 34](#_Toc476300543)

[3.1.2.1	Unique resource identifier	 PAGEREF _Toc476300544 \h 34](#_Toc476300544)

[3.1.2.2	Keywords for Spatial Data Theme(s)	 PAGEREF _Toc476300545 \h 37](#_Toc476300545)

[3.1.2.3	Spatial resolution	 PAGEREF _Toc476300546 \h 38](#_Toc476300546)

[3.1.2.4	Resource language	 PAGEREF _Toc476300547 \h 40](#_Toc476300547)

[3.1.2.5	Topic category	 PAGEREF _Toc476300548 \h 41](#_Toc476300548)

[3.1.3	Distribution info section	 PAGEREF _Toc476300549 \h 42](#_Toc476300549)

[3.1.3.1	Resource locator for data set or series	 PAGEREF _Toc476300550 \h 42](#_Toc476300550)

[3.1.4	Data quality info section	 PAGEREF _Toc476300551 \h 44](#_Toc476300551)

[3.1.4.1	Scope	 PAGEREF _Toc476300552 \h 44](#_Toc476300552)

[3.1.4.2	Conformity	 PAGEREF _Toc476300553 \h 44](#_Toc476300553)

[3.1.4.3	Lineage	 PAGEREF _Toc476300554 \h 46](#_Toc476300554)

[3.2	Interoperability metadata for data sets and data set series	 PAGEREF _Toc476300555 \h 48](#_Toc476300555)

[3.2.1	Direct properties of MD_Metadata element	 PAGEREF _Toc476300556 \h 48](#_Toc476300556)

[3.2.1.1	Coordinates reference systems	 PAGEREF _Toc476300557 \h 48](#_Toc476300557)

[3.2.1.2	Temporal reference systems	 PAGEREF _Toc476300558 \h 50](#_Toc476300558)

[3.2.2	Identification info section	 PAGEREF _Toc476300559 \h 51](#_Toc476300559)

[3.2.2.1	Spatial representation type	 PAGEREF _Toc476300560 \h 51](#_Toc476300560)

[3.2.2.2	Character encoding	 PAGEREF _Toc476300561 \h 52](#_Toc476300561)

[3.2.3	Distribution info section	 PAGEREF _Toc476300562 \h 53](#_Toc476300562)

[3.2.3.1	Data encoding	 PAGEREF _Toc476300563 \h 53](#_Toc476300563)

[3.2.4	Data quality info section	 PAGEREF _Toc476300564 \h 54](#_Toc476300564)

[3.2.4.1	Topological consistency	 PAGEREF _Toc476300565 \h 54](#_Toc476300565)

[3.2.5	Recommended theme-specific metadata elements	 PAGEREF _Toc476300566 \h 59](#_Toc476300566)

[**4**	**Conformance Classes for Spatial Data Services	 PAGEREF _Toc476300567 \h 60**](#_Toc476300567)

[4.1	Baseline metadata for Spatial Data Services	 PAGEREF _Toc476300568 \h 60](#_Toc476300568)

[4.1.1	Direct properties of MD_Metadata element	 PAGEREF _Toc476300569 \h 60](#_Toc476300569)

[4.1.1.1	Resource type	 PAGEREF _Toc476300570 \h 60](#_Toc476300570)

[4.1.2	Identification info section	 PAGEREF _Toc476300571 \h 61](#_Toc476300571)

[4.1.2.1	Restriction on the spatial resolution	 PAGEREF _Toc476300572 \h 61](#_Toc476300572)

[4.1.2.2	Spatial Data Service category keywords	 PAGEREF _Toc476300573 \h 62](#_Toc476300573)

[4.1.2.3	Spatial Data Service type	 PAGEREF _Toc476300574 \h 63](#_Toc476300574)

[4.1.2.4	Linking to provided data sets using coupled resource	 PAGEREF _Toc476300575 \h 64](#_Toc476300575)

[4.1.3	Distribution info section	 PAGEREF _Toc476300576 \h 66](#_Toc476300576)

[4.1.3.1	Resource locator for services	 PAGEREF _Toc476300577 \h 66](#_Toc476300577)

[4.1.4	Data quality info section	 PAGEREF _Toc476300578 \h 68](#_Toc476300578)

[4.1.4.1	Scope	 PAGEREF _Toc476300579 \h 68](#_Toc476300579)

[4.2	Metadata for Network Services	 PAGEREF _Toc476300580 \h 70](#_Toc476300580)

[4.2.1	Identification info section	 PAGEREF _Toc476300581 \h 70](#_Toc476300581)

[4.2.1.1	Spatial Data Service type	 PAGEREF _Toc476300582 \h 70](#_Toc476300582)

[4.2.2	Data quality info section	 PAGEREF _Toc476300583 \h 70](#_Toc476300583)

[4.2.2.1	Conformity	 PAGEREF _Toc476300584 \h 70](#_Toc476300584)

[4.3	Metadata for Invocable Spatial Data Services	 PAGEREF _Toc476300585 \h 73](#_Toc476300585)

[4.3.1	Identification info section	 PAGEREF _Toc476300586 \h 73](#_Toc476300586)

[4.3.1.1	Spatial Data Service type	 PAGEREF _Toc476300587 \h 73](#_Toc476300587)

[4.3.2	Distribution info section	 PAGEREF _Toc476300588 \h 73](#_Toc476300588)

[4.3.2.1	Resource locator	 PAGEREF _Toc476300589 \h 73](#_Toc476300589)

[4.3.3	Data quality info section	 PAGEREF _Toc476300590 \h 75](#_Toc476300590)

[4.3.3.1	Conformity to INSPIRE Implementation Rules	 PAGEREF _Toc476300591 \h 75](#_Toc476300591)

[4.3.3.2	Category of the Spatial Data Service	 PAGEREF _Toc476300592 \h 76](#_Toc476300592)

[4.3.3.3	Conformity to technical specifications	 PAGEREF _Toc476300593 \h 78](#_Toc476300593)

[4.4	Metadata for Interoperable Spatial Data Services	 PAGEREF _Toc476300594 \h 81](#_Toc476300594)

[4.4.1	Direct properties of MD_Metadata element	 PAGEREF _Toc476300595 \h 81](#_Toc476300595)

[4.4.1.1	Coordinate Reference System Identifier	 PAGEREF _Toc476300596 \h 81](#_Toc476300596)

[4.4.2	Identification info section	 PAGEREF _Toc476300597 \h 82](#_Toc476300597)

[4.4.2.1	Conditions applying to access and use – technical restrictions	 PAGEREF _Toc476300598 \h 82](#_Toc476300598)

[4.4.2.2	Responsible party – custodian	 PAGEREF _Toc476300599 \h 82](#_Toc476300599)

[4.4.3	Data quality info section	 PAGEREF _Toc476300600 \h 83](#_Toc476300600)

[4.4.3.1	Minimum estimated Quality of Service	 PAGEREF _Toc476300601 \h 83](#_Toc476300601)

[4.5	Metadata for Harmonised Spatial Data Services	 PAGEREF _Toc476300602 \h 86](#_Toc476300602)

[4.5.1	Identification info section	 PAGEREF _Toc476300603 \h 86](#_Toc476300603)

[4.5.1.1	Invocation metadata	 PAGEREF _Toc476300604 \h 86](#_Toc476300604)

[**Annex A**	**Abstract Test Suites	 PAGEREF _Toc476300605 \h 89**](#_Toc476300605)

[A.1	ATS: Metadata for INSPIRE datasets and data set series	 PAGEREF _Toc476300606 \h 89](#_Toc476300606)

[A.1.1	Conformance Class 1: Baseline metadata for data sets and data set series	 PAGEREF _Toc476300607 \h 89](#_Toc476300607)

[A.1.2	Conformance Class 2: Interoperability metadata for data sets and data set series	 PAGEREF _Toc476300608 \h 89](#_Toc476300608)

[A.2	ATS: Metadata for INSPIRE Spatial Data Services	 PAGEREF _Toc476300609 \h 89](#_Toc476300609)

[A.2.1	Conformance Class 3: Baseline metadata for Spatial Data Services	 PAGEREF _Toc476300610 \h 89](#_Toc476300610)

[A.2.2	Conformance Class 4: Metadata for INSPIRE Network Services	 PAGEREF _Toc476300611 \h 89](#_Toc476300611)

[A.2.3	Conformance Class 5: Metadata for Invocable Spatial Data Services	 PAGEREF _Toc476300612 \h 89](#_Toc476300612)

[A.2.4	Conformance Class 6: Metadata for Interoperable Spatial Data Services	 PAGEREF _Toc476300613 \h 89](#_Toc476300613)

[A.2.5	Conformance Class 7: Metadata for Harmonised Spatial Data Services	 PAGEREF _Toc476300614 \h 90](#_Toc476300614)

[**Annex B**	**Mapping of ISO 19115:2003 Core elements and INSPIRE Implementing Rules for metadata (informative)	 PAGEREF _Toc476300615 \h 91**](#_Toc476300615)

[B.1	Spatial dataset and spatial dataset series	 PAGEREF _Toc476300616 \h 91](#_Toc476300616)

[B.2	Services	 PAGEREF _Toc476300617 \h 92](#_Toc476300617)

[B.3	Conclusion	 PAGEREF _Toc476300618 \h 94](#_Toc476300618)

[**Annex C**	**INSPIRE metadata element catalog (informative)	 PAGEREF _Toc476300619 \h 95**](#_Toc476300619)

[C.1	Overview of the required INSPIRE metadata elements	 PAGEREF _Toc476300620 \h 96](#_Toc476300620)

[C.1.1	Spatial data sets and data sets series	 PAGEREF _Toc476300621 \h 96](#_Toc476300621)

[C.1.2	Spatial Data Services	 PAGEREF _Toc476300622 \h 98](#_Toc476300622)

[C.2	INSPIRE Implementing Rules for metadata (regulation 1205/2008)	 PAGEREF _Toc476300623 \h 102](#_Toc476300623)

[C.2.1	Resource title	 PAGEREF _Toc476300624 \h 102](#_Toc476300624)

[C.2.2	Resource abstract	 PAGEREF _Toc476300625 \h 102](#_Toc476300625)

[C.2.3	Resource type	 PAGEREF _Toc476300626 \h 103](#_Toc476300626)

[C.2.4	Resource locator	 PAGEREF _Toc476300627 \h 103](#_Toc476300627)

[C.2.5	Unique resource identifier	 PAGEREF _Toc476300628 \h 104](#_Toc476300628)

[C.2.6	Coupled resource	 PAGEREF _Toc476300629 \h 105](#_Toc476300629)

[C.2.7	Resource language	 PAGEREF _Toc476300630 \h 106](#_Toc476300630)

[C.2.8	Topic category	 PAGEREF _Toc476300631 \h 106](#_Toc476300631)

[C.2.9	Spatial data service type	 PAGEREF _Toc476300632 \h 107](#_Toc476300632)

[C.2.10	Keyword value	 PAGEREF _Toc476300633 \h 107](#_Toc476300633)

[C.2.11	Originating controlled vocabulary	 PAGEREF _Toc476300634 \h 108](#_Toc476300634)

[C.2.12	Geographic bounding box	 PAGEREF _Toc476300635 \h 109](#_Toc476300635)

[C.2.13	Temporal extent	 PAGEREF _Toc476300636 \h 110](#_Toc476300636)

[C.2.14	Date of publication	 PAGEREF _Toc476300637 \h 110](#_Toc476300637)

[C.2.15	Date of last revision	 PAGEREF _Toc476300638 \h 111](#_Toc476300638)

[C.2.16	Date of creation	 PAGEREF _Toc476300639 \h 111](#_Toc476300639)

[C.2.17	Lineage	 PAGEREF _Toc476300640 \h 112](#_Toc476300640)

[C.2.18	Spatial resolution	 PAGEREF _Toc476300641 \h 112](#_Toc476300641)

[C.2.19	Specification	 PAGEREF _Toc476300642 \h 113](#_Toc476300642)

[C.2.20	Degree	 PAGEREF _Toc476300643 \h 114](#_Toc476300643)

[C.2.21	Conditions applying to access and use	 PAGEREF _Toc476300644 \h 114](#_Toc476300644)

[C.2.22	Limitations on public access	 PAGEREF _Toc476300645 \h 117](#_Toc476300645)

[C.2.23	Responsible party	 PAGEREF _Toc476300646 \h 117](#_Toc476300646)

[C.2.24	Responsible party role	 PAGEREF _Toc476300647 \h 118](#_Toc476300647)

[C.2.25	Metadata point of contact	 PAGEREF _Toc476300648 \h 118](#_Toc476300648)

[C.2.26	Metadata date	 PAGEREF _Toc476300649 \h 119](#_Toc476300649)

[C.2.27	Metadata language	 PAGEREF _Toc476300650 \h 119](#_Toc476300650)

[C.3	Implementing Rules for interoperability of spatial data sets and services (regulations 1089/2010 and 1253/2013)	 PAGEREF _Toc476300651 \h 120](#_Toc476300651)

[C.3.1	Coordinate Reference System	 PAGEREF _Toc476300652 \h 120](#_Toc476300652)

[C.3.2	Temporal Reference System	 PAGEREF _Toc476300653 \h 121](#_Toc476300653)

[C.3.3	Encoding	 PAGEREF _Toc476300654 \h 122](#_Toc476300654)

[C.3.4	Character Encoding	 PAGEREF _Toc476300655 \h 122](#_Toc476300655)

[C.3.5	Spatial representation type	 PAGEREF _Toc476300656 \h 123](#_Toc476300656)

[C.3.6	Topological Consistency	 PAGEREF _Toc476300657 \h 123](#_Toc476300657)

[C.4	Implementing Rules for Invocable Spatial Data Services (Regulation 1312/2014, Annex I)	 PAGEREF _Toc476300658 \h 125](#_Toc476300658)

[C.4.1	Category	 PAGEREF _Toc476300659 \h 125](#_Toc476300659)

[C.4.2	Resource locator	 PAGEREF _Toc476300660 \h 126](#_Toc476300660)

[C.4.3	Specification	 PAGEREF _Toc476300661 \h 127](#_Toc476300661)

[C.5	Implementing Rules for Interoperable Spatial Data Services (Regulation 1312/2014, Annex II)	 PAGEREF _Toc476300662 \h 128](#_Toc476300662)

[C.5.1	Coordinate Reference System	 PAGEREF _Toc476300663 \h 128](#_Toc476300663)

[C.5.2	Criteria	 PAGEREF _Toc476300664 \h 129](#_Toc476300664)

[C.5.3	Measurement	 PAGEREF _Toc476300665 \h 129](#_Toc476300665)

[C.6	Implementing Rules for Harmonised Spatial Data Services (Regulation 1312/2014, Annex III)	 PAGEREF _Toc476300666 \h 130](#_Toc476300666)

[C.6.1	Invocation metadata	 PAGEREF _Toc476300667 \h 130](#_Toc476300667)

[C.7	Theme-specific metadata elements from INSPIRE Data Specifications	 PAGEREF _Toc476300668 \h 131](#_Toc476300668)

[C.7.1	Maintenance information	 PAGEREF _Toc476300669 \h 136](#_Toc476300669)

[C.7.2	Spatial representation information	 PAGEREF _Toc476300670 \h 136](#_Toc476300670)

[C.7.3	Supplemental information	 PAGEREF _Toc476300671 \h 137](#_Toc476300671)

[C.7.4	Process step	 PAGEREF _Toc476300672 \h 137](#_Toc476300672)

[C.7.5	Data source	 PAGEREF _Toc476300673 \h 139](#_Toc476300673)

[C.7.6	Browse graphic information	 PAGEREF _Toc476300674 \h 140](#_Toc476300674)

[C.7.7	Image description	 PAGEREF _Toc476300675 \h 140](#_Toc476300675)

[C.7.8	Content information	 PAGEREF _Toc476300676 \h 141](#_Toc476300676)

[C.7.9	Digital transfer options information	 PAGEREF _Toc476300677 \h 142](#_Toc476300677)

[C.7.10	Extent	 PAGEREF _Toc476300678 \h 142](#_Toc476300678)

[C.7.11	Data Quality	 PAGEREF _Toc476300679 \h 143](#_Toc476300679)

[**Annex D**	**Referenced code lists and code list values	 PAGEREF _Toc476300680 \h 145**](#_Toc476300680)

[D.1	Limitations on public access	 PAGEREF _Toc476300681 \h 145](#_Toc476300681)

[D.2	Conditions Applying To Access And Use	 PAGEREF _Toc476300682 \h 146](#_Toc476300682)

[D.3	Quality of Service criteria code	 PAGEREF _Toc476300683 \h 146](#_Toc476300683)

[D.4	Default Coordinate Reference Systems	 PAGEREF _Toc476300684 \h 147](#_Toc476300684)

[**Annex E**	**Mapping between IR element numbers and TG Requirements	 PAGEREF _Toc476300685 \h 150**](#_Toc476300685)

[**Annex F**	**Mapping for Requirements in previous TG versions	 PAGEREF _Toc476300686 \h 153**](#_Toc476300686)

[**Annex G**	**Examples of complete INSPIRE metadata records	 PAGEREF _Toc476300687 \h 157**](#_Toc476300687)





**Acknowledgements**

Many individuals and organisations have contributed to the development of these Guidelines.

The original INSPIRE Drafting Team on Metadata (2006-08) included: Marcel Reuvers (Netherlands), Nicolas Lesage (France), Kristian Senkler (Germany), Michael Gould (Spain), Gil Ross (UK), Stefano Nativi (Italy), Jan Hjelmager (Denmark), Franz Daffner (European Environment Agency), Per Ryghaud (Norway), Thomas Vögele and Fred Kruse (Germany), David Danko (USA).

This version 2.0 is an extensive revision of the previous version 1.3 both in structure and content based on the work of the INSPIRE Maintenance and Implementation Group (MIG) subgroup for the Work Package 8: Metadata (MIWP-8). The editing work including restructuring of the text into Conformance Class chapters and TG Requirement text revisions for added XML element level precision was done by Ilkka Rinne of Spatineo Inc under contract for the European Commission Joint Research Centre (JRC) in January - April 2016.

We wish to thank the members of the MIWP-8 group as well as Michael Lutz, Angelo Quaglia and Freddy Fierens of the JRC for the thorough groundwork, insightful feedback and contributions to document during the editing work.The MIWP-8 group was chaired by Michael Östling (Sweden), and included the following members (in alphabetical order): Christian Ansorge (EEA), Lars Inge Arnevik (Norway), Vincent Bombaerts (Belgium), Pierluigi Cara (Italy), Radoslav Chudý (Czech Republic), Ine de Visser (Netherlands), Daniele Francioli (JRC), Christine Gassner (Austria), Alejandro Guinea de Salas (Spain), Paul Hasenohr (EEA), Željko Hecimovic (Croatia), Frédéric Houbie (France), Lucie Kondrova (Czech Republic), Peter Kochmann (Germany), Marc Léobet (France), Marie Lambois (France), Darja Lihteneger (EEA), Manfred Mittelboeck, (Austria), Javier Nogueras Iso (Spain), Geraldine Nolf (Belgium), Andrea Perego (JRC),  Tomas Reznik (Czech Republic), James Reid (UK), Eliane Roos (France), Antonio Rotundo, (Italy), Martin Seiler (Germany), Kristian Senkler (Germany),  André Schneider (Switzerland),  Age Sild (Estonia), and Pawel Soczewski (Poland).


**Contact information**

European Commission Joint Research Centre

B.6 Digital Economy 

<https://inspire.ec.europa.eu/feedback>  




**Foreword**

Directive 2007/2/EC of the European Parliament and of the Council [INS DIR], adopted on 14 March 2007 aims at establishing an Infrastructure for Spatial Information in the European Community (INSPIRE) for environmental policies, or policies and activities that have an impact on the environment. INSPIRE will make available relevant, harmonised and quality geographic information to support the formulation, implementation, monitoring and evaluation of policies and activities, which have a direct or indirect impact on the environment.

INSPIRE is based on the infrastructures for spatial information established and operated by the 28 Member States of the European Union. The Directive addresses 34 spatial data themes needed for environmental applications, with key components specified through technical implementing rules. This makes INSPIRE a unique example of a legislative “regional” approach.

To ensure that the spatial data infrastructures of the Member States are compatible and usable in a Community and trans-boundary context, the Directive requires that common Implementing Rules (IR) are adopted in the following areas. 

- Metadata; 
- The interoperability and harmonisation of spatial data and services for selected themes (as described in Annexes I, II, III of the Directive); 
- Network Services; 
- Measures on sharing spatial data and services; 
- Co-ordination and monitoring measures. 

The Implementing Rules are adopted as Commission Decisions or Regulations, and are legally binding. 

In addition to the Implementing Rules, non-binding Technical Guidance documents describe detailed implementation aspects and relations with existing standards, technologies and practices in order to support the technical implementation process. They may need to be revised during the course of implementing the infrastructure to take into account the evolution of technology, new requirements, and cost benefit considerations. In other words, these Technical Guidance documents are supporting material to assist in the technical implementation of the INSPIRE Directive but no additional obligations can be derived from these documents over and above the obligations set out in the Directive and the Implementing Rules. The Technical Guidance documents are also not intended to interpret legal obligations. Figure 1 illustrates the relationship between the INSPIRE Regulations containing Implementing Rules and their corresponding Technical Guidance documents.

This Technical Guidance document relates to the implementation of the requirements related to metadata for spatial data sets and series and spatial data services (including network services) included in [Regulation 1205/2008] and [Regulation 1089/2010]. 

Implementing this Technical Guidance are designed to maximise the interoperability of INSPIRE services. Technical Guidance documents describe how Member States might implement the Implementing Rules described in a Commission Regulation. The technical provisions and the underlying concepts are often illustrated by use case diagrams and accompanied by examples. Technical Guidance documents may also include non-binding technical recommendations that should be satisfied if a Member State chooses to conform to the Technical Guidance. However, these recommendations have no legally binding effect.

![TG vs IR](Aspose.Words.bef9e791-4ef2-43dc-ae9d-769f51fa1525.003.png)

***Figure  SEQ Figure \\* ARABIC 1:** Relationship between the INSPIRE Implementing Rules and the associated Technical Guidance.*


|<p>**Disclaimer**</p><p>This document has been developed collaboratively through the INSPIRE maintenance and implementation framework, involving experts of the European Commission services, the European Environment Agency, EU Member States, the Accession and EFTA Countries. The document should be regarded as presenting an informal consensus position on best practice agreed by all partners. However, the document does not necessarily represent the official, formal position of any of the partners. To the extent that the European Commission's services provided input to this technical document, such input does not necessarily reflect the views of the European Commission and its services. This document does not bind the Commission and its services, nor can the Commission and its services be held responsible for any use which may be made of the information contained herein.</p><p></p><p>The technical document is intended to facilitate the implementation of Directive 2007/2/EC and is not legally binding. Any authoritative reading of the law should only be derived from Directive 2007/2/EC itself and other applicable legal texts or principles such as the related Implementing Rules. Only the Court of Justice of the European Union is competent to authoritatively interpret Union legislation.</p>|
| :- |
**Foreword to this version**

The previous version 1.3 of this Technical Guidelines document has been widely used since its publication in 2013. It has led to a lot of feedback concerning unclear TG Requirements and implementation choices, which this version aims to answer and clarify. This work has been done under INSPIRE Maintenance and Implementation Group (MIG) temporary sub-group for work package 8 (MIWP-8: Metadata). According to its terms of reference[` `Terms of Reference for the MIWP-8 group: <https://ies-svn.jrc.ec.europa.eu/attachments/download/780/Inspire%20MIG%20ToR%20Update%20TG%20Metadata%20final.pdf> 
], this new version of the TG document addresses the following issues:

- Integrate metadata for Spatial Data Services
- Integrate metadata for interoperability 
- Integrate theme-specific metadata 
- Language neutral identifiers – more use of Anchors
- Review and possibly revise guidelines for implementing the *Unique Resource Identifier* element
- Review and possibly revise guidelines for implementing “data-service-coupling” (coupled resources)
- Guidelines for implementing the element *conditions applying to access and use* are not in line with EN ISO 19115:2005.

Possible future work related to metadata (in relation also to other actions in the MIWP 2016-2020) not necessarily involving an update of these guidelines:

- Harmonized restrictions/licenses
- Relation to ISO19115-1:2014
- References to conformance classes in registry (see action 2016.3)
- Using metadata for INSPIRE monitoring and reporting (see action 2016.2)
- Add Abstract Test suite (see action 2016.3)
- Revising the XPaths used in the document to be less restrictive, so that they also match the corresponding elements in all profiles conformant with [ISO 19139]

Another important driver for this revision has been the activities of the group MIWP-5: Validation & conformity testing concerning the Conformance Classes and Abstract Test Suites for the INSPIRE metadata. Several issues concerning the testability and interpretation of technical requirements of the Implementation Rules for metadata expressed in version 1.3 of this document were raised during the drafting of the Test Cases for INSPIRE metadata.

This new version aims at clarifying and expressing technical requirements for INSPIRE metadata, improving the readability of the document, and combining the metadata related technical requirements for INSPIRE data sets, data set series and Spatial Data Services in one document. The technical requirements have been organised into Conformance Classes based on both the type of the described resources (data sets & services) and the different INSPIRE Regulations containing the legal requirements for providing INSPIRE metadata.

In the versions 1.0 - 1.3 of this document the definition of a formal INSPIRE profile of ISO 19115 combined with elements from ISO 19119 formed the basis of the presented technical requirements. The ISO 19115 Core element set was extended with INSPIRE specific constraints and extensions. The mapping from the ISO 19115/19119 elements into XML elements according to ISO/TS 19139 was then implicitly given in the text of the technical requirements and the mapping tables for each of the required metadata element described in the INSPIRE Implementing Rule documents. This hybrid approach of presenting the INSPIRE requirements as an abstract ISO 19115 profile while at the same time stating explicit XML element level requirements in the technical requirements, led to some confusion to what is actually required by the technical specification.



The technical requirements in this version of the specification are presented within the context of the corresponding INSPIRE Regulations, and expressed by mentioning the required XML elements and attributes explicitly. Thus the document aims to provide a clear guidance on how to use the ISO 19139 XML Schemas combined with the XML Schema implementation of ISO 19119 as published by the Open Geospatial Consortium (OGC) for providing all the required metadata elements of the relevant INSPIRE Regulations in an XML format. This clarification in the level of abstraction of the technical requirements was carried out to emphasise that the XML encoding of the metadata based on ISO 19139 standard is required in order to be compliant with this technical specification.

Special care has been taken to not make any unnecessary changes in the required metadata elements in between the version 1.3 and 2.0. The goal has been to only clarify the existing requirements in cases where more than one interpretation of the Implementation Rules existed, or where the required XML encoding was unclear or ambiguous. Some harmonisation between the XML encodings of the elements required by different INSPIRE Regulations has also been done to make the work of the metadata providers and INSPIRE metadata handling software providers easier. 

***Reading guidance and transition period***

As the structure of the document and the expressions have changed considerably from the previous version of the document, the following sections have been included to help the readers in locating the specific elements and technical requirements in this version of the document:

- The informative  REF \_Ref465954085 \n \h Annex B contains the mapping between the ISO 19115:2003 Core elements and INSPIRE Implementing Rules for metadata in section 1.1 of version 1.3.
- The informative  REF \_Ref465954104 \n \h Annex C contains detailed tables for all the INSPIRE metadata elements described in the INSPIRE Regulations for discovery and interoperability metadata.  The first section of this annex contains on overview table for these elements with the Regulation references and required INSPIRE multiplicities and conditions of each element.
- ` `REF \_Ref465954119 \n \h Annex D contains a listing of the code lists referenced in this document including the URI’s of the code lists and their current content.
- ` `REF \_Ref465954126 \n \h Annex E contains a mapping table between the Implementation Rule sections containing the required metadata elements and the TG Requirements as expressed in the indicated sections in this document.
- ` `REF \_Ref465954133 \n \h Annex F contains a mapping table between the TG Requirements contained in the version 1.3 and the corresponding TG Requirements in this document. This table also contains the mapping between the Implementation Requirements and Recommendations contained in [TG SDS] and the TG Requirements and Recommendations concerning Spatial Data Services in this document.

As many Member States have already implemented the previous version of the Technical Guidance for metadata, the transition between version 1.3 and 2.0 will require some developments. It is especially true for elements where it has been necessary to modify or clarify the structure or content of the required XML elements. The metadata handling and validating tools created to comply with the Technical Guidance version 1.3 may need updating to fully comply with this version.

To facilitate a smooth transition from version 1.3 to version 2.0, a transitional period of 3 years has been defined, starting from 19 December 2016. During this period, the metadata records compliant with both version 1.3 and 2.0 implementations will be considered as “compliant with the INSPIRE Technical Guidelines for Metadata”. During the transitional period, the validator used in the INSPIRE geoportal will validate against and will provide validation reports for both versions 1.3 and 2.0. The better result will be used for the value of the compliance meter. After the transitional period, the geoportal will only validate against version 2.0.

**Revision history**

***Changes from the version 1.3 to 2.0***

Due to the extensiveness of the structural changes and revision of the textual content for this version, the following list only includes changes directly affecting the TG Requirements and Recommendations.

**Requirements/recommendations removed (compared to version 1.3):**

- Section 1.2 INSPIRE specific constraints (SC) has been removed. The restrictions have been integrated into the relevant TG Requirements in the document.
- TG Recommendation 6 has been removed.
- TG Recommendations 7 and 8 have been removed.
- TG Requirement 6 concerning the use of RS\_Identifier has been removed.
- TG Requirement 11 has been removed as redundant due to the required values being specified as an enumeration in the XML Schema.
- TG Recommendation 13 concerning using both code and human-readable keywords has been removed.

**New requirements/recommendations in version 2.0:**

- A new  *REF req\_common\_xml\_schema \h  \\* MERGEFORMAT TG Requirement C.1* has been added to explicitly require using one of the listed XML Schemas for encoding the [ISO 19115] and [ISO 19119] metadata elements.
- A new  *REF req\_common\_root\_element \h  \\* MERGEFORMAT TG Requirement C.2* has been added to require the use of MD\_Metadata as the parent element for the metadata records.
- A new  *REF req\_common\_code\_list\_values \h  \\* MERGEFORMAT TG Requirement C.3* has been added to specify encoding the code list values.
- A new  *REF req\_common\_free\_text \h  \\* MERGEFORMAT TG Requirement C.4* has been added to specify encoding the Non-empty Free Text Elements.
- New  *REF rec\_data\_resource\_locator\_additional\_inf \h  \\* MERGEFORMAT TG Recommendation 1.8* and  *REF rec\_sds\_resource\_locator\_additional\_info \h  \\* MERGEFORMAT TG Recommendation 3.4* have been added to recommend the use on name, description and function properties of CI\_OnlineResource element in providing the Resource locator element.
- A new  *REF rec\_data\_resolvable\_uids \h  \\* MERGEFORMAT TG Recommendation 1.2* for using resolvable URIs for the data set identification has been added.
- A new  *REF req\_common\_max\_1\_date\_last\_revision \h  \\* MERGEFORMAT TG Requirement C.13* was added to explicitly require that at most one date of last revision is given.
- A new  *REF req\_common\_temporal\_extent \h  \\* MERGEFORMAT TG Requirement C.14* was added to require the XML encoding of the temporal extent, if given.
- New  *REF req\_data\_one\_dq\_element \h  \\* MERGEFORMAT TG Requirement 1.9* and  *REF req\_sds\_one\_dq\_element \h  \\* MERGEFORMAT TG Requirement 3.8* have been created to cover the INSPIRE specific constraint SC6 concerning declaring the scope of the *dataQualityInfo*.
- A new  *REF req\_common\_md\_date \h  \\* MERGEFORMAT TG Requirement C.7* has been added to explicitly require the Metadata date element described in section 2.11.2 of the version 1.3.
- New  *REF req\_isdss\_crs \h  \\* MERGEFORMAT TG Requirement 2.1* and  *REF req\_isdss\_crs\_id \h  \\* MERGEFORMAT TG Requirement 2.2* were added for requiring describing the Coordinate Reference System (interoperability metadata).
- A new  *REF req\_isdss\_temporal\_rs \h  \\* MERGEFORMAT TG Requirement 2.3* was added for requiring describing the Temporal reference systems (interoperability metadata).
- A new  *REF req\_isdss\_spatial\_representation\_type \h  \\* MERGEFORMAT TG Requirement 2.4* was added for requiring describing the Spatial representation type (interoperability metadata).
- A new  *REF req\_isdss\_character\_encoding \h  \\* MERGEFORMAT TG Requirement 2.5* was added for requiring describing the Character encoding (interoperability metadata).
- A new  *REF req\_isdss\_data\_encoding \h  \\* MERGEFORMAT TG Requirement 2.6* was added for requiring describing the Data encoding (interoperability metadata).
- New  *REF req\_isdss\_topo\_consistency\_quantitative \h  \\* MERGEFORMAT TG Requirement 2.7* and  *REF req\_isdss\_topo\_consistency\_descriptive \h  \\* MERGEFORMAT TG Requirement 2.8* were added for requiring describing the topological consistency (interoperability metadata).
- A new  *REF req\_sds\_service\_identification\_element \h  \\* MERGEFORMAT TG Requirement 3.2* was added to explicitly require *srv:SV\_ServiceIdentification* element to be used for identifying Spatial Data Services.
- A new  *REF req\_sds\_spatial\_resolution \h  \\* MERGEFORMAT TG Requirement 3.3* was added to require describing restrictions on spatial resolution for Spatial Data Services within the abstract element.

**Changed requirements/recommendations:**

- Providing a non-empty Resource title element (section 2.2.1) is now explicitly required in  *REF req\_common\_title \h  \\* MERGEFORMAT TG Requirement C.8*.
- Providing a non-empty Resource abstract element (section 2.2.2) is now explicitly required in  *REF req\_common\_abstract \h  \\* MERGEFORMAT TG Requirement C.9*.

**Renumbered, moved, combined requirements/recommendations:**

- Section 1.1 ISO Core Metadata Elements has been moved into  REF \_Ref465954081 \n \h Annex B.
- TG Requirement 3 concerning the Resource locator element for data sets and dataset series is now the  *REF req\_data\_resource\_locator \h  \\* MERGEFORMAT TG Requirement 1.8.* This requirement also now contains explicit XML element required.
- TG Requirement 4 concerning the Resource locator element for Services is now the  *REF req\_sds\_resource\_locator \h  \\* MERGEFORMAT TG Requirement 3.7*. This requirement also now contains explicit XML element required. The list of the possible resource types the provided URL should point to has been moved into  *REF rec\_sds\_resource\_type\_url\_target \h  \\* MERGEFORMAT TG Recommendation 3.5*.
- TG Requirement 5 concerning the Unique Resource Identifier for data sets and data set series is now the  *REF req\_data\_dataset\_uid \h  \\* MERGEFORMAT TG Requirement 1.3*. The IR Requirement for providing both the code and the code space has been interpreted as integrated parts of a single URI character string.
- TG Recommendation 9 about deleting the Unique Resource Identifiers has been clarified as  *REF rec\_data\_persistent\_uid \h  \\* MERGEFORMAT TG Recommendation 1.3*.
- TG Recommendations 3, 4 and 5 have been combined as  *REF rec\_common\_abstract \h  \\* MERGEFORMAT TG Recommendation C.4*.
- The *hierachyLevel* element required in TG Requirements 1 and 2 is now stated in  *REF req\_data\_resource\_type \h  \\* MERGEFORMAT TG Requirement 1.1* (for data sets and data set series) and  *REF req\_sds\_resource\_type \h  \\* MERGEFORMAT TG Requirement 3.1* (for Spatial Data Services)
- The content of the TG Requirement 7 concerning Coupled resource for services has been clarified and is now the  *REF req\_sds\_sds\_coupled\_resource \h  \\* MERGEFORMAT TG Requirement 3.6*.
- The TG Requirements 8 and 9 concerning Resource language are now combined in  *REF req\_data\_resource\_language \h  \\* MERGEFORMAT TG Requirement 1.6*.
- The TG Recommendation 10 about the default value for Resource language has now been integrated in  REF req\_data\_resource\_language \h  \\* MERGEFORMAT *TG Requirement 1.6*. For data sets and series containing non-textual information only, the ISO 639-2/B value "zxx" is now required instead of the previous recommendation for using the metadata language.
- TG Requirement 10 concerning Topic category is now the  *REF req\_data\_topic\_category \h  \\* MERGEFORMAT TG Requirement 1.7.*
- TG Requirement 12 concerning the Spatial data service type is now stated as  *REF req\_sds\_sds\_type \h  \\* MERGEFORMAT TG Requirement 3.5*,  *REF req\_ns\_sds\_type \h  \\* MERGEFORMAT TG Requirement 4.1* (Network services) and  *REF req\_sds\_invocable\_sds\_type \h  \\* MERGEFORMAT TG Requirement 5.1* (Invocable Spatial Data Services).
- TG Requirements 13, 14 and 15 concerning using at least one keyword are now stated as  *REF req\_data\_theme\_keyword \h  \\* MERGEFORMAT TG Requirement 1.4* (for data sets and data set series) and  *REF req\_sds\_sds\_category \h  \\* MERGEFORMAT TG Requirement 3.4* (for Spatial Data Services).
- TG Requirement 16 concerning keywords from controlled vocabularies is now integrated into  *REF req\_common\_keyword\_originating\_cv \h  \\* MERGEFORMAT TG Requirement C.15*.
- TG Recommendation 11 has been reworded into  *REF rec\_common\_use\_cvs \h  \\* MERGEFORMAT TG Recommendation C.7*.
- TG Recommendation 12 has been split into  *REF rec\_data\_additional\_keywords \h  \\* MERGEFORMAT TG Recommendation 1.5* (for data sets and data set series) and  *REF rec\_sds\_additional\_keywords \h  \\* MERGEFORMAT TG Recommendation 3.3* (for Spatial Data Services). 
- TG Requirements 17 and 18 concerning Originating controlled vocabularies of keywords are now combined in  *REF req\_common\_keyword\_originating\_cv \h  \\* MERGEFORMAT TG Requirement C.15*.
- TG Requirement 19 concerning grouping of the keywords referring to the same controlled vocabulary is now stated as the  *REF req\_common\_group\_keywords\_by\_cv \h  \\* MERGEFORMAT TG Requirement C.16*.
- TG Requirements 20 and 21 concerning the Geographic bounding box are now combined into  *REF req\_common\_bounding\_box \h  \\* MERGEFORMAT TG Requirement C.19*. The INSPIRE specific constraint SC13 for specifying the use of any coordinate reference system with Greenwich Prime Meridian has been removed, as the ISO 19139 XML Schema explicitly requires the use in WGS 84 coordinate reference system coordinates in the EX\_GeographicBoundingBox element.
- The TG Requirements 22, 23 and 24 concerning Temporal references have been combined in  *REF req\_common\_temporal\_reference \h  \\* MERGEFORMAT TG Requirement C.11*.
- The TG Requirement 25 has been rephrased as  *REF req\_common\_max\_1\_date\_creation \h  \\* MERGEFORMAT TG Requirement C.12* to clarify that the creation date is not mandatory, but one of date of publication, date of creation or date of last revision.
- TG Requirement 26 concerning the Lineage element is now stated in  *REF req\_data\_lineage \h  \\* MERGEFORMAT TG Requirement 1.11*.
- TG Requirement 27 concerning Spatial resolution is now stated in  *REF req\_data\_spatial\_resolution \h  \\* MERGEFORMAT TG Requirement 1.5* (for data sets and data sets series) and in  *REF req\_sds\_spatial\_resolution \h  \\* MERGEFORMAT TG Requirement 3.3* (for Spatial Data Services).
- TG Requirements 28 and 29 concerning the conformity declarations against the INSPIRE Implementation Rules for interoperability of spatial data sets and services is now stated in  *REF req\_data\_conformity \h  \\* MERGEFORMAT TG Requirement 1.10* (for data sets and data set series) and  *REF req\_sds\_invocable\_conformity \h  \\* MERGEFORMAT TG Requirement 5.3* (for Invocable Spatial Data Services). TG Recommendation 19 concerning the conformity declarations against the INSPIRE Implementation Rules for network services is now stated in  *REF rec\_ns\_conformity \h  \\* MERGEFORMAT TG Recommendation 4.1*. The common structure for declaring the conformity against a specification is given in  *REF req\_common\_conformity \h  \\* MERGEFORMAT TG Requirement C.20*,  *REF req\_common\_conformity\_specification \h  \\* MERGEFORMAT TG Requirement C.21* and  *REF req\_common\_conformity\_degree \h  \\* MERGEFORMAT TG Requirement C.22*.
- The TG Requirements 30, 31, 32, 33 and 34 concerning the Limitations on public access and the Conditions applying to access and use elements have been revised and split into  *REF req\_common\_limitations\_public\_access \h  \\* MERGEFORMAT TG Requirement C.17* about Limitations on public access, and  *REF req\_common\_limitations\_access\_and\_use \h  \\* MERGEFORMAT TG Requirement C.18* about Conditions applying to access and use. The XML encoding of these elements have been clarified and harmonised. For both elements only the *MD\_LegalConstraints* shall now be used containing a combination of *accessConstraints*, *useConstraints* and *otherConstraints* as described in sections  REF \_Ref476228144 \r \h 2.3.6 and  REF \_Ref476228147 \r \h 2.3.7. Referring to the new INSPIRE code lists for the reason of the Limitations on public access as well as Conditions applying to access and use ("no conditions" or "unknown") is now mandatory using the *gmx:Anchor* element.
- TG Requirements 35 and 36 as well as the INSPIRE specific constraint SC14 concerning the responsible organisation are now covered by  *REF req\_common\_responsible\_organisation \h  \\* MERGEFORMAT TG Requirement C.10*.
- TG Requirements 37 and 38 concerning the Metadata point of contact are now given as  *REF req\_common\_md\_point\_of\_contact \h  \\* MERGEFORMAT TG Requirement C.6*.
- TG Requirement 39 concerning the Metadata language is now stated as  *REF req\_common\_md\_language \h  \\* MERGEFORMAT TG Requirement C.5*.

**Normative references**

The following referenced documents are indispensable for the application of this document. For dated references, only the edition cited applies. For undated references, the latest edition of the referenced document (including any amendments) applies. For ISO standards that have also been adopted as EN by CEN, the relevant CEN reference and adoption date are given, with the ISO number and adoption date in parentheses.

[ISO/IEC Directives Part 2] ISO/IEC Directives Part 2: Principles to structure and draft documents intended to become International Standards, Technical Specifications or Publicly Available Specifications, 7th edition, 2016.

[ISO 19105] EN ISO 19105:2005, Geographic Information – Conformance and testing (ISO 19105:2000)



[ISO 19108] EN ISO 19108:2005, Geographic Information – Temporal Schema (ISO 19108:2002)

[ISO 19112] EN ISO 19112:2005, Geographic Information – Spatial referencing by geographic identifiers (ISO 19112:2003)

[ISO 19115] EN ISO 19115:2005, Geographic information – Metadata (ISO 19115:2003)

[ISO 19119] EN ISO 19119:2005, Geographic information – Services (ISO 19119:2005)

[ISO 19139] ISO/TS 19139:2007, Geographic information – Metadata – XML schema implementation 

[ISO 639-2] ISO 639-2:1998, Codes for the representation of names of languages – Part 2: Alpha-3 code

[ISO 8601] ISO 8601:2004, Data elements and interchange formats – Information interchange – Representation of dates and times

[CSW2 AP ISO] OpenGIS Catalogue Services Specification 2.0.2 - ISO Metadata Application Profile, Version 1.0.0, OGC 07-045, 2007

[INSPIRE Directive] Directive 2007/2/EC of the European Parliament and of the Council of 14 March 2007 establishing an Infrastructure for Spatial Information in the European Community (INSPIRE)

[Regulation 1205/2008] Commission Regulation (EC) No 1205/2008 of 3 December 2008 implementing Directive 2007/2/EC of the European Parliament and of the Council as regards metadata. 

NOTE	[Regulation 1205/2008] is informally also known as "Implementing Rules for metadata".

[Regulation 976/2009] Commission Regulation (EC) No 976/2009 of 19 October 2009 implementing Directive 2007/2/EC of the European Parliament and of the Council as regards the Network Services, as amended by

- Commission Regulation (EC) No 1088/2010 of 23 November 2010 amending Regulation (EC) No 976/2009 as regards download services and transformation services; and
- Commission Regulation (EU) No 1311/2014 of 10 December 2014 amending Regulation (EC) No 976/2009 as regards the definition of an INSPIRE metadata element

NOTE	[Regulation 976/2009] is informally also known as "Implementing Rules for network services".

[Regulation 1089/2010] Commission Regulation (EU) No 1089/2010 of 23 November 2010 implementing Directive 2007/2/EC of the European Parliament and of the Council as regards interoperability of spatial data sets and services, as amended by

- Commission Regulation (EU) No 102/2011 of 4 February 2011 amending Regulation (EU) No 1089/2010 implementing Directive 2007/2/EC of the European Parliament and of the Council as regards interoperability of spatial data sets and services;
- Commission Regulation (EU) No 1253/2013 of 21 October 2013 amending Regulation (EU) No 1089/2010 implementing Directive 2007/2/EC as regards interoperability of spatial data sets and services; and
- Commission Regulation (EU) No 1312/2014 of 10 December 2014 amending Regulation (EU) No 1089/2010 implementing Directive 2007/2/EC of the European Parliament and of the Council as regards interoperability of spatial data services.

NOTE [Regulation 1089/2010] is informally also known as "Implementing Rules for interoperability of spatial data sets and services" or IR-ISDSS for short.

[OGC Specification Model] The Specification Model – A Standard for Modular specifications, Open Geospatial Consortium, OGC 08-131r3,	<https://portal.opengeospatial.org/files/?artifact_id=34762> 


**Other references**

[TG SDS] Technical Guidance for INSPIRE Spatial Data Services and services allowing spatial data services to be invoked, version 4.0, <http://inspire.ec.europa.eu/id/document/tg/sds/4.0> 

[TG DiscoveryS] Technical Guidance for INSPIRE Discovery Services, version 3.1, <http://inspire.jrc.ec.europa.eu/documents/Network_Services/TechnicalGuidance_DiscoveryServices_v3.1.pdf> 

[TG ViewS] Technical Guidance for the implementation of INSPIRE View Services, version 3.11, <http://inspire.ec.europa.eu/documents/Network_Services/TechnicalGuidance_ViewServices_v3.11.pdf> 

[TG DownloadS] Technical Guidance for the implementation of INSPIRE Download Services, version 3.1, <http://inspire.ec.europa.eu/documents/Network_Services/Technical_Guidance_Download_Services_v3.1.pdf> 

[TG DS] Technical Guidelines – INSPIRE data specifications, <http://inspire.ec.europa.eu/index.cfm/pageid/2> 

[ISO 19115-1] ISO 19115-1:2014, Geographic information – Metadata – Part 1: Fundamentals

[ISO 19115-3] ISO/TS 19115-3:2016, Geographic information – Metadata – Part 3: XML schema implementation for fundamental concepts

[ISO 19157] ISO 19157:2013, Geographic information -- Data quality. 

NOTE	This document is not listed under normative references because it is only referred as an inspiration for the ISO 19139 encoding of the INSPIRE metadata elements Topological consistency and Data quality. The ISO 19157:2013 standard should be used together with a newer version of ISO metadata standard for geographic information, [ISO 19115-1].

[ISO 10646] ISO/IEC 10646:2014, Information technology -- Universal Coded Character Set (UCS)

[ISO 15836] ISO 15836:2009, Information and documentation – The Dublin Core metadata element set


**Terms and abbreviations**

The terms concerning requirements, conformance test classes and tests are based on the OGC document The Specification Model - A Standard for Modular specifications (08-131r3)[` `See http://www.opengeospatial.org/standards/modularspec
]. Note that the intermediate structuring entities "requirements module" and "conformance module" are not included here for simplicity. Instead, the requirements are directly included in requirements classes and conformance tests in conformance test classes.

**Abstract test suite (ATS)** is a set of *conformance classes* that define tests for all requirements of a specification [derived from OGC Specification Model and ISO 19105]

**Access point** (of a Spatial Data Service) is an URL for retrieving a detailed description of a *Spatial Data Service*, including a list of *end points* to allow its execution.

**Conformance class** is a set of *conformance test modules* that must be applied to receive a single certificate of conformance [OGC Specification Model]

**Conformance test module** (or abstract test module) is a set of related *conformance test cases*, all within a single *conformance class* [OGC Specification Model]

**Conformance test case** (or abstract test case) is a test for a particular *requirement* or a set of related requirements [OGC Specification Model].

NOTE: An abstract or conformance test case is a formal basis for deriving executable test cases. It should be complete in the sense that it is sufficient to enable a test verdict to be assigned unambiguously to each potentially observable test outcome.

**(Spatial) data set** is an identifiable collection of (spatial) data [INSPIRE Directive].

**(Spatial) data set series** is a collection of (spatial) data sets sharing the same product specification [Regulation 1205/2008].

**Discovery Service** is a service that makes it possible to search for spatial data sets and services on the basis of the content of the corresponding metadata and to display the content of the metadata [INSPIRE Directive, Art. 11].

**Download Service** is a service enabling copies of spatial data sets, or parts of such sets, to be downloaded and, where practicable, accessed directly [INSPIRE Directive, Art. 11]. 

**End point** (of a Spatial Data Service) is an URL used for directly calling an operation provided by the *Spatial Data Service*.

**Executable test suite** (ETS) is a set of executable test cases [ISO 19105].

**Harmonised Spatial Data Service** is an interoperable spatial data service which fulfils the requirements of Annex VII [Regulation 1089/2010, Art. 1]. 

**Interoperable Spatial Data Service** is an invocable spatial data service which fulfils the requirements of Annex VI [Regulation 1089/2010, Art. 1].  

**Invocable Spatial Data Service** is a spatial data service that (a) has metadata which fulfils the requirements of [Regulation 1205/2008], (b) has at least one resource locator that is an access point, (c) is conformant with a documented and publicly available set of technical specifications providing the information necessary for its execution [Regulation 1089/2010, Art. 1].

**Network Services** are services provided for in Article 11(1) of [INSPIRE Directive] for the discovery, viewing, download and transformation of spatial data sets and services. The service shall be conformant regarding the specific requirements in [Regulation 976/2009]. 

**Non-empty Free Text Element** is an XML element with textual content encoded either using *gco:CharacterString*, *gmx:Anchor* or *gmd:PT\_FreeText* element of the ISO 19139 XML Schema. See section 2.2 for more information.

NOTE The technical specifications could e.g. be a web site documentation explaining how to use the service, or they could be more formal, e.g. a WSDL document or a description of a RESTful interface. 

**Recommendation** is an expression in the content of a document conveying a suggested possible choice or course of action deemed to be particularly suitable without necessarily mentioning or excluding others. In the negative form, a recommendation is the expression that a suggested possible choice or course of action is not preferred but it is not prohibited [ISO/IEC Directives Part 2].

**Requirement** is an expression in the content of a document conveying criteria to be fulfilled if compliance with the document is to be claimed and from which no deviation is permitted.  [ISO/IEC Directives Part 2].

**Spatial Data Services** are the operations which may be performed, by invoking a computer application, on the spatial data contained in spatial data sets or on the related metadata [INSPIRE Directive, Art. 3].

**Statement of conformity** is the result of running an *executable test suite*, and it contains statements about the conformity of the particular *conformance subject* against the *conformance test classes* implemented in the used *executable test suite.* The statement of conformity has no legal significance as itself, but it can be a useful tool for evaluating the conformity of the particular *conformity subject* against the legal regulations the tests in the *conformance test classes* of the particular *conformance test suites* are founded on.

**Transformation Service** is a service enabling spatial data sets to be transformed with a view to achieving interoperability [INSPIRE Directive, Art. 11]. 

**View Service** is a service making it possible, as a minimum, to display, navigate, zoom in/out, pan, or overlay viewable spatial data sets and to display legend information and any relevant content of metadata [INSPIRE Directive, Art. 11].

**Verbal forms for expression of provisions**

In accordance with the ISO rules for drafting, the following verbal forms shall be interpreted in the given way:

- “shall” / “shall not”: a requirement, mandatory to comply with the technical guidelines
- “should” / “should not”: a recommendation, but an alternative approach may be chosen for a specific case if there are reasons to do so 
- “may” / “need not”: a permission

***Requirements and recommendations notation***

Requirements and the recommendations for INSPIRE Metadata Implementing Rules within this specification are highlighted and numbered as shown below:

**TG Requirement #.#: metadata/2.0/req/<conformance-class-id>/<requirement-id>**		

Technical Guidelines Requirements are shown using this style

**TG Recommendation #.#: metadata/2.0/rec/<conformance-class-id>/<requirement-id>**

Technical Guidelines Recommendations are shown using this style.

The requirements and recommendations are grouped into Conformance Classes containing all the requirements specific to a particular type of metadata record or a requirement set originating with a particular Implementation Rule document. 

The Conformance Class definitions in this specification are highlighted and numbered as shown below:

**Conformance Class #**:	**metadata/2.0/<conformance-class-id>**

Conformance Classes are shown using this style.

Recommendations and requirements are prefixed with the number of their conformance class and numbered consecutively. Requirements and recommendations that are common to several conformance classes (see section  REF \_Ref459654184 \r \h 2) are prefixed with C (for “Common”).

Each conformance class, requirement and recommendation also have a unique identifier consisting of a common namespace (**metadata/2.0/, metadata/2.0/req/** and **metadata/2.0/rec/**, respectively), the id of the conformance class and the id of the requirement or recommendation.

NOTE	Requirements as specified in the INSPIRE Regulations and Implementing Rules are legally binding, and that requirements and recommendations as specified in INSPIRE Technical Guideline are not legally binding. Therefore, within this technical guideline we have used the terms ‘TG requirement’ and ‘TG recommendation’ to indicate what is technically required or recommended to conform to this Technical Guidelines specification.

***Quoted INSPIRE Regulation text***

Directed quotations from INSPIRE Implementation Rules and other legally mandated regulations are expressed as quoted text blocks using the following style:


*5. TEMPORAL REFERENCE*

``*This metadata element addresses the requirement to have information on the temporal dimension of the data as referred to in Article 8(2)(d) of Directive 2007/2/EC. At least one of the metadata elements referred to in points 5.1 to 5.4 shall be provided. The value domain of the metadata elements referred to in points 5.1 to 5.4 is a set of dates. Each date shall refer to a temporal reference system and shall be expressed in a form compatible with that system. The default reference system shall be the Gregorian calendar, with dates expressed in accordance with ISO 8601.*


***XPath expressions***

XML Path Language (XPath) is a W3C Recommendation for addressing parts of an XML document[` `XML Path Language (Xpath), version 1.0, https://www.w3.org/TR/xpath/
]. This compact notation allows many defaults and abbreviations for common cases. The simplest XPath takes a form such as /A/B/C which selects C elements that are children of B elements that are children of the A element that forms the outermost element of the model. More complex expressions can be constructed by specifying an axis other than the default 'child' axis, a node test other than a simple name, or predicates, which can be written in square brackets after any step. The main rules are the following ones:

\* 	selects all element children of the context node;

text() 	selects all text node children of the context node;

@name 	selects the name attribute of the context node;

@\* 	selects all the attributes of the context node;

. 	selects the context node;

.//para 	selects the para element descendants at any level of the context node;

.. 	selects the parent of the context node.

In this document XPath expressions are used for exactly specifying the locations of the required and recommended XML elements within the XML document structure containing the metadata content. Sometimes, in order to manage the polymorphism, the XPath expression deals with some elements in the path in a generic way (e.g., property\_element\_name/\*/datatype\_property\_name). This is done for example for some requirements and examples to be applicable to both data set and service identification elements.

Where profiles conformant to [ISO 19139] are being used to encode INSPIRE metadata records, the XPath expressions used in the text of TG requirements may need to be adapted to match the profile.

***XML examples***

The XML examples are numbered for easier referencing and shown as text blocks with a fixed-width font on a grey background:


**/gmd:MD\_Metadata/gmd:hierarchyLevel:**

``<gmd:hierarchyLevel>    <gmd:MD\_ScopeCode

`		`codeList=http://standards.iso.org/iso/19139/resources/gmxCodelists.xml#MD\_ScopeCode codeListValue="dataset"/>  

</gmd:hierarchyLevel>

***Example X.Y**: Resource type "dataset" given using gmd:hierarchyLevel property*

The location of the XML elements within the document structure is given using XPath syntax at the top of the text block in bold font.

NOTE	XML Examples are informative and are provided for information only and are expressly not normative.

***Numbering of requirements, examples, figures and tables***

The TG Requirements, TG Recommendations, XML examples, tables and figures are numbered using two-part, dot-separated identifiers: The first part refers to the containing Conformance Class and the second is a running number within the Conformance Class. In the chapter 2 "Common requirements for ISO/TC 19139:2007 based INSPIRE metadata records" which does not comprise a Conformance Class, but is referred to from the Conformance Class chapters, the first part is a letter "C". This numbering style is used to help associating the referred requirements with their containing Conformance Classes.

***XML namespaces and prefixes used in this document***

XML element prefixes are used in this document to refer to the namespaces as follows:


|**prefix**|**Namespace URI**|
| :- | :- |
|gmd|http://www.isotc211.org/2005/gmd|
|gco|http://www.isotc211.org/2005/gco|
|gmx|http://www.isotc211.org/2005/gmx|
|srv|http://www.isotc211.org/2005/srv|
|gml|http://www.opengis.net/gml/3.2 (for GML 3.2.1) or <br>http://www.opengis.net/gml (for GML 3.2.0)|
|xsi|http://www.w3.org/2001/XMLSchema-instance|
|xlink|http://www.w3.org/1999/xlink|


|INSPIRE|Technical Guidelines for the implementation of INSPIRE dataset and service metadata based on ISO/TS 19139:2007|
| :- | :- |
|Version 2.0.2|2017-08-31|Page  PAGE 156|

# **Overview**
# ***Introduction***
Data sets and the Spatial Data Services providing them need to be discoverable by the people requiring the provided information to be available. In INSPIRE the discoverability of these resources is based on two equally important things: the data and service providers describing their resources using the metadata elements according to rules mandated by the INSPIRE Regulations, and on the other hand, the Discovery Services providing online access to query the provided metadata.

Both of the components mentioned above need to be functional and kept up-to-date to enable the Infrastructure of Spatial Information in Europe. The technical requirements for providing Discovery Services are given in [TG DiscoveryS], and the requirements for the metadata content and structure in this document.

[INSPIRE Directive], recital 15:

*(15) 	The loss of time and resources in searching for existing spatial data or establishing whether they may be used for a particular purpose is a key obstacle to the full exploitation of the data available. Member States should therefore provide descriptions of available spatial data sets and services in the form of metadata.*

[INSPIRE Directive], Article 5(1):

*1. 	Member States shall ensure that metadata are created for the spatial data sets and services corresponding to the themes listed in Annexes I, II and III, and that those metadata are kept up to date.*

According to Article 5(4) of [INSPIRE Directive], Implementing Rules shall be adopted taking account of relevant, existing international standards and user requirements. In the context of metadata for spatial data and Spatial Data Services, the standards [ISO 19115], [ISO 19119], [ISO 19139] and [ISO 15836] (Dublin Core) have been identified as important standards or technical specifications.

[Regulation 1205/2008] containing the legal requirements for providing the INSPIRE metadata was adopted on of 3rd December 2008, and published on the Official Journal of the European Union on 4th December (*OJ L 326, 4.12.2008, p. 12–30)*. Any reference in this document to “Implementing Rules for Metadata” refers to the above-mentioned regulation. 

The [Regulation 1205/2008] sets out the requirements for the creation and maintenance of metadata for spatial data sets, spatial data set series and Spatial Data Services corresponding to the themes listed in Annexes I, II and III of the [INSPIRE Directive][` `The metadata elements defined in the Implementing Rules for Metadata are usually called discovery metadata.
]. It defines a number of metadata elements, their multiplicities and the value domains to be used in the metadata.

In addition to [Regulation 1205/2008], [Regulation 1089/2010] and its first two sub-sequent amendments[` `Commission Regulation (EU) No 102/2011 of 4 February 2011 amending Regulation (EU) No 1089/2010 implementing Directive 2007/2/EC of the European Parliament and of the Council as regards interoperability of spatial data sets and services (OJ L 31, 05/02/2011, p. 13–34)
],,[` `Commission Regulation (EU) No 1253/2013 of 21 October 2013 amending Regulation (EU) No 1089/2010 implementing Directive 2007/2/EC as regards interoperability of spatial data sets and services (Annex II+III amendment).
] define six additional *metadata elements for interoperability* as well as some theme-specific requirements for the discovery metadata elements[` `The metadata elements defined in the Implementing Rules for interoperability of spatial data sets and services are also sometimes referred to as evaluation and use metadata.
]. Any reference in this document to “Implementing Rules for interoperability of spatial data sets and services” refers to the above-mentioned Regulation.

The third of the most relevant documents concerning INSPIRE metadata is [Regulation 1312/2014] amending [Regulation 1089/2010]. It contains additional requirements for the metadata of INSPIRE Spatial Data Services categorised in three levels of harmonisation: Invocable, Interoperable and Harmonised Spatial Data Services. The additional requirements for each category were added as Annexes V to VII of [Regulation 1089/2010].



The aim of this document is to define how the requirements of the mentioned INSPIRE regulations for metadata can be implemented using an XML format defined in [ISO 19139] based on data models of [ISO 19115] and [ISO 19119] to achieve harmonised technical access and use of the INSPIRE metadata for spatial data sets from all INSPIRE themes and Spatial Data Services used for providing and processing them across all EU Member States.
# **Roadmap and timelines for provisioning INSPIRE metadata**
The timelines relevant for the provision of discovery metadata are different from those for metadata for interoperability. The former need to be provided according to the deadlines specified in the INSPIRE Directive for the Implementing Rules for Metadata (2 years after adoption for Annex I and II and 5 years after adoption for Annex III), while the latter need to be provided according to the deadlines specified in the INSPIRE Directive for the Implementing Rules for interoperability of spatial data sets and services (2 years after adoption for newly created or extensively restructured data sets, and 7 years for all other data sets).

` `REF \_Ref465957431 \h  \\* MERGEFORMAT Figure 2 gives an overview of the dates at which the requirements included in the two Implementing Rules for data sets related to Annex I, II or III have to be met[` `Dates in this figure are accurate at the time of publication. For definitive dates refer to the roadmap published on the INSPIRE website (<http://inspire.ec.europa.eu/inspire-roadmap/61>).
].

![](Aspose.Words.bef9e791-4ef2-43dc-ae9d-769f51fa1525.004.png)

***Figure  SEQ Figure \\* ARABIC 2:** Illustration of Implementation Roadmap for discovery metadata, metadata for interoperability, and metadata for Invocable Spatial Data Services.*
# **Categories of INSPIRE Spatial Data Services**
The spatial data services covered by the INSPIRE Directive are defined in Art. 4(3) as follows:


*“This Directive shall also cover the spatial data services relating to the data contained in the spatial data sets referred to in paragraph 1.”* 


This means, the Directive covers all SDS that relate to INSPIRE-relevant data as defined in Art. 4(1) of [INSPIRE Directive]. In addition, an SDS could also include other data.

According to Art. 5(1) of [INSPIRE Directive], all SDSs within INSPIRE shall be described with metadata in conformity with [Regulation 1205/2008]. 

The SDSs that Member States establish and operate according to Art. 11 of [INSPIRE Directive] are called *network services*. All network services shall meet the requirements specified in [Regulation 976/2009].

Those SDS that are not network services, but fulfil the requirements of [Regulation 1205/2008], have at least one resource locator and follow a publicly available technical specification are called *invocable spatial data services*. All invocable SDS shall meet the requirements specified in [Regulation 1089/2010]. All other SDS are referred to in this document as *other SDS*. 

SDS regulated by [Regulation 1089/2010] are further divided into three different categories depending on level of interoperability: Invocable SDS, Interoperable SDS and Harmonised SDS. SDS regulated by [Regulation 976/2009] (i.e. *network services*) consist of four different types of services: discovery services, view services, download services and transformation services.

` `REF \_Ref429468006 \h  \\* MERGEFORMAT Figure 3 gives an overview of the different types of spatial data services.


![](Aspose.Words.bef9e791-4ef2-43dc-ae9d-769f51fa1525.005.png)

***Figure  SEQ Figure \\* ARABIC 3**: Spatial data services in the context of INSPIRE and their relationships to different types and categories of services. \* Discovery Services also take the role as making it possible to invoke a service. [TG SDS]* 

# ***XML Encoding of ISO metadata***
This encoding of the INSPIRE metadata in this technical specification is based on the ISO Standards [ISO 19115], [ISO 19119] and [ISO 19139]. The abstract standards [ISO 19115] and [ISO 19119] provide a structural model and specify the content of the set of metadata elements used in this specification, but they do not specify the encodings of those elements. The [ISO 19139] specifies an XML encoding of [ISO 19115] elements, but not for the service-specific metadata elements contained in [ISO 19119]. To provide an XML encoding also for the INSPIRE service metadata, XML Schemas implementing the [ISO 19119] model have been published by the OGC[` `<http://schemas.opengis.net/csw/2.0.2/profiles/apiso/1.0.0/apiso.xsd> 
]. These XML Schemas, though not officially endorsed by ISO, are widely used within the metadata community, and have been chosen to be used also in INSPIRE since version 1.0 of this specification.

NOTE	Currently, the *gmx* namespace is not included in the referenced schema for [ISO 19119]. Consequently, all elements defined in the gmx namespace (e.g. gmx:Anchor) are not valid according to this schema. This issue has been raised with OGC[` `See OGC change request at <http://ogc.standardstracker.org/show\_request.cgi?id=435> 
]. Until the OGC agrees to host a version of the xml schema that fixes the known problems, these will be hosted by JRC[` `The schemas are made available as draft schemas on the INSPIRE schema repository at <http://inspire.ec.europa.eu/draft-schemas/inspire-md-schemas/apiso-inspire/apiso-inspire.xsd> and <http://inspire.ec.europa.eu/draft-schemas/inspire-md-schemas/srv/1.0/> 
].

The requirements defined in this document are based on [ISO 19139], which in turn is an implementation of the [ISO 19115], and OGC XML Schema implementation of the [ISO 19119]. 

NOTE	ISO 19115:2003 has been recently replaced by the new Standard named 19115-1:2014, describing general-purpose metadata. This new revision is a part of an overall ISO standard 19115 on geographic metadata, along with 19115-2, regarding the extensions for acquisition and processing, and 19115-3 defining the XML schema implementation of metadata fundamentals. In relation with the issues addressed in this document, the main changes in the new standard are the following:

- The concept of ‘Core metadata’ was removed and was translated into the normative Annex F (of [ISO 19115-1]) describing the discovery metadata for geographic resources (datasets, series and services);
- Metadata for services deriving from ISO 19119 was included;
- Metadata concerning data quality was moved to the new specific Standard ISO 19157.

It was decided in the MIWP-8 sub-group that new versions of the ISO 19115 standard were out of scope for this version of this specification. The future versions of this Technical Guidelines may be revised taking into account the new ISO 19115 family standards.

A comparison between the core metadata given in [ISO 19115], the INSPIRE metadata elements for spatial datasets, spatial dataset series and services as defined in [Regulation 1205/2008], and the discovery metadata for geographic datasets, series and services defined in [ISO 19115-1] is available in the Annex III of the GeoDCAT-AP specification[` `See https://joinup.ec.europa.eu/asset/dcat\\_application\\_profile/asset\\_release/geodcat-ap-v10
].
# ***INSPIRE Validator Service***
A RESTful Web service that can be invoked by http request to validate INSPIRE Metadata has been created by the JRC (<http://inspire-geoportal.ec.europa.eu/validator2/>). 

NOTE	The validator is not intended to be an operational tool, and at the time of writing only supports validation against version 1.3 of the metadata technical guidelines.

All the files of the Validator including documentation are available under EU Public License from the JoinUp Platform (<https://joinup.ec.europa.eu/software/validator/home>). Interested stakeholders are welcome to adapt the current Validator to their own language, and contribute it back through JoinUp to enrich the collective portfolio of tools supporting the implementation of INSPIRE.

At the time of writing, the design and implementation of a new, more comprehensive INSPIRE validator containing validation functionality for data sets, services and metadata is in progress under the work of the MIG temporary sub group MIWP-5: Validation and conformity testing, with support through the ISA Action ARE3NA (A Reusable INSPIRE Reference Platform, <https://joinup.ec.europa.eu/community/are3na/description>). This new validator will implement the Conformance Classes for requirements in versions 1.3 and 2.0.
# ***Position and structure of this document***
This document is a technical specification for implementing the legal requirements of the [INSPIRE Directive] and related Commission Regulations for providing the spatial data sets and Spatial Data Services metadata. The purpose of this specification is to provide a standards compliant and unambiguous technical method for providing all the required metadata required by INSPIRE Regulations using XML encoding based on [ISO 19139] standard.

In addition to the structural requirements formalized through required XML elements in the Technical Guidelines Requirements of this specification, the conformance to INSPIRE is a matter of semantics of the information provided. The minimum requirements expressed in the Implementing Rules also have to be met semantically, i.e. with metadata contents strictly satisfying the INSPIRE requirements.

The INSPIRE Maintenance and Implementation Group (MIG) strongly recommends the EU Member States follow the technical requirements given in this specification for providing the metadata describing the INSPIRE spatial data sets and Spatial Data Services. Harmonisation beyond the abstract level of requirements contained in the INSPIRE Regulations is necessary for reaching the goals of data set and service interoperability and information reuse set for the Infrastructure of Spatial Information in Europe.

This specification consists of 7 Conformance Classes (see also  REF \_Ref467690379 \h **Figure 4**):

- Conformance Class 1: INSPIRE data sets and data set series baseline metadata (section  REF \_Ref465959993 \r \h 3.1),
  - Conformance Class 2: INSPIRE data sets and data set series interoperability metadata (section  REF \_Ref465960006 \r \h 3.2),
- Conformance Class 3: INSPIRE Spatial Data Service baseline metadata (section  REF \_Ref465960019 \r \h 4.1),
  - Conformance Class 4: INSPIRE Network Services metadata (section  REF \_Ref465960026 \r \h 4.2),
  - Conformance Class 5: INSPIRE Invocable Spatial Data Services metadata (section ( REF \_Ref465960036 \r \h 4.3),
    - Conformance Class 6: INSPIRE Interoperable Spatial Data Services metadata (section  REF \_Ref465960043 \r \h 4.4), and
    - Conformance Class 7: INSPIRE Harmonised Spatial Data Services metadata (section  REF \_Ref465960051 \r \h 4.5).

The indention of the above list indicates the requirement inclusion hierarchy between Conformance Classes: A Conformance Class intended as sub-element in the list also includes all the TG Requirements of the parent level Conformance Classes. Section 2 contains TG Requirements and Recommendations describing metadata elements that shall be used in the same way in more than one of the mentioned Conformance Classes.

![](Aspose.Words.bef9e791-4ef2-43dc-ae9d-769f51fa1525.006.png)

***Figure  SEQ Figure \\* ARABIC 4**: Structure of the conformance classes in this Technical Guidance document.*
# **TG Requirements, TG Recommendations and conformance**
The TG Requirements of this specification have been selected to cover all the requirements of the INSPIRE Implementing Rule regulations for the metadata descriptions of the INSPIRE data set and services. All the TG Requirements included in each of the Conformance Classes of this specification shall be fulfilled in order for conformance subject (metadata record) to be considered compliant with the Conformance Class. Furthermore, any metadata record fulfilling all the TG Requirements included in a Conformance Class shall be considered compliant with that Conformance Class.

In addition to the TG Requirements, the document sections defining the Conformance Classes also include TG Recommendations. These recommendations suggest additional, non-mandatory methods for increasing the interoperability, and harmonisation of the provided metadata, or propose good defaults to content of structure of the metadata, where several options for expression are allowed. The TG Recommendations should be followed if there are no compelling reasons not to. Following or not following TG Recommendations shall not be considered as measure of conformance against their containing Conformance Classes.

The conformity with a Conformance Class shall be evaluated as defined in the Abstract Test Suites in  REF \_Ref476125052 \n \h Annex A, which shall include Test cases for each of the TG Requirements included in the Conformance Class. The Abstract Test Suites may also include tests for fulfilling the TG Recommendations to provide further interoperability improvement or deprecation hints to help both the metadata providers and the INSPIRE metadata handling software developers. If included, the failure or success of passing these TG Recommendation tests shall not have an effect of the evaluated conformance measure of the metadata record under test.


# **Common requirements for ISO/TC 19139:2007 based INSPIRE metadata records**

# ***Metadata structure and encoding***
**TG Requirement C.seq Req \r11: metadata/2.0/req/common/xml-schema**

INSPIRE metadata records shall be encoded in XML format valid against one of the following XML Schemas:- [**CSW2 AP ISO**] XML Schema[` `<http://inspire.ec.europa.eu/draft-schemas/inspire-md-schemas/> importing the \*srv\* namespace for encoding service metadata and referring to GML version 3.2.1 available in the OGC schema repository (as defined in the schemas at <http://inspire.ec.europa.eu/draft-schemas/inspire-md-schemas/srv/1.0/>), or an unmodified copy.
],- [**ISO 19139**] XML Schema as available in the ISO repository[` `[\*http://www.isotc211.org/2005/gmd/gmd.xsd](http://www.isotc211.org/2005/gmd/gmd.xsd)\* referring to GML version 3.2.1 available in the ISO schema repository, or an unmodified copy.
], or- [**ISO 19139**] XML Schema as available in the OGC schema repository[` `[\*http://schemas.opengis.net/iso/19139/20070417/gmd/gmd.xsd](http://schemas.opengis.net/iso/19139/20070417/gmd/gmd.xsd)\* referring to GML version 3.2.1 available in the OGC schema repository, or [\*http://schemas.opengis.net/iso/19139/20060504/gmd/gmd.xsd](http://schemas.opengis.net/iso/19139/20060504/gmd/gmd.xsd)\* referring to GML version 3.2.0 available in the OGC schema repository, or unmodified copies of either of these.
].All three of these XML Schemas declare the same namespace [*http://www.isotc211.org/2005/gmd*](http://www.isotc211.org/2005/gmd).

The metadata identification info property for INSPIRE Spatial Data Services shall be encoded using the service metadata XML Schema available in the OGC schema repository. This schema is an XML implementation of the [ISO 19119] service metadata, and it declares the namespace http://www.isotc211.org/2005/srv.

NOTE	These guidelines extensively use XPath expressions in the requirements and recommendations. If profiles conformant to [ISO 19139] are being used to encode INSPIRE metadata records, these XPath expressions may need to be adapted to match the profile.

The choice of which XML Schemas to use for encoding the metadata records depends on the existing technical solutions available, as well as on the GML version wished to be used: 

- If the delivery of the metadata records is done via a Discovery Service supporting the [CSW2 AP ISO] standard, using the XML Schema of this specification is a natural choice. The [CSW2 AP ISO] XML Schema imports the OGC version 2006-05-04 of the *gmd* namespace, and through it the OGC GML XML Schema version 3.2.0. The [CSW2 AP ISO] XML Schema also imports the *srv* namespace for describing service metadata. Note that GML 3.2.0 has target namespace *http://www.opengis.net/gml,* the same as GML version 3.1.1.
- If using GML version 3.2.1 in the metadata (namespace *http://www.opengis.net/gml/3.2*), then it is recommended to use either the official [ISO 19139] XML Schema available at the ISO schema repository, or the nearly identical version “2007-04-07” available in the OGC schema repository. Note that in this case, the same *srv* namespace elements referring to GML 3.2.0 would still be required for describing service metadata. This means that for service metadata records there may two versions of GML in use at the same time from namespaces *http://www.opengis.net/gml* and *http://www.opengis.net/gml/3.2*.

**TG Requirement C.seq Req2: metadata/2.0/req/common/root-element**

The metadata for an INSPIRE data set, data set series or service shall be encoded using exactly one gmd:*MD\_Metadata* element as specified in the XML Schema rules and in the TG Requirements of the Conformance Classes in this specification.Additionally the requirements of [ISO 19139], [ISO 19115] and [ISO 19119] shall be followed for describing the metadata records in cases where neither the XML Schemas nor the TG Requirements in this specification require otherwise.

Note that the use of these guidelines to create INSPIRE metadata ensures that the metadata is not in conflict with [ISO 19115] or [ISO 19119]. However, full conformance to [ISO 19115] implies the provision of additional metadata elements which are not required by the INSPIRE Implementing Rules and thus out-of-scope of this specification.
# **Encoding of code list values**
INSPIRE metadata elements that are mapped to code lists from [ISO 19139], the relevant requirements mention the code list to be used.

**TG Requirement C.seq Req3: metadata/2.0/req/common/code-list-value**

The code list value shall be encoded using the *codeListValue* attribute of the relevant ISO 19139 element. The value shall be the identifier of the code list value, as defined in the name column of the tables in [ISO 19115], Annex B.

Note that [ISO 19115] allows code lists to be extended. In cases, where, for the INSPIRE metadata elements, only the values defined in [ISO 19115, Annex B] (or a subset thereof), can or should be used, this is stated in the relevant requirement or recommendation. Additional extended values may still be used, but may be ignored by INSPIRE metadata clients.

Both the value of the codeList attribute (a URL that references a code list definition within a register or a code list catalogue) and the textual content of the ISO 19139 element are purely informative. The codeList value may e.g. point to the code list dictionary in the ISO 19139 repository at <http://standards.iso.org/iso/19139/resources/codelist/>, and if a text is provided, it may contain the translation of the code list value in the language of the metadata. 


<CI\_DateTypeCode codeList="http://standards.iso.org/iso/19139/resources/codelist/gmxCodelists.xml#CI\_DateTypeCode" codeListValue="creation">Creazione</CI\_DateTypeCode>

***Example  STYLEREF 1 \s 2. SEQ Example \\* ARABIC \s 1 1**: An instance of CI\_DateTypeCode expressed in the default language of the metadata (here: Italian).*

In some cases, an INSPIRE metadata element is mapped to a free-text element in ISO 19139, but these TGs recommend or require the use of a code list value through an *gmx:Anchor* element (see section  REF \_Ref455671046 \r \h 2.1.2). In these cases, the relevant requirements/recommendations specify how to use the *gmx:Anchor* element.

# **Encoding of free text values**
The ISO 19139 XML Schemas allow using alternative ways of encoding free text. The basic element for providing text of unrestricted length with no internal XML structure is *gco:CharacterString*. This element is appropriate when the text does not refer to a specific external resource or registry, and it is not necessary to highlight the fact that the text is provided using a particular natural language or locale.


<gmd:keyword>

`  `**<gco:CharacterString>weather data</gco:CharacterString>**

</gmd:keyword>

***Example  STYLEREF 1 \s 2. SEQ Example \\* ARABIC \s 1 2**: A (user-defined) keyword declared using gco:CharacterString.*

When the provided text is a term or code referring to an externally defined explanation or registry value, *gmx:Anchor* element is recommended over *gco:CharacterString*. It contains and additional attribute group enabling linking the provided piece of text with an external describing resource. The most important of these attributes in this context is *xlink:href*, which contains the actual reference in URI[` `Unique Resource Identifier (URI) is a compact sequence of characters that identifies an abstract or physical resource. In the Internet related technical context the URI is defined by the IETF Internet Standard "Uniform Resource Identifier (URI): Generic Syntax" (RFC 3986).
] format.


<gmd:keyword>

`  `**<gmx:Anchor xlink:href="http://inspire.ec.europa.eu/theme/mf">Meteorological geographical features</gmx:Anchor>**

</gmd:keyword>

***Example  STYLEREF 1 \s 2. SEQ Example \\* ARABIC \s 1 3**: A keyword declared using gmx:Anchor element pointing to the controlled vocabulary from which it is taken (in this case, the INSPIRE theme register).*

The text value of the *gmx:Anchor* element should be still be given in addition to the *xlink:href* attribute, and it should be given in a form intended for human observation. If the text is a natural language term, and there is well-known translation of it in the language of the metadata record, the translation could be used as the value of the element.

In the ISO 19139 XML Schema the *gmx:Anchor* element is defined as substitution to *gco:CharacterString* meaning that it is syntactically allowed to use *gmx:Anchor* element instead of *gco:CharacterString* in any parts of the XML document where *gco:CharacterString* element is required by the XML Schema rules.

There is also a third element defined in the ISO 19139 XML Schema for expressing free text: *gmd:PT\_FreeText*. This element is intended for providing textual data with an explicit mention of the locale of the provided text. The *gmd:PT\_FreeText* element is not defined as the head of the substitution group for *gco:CharacterString element*, and thus cannot be used as a drop-in replacement for it in the way that the *gmx:Anchor* element can. However, its structure can still be re-used by dynamically re-typing the parent element using *xsi:type* attribute. Through this mechanism it is possible to narrow down the type of an XML element to a type derived from the one originally defined for the element in the XML Schema rules. In this case the parent elements containing the *gco:CharacterString* element (of type *gco:CharacterString\_PropertyType*) can be locally re-typed to *gmd:PT\_FreeText\_PropertyType* (see  REF \_Ref463631257 \h  \\* MERGEFORMAT Example 2.4).



<gmd:organisationName xsi:type="gmd:PT\_FreeText\_PropertyType">  <gco:CharacterString>Ilmatieteen laitos</gco:CharacterString>  <gmd:PT\_FreeText>    <gmd:textGroup>      <gmd:LocalisedCharacterString locale="#locale-swe">Meteorologiska institutet</gmd:LocalisedCharacterString>    </gmd:textGroup>    <gmd:textGroup>      <gmd:LocalisedCharacterString locale="#locale-en">Finnish Meteorological Institute</gmd:LocalisedCharacterString>    </gmd:textGroup>  </gmd:PT\_FreeText></gmd:organisationName>

***Example  STYLEREF 1 \s 2. SEQ Example \\* ARABIC \s 1 4**: gmd:organisationName element dynamically re-typed to gmd:PT\_FreeText\_PropertyType allowing gmd:PT\_FreeText to be added in addition to gco:CharacterString child element.*

When re-typed, the property element allows both *gco:CharacterString* and *gmd:PT\_FreeText* children to be provided. A *gmd:PT\_FreeText* element may in turn contain zero or more *gmd:textGroup* elements, each containing a localised textual content with an explicit locale attribute referring to a locale *description* with a language code and a character set, and optionally a country. The element *gmd:MD\_Metatada/gmd:locale* may be used for defining the referred locale definitions within the metadata record using a local XPointer URL[` `Uniform Resource Locator is a reference to a web resource that specifies its location on a computer network and a mechanism for retrieving it. A URL is a specific type of Uniform Resource Identifier (URI).
] reference (see Example C.4). Note that providing the *gco:CharacterString* element in addition to the *gmd:PT\_FreeText* element is required to make it easier for automatic metadata processing systems to find the free text content even if they are not able to understand the *gmd:PT\_FreeText* structure.

Note that using explicitly localised free text is usually not required in INSPIRE metadata records, as the entire metadata record must be provided using the same natural language (see section 2.3.1). Localised versions of the metadata records are provided by using the language selection mechanism of the INSPIRE Discovery Service[` `Technical Guidance for the implementation of INSPIRE Discovery Services, version 3.1, section 4.5 Language Requirements
].

**TG Requirement C.seq Req4: metadata/2.0/req/common/free-text**

Free text elements of type *gco:CharacterString\_PropertyType* in INSPIRE metadata shall be expressed in one of the following ways:1. using the *gco:CharacterString* child element,*2. using *gmx:Anchor* child element, or3. re-typing the containing element to *gmd:PT\_FreeText\_PropertyType* using the *xsi:type* attribute and providing both *gco:CharacterString* and *gmd:PT\_FreeText* child elements.For options 1 and 2 the character string content of elements shall be provided in the language of the metadata. For option 3 the definition of the used locale shall be provided either using an URI pointing to a *gmd:MD\_Metadata/gmd:locale* element within the same document or to an externally provided *gmd:PT\_Locale* element. The character string content shall not be empty unless explicitly allowed in the element specific TG Requirements.

For convenience and requirement text brevity reasons a special reserved term "Non-empty Free Text Element" is used in this document where any of these three options is allowed.

**

**/gmd:MD\_Metadata/gmd:locale:**

<gmd:locale>  <gmd:PT\_Locale id="locale-swe">    <gmd:languageCode>      <gmd:LanguageCode        codeList="http://www.loc.gov/standards/iso639-2"        codeListValue="swe">Swedish</gmd:LanguageCode>    </gmd:languageCode>    <gmd:characterEncoding>      <gmd:MD\_CharacterSetCode

`			`codeList="http://standards.iso.org/iso/19139/resources/
gmxCodelists.xml#MD\_CharacterSetCode"         codeListValue="utf8">UTF-8</gmd:MD\_CharacterSetCode>    </gmd:characterEncoding>  </gmd:PT\_Locale></gmd:locale>

***Example  STYLEREF 1 \s 2. SEQ Example \\* ARABIC \s 1 5**:  Locale definition for Swedish language provided for referencing using the gmd:locale element. The gmd:PT\_Locale child element has the id attribute "locale-swe" which can be used as the URL fragment identifier in a local XPointer referring to this element from within the same XML document.*
# ***General requirements***
# **File identifier**
When regularly harvesting metadata from discovery services of several Member States (as done by the EU INSPIRE geoportal), it is helpful to be able to identify duplicate metadata elements and updates of metadata records. This can be ensured by providing a globally unique and persistent identifier of the metadata record through the *fileIdentifier* element.

**TG Recommendation C. seq Rec \r11: metadata/2.0/rec/common/fileIdentifier**

The metadata record should contain a globally unique and persistent *fileIdentifier* element.

Global uniqueness of the *fileIdentifier* can be ensured, for example, by 

- using UUIDs, e.g. 123e4567-e89b-12d3-a456-426655440000, or 
- using an identifier scheme including a country coce prefix, e.g. FR\_IGNF\_BDCARTOr\_3-1\_TOPONYMIE (FR\_<producer>\_<product>\_<version>\_<theme>)

NOTE	The fileIdentifier element is mandatory in [CSW2 AP ISO], which also requires that “to simplify catalogue mining, each *MD\_DataIdentification* instance being part of a *MD\_Metadata* instance must have an identifier having a code value that is equal to the *fileIdentifier* of the owning *MD\_Metadata* instance”.
# **Metadata language**
The element for the language in which the metadata content is provided, is described in [Regulation 1205/2008], Part B, 10.3:


*10.3. Metadata language*

`	`*This is the language in which the metadata elements are expressed.The value domain of this metadata element is limited to the official languages of the Community expressed in conformity with ISO 639-2.*


In the Tables 1 and 2 of [Regulation 1205/2008], Part C, the multiplicity of this element is exactly one for both data sets and services.

**TG Requirement C.seq Req5: metadata/2.0/req/common/metadata-language-code**

The language of the provided metadata content shall be given. It shall be encoded using *gmd:MD\_Metadata*/*gmd:language*/*gmd:LanguageCode* element pointing to one of the three-letter language codes of the ISO 639-2/B code list[` `Attribute codeList shall be "http://www.loc.gov/standards/iso639-2/" and the attribute codeListValue shall contain one of the three-letter bibliographic language code values.
].Only the code values for the official languages of the European Union[` `At the time of writing there are 24 official languages of the EU, see http://ec.europa.eu/languages/policy/linguistic-diversity/official-languages-eu\\_en.htm
] shall be used.The multiplicity of this element is 1.

**TG Recommendation C. seq Rec \r11: metadata/2.0/rec/common/metadata-language-name**

The name of the language(s) of the described resource in the language of the metadata should be used as the text content of the *gmd:LanguageCode* element.
# **Metadata point of contact**
The element for providing the name and contact information for the organisation responsible for the creation of maintenance of the metadata is described in [Regulation 1205/2008], Part B, 10.1:


*10.1. Metadata point of contact*

*This is the description of the organisation responsible for the creation and maintenance of the metadata.* 

*This description shall include:* 

*— the name of the organisation as free text,*

*— a contact e-mail address as a character string*


In the Tables 1 and 2 of [Regulation 1205/2008], Part C, the multiplicity of this element is one or more for both data sets and services.

**TG Requirement C.seq Req6: metadata/2.0/req/common/md-point-of-contact**

Point of contact for the responsible party for the provided metadata shall be given using element *gmd:MD\_metadata*/*gmd:*contact/*gmd:CI\_ResponsibleParty*.The multiplicity of this element is 1..\*.The *gmd:CI\_ResponsibleParty* element shall contain the following child elements:*	The name of the responsible organisation shall be provided as the value of *gmd:organisationName* element with a Non-empty Free Text Element content.The email address of the organisation shall be provided as the value of *gmd:contactInfo*/*gmd:CI\_Contact*/*gmd:address*/*gmd:CI\_Address*/*gmd:electronicMailAddress* element with a Non-empty Free Text Element containing a functioning email address of the responsible party. The value of *gmd:role*/*gmd:CI\_RoleCode* shall point to the value "pointOfContact" of [ISO 19139] code list CI\_RoleCode[` `Attribute codeList shall be "http://standards.iso.org/iso/19139/resources/gmxCodelists.xml#CI\\_RoleCode" and value of codeListValue attribute "pointOfContact"
].

**TG Recommendation C. seq Rec2: metadata/2.0/rec/common/organisation-name**

The name of the organisation should be given in full, without abbreviations. It is recommended to use an email address of the organisation instead of personal email address.

Example fragment of the metadata document fulfilling  REF req\_common\_md\_point\_of\_contact \h  \\* MERGEFORMAT TG Requirement C.6 is given as  REF \_Ref476231200 \h  \\* MERGEFORMAT Example 2.6.


**/gmd:MD\_Metadata/gmd:contact:**

<gmd:contact> <gmd:CI\_ResponsibleParty>   <gmd:organisationName>     <gco:CharacterString>European Commission, Joint Research Centre<gco:CharacterString>   </gmd:organisationName>   <gmd:contactInfo>     <gmd:CI\_Contact>       <gmd:address>         <gmd:CI\_Address>            <gmd:electronicMailAddress>              <gco:CharacterString>

ies-contact@jrc.ec.europa.eu</gco:CharacterString>            </gmd:electronicMailAddress>          </gmd:CI\_Address>        </gmd:address>      </gmd:CI\_Contact>    </gmd:contactInfo>    <gmd:role>      <gmd:CI\_RoleCode

`			`codeList="http://standards.iso.org/iso/19139/resources/gmxCodelists.xml#CI\_RoleCode"

`        `codeListValue="pointOfContact"></gmd:CI\_RoleCode>    </gmd:role>  </gmd:CI\_ResponsibleParty></gmd:contact>

***Example  STYLEREF 1 \s 2. SEQ Example \\* ARABIC \s 1 6**: Providing metadata point of contact information.*

# **Metadata date**
The metadata date element is described in [Regulation 1205/2008], Part B, 10.2:


*10.2. Metadata date*

*The date which specifies when the metadata record was created or updated. This date shall be expressed in conformity with ISO 8601.*


In the Tables 1 and 2 of [Regulation 1205/2008], Part C, the multiplicity of this element is exactly one for both data sets and services.

**TG Requirement C.seq Req7: metadata/2.0/req/common/md-date**

The latest update date of the metadata description shall be given for each metadata record. It shall be encoded using the *gmd:MD\_Metadata*/*gmd:dateStamp* element. If no updates to the metadata have been made since publishing it, the creation date of the metadata shall be used instead.The multiplicity of this element is 1.

# ***Identification info section***
The metadata elements described in this section are contained within the first *gmd:identificationInfo* property of *gmd:MD\_Metadata* element.

Note that *gmd:MD\_DataIdentification* object shall be used as the value of *gmd:identificationInfo* property for data sets and series and *srv:SV\_ServiceIdentification* object used for services, as described in sections 3.1 and 4.1 correspondingly.
# **Resource title**
The elements for the resource is described in [Regulation 1205/2008], Part B, 1.1:


*1.1. Resource title*

*This a characteristic, and often unique, name by which the resource is known.The value domain of this metadata element is free text*


In the Tables 1 and 2 of [Regulation 1205/2008], Part C, the multiplicity of this element is exactly one for both data sets and services. The Implementation Rules requirements above are reflected in this specification as the following Requirement:

**TG Requirement C.seq Req8: metadata/2.0/req/common/resource-title**

A human readable, non-empty title of the described data set, data set series or service shall be provided. It shall be encoded using the *gmd:citation*/*gmd:CI\_Citation/gmd:title* element with a Non-empty Free Text Element content in the language of the metadata.The multiplicity of the element is 1.

**TG Recommendation C. seq Rec3: metadata/2.0/rec/common/resource-title**

The Resource title should be concise and clearly understandable. It should not contain unexplained acronyms or abbreviations. It is recommended a maximum length of 250 characters and keeping the similarity with the original title of the resource, in the sense of the ‘official naming’.

If the data or service is part of a larger project, it is recommended to indicate the Project at the end of the title, in brackets. In case of Project names, abbreviations are allowed, as long as the rest of the title follows the guidelines above and the abbreviation is spelled out immediately in the abstract. 

# **Resource abstract**
The element for the resource abstract is described in [Regulation 1205/2008], Part B, 1.2:


*1.2. Resource abstract*

*This is a brief narrative summary of the content of the resource. The value domain of this metadata element is free text*


In the Tables 1 and 2 of [Regulation 1205/2008, Part C], the multiplicity of this element is exactly one for both data sets and services. The Implementation Rules requirements above are reflected in this specification as the following Requirement:

**TG Requirement C.seq Req9: metadata/2.0/req/common/resource-abstract**

A non-empty brief narrative summary of the content of the described data set, data set series or service shall be provided. It shall be encoded using the *gmd:abstract* element with a Non-empty Free Text Element content in the language of the metadata.The multiplicity of this element is 1.

**TG Recommendation C. seq Rec4: metadata/2.0/rec/common/resource-abstract**

The resource abstract is a succinct description that can include:- A brief summary with the most important details that summarise the data or service- Coverage: linguistic transcriptions of the extent or location in addition to the bounding box- Main attributes- Data sources- Legal references- Importance of the workThe most important details of the description should be summarised in the first sentence or the first 256 characters.Unexplained acronyms should not be used.

# **Responsible organisation and point of contact for the described resource**
The [INSPIRE Directive], Article 5 requires the information about the public authorities responsible for the establishment, management, maintenance and distribution of spatial data sets and services to be included in the metadata. [INSPIRE Directive, Article 11(2)(g)] requires this information to be provided also as search criteria in INSPIRE Discovery Services. The element for describing the responsible party for the resource is given in [Regulation 1205/2008, Part B 9.1 and 9.2]:


*9.1. Responsible party*

*This is the description of the organisation responsible for the establishment, management, maintenance and distribution of the resource.*

*This description shall include:*

``*— the name of the organisation as free text,*

*— a contact e-mail address as a character string.*

*9.2. Responsible party role*

*This is the role of the responsible organisation.*

*The value domain of this metadata element is defined in Part D.*


In the Tables 1 and 2 of [Regulation 1205/2008, Part C], the multiplicity of this element is defined as at least one.

**TG Requirement C.seq Req10: metadata/2.0/req/common/responsible-organisation**

The point of contact for the organisation responsible for the establishment, management, maintenance and distribution of the described resource shall be given using element *gmd:pointOfContact*/*gmd:CI\_ResponsibleParty*.The multiplicity of this element is 1..\*.The *gmd:CI\_ResponsibleParty* element shall contain the following child elements:*	The name of the organisation shall be given as the value of *gmd:pointOfContact*/*gmd:CI\_ResponsibleParty*/*gmd:organisationName* element with a Non-empty Free Text Element content.The email address of the organisation shall be provided as the value of *gmd:pointOfContact*/*gmd:CI\_ResponsibleParty*/*gmd:contactInfo*/*gmd:CI\_Contact*/*gmd:address*/*gmd:CI\_Address*/*gmd:electronicMailAddress* element with a Non-empty Free Text Element containing a functioning email address of the responsible party.The value of *gmd:pointOfContact*/*gmd:CI\_ResponsibleParty*/*gmd:role*/*gmd:CI\_RoleCode* shall point to the most relevant value of ISO 19139 code list CI\_RoleCode[` `Attribute codeList shall be "http://standards.iso.org/iso/19139/resources/gmxCodelists.xml#CI\\_RoleCode".
].

**TG Recommendation C. seq Rec5: metadata/2.0/rec/common/responsible-organisation**

The name of the organisation should be given in full, without abbreviations. It is recommended to use an email address of the organisation instead of personal email address.

The structure and content of the *gmd:pointOfContact* property is the same as the property with same name used for the metadata point of contact (*gmd:MD\_Metadata*/*gmd:contact*). The only exception is the role code, which is restricted only to value "pointOfContact" for metadata point of contact. In here on the contrary the most appropriate value from the code list shall be used for the role code.For an XML example of the responsible party element, see section  REF \_Ref460923763 \r \h 2.2.3.
# **Temporal references**
The Implementation Rule text in [Regulation 1205/2008], Part B 5, and the Tables 1 and 2 in its Part C require at least one of the following temporal references to be given for INSPIRE data sets and services:


*5. TEMPORAL REFERENCE*

``*This metadata element addresses the requirement to have information on the temporal dimension of the data as referred to in Article 8(2)(d) of Directive 2007/2/EC. At least one of the metadata elements referred to in points 5.1 to 5.4 shall be provided. The value domain of the metadata elements referred to in points 5.1 to 5.4 is a set of dates. Each date shall refer to a temporal reference system and shall be expressed in a form compatible with that system. The default reference system shall be the Gregorian calendar, with dates expressed in accordance with ISO 8601.*


Thus one of the following information is required by [Regulation 1205/2008]:

- temporal extent of the described resource,
- date of publication,
- date of last revision or,
- date of creation.

ISO 19115 data model is more demanding than INSPIRE in this respect. Therefore, whilst providing a temporal extent for the resource would suffice to satisfy the [Regulation 1205/2008], it is not enough to be compliant with ISO 19115, which requires to use at least one of date of publication, date of last revision, or the date of creation. Additionally the XML Schema of [ISO 19139] requires the date or time expression to be encoded using [ISO 8601].

To fulfil both INSPIRE and ISO 19115/19139 requirements the following is required in this specification:

**TG Requirement C.seq Req11: metadata/2.0/req/common/temporal-reference**

At least one temporal reference describing the resource shall be given using *gmd:citation/gmd:CI\_Citation/gmd:date/gmd:CI\_Date/gmd:date* element, with one of the following date types:- *publication* for date of publication of the resource,- *revision* for the date of last revision of the resource, or- *creation* for the date of creation of the resource*.*The date type shall be given using the *gmd:citation*/*gmd:CI\_Citation*/*gmd:date*/*gmd:CI\_Date*/*gmd:dateType*/*gmd:CI\_DateTypeCode* element and it shall point to the corresponding value of [ISO 19139] code list CI\_DateTypeCode mentioned above[` `Attribute codeList shall have value "http://standards.iso.org/iso/19139/resources/gmxCodelists.xml#CI\\_DateTypeCode" and the attribute codeListValue one of "publication", "revision" or "creation".
].*The date values shall be expressed using Gregorian calendar and in accordance with [ISO 8601] with either date precision or date and time precision. For date precision the *gmd:CI\_Date*/*gmd:date*/*gco:Date* element, and for date and time precision *gmd:CI\_Date*/*gmd:date*/*gco:DateTime* element shall be used.

Additionally the [Regulation 1205/2008] restricts the multiplicity of the date of last revision and the date of creation to the maximum of one. To comply with these Implementation Rules, the following two Requirements must be fulfilled:

**TG Requirement C.seq Req12: metadata/2.0/req/common/max-1-date-of-creation**

Not more than one date of creation for the described resource shall be given.

**TG Requirement C.seq Req13: metadata/2.0/req/common/max-1-date-of-last-revision**

Not more than one date of last revision for the described resource shall be given.

**TG Recommendation C. seq Rec6: metadata/2.0/rec/common/date-of-last-revision-dataset**

In case of spatial data set, at least the date of the last revision of the spatial data set should be reported.

**TG Requirement C.seq Req14: metadata/2.0/req/common/temporal-extent**

If a temporal reference is provided using the temporal extent, it shall be encoded using the *gmd:extent/gmd:EX\_Extent* element with one or more *gmd:temporalElement/gmd:EX\_TemporalExtent/gmd:extent* child elements. The value of each of these element may be an individual date or a time period between two dates.The multiplicity of this element is 0..\*.A single individual date or a time period shall be encoded using one *gmd:temporalElement/gmd:EX\_TemporalExtent/gmd:extent* element. For individual dates this element shall contain a *gml:TimeInstant/gml:timePosition* element with the date value given according to [ISO 8601].For a single time period the *gmd:temporalElement/gmd:EX\_TemporalExtent/gmd:extent* element shall contain a *gml:TimePeriod* element containing start and end dates of the period. In case the time period is open-ended with either the start or the end date unknown, the elements *gml:startPosition* or *gml:endPosition* may be used with an empty value and the attribute *indeterminatePosition* with value "unknown". If the temporal extent is on-going, the *gml:endPosition* may be used with an empty value and the attribute *indeterminatePosition* with value "now".Individual dates and time periods may be combined to form a complex temporal extent using multiple *gmd:temporalElement/gmd:EX\_TemporalExtent/gmd:extent* elements.

An example XML fragment with only a *gmd:CI\_Citation* element with the revision date of a service provided as the temporal reference, is given as  REF \_Ref463632319 \h  \\* MERGEFORMAT Example 2.7.


**/gmd:MD\_Metadata/gmd:identificationInfo/\*/gmd:citation/gmd:CI\_Citation:**

``<gmd:CI\_Citation>  <gmd:title>    <gco:CharacterString>INSPIRE compliant View Service for the Finnish Cadastral Parcels</gco:CharacterString>  </gmd:title>  <gmd:date>    <gmd:CI\_Date>      <gmd:date>        <gco:Date>2013-02-21</gco:Date>      </gmd:date>      <gmd:dateType>        <gmd:CI\_DateTypeCode

`				`codeList="http://standards.iso.org/iso/19139/resources/
gmxCodelists.xml#CI\_DateTypeCode"

`				`codeListValue="revision">révision</gmd:CI\_DateTypeCode>      </gmd:dateType>    </gmd:CI\_Date>  </gmd:date></gmd:CI\_Citation>

***Example  STYLEREF 1 \s 2. SEQ Example \\* ARABIC \s 1 7**: Revision date for a View Service provided as the only mandatory temporal reference. Note the use of localised French term "révision" as the textual value of the date type code element pointing to the non-localised code list value "revision".*



<gmd:MD\_Metadata …

`	`…

`	`<gmd:identificationInfo>

`		`<gmd:MD\_DataIdentification>

`			`…

`			`<gmd:extent>

`				`<gmd:EX\_Extent>

`					`<gmd:temporalElement>

`						`<**gmd:EX\_TemporalExtent>**

`							`**<gmd:extent>**

`								`**<gml:TimePeriod gml:id="IDd2febbb4-e66f-4ac8-ba76-8fd9bc7c8be6">**

`									`**<gml:beginPosition>2008-01-01T11:45:30</gml:beginPosition>**

`									`**<gml:endPosition>2008-12-31T09:10:00</gml:endPosition>**

`								`**</gml:TimePeriod>**

`							`**</gmd:extent>**

`						`**</gmd:EX\_TemporalExtent>**

`					`</gmd:temporalElement>

`				`</gmd:EX\_Extent>

`			`</gmd:extent>

`			`…

`		`</gmd:MD\_DataIdentification>

`		`…

`	`</gmd:identificationInfo>

`	`…

</gmd:MD\_Metadata>

***Example  STYLEREF 1 \s 2. SEQ Example \\* ARABIC \s 1 8**: Temporal extent*
# **Using keywords**
The keyword value is a commonly used word, formalised word or phrase used to describe the subject. While the topic category is too coarse for detailed queries, keywords help narrowing a full text search and they allow for structured keyword search. [INSPIRE Directive], Article 11(2)(a) requires keyword information to be provided as search criteria in INSPIRE Discovery Services.

Exact references to the controlled vocabulary keywords are necessary for using the keywords in cross-data set and cross-service searches. Specifying the origin of a keyword originating from a controlled vocabulary is described in [Regulation 1205/2008], Part B, 3.2:


*3.2. Originating controlled vocabulary*

``*If the keyword value originates from a controlled vocabulary (thesaurus, ontology), for example GEMET, the citation of the originating controlled vocabulary shall be provided. This citation shall include at least the title and a reference date (date of publication, date of last revision or of creation) of the originating controlled vocabulary.*

**TG Requirement C.seq Req15: metadata/2.0/req/common/keyword-originating-cv**

When using keywords originating from a controlled vocabulary, the originating controlled vocabulary shall be cited using *gmd:descriptiveKeywords*/*gmd:MD\_Keywords/gmd:thesaurusName/gmd:CI\_Citation* element.The title of the vocabulary shall be given using *gmd:title element* with a Non-empty Free Text Element content. *The publication date of the vocabulary shall be given using the gmd:date/gmd:CI\_Date/gmd:date/gco:Date* and *gmd:dateType/gmd:CI\_DateTypeCode[` `Attribute codeList shall have value "http://standards.iso.org/iso/19139/resources/gmxCodelists.xml#CI\\_DateTypeCode" and the attribute codeListValue value "publication".
]* elements.

NOTE	Specifying the correct publication date of the thesaurus is important for knowing which version of the thesaurus has been used.

**TG Recommendation C. seq Rec7: metadata/2.0/rec/common/use-cvs**

If keyword values are made available as a collection of specific, well-defined terms (controlled vocabularies), those should be preferred over free-text terms.

**TG Recommendation C. seq Rec8: metadata/2.0/rec/common/use-anchors-for-cv-keywords**

If the keywords from controlled vocabularies are used and the individual keywords have a specified canonical URI within that controlled vocabulary, these keywords should be encoded using the *gmd:keyword/gmx:Anchor* element. The *xlink:href* attribute of the *gmx:Anchor* element should be used for referring to the canonical URI of the keyword.

**TG Recommendation 1. seq Rec9: metadata/2.0/rec/common/use-anchors-for-thesauri**

For references to well-known thesauri or controlled vocabularies, the *title* element of the *thesaurusName* should be encoded using the *gmd:title/gmx:Anchor* element. The *xlink:href* attribute of the *gmx:Anchor* element should be used for referring to the URI of the thesaurus or controlled vocabulary.


**/gmd:MD\_Metadata/gmd:identificationInfo/gmd:MD\_DataIdentification/gmd:descriptiveKeywords/gmd:MD\_Keywords/gmd:thesaurusName**

`    `<gmd:thesaurusName>

`      `<gmd:CI\_Citation>

`        `<gmd:title>

`          `**<gmx:Anchor xlink:href="http://www.eionet.europa.eu/gemet/inspire\_themes">GEMET - INSPIRE themes, version 1.0</gmx:Anchor>**

`        `</gmd:title>        <gmd:date>          <gmd:CI\_Date>            <gmd:date>              <gco:Date>2008-06-01</gco:Date>            </gmd:date>            <gmd:dateType>              <gmd:CI\_DateTypeCode codeList="http://standards.iso.org/iso/19139/resources/gmxCodelists.xml#CI\_DateTypeCode" codeListValue="publication">publication</gmd:CI\_DateTypeCode>            </gmd:dateType>          </gmd:CI\_Date>        </gmd:date>      </gmd:CI\_Citation>    </gmd:thesaurusName>

***Example  STYLEREF 1 \s 2. SEQ Example \\* ARABIC \s 1 9:** Use of gmx:Anchor elements for the vocabulary title, with a reference to the vocabulary, the GEMET – INSPIRE themes thesaurus in this case.*

In addition, XML fragment documents containing the *CI\_Citation* elements for commonly used thesauri and controlled vocabularies will be made available in the <http://inspire.ec.europa.eu/id/citation/> namespace. References to these *CI\_Citation* fragment documents may be used to encode the specification element by reference, using the *xlink:href* attribute of the *gmd:thesaurusName* element (see  REF \_Ref467573452 \h  \\* MERGEFORMAT Example 2.10). 

NOTE 1	The pre-defined *CI\_Citation* elements will be designed to fulfil TG requirement C.15 and will be made available in different languages. The appropriate language version of the *CI\_Citation* element can be accessed using content negotiation (using the *Accept-Language* HTTP header).

NOTE 2	In order to ensure compatibility with all clients (including those that cannot resolve xlinks**)**, the *gmd:thesaurusName* can also contain the *CI\_Citation* fragment (see  REF \_Ref467573551 \h  \\* MERGEFORMAT Example 2.11 REF \_Ref467568402 \h  \\* MERGEFORMAT **Example 2.19**). In this case, according to [ISO 19136], *"if both a link and content are present in an instance of a property element, then the object found by traversing the xlink:href link shall be the normative value of the property. The object included as content shall be used by the data recipient only if the remote instance cannot be resolved; this may be considered to be a "cached" version of the object."*

The use of *gmx:Anchor* elements and pre-defined XML fragments for *CI\_Citations* will help avoid issues with spelling errors or similar mistakes when providing the *thesaurusName* elements. They will also allow the unique identification of controlled vocabularies in the metadata.


**/gmd:MD\_Metadata/gmd:identificationInfo/gmd:MD\_DataIdentification/gmd:descriptiveKeywords/gmd:MD\_Keywords/gmd:thesaurusName**

`    `<gmd:thesaurusName **xlink:href="http://inspire.ec.europa.eu/id/citation/voc/gemet-inspire-themes-1.0"**/>

***Example  STYLEREF 1 \s 2. SEQ Example \\* ARABIC \s 1 10:** Encoding the thesaurusName by reference to an XML fragment document containing the CI\_Citation element.*


**/gmd:MD\_Metadata/gmd:identificationInfo/gmd:MD\_DataIdentification/gmd:descriptiveKeywords/gmd:MD\_Keywords/gmd:thesaurusName**

`    `<gmd:thesaurusName **xlink:href="http://inspire.ec.europa.eu/id/citation/voc/gemet-inspire-themes-1.0"**>

`      `<gmd:CI\_Citation>

`        `<gmd:title>

`          `<gmx:Anchor xlink:href="http://www.eionet.europa.eu/gemet/inspire\_themes">GEMET - INSPIRE themes, version 1.0</gmx:Anchor>

`        `</gmd:title>        <gmd:date>          <gmd:CI\_Date>            <gmd:date>              <gco:Date>2008-06-01</gco:Date>            </gmd:date>            <gmd:dateType>              <gmd:CI\_DateTypeCode codeList="http://standards.iso.org/iso/19139/resources/gmxCodelists.xml#CI\_DateTypeCode" codeListValue="publication">publication</gmd:CI\_DateTypeCode>            </gmd:dateType>          </gmd:CI\_Date>        </gmd:date>      </gmd:CI\_Citation>    </gmd:thesaurusName>

***Example  STYLEREF 1 \s 2. SEQ Example \\* ARABIC \s 1 11:** Including the CI\_Citation element in addition to a reference to a pre-defined XML fragment document.*


The following keyword grouping requirement is added for ISO 19115 compliance:

**TG Requirement C.seq Req16: metadata/2.0/req/common/group-keywords-by-cv**

All keywords originating from the same controlled vocabulary, or its version, shall be grouped under one *gmd:descriptiveKeywords*/*gmd:MD\_Keywords* element. A single *gmd:MD\_Keywords* element may only contain keywords originating from the one cited controlled vocabulary, or its version.

Further requirements for using keywords are given in the Conformance Class 1 data sets and data set series (section 3.1.2.2), Conformance Class 2 Spatial Data Services (section 4.1.2.2). 



**/gmd:MD\_Metadata/gmd:identificationInfo/\*/gmd:descriptiveKeywords/gmd:MD\_Keywords:**

<gmd:MD\_Keywords>

`  `<gmd:keyword>

`    `<gmx:Anchor xlink:href="http://inspire.ec.europa.eu/theme/ac">Atmospheric conditions</gmx:Anchor>

`  `</gmd:keyword>

`  `<gmd:keyword>

`    `<gmx:Anchor xlink:href="http://inspire.ec.europa.eu/theme/mf">Meteorological geographical features</gmx:Anchor>

`  `</gmd:keyword>

`  `<gmd:thesaurusName>

`    `<gmd:CI\_Citation>

`      `<gmd:title>

`        `<gmx:Anchor xlink:href="http://www.eionet.europa.eu/gemet/inspire\_themes">GEMET - INSPIRE themes, version 1.0</gmx:Anchor>

`      `</gmd:title>

`      `<gmd:date>

`        `<gmd:CI\_Date>

`          `<gmd:date>

`            `<gco:Date>2008-06-01</gco:Date>

`          `</gmd:date>

`          `<gmd:dateType>

`            `<gmd:CI\_DateTypeCode

`			`codeList="http://standards.iso.org/iso/19139/resources/gmxCodelists.xml#CI\_DateTypeCode"

`			`codeListValue="publication" />

`          `</gmd:dateType>

`        `</gmd:CI\_Date>

`      `</gmd:date>

`    `</gmd:CI\_Citation>

`  `</gmd:thesaurusName>

</gmd:MD\_Keywords>

***Example  STYLEREF 1 \s 2. SEQ Example \\* ARABIC \s 1 12**: Using and grouping keywords from controlled vocabularies*

# **Limitations on public access**
The element for the limitations on public access is described in [Regulation 1205/2008], Part B, 8.2:


*8.2. Limitations on public access*

*When Member States limit public access to spatial data sets and spatial data services under Article 13 of Directive 2007/2/EC, this metadata element shall provide information on the limitations and the reasons for them.*

*If there are no limitations on public access, this metadata element shall indicate that fact.*

*The value domain of this metadata element is free text.*


In the Tables 1 and 2 of [Regulation 1205/2008], Part C, the multiplicity of this element is one or more for both data sets and services. 

The Article 13 of the [INSPIRE Directive] contains a list of cases where limitations to public access can be set. Concerning providing the metadata for the data sets and services through Discovery services, the limitations on public access can be set on the base of reasons of international relations, public security or national defence.

Concerning providing View, Download or Transformation Services, or e-commerce services referred to in Article 14(3) of [INSPIRE Directive], limitations on public access can be set on the base of the following reasons ([INSPIRE Directive], Article 13):

*(a)	the confidentiality of the proceedings of public authorities, where such confidentiality is provided for by law;*

*(b)	international relations, public security or national defence;* 

*(c)	the course of justice, the ability of any person to receive a fair trial or the ability of a public authority to conduct an enquiry of a criminal or disciplinary nature;*

*(d)	the confidentiality of commercial or industrial information, where such confidentiality is provided for by national or Community law to protect a legitimate economic interest, including the public interest in maintaining statistical confidentiality and tax secrecy;*

*(e)	intellectual property rights;*

*(f)	the confidentiality of personal data and/or files relating to a natural person where that person has not consented to the disclosure of the information to the public, where such confidentiality is provided for by national or Community law;*

*(g)	the interests or protection of any person who supplied the information requested on a voluntary basis without being under, or capable of being put under, a legal obligation to do so, unless that person has consented to the release of the information concerned;*

*(h)	the protection of the environment to which such information relates, such as the location of rare species.*


ISO 19115 provides a general mechanism for documenting different categories of constraints applicable to the resource (or its metadata). In ISO 19139 XML Schema this mechanism is supported by the element *gmd:MD\_Constraints* and its specifications:

- *gmd:MD\_LegalConstraints* for legal constraints;
- *gmd:MD\_SecurityConstraints* for security constraints.

Since *gmd:MD\_SecurityConstraints* has for many countries only military use, only the element *gmd:MD\_LegalConstraints* is used for this information in the context of this specification.

To make the references to the allowed reasons in Article 13 for limiting public access explicit, an INSPIRE code list (Annex D.1 “Limitations on public access) with all the reason values is used in *gmd:otherConstraints* elements. However, because the domain of the *gmd:otherConstraints* is a character string (free text), the references to the code list values are done using *gmx:Anchor* and its *xlink:href* attribute with the URL pointing to the specified code list value in the INSPIRE Registry.

**TG Requirement C.seq Req17: metadata/2.0/req/common/limitations-on-public-access**

Limitations on public access (or lack of such limitations) for the described resource shall be described using exactly one *gmd:resourceConstraints/gmd:MD\_LegalConstraints* element. This element shall not be the same one as used for describing conditions applying to access and use (see 2.4.7).

The limitations on public access (or lack of such limitations) based on reasons referred to in point (a) or in points (c) to (h) of Article 13(1) of INSPIRE Directive quoted above, the gmd:resourceConstraints/gmd:MD\_LegalConstraints  element shall include a combination of 

\- one instance of *gmd:accessConstraints*/*gmd:MD\_RestrictionCode* element with code list value "otherRestrictions"[` `Attribute codeList with value "http://standards.iso.org/iso/19139/resources/gmxCodelists.xml" and attribute codeListValue "otherRestrictions".
] and- at least one instance of *gmd:otherConstraints*/*gmx:Anchor* pointing to one of the values from the code list for LimitationsOnPublicAccess[` `INSPIRE Registry, attribute xlink:href with URL value starting with "http://inspire.ec.europa.eu/metadata-codelist/LimitationsOnPublicAccess/" and postfixed with one of values of code list LimitationsOnPublicAccess, see Annex D.1
]. If there are no limitations on public access, the element shall point to the code list value "noLimitations".

` `REF \_Ref463952381 \h  \\* MERGEFORMAT Example 2.13 shows a fragment of the metadata document declaring limitation on public access based on Article 13(1) a of the [INSPIRE Directive].


**/gmd:MD\_Metadata/gmd:identificationInfo/\*/gmd:resourceConstraints**:

``<gmd:resourceConstraints>  <gmd:MD\_LegalConstraints>    <gmd:accessConstraints>      <gmd:MD\_RestrictionCode         codeList="http://standards.iso.org/iso/19139/resources/gmxCodelists.xml#MD\_RestrictionCode"         codeListValue="otherRestrictions" />    </gmd:accessConstraints>    <gmd:otherConstraints>      <gmx:Anchor         xlink:href="http://inspire.ec.europa.eu/metadata-codelist/LimitationsOnPublicAccess/INSPIRE\_Directive\_Article13\_1a">

Limitation d’accés public basé sur l’article 13(1) de la directive INSPIRE

`      `</gmx:Anchor>    </gmd:otherConstraints>  </gmd:MD\_LegalConstraints></gmd:resourceConstraints>

***Example  STYLEREF 1 \s 2. SEQ Example \\* ARABIC \s 1 13**: Limitations on public access based on the Article 13(1) a described using a combination of gmd:accessConstraints and gmd:otherConstraints with the xlink:href attribute of the Anchor element pointing to the non-localized code list in the INSPIRE Registry. The textual content of the gmx:Anchor element is given in the language of the metadata (French in this case).*

# **Conditions applying to access and use**
The information about conditions for accessing the spatial data sets and services are discussed in [INSPIRE Directive], Article 5 (b), stating that metadata shall include:


*(b) conditions applying to access to, and use of, spatial data sets and services and, where applicable, corresponding fees;*

[INSPIRE Directive], Article 11(2)(f) requires these conditions to be provided also as search criteria in INSPIRE Discovery Services.

The element for the limitations on public access is described in [Regulation 1205/2008], Part B, 8.1:


*8.1. Conditions applying to access and use*

*This metadata element defines the conditions for access and use of spatial data sets and services, and where applicable, corresponding fees as required by Article 5(2)(b) and Article 11(2)(f) of Directive 2007/2/EC.*

*The value domain of this metadata element is free text.*

*The element must have values. If no conditions apply to the access and use of the resource, ‘no conditions apply’ shall be used. If conditions are unknown, ‘conditions unknown’ shall be used.*

*This element shall also provide information on any fees necessary to access and use the resource, if applicable, or refer to a uniform resource locator (URL) where information on fees is available.*


In the Tables 1 and 2 of [Regulation 1205/2008], Part C, the multiplicity of this element is one or more for both data sets and services. 

**TG Requirement C.seq Req18: metadata/2.0/req/common/conditions-for-access-and-use**

Conditions for access and use of the described resource shall be described using exactly one *gmd:resourceConstraints/gmd:MD\_LegalConstraints* element. This element shall not be the same used for describing limitations on public access (see 2.4.6).

The *gmd:resourceConstraints/gmd:MD\_LegalConstraints* element for conditions for access and use shall be encoded as follows:One instance of either *gmd:accessConstraints* or *gmd:useConstraints* element shall be given. In both cases this element shall contain a *gmd:MD\_RestrictionCode element* with code list value "otherRestrictions"[` `Attribute codeList with value "http://standards.iso.org/iso/19139/resources/gmxCodelists.xml" and attribute codeListValue "otherRestrictions".
].Additionally at least one instance of *gmd:otherConstraints shall be given* describing the actual conditions.If no conditions apply the *gmd:otherConstraints* shall include a *gmx:Ancho*r element pointing to the value "noConditionsApply" in the code list ConditionsApplyingToAccessAndUse[` `INSPIRE Registry, attribute xlink:href with URL value "http://inspire.ec.europa.eu/metadata-codelist/

ConditionsApplyingToAccessAndUse/noConditionsApply", see Annex D.2.
].If the conditions are unknown *gmd:otherConstraints* shall include a *gmx:Anchor* element pointing to the value "conditionsUnknown" in the code list ConditionsApplyingToAccessAndUse[` `INSPIRE Registry, attribute xlink:href with URL value "http://inspire.ec.europa.eu/metadata-codelist/

ConditionsApplyingToAccessAndUse/conditionsUnknown", see Annex D.2.
].In other cases *gmd:otherConstraints* shall include a Non-empty Free Text Element with a textual description of the conditions in the language of the metadata. This text shall include descriptions of terms and conditions, including where applicable, the corresponding fees or an URL pointing to an online resource where these terms and conditions are described.

NOTE	the *gmd:otherConstraints* element shall NOT contain an *gmx:Anchor* link to the code list for LimitationsOnPublicAccess, because it is reserved only for documenting LimitationsOnPublicAccess (see section  REF \_Ref488847553 \r \h 2.3.6).

**TG Recommendation C. seq Rec10: metadata/2.0/rec/common/licences**

For detailed information about the licensing of the resource it is recommended to provide a link to a license type (e.g. <http://creativecommons.org/licenses/by/3.0>), a website or to a document containing the necessary information.

` `REF \_Ref463952654 \h  \\* MERGEFORMAT Example 2.14 shows an XML fragment of a data set metadata record with both limitations on public access and conditions applying to access and use described using separate *gmd:resourceConstraints* elements.


**/gmd:MD\_Metadata/gmd:identificationInfo/\*/gmd:resourceConstraints:**

``<gmd:resourceConstraints>  <gmd:MD\_LegalConstraints>    <gmd:accessConstraints>      <gmd:MD\_RestrictionCode         codeList="http://standards.iso.org/iso/19139/resources/gmxCodelists.xml#MD\_RestrictionCode"         codeListValue="otherRestrictions" />    </gmd:accessConstraints>    <gmd:otherConstraints>      <gmx:Anchor         xlink:href="http://inspire.ec.europa.eu/metadata-codelist/LimitationsOnPublicAccess/noLimitations">

No limitations on public access

`      `</gmx:Anchor>    </gmd:otherConstraints>  </gmd:MD\_LegalConstraints></gmd:resourceConstraints><gmd:resourceConstraints>  <gmd:MD\_LegalConstraints>    <gmd:useConstraints>      <gmd:MD\_RestrictionCode         codeList="http://standards.iso.org/iso/19139/resources/gmxCodelists.xml#MD\_RestrictionCode"         codeListValue="otherRestrictions" />    </gmd:useConstraints>    <gmd:otherConstraints>      <gmx:Anchor         xlink:href="http://inspire.ec.europa.eu/metadata-codelist/

ConditionsApplyingToAccessAndUse/noConditionsApply">

No conditions apply to access and use

`      `</gmx:Anchor>    </gmd:otherConstraints>  </gmd:MD\_LegalConstraints></gmd:resourceConstraints>

***Example  STYLEREF 1 \s 2. SEQ Example \\* ARABIC \s 1 14**: Limitations on public access together with conditions of access and use are provided using two gmd:resourceConstraints elements. In this case there are no limitations on public access nor conditions for access and use. The gmd:useConstraints element is used in this example for declaring conditions for access and use.*

# **Geographic bounding box**
Defining the geographic containing boundary of the described resource enables searches for resources using their area or location of interest. [INSPIRE Directive, Article 11(2)(e)] therefore requires this information to be provided also as search criteria in INSPIRE Discovery Services. 

[Regulation 1205/2008, Part B, 4.1] describes an element intended for this purpose as follows:


*4.1. Geographic bounding box*

*This is the extent of the resource in the geographic space, given as a bounding box.*

*The bounding box shall be expressed with westbound and eastbound longitudes, and southbound and northbound latitudes in decimal degrees, with a precision of at least two decimals.*


The multiplicity of this element is one or more for data sets or data set series as defined in Table 1 and zero or more for services as defined in Table 2 of [Regulation 1205/2008], Part C. For services this information is only required if the described Spatial Data Service has an explicit geographic extent.

**TG Requirement C.seq Req19: metadata/2.0/req/common/bounding-box**

A minimal containing geographic bounding box of the data set or data set series shall be described. This bounding box shall be encoded using one or more *gmd:extent*/*gmd:EX\_Extent*/*gmd:geographicElement*/*gmd:EX\_GeographicBoundingBox* elements.The multiplicity of this element is 1..\* for data sets and data set series, and 0..n for services.The bounding coordinate values for west and east bound longitudes and south and north bound latitudes shall be given in decimal degree values using WGS 84 Coordinate Reference System, as specified for the EX\_GeographicBoundingBox class of the [ISO 19115] data model. The coordinates shall be given with at least 2 decimal precision.


**/gmd:MD\_Metadata/gmd:identificationInfo/\*/gmd:extent:**

<gmd:extent>  <gmd:EX\_Extent>    <gmd:geographicElement>      <gmd:EX\_GeographicBoundingBox>        <gmd:westBoundLongitude>          <gco:Decimal>-15.00</gco:Decimal>        </gmd:westBoundLongitude>        <gmd:eastBoundLongitude>          <gco:Decimal>45.00</gco:Decimal>        </gmd:eastBoundLongitude>        <gmd:southBoundLatitude>          <gco:Decimal>35.00</gco:Decimal>        </gmd:southBoundLatitude>        <gmd:northBoundLatitude>          <gco:Decimal>72.00</gco:Decimal>        </gmd:northBoundLatitude>      </gmd:EX\_GeographicBoundingBox>    </gmd:geographicElement>  </gmd:EX\_Extent></gmd:extent>

***Example  STYLEREF 1 \s 2. SEQ Example \\* ARABIC \s 1 15:** Geographic bounding box for a data set or service provided using gmd:EX\_GeographicBoundingBox.*

# ***Data quality info section***
The metadata elements described in this section are contained within the *gmd:dataQualityInfo/gmd:DQ\_DataQuality* child element of *gmd:MD\_Metadata* element.
# **Conformity**

The declared conformity of the described resource to INSPIRE Implementing Rules and other specifications shall be given in the metadata element Specification and Degree as stated in [Regulation 1205/2008], Part B 7:


*7.1. Specification*

*This is a citation of the implementing rules adopted under Article 7(1) of Directive 2007/2/EC or other specification to which a particular resource conforms.* 

*A resource may conform to more than one implementing rules adopted under Article 7(1) of Directive 2007/2/EC or other specification.*

*This citation shall include at least the title and a reference date (date of publication, date of last revision or of creation) of the implementing rules adopted under Article 7(1) of Directive 2007/2/EC or of the specification.*

*7.2. Degree*

*This is the degree of conformity of the resource to the implementing rules adopted under Article 7(1) of Directive 2007/2/EC or other specification.*

*The value domain of this metadata element is defined in Part D.*


In the Tables 1 and 2 of [Regulation 1205/2008], Part C, the multiplicity of this element is one or more for both data sets and services. 

These conformity declarations help the users of the Discovery services in finding spatial data sets and services conforming to the INSPIRE or other specifications in the use cases where such conformity is required or preferred. Discovery services may contain metadata for both conforming and not conforming to these specifications. [INSPIRE Directive], Article 11(2)(d) requires this information to be provided as search criteria in INSPIRE Discovery Services.

In this specification the above Implementing Rule text is interpreted to mean that the conformity shall be declared at least to the following regulations depending on the described INSPIRE resource type:

- **Data sets and data set series** shall declare conformity to [Regulation 1089/2010].
- **Network Services** should declare conformity to [Regulation 976/2009].
- **Invocable Spatial Data Services** (including interoperable and harmonised Spatial Data Services) shall declare conformity to [Regulation 1089/2010].

The specific TG Requirements for adding these conformity declarations are included in the corresponding Conformance Classes for these resource type. The TG Requirements below shall be followed for encoding the conformity for all of these resource types. 

**TG Requirement C.seq Req20: metadata/2.0/req/common/conformity**

The degree of conformity of the described resource with an INSPIRE Implementing Rule, specification document or Conformance Class, shall be given using one or several *gmd:DQ\_ConformanceResult* elements under *gmd:report*/*gmd:DQ\_DomainConsistency/gmd:result*. For each conformity statement (i.e. for each specification), a separate *gmd:DQ\_ConformanceResult* element shall be used.

The multiplicity of this element is 1..\*.


**/gmd:MD\_Metadata/:**

<dataQualityInfo>

`  `<DQ\_DataQuality>

`    `<scope (…) />

`    `<report>

`      `<DQ\_DomainConsistency>

`        `<result>

`          `<DQ\_ConformanceResult>

`            `(…)

`          `</DQ\_ConformanceResult>

`        `</result>

`      `</DQ\_DomainConsistency>

`    `</report>

`    `<report>

`      `<DQ\_DomainConsistency>

`        `<result>

`          `<DQ\_ConformanceResult>

`            `(…)

`          `</DQ\_ConformanceResult>

`        `</result>

`      `</DQ\_DomainConsistency>

`    `</report>

`  `</DQ\_DataQuality>

</dataQualityInfo>

***Example  STYLEREF 1 \s 2. SEQ Example \\* ARABIC \s 1 16:** Providing several conformity statements*

**TG Requirement C.seq Req21: metadata/2.0/req/common/conformity-specification**

Each *gmd:report*/*gmd:DQ\_DomainConsistency/gmd:result/gmd:DQ\_ConformanceResult* element shall include a citation of the INSPIRE Implementing Rule, specification document or Conformance Class, including its official title and the date of publication of the document, using *gmd:specification*/*gmd:CI\_Citation* element.The title shall be given using the *gmd:title* child element of the citation element with a Non-empty Free Text Element content. For the INSPIRE Implementation Rule documents the value of the title element shall match exactly the official title of the cited document in the language of the metadata.The publication date of the cited document shall be given using *gmd:date* child element. The date value shall be expressed in accordance with ISO 8601 with only the date part included.The date type code element *gmd:date*/*gmd:CI\_Date*/*gmd:dateType*/*gmd:CI\_DateTypeCode* shall be given and it shall point to the value "publication" of the ISO 19139 code list CI\_DateTypeCode[` `Attribute codeList shall have value "http://standards.iso.org/iso/19139/resources/gmxCodelists.xml#CI\\_DateTypeCode" and the attribute codeListValue value "publication".
].

**TG Recommendation C. seq Rec11: metadata/2.0/rec/common/use-anchors-for-specifications**

For references to well-known INSPIRE legal acts, technical guidance documents or conformance classes, the title element of the specification should be encoded using the *gmd:title/gmx:Anchor* element. The *xlink:href* attribute of the *gmx:Anchor* element should be used for referring to the URI of the specification.

**/gmd:MD\_Metadata/gmd:dataQualityInfo/gmd:DQ\_DataQuality/gmd:report/gmd:DQ\_DomainConsistency/gmd:result/gmd:specification**

`    `<gmd:specification>      <gmd:CI\_Citation>        <gmd:title>          **<gmx:Anchor xlink:href="http://data.europa.eu/eli/reg/2010/1089">**COMMISSION REGULATION (EU) No 1089/2010 of 23 November 2010 implementing Directive 2007/2/EC of the European Parliament and of the Council as regards interoperability of spatial data sets and services</**gmx:Anchor**>        </gmd:title>        <gmd:date>          <gmd:CI\_Date>            <gmd:date>              <gco:Date>2010-12-08</gco:Date>            </gmd:date>            <gmd:dateType>              <gmd:CI\_DateTypeCode codeList="http://standards.iso.org/iso/19139/resources/gmxCodelists.xml#CI\_DateTypeCode" codeListValue="publication">publication</gmd:CI\_DateTypeCode>            </gmd:dateType>          </gmd:CI\_Date>        </gmd:date>      </gmd:CI\_Citation>    </gmd:specification>

***Example  STYLEREF 1 \s 2. SEQ Example \\* ARABIC \s 1 17:** Using an gmx:Anchor element for the specification title*

In addition, XML fragment documents containing the *CI\_Citation* elements for the INSPIRE legal acts, technical guidance documents and conformance classes will be made available in the <http://inspire.ec.europa.eu/id/citation/> namespace. References to these *CI\_Citation* fragment documents may be used to encode the specification element by reference, using the *xlink:href* attribute of the *gmd:specification* element (see  REF \_Ref467568104 \h  \\* MERGEFORMAT Example 2.18). 

NOTE 1	The pre-defined *CI\_Citation* elements will be designed to fulfil TG requirement C.21 and will be made available in different languages. The appropriate language version of the *CI\_Citation* element can be accessed using content negotiation (using the *Accept-Language* HTTP header).

NOTE 2	In order to ensure compatibility with all clients (including those that cannot resolve xlinks**)**, the *gmd:specification* can also contain the *CI\_Citation* fragment (see  REF \_Ref467568402 \h  \\* MERGEFORMAT Example 2.19). In this case, according to [ISO 19136], *"if both a link and content are present in an instance of a property element, then the object found by traversing the xlink:href link shall be the normative value of the property. The object included as content shall be used by the data recipient only if the remote instance cannot be resolved; this may be considered to be a "cached" version of the object."*

The use of *gmx:Anchor* elements and pre-defined XML fragments for *CI\_Citations* will help avoid issues with spelling errors or similar mistakes when providing the specification elements. They will also allow the unique identification of specifications in the metadata.

**/gmd:MD\_Metadata/gmd:dataQualityInfo/gmd:DQ\_DataQuality/gmd:report/gmd:DQ\_DomainConsistency/gmd:result/gmd:specification**

`    `<gmd:specification **xlink:href="http://inspire.ec.europa.eu/id/citation/ir/reg-1089-2010"**/>

***Example  STYLEREF 1 \s 2. SEQ Example \\* ARABIC \s 1 18:** Encoding the specification by reference to an XML fragment document containing the CI\_Citation element.*

**/gmd:MD\_Metadata/gmd:dataQualityInfo/gmd:DQ\_DataQuality/gmd:report/gmd:DQ\_DomainConsistency/gmd:result/gmd:specification**

`    `<gmd:specification **xlink:href="http://inspire.ec.europa.eu/id/citation/ir/reg-1089-2010"**>      <gmd:CI\_Citation>        <gmd:title>          <gco:CharacterString>COMMISSION REGULATION (EU) No 1089/2010 of 23 November 2010 implementing Directive 2007/2/EC of the European Parliament and of the Council as regards interoperability of spatial data sets and services</gco:CharacterString>        </gmd:title>        <gmd:date>          <gmd:CI\_Date>            <gmd:date>              <gco:Date>2010-12-08</gco:Date>            </gmd:date>            <gmd:dateType>              <gmd:CI\_DateTypeCode                codeList="http://standards.iso.org/iso/19139/resources/gmxCodelists.xml#CI\_DateTypeCode"                codeListValue="publication">publication</gmd:CI\_DateTypeCode>            </gmd:dateType>          </gmd:CI\_Date>        </gmd:date>      </gmd:CI\_Citation>    </gmd:specification>

***Example  STYLEREF 1 \s 2. SEQ Example \\* ARABIC \s 1 19:** Including the CI\_Citation element in addition to a reference to a pre-defined XML fragment document.*

**TG Requirement C.seq Req22: metadata/2.0/req/common/conformity-degree**

Each *gmd:report*/*gmd:DQ\_DomainConsistency/gmd:result/gmd:DQ\_ConformanceResult* element containing a specification citation described in Requirement C.21 shall also include the degree of declared conformity against this specification using *gmd:pass* property with *gco:Boolean* value of "true" for a conformant resource and "false" for non-conformant resource. If the conformity has not yet been evaluated, the *gmd:pass* element shall be empty and contain a nil reason attribute with value "unknown"[` `Attribute gco:nilReason="unknown".
].


# **Conformance Classes for data sets**
# ***Baseline metadata for data sets and data set series***
**Conformance Class 1: metadata/2.0/datasets-and-series**

**Title:** INSPIRE data sets and data set series baseline metadata**Conformance subject**: Metadata records describing an INSPIRE data set or data set series encoded in ISO 19139 based XML format.A metadata record fulfilling all the TG Requirements of this Conformance Class is compliant with the INSPIRE metadata Implementation Rules for data sets and data set series as defined in [**Regulation 1205/2008**].This Conformance Class includes TG Requirements C.1 – C.22 and TG Requirements 1.1 – 1.11 from this specification.

The metadata elements described in the section 3.1.1 are direct child elements of *gmd:MD\_Metadata* element. The metadata elements contained within properties *gmd:identificationInfo*, *gmd:distributionInfo* and *gmd:dataQualityInfo* are described in sections 3.1.2 - 3.1.4 correspondingly.
# **Direct properties of MD\_Metadata element**
# **Resource type**
The element for declaring the type of the resource is described in [Regulation 1205/2008], Part B, 1.3:


*1.3. Resource type*

*This is the type of resource being described by the metadata. The value domain of this metadata element is defined in Part D.1*


Table 1 contained in Part C of the same document defines the multiplicity of this element to exactly one for data sets and data set series. The resources conforming to this Conformance Class are either datasets or data set series, and thus this Implementation Rule requirement is reflected into the following technical Requirement:

**TG Requirement 1.seq Req \r11: metadata/2.0/req/datasets-and-series/resource-type**

The resource type shall be declared as "dataset" or "series" using the first *gmd:hierarchyLevel* child element* of *gmd:MD\_Metadata.* The *gmd:hierarchyLevel* shall* contain* a *gmd:MD\_ScopeCode* element[` `Attribute codeList with value "http://standards.iso.org/iso/19139/resources/gmxCodelists.xml#MD\\_ScopeCode" and the attribute codeListValue with value "dataset" or "series".
].



/gmd:MD\_Metadata/gmd:hierarchyLevel:

``<gmd:hierarchyLevel>    <gmd:MD\_ScopeCode codeList="http://standards.iso.org/iso/19139/resources/gmxCodelists.xml#MD\_ScopeCode" codeListValue="dataset" />

</gmd:hierarchyLevel>

***Example  STYLEREF 1 \s 3. SEQ Example \\* ARABIC \s 1 1:** Resource type "dataset" given using gmd:hierarchyLevel property.*

# **Identification info section**
The metadata elements described in this section are contained within the first *gmd:identificationInfo* property of the *gmd:MD\_Metadata* element.

**TG Requirement 1.seq Req2: metadata/2.0/req/datasets-and-series/only-one-md-data-identification**

The first gmd:*identificationInfo* property of *gmd:MD\_Metadata* element shall contain only one *gmd:MD\_DataIdentification* element for identifying the described INSPIRE data set or data set series.

The ISO 19139 XML Schema allows more than one *gmd:IdentificationInfo* properties to be given for each *gmd:MD\_Metadata* element. The purpose of this requirement is to harmonise the structure of the ISO 19139 based INSPIRE metadata records by declaring that while more than one instance can be given, readers can safely assume that only the first instance is used for INSPIRE resource identification.

**TG Recommendation 1. seq Rec \r11: metadata/2.0/rec/datasets-and-series/md-element-id**

The *gmd:MD\_DataIdentification* elements should contain a unique identifier of the element itself to be used for referring from within the Spatial Data Service metadata records to indicate a coupled resource. This identifier should be provided as the value of attribute i*d* of *gmd:MD\_DataIdentification* element.This identifier should be persistent for a particular data set or service, and unique within the all the *id* elements of the metadata record document and other XML documents it may appear in (like GetRecords responses of Discovery Service). The persistence of the *id* attributes is important to prevent breaking the coupled resource links between the service metadata and the data set metadata.

NOTE	A unique identifier of the *gmd:MD\_DataIdentification* element is not necessary when building the coupled resource link by providing a Unique Resource Identifier that is resolved to a URL containing an abstract pointer to the gmd:MD\_DataIdentification element (see section  REF \_Ref459284383 \r \h 4.1.2.4).

See  REF \_Ref463959233 \h  \\* MERGEFORMAT Example 3.2 for an example of providing the *id* attribute.

# **Unique resource identifier**
The [Regulation 1205/2008], Part B, 1.5 describes an element for uniquely identifying the described resource: 




*1.5. Unique resource identifier*

*A value uniquely identifying the resource.*

*The value domain of this metadata element is a mandatory character string code, generally assigned by the data owner, and a character string namespace uniquely identifying the context of the identifier code (for example, the data owner).*


Table 1 contained in Part C of the same document defines the multiplicity of this element to one or more for data sets and data set series.

**TG Requirement 1.seq Req3: metadata/2.0/req/datasets-and-series/dataset-uid**

A unique identifier shall be given for each described dataset or data sets series. This identifier shall be a URI consisting of a namespace uniquely identifying a naming context governed by an identifier authority, and a code unique within this namespace.The identifying URI shall be encoded using *gmd:citation*/*gmd:CI\_Citation*/*gmd:identifier*/*\**/*gmd:code* element with a Non-empty Free Text Element content.The multiplicity of this element is 1..\*.

NOTE	The [ISO 19139] xml schemas allow the use of either the *MD\_Identifier* type or its sub-type *RS\_Identifier*, which, in addition to the mandatory *code* property, also contains an optional *codeSpace* property. Since many applications only consider the code attribute and semantically *RS\_Identifier* is intended as an *"identifier (…) for reference systems"* [ISO 19115], the *MD\_Identifier* type should be used wherever possible and the complete URI should be encoded in the code element. This also facilitates the implementation of data-service-coupling based on the unique resource identifier (see also 4.1.2.4).

**TG Recommendation 1. seq Rec \r11: metadata/2.0/rec/datasets-and-series/use\_md\_identifier**

It is strongly recommended to use the *MD\_Identifier* instead of the the *RS\_Identifier* type and to encode the complete URI in the code element. 

In accordance with the Best Practices that are currently being developed for (spatial) data on the web[` `See <https://www.w3.org/TR/dwbp/> and <https://www.w3.org/TR/sdw-bp/> 
], it is recommended to use resolvable and persistent identifiers (in particular, HTTP URIs). This will also make it easier to provide direct links to data sets and their descriptions from outside the INSPIRE infrastructure. 

**TG Recommendation 1. seq Rec2: metadata/2.0/rec/datasets-and-series/resolvable-uid**

It is recommended to make the unique resource identifier resolvable into a document providing information about described data set or data sets series. In the case of HTTP URIs[` `HTTP URIs in the text also include HTTPS URIs
], the public DNS and the usual HTTP URI resolving mechanisms should be used for implementing this resolvability. For other types of URIs, a resolving service should be provided implementing similar functionality.This document retrieved as the result of the resolving process may be, but is not required to be, the metadata description of the described resource. It is also recommended that viewing of the provided document does not require user authentication, authorisation or specialised viewing tools beyond a typical web browser.

**TG Recommendation 1. seq Rec3: metadata/2.0/rec/datasets-and-series/persistent-uid**

The providers of unique resource identifiers should take great care in ensuring that the issued identifiers remain valid and available for the entire availability period of the identified resource, and preferably also after the data set or the data set series has been made unavailable.If a published unique identifier for a resource must be changed during the availability time of the resource, both the old and the new identifier should resolve to the same document described in TG Recommendation 1.2. If this is not possible, the old identifier should resolve to document providing information about the change in the unique identifier and provide the new unique identifier of the described resource.Assigning a published unique resource identifier to another or an extensively restructured data set or data set series should be avoided. Instead a new unique resource identifier should be assigned to the data set in these cases.The persistence and process of preventing breaking the identifier resolvability is crucial for keeping the links between the services and the provided data sets functional.


**/gmd:MD\_Metadata/gmd:identificationInfo/gmd:MD\_DataIdentification:**

``<gmd:MD\_DataIdentification id="md-so-1002001">

`  `<gmd:citation>

`    `<gmd:CI\_Citation>

`      `<gmd:title>        <gco:CharacterString>INSPIRE\_Flurstücke\_ALKIS\_NRW</gco:CharacterString>      </gmd:title>      <gmd:date>        <gmd:CI\_Date>          <gmd:date>            <gco:Date>2016-07-01</gco:Date>          </gmd:date>          <gmd:dateType>            <gmd:CI\_DateTypeCode codeList="http://standards.iso.org/iso/19139/resources/gmxCodelists.xml#CI\_DateTypeCode" codeListValue="publication" />          </gmd:dateType>        </gmd:CI\_Date>      </gmd:date>

`      `<gmd:identifier>        <gmd:MD\_Identifier>          <gmd:code>            <gmx:Anchor xlink:href="https://registry.gdi-de.org/id/de.nw/inspire-cp-alkis"</gmx:Anchor>          </gmd:code>        </gmd:MD\_Identifier>      </gmd:identifier>

`    `</gmd:CI\_Citation>

`  `</gmd:citation>

...

</gmd:MD\_DataIdentification>

***Example  STYLEREF 1 \s 3. SEQ Example \\* ARABIC \s 1 2:** Unique identifier for a INSPIRE ProtectedSites data set given using gmd:identifier element within the gmd:citation element. Note also the recommended id attribute of the gmd:MD\_DataIdentifier to be used for couple resource linking*


# **Keywords for Spatial Data Theme(s)**
The [Regulation 1205/2008], Part B, 3 describes how the Keyword elements shall be used for describing the relevant INSPIRE spatial data themes for the described data set or data set series:


*3. KEYWORD*

*(…)*

*If a resource is a spatial data set or spatial data set series, at least one keyword shall be provided from the general environmental multilingual thesaurus (GEMET) describing the relevant spatial data theme as defined in Annex I, II or III to Directive 2007/2/EC.*


**TG Requirement 1.seq Req4: metadata/2.0/req/datasets-and-series/inspire-theme-keyword**

The INSPIRE Spatial Data Theme(s), to which the data set belongs to, shall be declared using at least one keyword from the INSPIRE Spatial Data Themes vocabulary of the general environmental multilingual thesaurus (GEMET). The keyword values shall be the exact text values of the terms in this vocabulary.These keywords shall be encoded using an *gmd:descriptiveKeywords*/*gmd:MD\_Keywords* element referring to the GEMET INSPIRE themes controlled vocabulary as specified in section 2.4.5. The value of the *gmd:thesaurusName/gmd:CI\_Citation/gmd:title* element shall contain value "GEMET - INSPIRE themes, version 1.0".For each INSPIRE Spatial Data Theme, a *gmd:keyword* element shall be included with the title of the theme as a Non-empty Free Text Element content in the language of the metadata.

**TG Recommendation 1. seq Rec4: metadata/2.0/rec/datasets-and-series/use-anchors-for-gemet**

For references to the GEMET – INSPIRE themes controlled vocabulary, the *title* element of the *thesaurusName* should be encoded using the *gmd:title/gmx:Anchor* element, with the *xlink:href* attribute  referring to <http://www.eionet.europa.eu/gemet/inspire_themes>.

The INSPIRE themes keywords should be encoded using the *gmd:keyword/gmx:Anchor* element, with the *xlink:href* attribute referring to the URI of the theme defined in the GEMET – INSPIRE themes controlled vocabulary.

NOTE	The URIs of the INSPIRE themes are also available in the INSPIRE theme register at <http://inspire.ec.europa.eu/theme>. 

See  REF \_Ref463961442 \h  \\* MERGEFORMAT Example 3.3 for an example of the XML fragment containing GEMET keywords for INSPIRE themes.



**/gmd:MD\_Metadata/gmd:identificationInfo/gmd:MD\_DataIdentification/gmd:descriptiveKeywords/gmd:MD\_Keywords:**

``<gmd:MD\_Keywords>  <gmd:keyword>

`    `<gmx:Anchor xlink:href="http://inspire.ec.europa.eu/theme/ac">Atmospheric conditions</gmx:Anchor>

`  `</gmd:keyword>

`  `<gmd:keyword>

`    `<gmx:Anchor xlink:href="http://inspire.ec.europa.eu/theme/mf">Meteorological geographical features</gmx:Anchor>

`  `</gmd:keyword>  <gmd:thesaurusName>    <gmd:CI\_Citation>      <gmd:title>        <gmx:Anchor xlink:href="http://www.eionet.europa.eu/gemet/inspire\_themes">GEMET - INSPIRE themes, version 1.0</gmx:Anchor>

`      `</gmd:title>      <gmd:date>        <gmd:CI\_Date>          <gmd:date>            <gco:Date>2008-06-01</gco:Date>          </gmd:date>          <gmd:dateType>            <gmd:CI\_DateTypeCode codeList="http://standards.iso.org/iso/19139/resources/gmxCodelists.xml#CI\_DateTypeCode" codeListValue="publication" />          </gmd:dateType>        </gmd:CI\_Date>      </gmd:date>    </gmd:CI\_Citation>  </gmd:thesaurusName></gmd:MD\_Keywords>

***Example  STYLEREF 1 \s 3. SEQ Example \\* ARABIC \s 1 3:** Keywords element for a data set belonging to two INSPIRE Spatial Data Themes: Atmospheric conditions and Meteorological geographical features.*

**TG Recommendation 1. seq Rec5: metadata/2.0/rec/datasets-and-series/additional-keywords**

In addition to the required keywords from the GEMET - INSPIRE themes vocabulary, it is recommended to provide at least two other keywords describing the data set or data set series.
# **Spatial resolution**
Spatial resolution refers to the level of detail of the data set. It shall be expressed as a set of zero to many resolution distances (typically for gridded data and imagery-derived products) or equivalent scales (typically for maps or map-derived products).


*6.2. Spatial resolution*

*Spatial resolution refers to the level of detail of the data set. It shall be expressed as a set of zero to many resolution distances (typically for gridded data and imagery-derived products) or equivalent scales (typically for maps or map-derived products).*

*An equivalent scale is generally expressed as an integer value expressing the scale denominator.*

*A resolution distance shall be expressed as a numerical value associated with a unit of length.*


The [Regulation 1205/2008], Part B, 6.2 describes an element intended for describing this information:

The multiplicity of this element as defined in [Regulation 1205/2008], Part C, Table 1 is zero or more, and it is "mandatory for data sets and data set series if an equivalent scale or a resolution distance can be specified."

**TG Requirement 1.seq Req5: metadata/2.0/req/datasets-and-series/spatial-resolution**

Spatial resolution for data set or data set series shall be given using either equivalent scale or a resolution distance, provided that these have been specified for the described data sets. If both ways have been specified, only one of the ways shall be used. The spatial resolution as equivalent scale shall be encoded using *gmd:spatialResolution*/*gmd:MD\_Resolution*/*gmd:equivalentScale*/*gmd:MD\_RepresentativeFraction*/*gmd:denominator*/*gco:Integer* element.The spatial resolution as resolution distance shall be encoded using *gmd:spatialResolution*/*gmd:MD\_Resolution*/*gmd:distance*/*gco:Distance* element.The multiplicity of this element is 0..n.

**TG Recommendation 1. seq Rec6: metadata/2.0/rec/datasets-and-series/spatial-resolution-interval**

If the spatial resolution is an interval, both bounding values of the interval should be given (either as equivalent scale or resolution distance) as two instances of the *gmd:spatialResolution*/*gmd:MD\_Resolution* element.


**/gmd:MD\_Metadata/gmd:identificationInfo/gmd:MD\_DataIdentification/gmd:spatialResolution:**

<gmd:spatialResolution>  <gmd:MD\_Resolution>    <gmd:equivalentScale>      <gmd:MD\_RepresentativeFraction>        <gmd:denominator>          <gco:Integer>50000</gco:Integer>        </gmd:denominator>      </gmd:MD\_RepresentativeFraction>    </gmd:equivalentScale>  </gmd:MD\_Resolution></gmd:spatialResolution>

***Example  STYLEREF 1 \s 3. SEQ Example \\* ARABIC \s 1 4:** Spatial resolution of a data set expressed using equivalent scale.*


**/gmd:MD\_Metadata/gmd:identificationInfo/gmd:MD\_DataIdentification/gmd:spatialResolution:**

<gmd:spatialResolution>  <gmd:MD\_Resolution>    <gmd:distance>

`      `<gco:Distance uom="dd">0.25</gco:Distance>

`    `</gmd:distance>  </gmd:MD\_Resolution></gmd:spatialResolution>

***Example  STYLEREF 1 \s 3. SEQ Example \\* ARABIC \s 1 5:** Spatial resolution of a data set expressed using distance.*

**

**/gmd:MD\_Metadata/gmd:identificationInfo/gmd:MD\_DataIdentification/gmd:spatialResolution:**

<gmd:spatialResolution>  <gmd:MD\_Resolution>    <gmd:distance>

`      `<gco:Distance uom="dd">0.24</gco:Distance>

`    `</gmd:distance>  </gmd:MD\_Resolution>

`  `<gmd:MD\_Resolution>    <gmd:distance>

`      `<gco:Distance uom="dd">0.26</gco:Distance>

`    `</gmd:distance>  </gmd:MD\_Resolution></gmd:spatialResolution>

***Example  STYLEREF 1 \s 3. SEQ Example \\* ARABIC \s 1 6:** Spatial resolution of a data set expressed using an interval of distances.*

# **Resource language**
The [Regulation 1205/2008], Part B, 1.7 describes an element for the language(s) used within the resource:


*1.7. Resource language*

*The language(s) used within the resource.*

*The value domain of this metadata element is limited to the languages defined in ISO 639-2.*


Table 1 contained in Part C of [Regulation 1205/2008] defines the multiplicity of this element to zero or more for data sets and data set series, allowing it to be left out if the resource does not contain textual information. However, the *gmd:language* property used for encoding this element has multiplicity 1..\* in ISO 19115 and in ISO 19139 XML Schema. To comply with ISO 19155 and the XML Schema rules, the element must always be given.

**TG Requirement 1.seq Req6: metadata/2.0/req/datasets-and-series/resource-language**

For data sets or data set series containing textual information, the language(s) used in the resource shall be given. The language(s) used shall be encoded using one or more *gmd:language*/*gmd:LanguageCode* elements pointing to one of the three-letter language codes of the ISO 639-2/B code list[` `attribute codeList shall be "http://www.loc.gov/standards/iso639-2/" and the attribute codeListValue shall contain one of the three-letter bibliographic language code values.
].

The multiplicity of the *gmd:language* element is 1..\*.If the described resource does not contain textual information expressed in a natural language the special code value "zxx" of the ISO 639-2/B reserved for "no linguistic content; not applicable" shall be used.

**TG Recommendation 1. seq Rec7: metadata/2.0/rec/datasets-and-series/language-name**

The name of the language(s) of the described resource in the language of the metadata should be used as the text content of the *gmd:LanguageCode* element.


**/gmd:MD\_Metadata/gmd:identificationInfo/gmd:MD\_DataIdentification/gmd:language:**

``<gmd:language>  <gmd:LanguageCode      codeList="http://www.loc.gov/standards/iso639-2/"      codeListValue="fin">Suomi</gmd:LanguageCode></gmd:language>

***Example  STYLEREF 1 \s 3. SEQ Example \\* ARABIC \s 1 7:** Resource language for a data set provided in Finnish. Note the content of the gmd:LanguageCode "Suomi": it is the name of the Finnish language in Finnish (the language of the metadata).* 
# **Topic category**
The topic category is a high-level classification scheme to assist in the grouping and topic-based search of available spatial data resources. A correct categorisation is very important to help users to search and find the resources they are looking for.

The [Regulation 1205/2008], Part B, 2.1 describes the topic category element as follows:


*2.1. Topic category*

*The topic category is a high-level classification scheme to assist in the grouping and topic-based search of available spatial data resources.*

*The value domain of this metadata element is defined in Part D.2.*


The topic categories defined in Part D 2 of the [Regulation 1205/2008] are derived directly from the topic categories defined in MD\_TopicCategoryCode (B.5.27 of ISO 19115).

The multiplicity of this element as defined in [Regulation 1205/2008], Part C, Table 1 is one or more.

**TG Requirement 1.seq Req7: metadata/2.0/req/datasets-and-series/topic-category**

The main theme(s) of the data set shall be described using of the ISO 19115 topic category code list values. The topic categories shall be encoded using *gmd:topicCategory*/*gmd:MD\_TopicCategoryCode* element[` `See Part D 2 of [Regulation 1205/2008] for the mapping between topics and INSPIRE themes.
].The multiplicity of this element is 1..\*.

Note that contrary to many other code lists which are defined in the ISO 19139 XML Schema as references to an external code list, *gmd:MD\_TopicCategoryCode* element is defined as a string enumeration.


**/gmd:MD\_Metadata/gmd:identificationInfo/gmd:MD\_DataIdentification/gmd:topicCategory:**

``<gmd:topicCategory>  <gmd:MD\_TopicCategoryCode>environment</gmd:MD\_TopicCategoryCode></gmd:topicCategory>

***Example  STYLEREF 1 \s 3. SEQ Example \\* ARABIC \s 1 8:** Topic category element with enumeration value "environment".*
# **Distribution info section**
The metadata elements described in this section are contained within the *gmd:distributionInfo/gmd:MD\_Distribution* child element of *gmd:MD\_Metadata* element.
# **Resource locator for data set or series**
The Resource Locator is the ‘navigation section’ of a metadata record which point users to the location (URL) where the data can be downloaded, or to where additional information about the resource may be provided.

Setting up the correct resource locators is important for the connection between the data and the services that provide access to them or for providing additional information concerning the resource.

The [Regulation 1205/2008], Part B, 1.4 describes an element intended for describing this information:


*1.4. Resource locator*

*The resource locator defines the link(s) to the resource and/or the link to additional information about the resource.*

*The value domain of this metadata element is a character string, commonly expressed as uniform resource locator (URL).*


The multiplicity of this element as defined in [Regulation 1205/2008], Part C, Table 1 is zero or more, and it is "mandatory if a URL is available to obtain more information on the resource, and/or access related services."

**TG Requirement 1.seq Req8: metadata/2.0/req/datasets-and-series/resource-locator**

A Resource locator linking to the service(s) providing online access to the described data set or data set series shall be given, if such online access is available.If no online access for the data set or data set series is available, but there is a publicly available online resource providing additional information about the described data set or data set series, the URL pointing to this resource shall be given instead.These links shall be encoded using *gmd:transferOptions*/*gmd:MD\_DigitalTransferOptions*/*gmd:onLine*/*gmd:CI\_OnlineResource*/*gmd*: *linkage*/*gmd:URL* element.The multiplicity of this element is 0..n.

A Resource Locator encoded using the gmd:CI\_OnlineResource element may also include *gmd:name*, *gmd:description*, and *gmd:function* properties.

**TG Recommendation 1. seq Rec8: metadata/2.0/rec/datasets-and-series/resource-locator-additional-info**

The *gmd:name*, *gmd:description*, and *gmd:function*/*gmd:CI\_OnLineFunctionCode* child elements of *gmd:CI\_OnlineResource* element containing the given *gmd:linkage* element should also be provided, if possible, to give additional information about the provided URL link. The *gmd:name* and the *gmd:description* elements should contain Non-empty Free Text Elements.If provided, the *gmd:CI\_OnLineFunctionCode* element should point to one of the values of the ISO 19139 code list CI\_OnLineFunctionCode[` `Attribute codeList with value "http://standards.iso.org/iso/19139/resources/gmxCodelists.xml#CI\\_OnLineFunctionCode".
]*.*

**TG Recommendation 1. seq Rec9*: metadata/2.0/rec/datasets-and-series/resource-locator-url***

The URL provided as the value of the *gmd:transferOptions*/*gmd:MD\_DigitalTransferOptions*/*gmd:onLine*/*gmd:CI\_OnlineResource*/*gmd*: *linkage*/*gmd:URL* element should point to one of following type of resources:- direct access for downloading the described data set,- a service metadata (capabilities) document of a Spatial Data Service used for providing this data set,- a service WSDL[` `W3C Web Services Description Language, https://www.w3.org/TR/wsdl
] document of a Spatial Data Service used for providing this data set (if SOAP[` `W3C Simple Object Access Protocol, or more recently, just SOAP, https://www.w3.org/TR/soap/
] binding is available), - a client application that directly accesses the described data set, or- a web page with further instructions for accessing the described data set.


**/gmd:MD\_Metadata/gmd:distributionInfo/gmd:MD\_Distribution/gmd:transferOptions:**

<gmd:transferOptions>  <gmd:MD\_DigitalTransferOptions>    <gmd:onLine>      <gmd:CI\_OnlineResource>        <gmd:linkage>          <gmd:URL>http://example.com/wfs?VERSION=2.0.0&amp;SERVICE=WFS&amp;REQUEST=GetFeature&amp;STOREDQUERY\_ID=urn:ogc:def:query:OGC-WFS::GetFeatureById&amp;ID=123345</gmd:URL>        </gmd:linkage>

`        `<gmd:name>          <gco:CharacterString>WFS GetFeature request for downloading the data set</gco:CharacterString>        </gmd:name>        <gmd:function>          <gmd:CI\_OnLineFunctionCode             codeList="http://standards.iso.org/iso/19139/resources/gmxCodelists.xml#CI\_OnLineFunctionCode"             codeListValue="download" />        </gmd:function>      </gmd:CI\_OnlineResource>    </gmd:onLine>  </gmd:MD\_DigitalTransferOptions></gmd:transferOptions>

***Example  STYLEREF 1 \s 3. SEQ Example \\* ARABIC \s 1 9:** Data set resource locator pointing directly to a WFS GetFeature operation for downloading the described data set.*



**/gmd:MD\_Metadata/gmd:dataQualityInfo/gmd:DQ\_DataQuality/gmd:scope/gmd:DQ\_Scope:**

<gmd:DQ\_Scope>  <gmd:level>    <gmd:MD\_ScopeCode        codeList="http://standards.iso.org/iso/19139/resources/gmxCodelists.xml#MD\_ScopeCode"       codeListValue="dataset" />  </gmd:level></gmd:DQ\_Scope>

***Example  STYLEREF 1 \s 3. SEQ Example \\* ARABIC \s 1 10:** Scope of the Data quality info is set to the entire described data set by giving the code (gmd:level) with value "dataset".*

# **Data quality info section**
The metadata elements described in this section are contained within the *gmd:dataQualityInfo/gmd:DQ\_DataQuality* child element of *gmd:MD\_Metadata* element.

# **Scope**
**TG Requirement 1.seq Req9: metadata/2.0/req/datasets-and-series/one-data-quality-element**

There shall be exactly one *gmd:dataQualityInfo/gmd:DQ\_DataQuality* element scoped to the entire described data set or data set series.The scoping shall be encoded using *gmd:scope*/*gmd:DQ\_Scope*/*gmd:level/gmd:MD\_ScopeCode* element referring to value "dataset" or "series" of ISO 19139 code list MD\_ScopeCode[` `Attribute codeList with value "http://standards.iso.org/iso/19139/resources/gmxCodelists.xml#MD\\_ScopeCode" and the attribute codeListValue with "service".
].

# **Conformity**
In conformance to [INSPIRE Directive], the metadata shall include a statement on the degree of conformity with the specifications against which its conformity has been evaluated.

**TG Requirement 1.seq Req10: metadata/2.0/req/datasets-and-series/conformity**

Metadata for an INSPIRE data set or data set series shall declare conformity to the Implementing Rules for interoperability of spatial data sets and services, and it shall be encoded using *gmd:report*/*gmd:DQ\_DomainConsistency/gmd:result/gmd:DQ\_ConformanceResult* element as specified in  REF req\_common\_conformity \h  \\* MERGEFORMAT TG Requirement C.20[`  `REF req\\_common\\_conformity \h  \\\* MERGEFORMAT TG Requirement C.20: degree of conformity using \*gmd:DQ\\_ConformanceResult.\*
]. This element shall contain citation of the [Regulation 1089/2010] encoded according to  REF req\_common\_conformity\_specification \h  \\* MERGEFORMAT TG Requirement C.21[`  `REF req\\_common\\_conformity\\_specification \h  \\\* MERGEFORMAT TG Requirement C.21: \*gmd:DQ\\_ConformanceResult\* shall include a citation of the specification document, ...
]. The degree of conformity shall be encoded as according to  REF req\_common\_conformity\_degree \h  \\* MERGEFORMAT TG Requirement C.22[`  `REF req\\_common\\_conformity\\_degree \h  \\\* MERGEFORMAT TG Requirement C.22: … \*gmd:DQ\\_ConformanceResult …\* shall also include the degree of declared conformity…
].

**TG Recommendation 1. seq Rec10: metadata/2.0/rec/datasets-and-series/uri-for-regulation-1089-2010**

If providing the specification title as an *gmx:Anchor* element (as recommended in TG Recommendation C.10), the following URI should be used to refer to [Regulation 1089/2010]: <http://data.europa.eu/eli/reg/2010/1089>.

NOTE	A pre-defined XML fragment containing the corresponding *CI\_Citation* element for [Regulation 1089/2010] will be provided at <http://inspire.ec.europa.eu/id/citation/ir/reg-1089-2010>.


**/gmd:MD\_Metadata/gmd:dataQualityInfo/gmd:DQ\_DataQuality/gmd:report/gmd:DQ\_DomainConsistency/gmd:result:**

<gmd:result>  <gmd:DQ\_ConformanceResult>    <gmd:specification xlink:href="http://inspire.ec.europa.eu/id/citation/ir/reg-1089-2010">      <gmd:CI\_Citation>        <gmd:title>          <gmx:Anchor xlink:href="http://data.europa.eu/eli/reg/2010/1089">COMMISSION REGULATION (EU) No 1089/2010 of 23 November 2010 implementing Directive 2007/2/EC of the European Parliament and of the Council as regards interoperability of spatial data sets and services</gmx:Anchor>        </gmd:title>        <gmd:date>          <gmd:CI\_Date>            <gmd:date>              <gco:Date>2010-12-08</gco:Date>            </gmd:date>            <gmd:dateType>              <gmd:CI\_DateTypeCode                codeList="http://standards.iso.org/iso/19139/resources/gmxCodelists.xml#CI\_DateTypeCode"                codeListValue="publication">publication</gmd:CI\_DateTypeCode>            </gmd:dateType>          </gmd:CI\_Date>        </gmd:date>      </gmd:CI\_Citation>    </gmd:specification>    <gmd:explanation>      <gco:CharacterString>This data set is conformant with the INSPIRE Implementing Rules for the interoperability of spatial data sets and services</gco:CharacterString>    </gmd:explanation>    <gmd:pass>      <gco:Boolean>true</gco:Boolean>    </gmd:pass>  </gmd:DQ\_ConformanceResult></gmd:result>

***Example  STYLEREF 1 \s 3. SEQ Example \\* ARABIC \s 1 11:** Conformity declaration against the [Regulation 1089/2010].*

Metadata for an INSPIRE data set or data set series can also include additional declarations of conformity, in particular to the abstract test suites and conformance classes defined for the INSPIRE data specifications.

**TG Recommendation 1. seq Rec11: metadata/2.0/rec/datasets-and-series/uris-for-ats-and-cc**

If declaring conformity to an abstract test suite or a conformance class using an *gmx:Anchor* element (as recommended in  REF rec\_common\_anchors\_for\_specifications \h  \\* MERGEFORMAT TG Recommendation C.11), the URI identifying the abstract test suite or a conformance class should be used in the *xlink:href* attribute of the specification title element.

NOTE	It is not currently planned to provide pre-defined XML fragments containing the *CI\_Citation* elements for the INSPIRE TG documents in the <http://inspire.ec.europa.eu/id/citation/> namespace. However, such fragments can be added if this is deemed useful by INSPIRE data providers.

**

**/gmd:MD\_Metadata/gmd:dataQualityInfo/gmd:DQ\_DataQuality/gmd:report/gmd:DQ\_DomainConsistency/gmd:result:**

<gmd:result>  <gmd:DQ\_ConformanceResult>    <gmd:specification>      <gmd:CI\_Citation>        <gmd:title>          **<gmx:Anchor xlink:href="http://inspire.ec.europa.eu/id/ats/data-hy/3.1">D2.8.I.8 Data Specification on Hydrography – Technical Guidelines, version 3.1</gmx:Anchor>**        </gmd:title>        <gmd:date>          <gmd:CI\_Date>            <gmd:date>              <gco:Date>2014-04-17</gco:Date>            </gmd:date>            <gmd:dateType>              <gmd:CI\_DateTypeCode                codeList="http://standards.iso.org/iso/19139/resources/gmxCodelists.xml#CI\_DateTypeCode"                codeListValue="publication">publication</gmd:CI\_DateTypeCode>            </gmd:dateType>          </gmd:CI\_Date>        </gmd:date>      </gmd:CI\_Citation>    </gmd:specification>    <gmd:explanation>      <gco:CharacterString>This data set is conformant with the INSPIRE Data Specification on Hydrography – Technical Guidelines, version 3.1</gco:CharacterString>    </gmd:explanation>    <gmd:pass>      <gco:Boolean>true</gco:Boolean>    </gmd:pass>  </gmd:DQ\_ConformanceResult></gmd:result>

***Example  STYLEREF 1 \s 3. SEQ Example \\* ARABIC \s 1 12:** Conformity declaration against an Abstract Test Suite.*

# **Lineage**
The processing history of result data set or data set series can provide valuable information about the applicability of the data for a particular use. This information may include information on the source data used and the main transformation steps that took place in creating the current data set or data set series.


*6.1. Lineage*

*This is a statement on process history and/or overall quality of the spatial data set. Where appropriate it may include a statement whether the data set has been validated or quality assured, whether it is the official version (if multiple versions exist), and whether it has legal validity.*

*The value domain of this metadata element is free text.*


The [Regulation 1205/2008], Part B, 6.1 describes an element intended for describing this information:

The multiplicity of this element as defined in [Regulation 1205/2008], Part C, Table 1 is one.

**TG Requirement 1.seq Req11: metadata/2.0/req/datasets-and-series/lineage**

The lineage statement for the described data set or data set series shall be given. It shall be included in the *gmd:dataQualityInfo*/*gmd:DQ\_DataQuality* element scoped to the entire described data sets or data sets series as specified by  REF req\_data\_one\_dq\_element \h  \\* MERGEFORMAT TG Requirement 1.9.The lineage shall be encoded using the *gmd:lineage*/*gmd:LI\_Lineage*/*gmd:statement* element with a Non-empty Free Text Element content, and it shall contain the description of the lineage of the described data set or series.The multiplicity of this element is 1.

**TG Recommendation 1. seq Rec12: metadata/2.0/rec/datasets-and-series/use-iso-dq-elements-and-measures**

If a data provider has a procedure for the quality management of their spatial data set (series) then the appropriate ISO data quality elements and measures should be used to evaluate and report (in the metadata) the results in addition to the Lineage metadata element.

**TG Recommendation 1. seq Rec13: metadata/2.0/rec/datasets-and-series/lineage-avoid-acronyms**

The use of abbreviations (including acronyms) should be avoided. If used, their meaning should be explained. 



# ***Interoperability metadata for data sets and data set series***
**Conformance Class 2: metadata/2.0/*isdss***

**Title:** INSPIRE data sets and data set series interoperability metadata**Conformance subject**: Metadata records describing INSPIRE data sets or data set series encoded in ISO 19139 based XML format.Metadata record fulfilling all the Requirements of this Conformance Class is compliant with the INSPIRE metadata Implementation Rules for data sets and data set series as defined in [Regulation 1205/2008] and Article 13 "Metadata required for Interoperability" of [Regulation 1089/2010] and its amendment [Regulation 1253/2013].This Conformance Class includes TG Requirements C.1 – C.22, TG Requirements 1.1 – 1.11 and TG Requirements 2.1 – 2.8 from this specification.

The metadata elements described in the section 3.2.1 are direct child elements of *gmd:MD\_Metadata* element. The metadata elements contained within elements *gmd:identificationInfo*, *gmd:distributionInfo* and *gmd:dataQualityInfo* are described in sections 3.2.2 - 3.2.4 correspondingly.
# **Direct properties of MD\_Metadata element**
# **Coordinates reference systems**
Describing the coordinate reference system(s) used in the data set makes discovering data sets with spatial coordinates provided in desired reference systems possible.

The [Regulation 1089/2010], Article 13 (1) describes an element intended for describing this information:


*1. 	Coordinate Reference System: Description of the coordinate reference system(s) used in the data set.*


The multiplicity of this element is one or more.

The [Regulation 1089/2010], Annex II, 1.5 states that the coordinate reference system identifiers used must originate from a common register:


*1.5. Coordinate Reference System Identifiers*
\*


*1. Coordinate reference system parameters and identifiers shall be managed in one or several common registers for coordinate reference systems.*

*2. Only identifiers contained in a common register shall be used for referring to the coordinate reference systems listed in this Section.*


**TG Requirement 2.seq Req \r11: metadata/2.0/req/isdss/crs**

The coordinate reference system(s) used in the described data set or data set series shall be given using element *gmd:referenceSystemInfo/gmd:MD\_ReferenceSystem/gmd:referenceSystemIdentifier/gmd:RS\_Identifier*.The multiplicity of this element is 1..\*.The *gmd:code* child element of *gmd:RS\_Identifier* is mandatory. The *gmd:codeSpace* child element shall be used if the code alone does not uniquely identify the referred coordinate reference system. Both *gmd:code* and *gmd:codeSpace* element (if given) shall contain Non-empty Free Text Elements.Only the coordinate reference system identifiers specified in a well-known common register shall be used.

**TG Recommendation 2. seq Rec \r11: metadata/2.0/rec/isdss/source-crs**

If the data set is provided through a download service that provides coordinate transformation functionality (i.e. allows to provide the data set in any coordinate reference system supported by the service), the source coordinate reference system(s) of the data set should be documented in the metadata.

**TG Requirement 2.seq Req2: metadata/2.0/req/isdss/crs-id**

If the coordinate reference system is listed in the table Default Coordinate Reference System Identifiers in Annex  REF \_Ref465002404 \n \h D.4, the value of the HTTP URI Identifier column shall be used as the value of *gmd:referenceSystemInfo/gmd:MD\_ReferenceSystem/
gmd:referenceSystemIdentifier/gmd:RS\_Identifier/gmd:code* element.The *gmd:codeSpace* element shall not be used in this case.


**/gmd:MD\_Metadata/gmd:referenceSystemInfo:**

<gmd:referenceSystemInfo>  <gmd:MD\_ReferenceSystem>    <gmd:referenceSystemIdentifier>      <gmd:RS\_Identifier>        **<gmd:code>          <gmx:Anchor xlink:href="http://www.opengis.net/def/crs/EPSG/0/4258">EPSG:4258</gmx:Anchor>        </gmd:code>**      </gmd:RS\_Identifier>    </gmd:referenceSystemIdentifier>  </gmd:MD\_ReferenceSystem></gmd:referenceSystemInfo>

***Example  STYLEREF 1 \s 3. SEQ Example \\* ARABIC \s 1 13:** The coordinate reference system ETRS89-GRS80 declared as used in the provided data set using the gmx:Anchor free text element.*

Some data sets (e.g. polulation distribution or health statistics) may have no direct spatial reference (i.e. a geometry attribute), but only an indirect one (e.g. to a statistical or administrative unit). In such cases, the data set providing the spatial reference (e.g. a data set of the NUTS statistical regions) should be considered as the spatial reference system for the data set. According to [ISO 19112], such reference systems are called “spatial reference systems using geographic identifiers”, but these are not conisered by [ISO 19139].

**TG Recommendation 2. seq Rec2: metadata/2.0/rec/isdss/srs-using-geographic-identifiers**

Also spatial reference systems using geographic identifiers should be identified using the element *gmd:referenceSystemInfo/gmd:MD\_ReferenceSystem/
gmd:referenceSystemIdentifier/gmd:RS\_Identifier/gmd:code*. A *gmx:Anchor* element should be used, whose *xlink:href* attribute refers to a URI that provides further information about the spatial reference systems using geographic identifiers.

NOTE	Best practices and examples on what URIs to use for spatial reference systems using geographic identifiers should be discussed on the thematic clusters platform[` `e.g. in the Statistical Cluster (<https://themes.jrc.ec.europa.eu/groups/profile/45/statistical-units-population-distribution-human-health-and-safety>)
].


**/gmd:MD\_Metadata/gmd:referenceSystemInfo:**

<gmd:referenceSystemInfo>  <gmd:MD\_ReferenceSystem>    <gmd:referenceSystemIdentifier>      <gmd:RS\_Identifier>        **<gmd:code>          <gmx:Anchor xlink:href="http://publications.europa.eu/resource/authority/atu">Administrative territoral units NAL</gmx:Anchor>        </gmd:code>**      </gmd:RS\_Identifier>    </gmd:referenceSystemIdentifier>  </gmd:MD\_ReferenceSystem></gmd:referenceSystemInfo>

***Example  STYLEREF 1 \s 3. SEQ Example \\* ARABIC \s 1 14:** Anchor element referring to a spatial reference systems using geographic identifiers (the list of the various administrative territorial units of the EU Member States, published by the EU Publications Office).*

# **Temporal reference systems**
Describing the temporal reference system(s) used in the data set makes discovering data sets with temporal coordinates provided in desired reference systems possible. 

The [Regulation 1089/2010], Article 13 (2) describes an element intended for describing this information:


*2. 	Temporal Reference System: Description of the temporal reference system(s) used in the data set.This element is mandatory only if the spatial data set contains temporal information that does not refer to the default temporal reference system.*


The multiplicity of this element is zero or more: it is not required if all temporal information in the data set uses the default temporal reference system. The default temporal reference system as regards to the INSPIRE metadata is Gregorian Calendar as defined in [Regulation 1205/2008], Annex, Part B, point 5.

**TG Requirement 2.seq Req3: metadata/2.0/req/isdss/temportal-rs**

The temporal reference system(s) used in the described data set or data set series shall be given using element *gmd:referenceSystemInfo/gmd:MD\_ReferenceSystem/gmd:referenceSystemIdentifier/gmd:RS\_Identifier*.The multiplicity of this element is 0..n.The *gmd:code* child element of *gmd:RS\_Identifier* is mandatory. The *gmd:codeSpace* child element shall be used if the code alone does not uniquely identify the referred coordinate reference system. Both *gmd:code* and *gmd:codeSpace* element (if given) shall contain Non-empty Free Text Elements.

**TG Recommendation 2. seq Rec \r11: metadata/2.0/rec/isdss/**

If a commonly known unique identifier for the referred temporal reference system is available in a common register, the registered identifier should be used as the value of the *gmd:referenceSystemInfo/gmd:MD\_ReferenceSystem/gmd:referenceSystemIdentifier/gmd:RS\_Identifier/gmd:code* element.

NOTE	The OGC Temporal Domain Working Group (TemporalDWG)[` `OGC TemporalDWG wiki: <http://external.opengeospatial.org/twiki\_public/TemporalDWG/WebHome> 
] is working on an OGC Best Practice document covering temporal coordinate reference systems and their identifiers. Unfortunately at the time of writing this document was still in early draft version. It is expected that the unambiguous identification of temporal reference systems will become easier in the future as the OGC Naming Authority will endorse HTTP URI format identifiers for the most typically used temporal reference systems.


**/gmd:MD\_Metadata/gmd:referenceSystemInfo:**

<gmd:referenceSystemInfo>  <gmd:MD\_ReferenceSystem>    <gmd:referenceSystemIdentifier>      <gmd:RS\_Identifier>        <gmd:code>          <gco:CharacterString>Julian calendar</gco:CharacterString>        </gmd:code>      </gmd:RS\_Identifier>    </gmd:referenceSystemIdentifier>  </gmd:MD\_ReferenceSystem></gmd:referenceSystemInfo>

***Example  STYLEREF 1 \s 3. SEQ Example \\* ARABIC \s 1 15:** Julian calendar declared as the temporal reference system used in the provided data set.*

# **Identification info section**
The metadata elements described in this section are contained within the first *gmd:identificationInfo/gmd:MD\_DataIdentification* child element of the *gmd:MD\_Metadata* element.
# **Spatial representation type**
The type in which the spatial data is represented may be of importance when evaluating the fit for purpose of the data set. The [Regulation 1089/2010], Article 13 (6) amended by [Regulation 1253/2013] describes an element intended for describing this information:


*6. Spatial Representation Type: The method used to spatially represent geographic information.*


The multiplicity of this element is one or more. From the values allowed in [ISO 19139], only the values vector, grid, TIN[` `TIN stands for triangulated irregular network. TIN is a digital data structure used in a geographic information system (GIS) for the representation of a surface.
] and textTable[` `The value textTable was added to the values originally suggested in the data specifications, for data sets with an indirect spatial reference.
] should be used. 

**TG Requirement 2.seq Req4:** **metadata/2.0/req/isdss/spatial-representation-type**

The spatial representation type shall be given using element *gmd:spatialRepresentationType/gmd:MD\_SpatialRepresentationTypeCode* referring to one of the values of ISO 19139 code list MD\_SpatialRepresentationTypeCode and one of the code list values "vector", "grid",  "tin" or “textTable”[` `Attribute codeList with value "http://standards.iso.org/iso/19139/resources/gmxCodelists.xml#MD\\_SpatialRepresentationTypeCode" and attribute codeListValue with value "vector", "grid", "tin" or “textTable”.
].Multiplicity of this element is 1..\*.


**/gmd:MD\_Metadata/gmd:identificationInfo/gmd:MD\_DataIdentification/gmd:spatialRepresentationType**

<gmd:spatialRepresentationType>  <gmd:MD\_SpatialRepresentationTypeCode    codeList="http://standards.iso.org/iso/19139/resources/gmxCodelists.xml#MD\_SpatialRepresentationTypeCode"    codeListValue="vector" /></gmd:spatialRepresentationType>

***Example  STYLEREF 1 \s 3. SEQ Example \\* ARABIC \s 1 16**: Spatial representation type of the described data set described as vector.*

# **Character encoding**
The character encoding describes the way the characters of the textual information are encoded in the described data set. The [Regulation 1089/2010], Article 13 (5) describes an element intended for describing this information:


*5. Character Encoding: The character encoding used in the data set.*

*This element is mandatory only if an encoding is used that is not based on UTF-8.*

The multiplicity of this element is zero or more: this element is only required if there are non UTF-8 based character encodings used in the data set. UTF-8 is an 8-bit variable size Universal Coded Character Set (UCS) transfer format specified in [ISO 10646][` `ISO 10646:2014 is downloadable from ISO/IEC Information Technology Task Force (ITTF) web site, http://standards.iso.org/ittf/PubliclyAvailableStandards/index.html
], section 9.2.

**TG Requirement 2.seq Req5: metadata/2.0/req/isdss/character-encoding**

The character encoding(s) shall be given for data sets and data sets series which use encodings not based on UTF-8 by using element *gmd:characterSet/gmd:MD\_CharacterSetCode* referring to one of the values of ISO 19139 code list MD\_CharacterSetCode[` `Attribute codeList with value "http://standards.iso.org/iso/19139/resources/gmxCodelists.xml#MD\\_CharacterSetCode".
].The multiplicity of this element is 0..n.If more than one character encoding is used within the described data set or data sets series, all used character encodings, including UTF-8 (code list value "utf8"), shall be given using this element.

NOTE	UTF-8 should be used for character encoding of INSPIRE data sets and data set series unless there are compelling and overriding reasons not to use it.


**/gmd:MD\_Metadata/gmd:identificationInfo/gmd:MD\_DataIdentification/gmd:characterSet**

<gmd:characterSet>  <gmd:MD\_CharacterSetCode codeList="http://standards.iso.org/iso/19139/resources/gmxCodelists.xml#MD\_CharacterSetCode" codeListValue="8859part1" /></gmd:characterSet>

***Example  STYLEREF 1 \s 3. SEQ Example \\* ARABIC \s 1 17**: ISO/IEC 8859-1 (also known as Latin 1) declared as the character encoding of the described data set.*

# **Distribution info section**
The metadata elements described in this section are contained within the *gmd:distributionInfo/gmd:MD\_Distribution* child element of *gmd:MD\_Metadata* element.

# **Data encoding**

To be able to determine if the data is encoded in a structure and format the can be accessed using the tools and data processing systems available in users' environments, it is necessary to declare the encoding in metadata. The [Regulation 1089/2010], Article 13 (3) describes an element intended for describing this information:


*3. Encoding: Description of the computer language construct(s) specifying the representation of data objects in a record, file, message, storage device or transmission channel.*


The multiplicity of this element is one or more.

**TG Requirement 2.seq Req6: metadata/2.0/req/isdss/data-encoding**

The encoding and the storage or transmission format of the provided data sets or data set series shall be given using the *gmd:distributionFormat/gmd:MD\_Format* element.The multiplicity of this element is 1..\*.The *gmd:name* and *gmd:version* child elements of *gmd:MD\_Format* are mandatory. Both of these elements shall contain Non-empty Free Text Elements.If the version of the encoding is unknown or if the encoding is not versioned, the *gmd:version* shall be left empty and the nil reason attribute shall be provided with either value "unknown" or "inapplicable" correspondingly[` `Attribute gco:nilReason="unknown" or "inapplicable".
].


**/gmd:MD\_Metadata/gmd:distributionInfo/gmd:distributionFormat:**

<gmd:distributionFormat>  <gmd:MD\_Format>    <gmd:name>      <gco:CharacterString>Addresses GML Application Schema</gco:CharacterString>

`    `</gmd:name>    <gmd:version>      <gco:CharacterString>3.0</gco:CharacterString>    </gmd:version>    <gmd:specification>      <gco:CharacterString>D2.8.I.5 Data Specification on Addresses – Technical Guidelines</gco:CharacterString>    </gmd:specification>  </gmd:MD\_Format>  </gmd:distributionFormat>  <gmd:distributionFormat>    <gmd:MD\_Format>      <gmd:name>        <gmx:Anchor xlink:href="http://inspire.ec.europa.eu/media-types/application/x-shapefile">Esri Shapefile</gmx:Anchor>      </gmd:name>    <gmd:version gco:nilReason="unknown" />  </gmd:MD\_Format></gmd:distributionFormat>

***Example  STYLEREF 1 \s 3. SEQ Example \\* ARABIC \s 1 18:** Data set has been declared to be available both in the INSPIRE Addresses GML Application Schema (encoded in XML) and in Esri Shapefile format. The gmx:Anchor is used to describe the latter, as the format is included in the code list for supported INSPIRE media types.*

# **Data quality info section**
The metadata elements described in this section are contained within the *gmd:dataQualityInfo/gmd:DQ\_DataQuality* child element of *gmd:MD\_Metadata* element.

# **Topological consistency**
Topological consistency is an important aspect of the data quality of a spatial data set: it describes trustworthiness and consistency of the geometry property values of the data set. Examples of such consistency measures would be number of incorrect line intersections, incorrectly closed polygons, duplicate curves or gaps in curves. These measures fall under a wider category of logical consistency of the data set. Topological consistency metadata element is described in [Regulation 1089/2010], Article 13 (4):


*4. Topological Consistency: Correctness of the explicitly encoded topological characteristics of the data set as described by the scope.*


The multiplicity of this element is zero or more with the following condition: The element is mandatory if the data set includes types from the Generic Network Model and does not assure centreline topology (connectivity of centrelines) for the network.

While the [Regulation 1089/2010] does not provide further guidance on how this element should be reported, the INSPIRE Data specifications include guidance on reporting topological consistency in two ways based on [ISO 19157]: by providing quantitative and descriptive results of the tests or checks done for the described data set. The former are expressed as numerical result values of specific topological consistency tests, and the latter by textual descriptions of the topological consistency checks.

**Providing quantitative results**

**TG Requirement 2.seq Req7: metadata/2.0/req/isdss/topological-consistency-quantitative-results**

The quantitative results for topological consistency measures shall be reported using the *gmd:report/gmd:DQ\_TopologicalConsistency* element with a *gmd:DQ\_QuantitativeResult* element as the value of its mandatory *gmd:result* property.The multiplicity of the element is 0..\*.The *gmd:valueUnit* and *gmd:value/gco:Record* child elements of *gmd:DQ\_QuantitativeResult* are mandatory and shall be used for giving a numerical or otherwise quantitative value of the evaluated topology consistency measure for the described data set or data set series.The type of the *gmd:value/gco:Record* element shall be chosen based on the result type of the particular measure, and it shall be declared using the *xsi:type* attribute of the *gco:Record element*.

**TG Recommendation 2. seq Rec2: metadata/2.0/rec/isdss/topological-consistency-measure-name**

The name of the topology consistency measure should be provided using the *gmd:nameOfMeasure* child element of each of the *gmd:DQ\_QuantitativeResult* elements*.* This element is a Non-empty Free Text Element. In the case where the result reflects more than one measure, a separate *gmd:nameOfMeasure* should be given to identify each included measure.

**TG Recommendation 2. seq Rec3: metadata/2.0/rec/isdss/topological-consistency-evaluation-method**

It is recommended to provide a short description of the evaluation method used for topological consistency check using the gmd:evaluationMethodDescription child element of  *gmd:DQ\_QuantitativeResult* element*.* This element is a Non-empty Free Text Element.If applicable, the evaluation method type should be declared using the *gmd:evaluationMethodType/gmd:DQ\_EvaluationMethodTypeCode* child element of *gmd:DQ\_QuantitativeResult* element referring to one of the values of ISO 19139 code list DQ\_EvaluationMethodTypeCode[` `Attribute codeList with value "http://standards.iso.org/iso/19139/resources/gmxCodelists.xml#DQ\\_EvaluationMethodTypeCode"
].

**TG Recommendation 2. seq Rec4: metadata/2.0/rec/isdss/topological-consistency/date**

It is recommended to provide the date of evaluating the topological consistency check using the *gmd:dateTime/gco:DateTime* child element of  *gmd:DQ\_QuantitativeResult* element*.* The value shall be expressed using Gregorian calendar and in accordance with [ISO 8601] date and time precision.

` `REF \_Ref463969082 \h  \\* MERGEFORMAT Example 3.19 contains an example of the quantitative results of one measure for the topological consistency evaluated for a data set in the INSPIRE Hydrography theme.

**/gmd:MD\_Metadata/gmd:dataQualityInfo/gmd:DQ\_DataQuality/gmd:report/gmd:DQ\_TopologicalConsistency:**

<gmd:DQ\_TopologicalConsistency>

`  `<gmd:nameOfMeasure>

`    `<gco:CharacterString>number of faulty point-curve connections</gco:CharacterString>

`  `</gmd:nameOfMeasure>

`  `<gmd:evaluationMethodType>

`    `<gmd:DQ\_EvaluationMethodTypeCode

`      `codeList="http://standards.iso.org/iso/19139/resources/gmxCodelists.xml#DQ\_EvaluationMethodTypeCode"

`      `codeListValue="indirect">Indirect</gmd:DQ\_EvaluationMethodTypeCode>

`  `</gmd:evaluationMethodType>

`  `<gmd:evaluationMethodDescription>

`    `<gco:CharacterString>A point-curve connection exists where different curves touch. These curves have an intrinsic topological relationship that shall reflect the true constellation. If the point-curve connection contradicts the universe of discourse, the point-curve connection is faulty with respect to this data quality measure. The data quality measure counts the number of errors of this kind.</gco:CharacterString>

`  `</gmd:evaluationMethodDescription>

`  `<gmd:dateTime>

`    `<gco:DateTime>2015-04-01T16:20:00</gco:DateTime>

`  `</gmd:dateTime>

`  `<gmd:result>

`    `<gmd:DQ\_QuantitativeResult>

`      `<gmd:valueUnit xlink:href="http://www.opengis.net/def/uom/OGC/1.0/unity"/>

`      `<gmd:value>

`        `<gco:Record xmlns:xs="http://www.w3.org/2001/XMLSchema"

`           `xsi:type="xs:integer">12</gco:Record>

`      `</gmd:value>

`    `</gmd:DQ\_QuantitativeResult>

`  `</gmd:result>

</gmd:DQ\_TopologicalConsistency>

***Example  STYLEREF 1 \s 3. SEQ Example \\* ARABIC \s 1 19:** Topological consistency reported using the quantitative result of one measure "number of faulty point-curve connections". The measure has been evaluated on 1st April 2015, and the type of resulting gco:Record element has been defined as integer using the local typing (xsi:type attribute).*

**Providing descriptive results**

The descriptive topological consistency measure is properly described in [ISO 19157], but unfortunately there is no obvious element for encoding it in the [ISO 19139] XML Schemas. To make it possible to encode the descriptive results without extending the [ISO 19139] XML Schema, the *gmd:DQ\_TopologicalConsistency* element is used with a specific type of *gmd:DQ\_ConformanceResult* element referring to the INSPIRE Generic Network Model. The actual textual description of the consistency result is reported using the *gmd:explanation* property.

**TG Requirement 2.seq Req8: metadata/2.0/req/isdss/topological-consistency-descriptive-results**

If the data set includes types from the Generic Network Model, it does not assure the centreline topology for the network, and the value of the topological consistency checks is not available as quantitative results, the result of the topological consistency shall be reported using the descriptive results.The descriptive topological consistency measures shall be reported using the *gmd:report/gmd:DQ\_TopologicalConsistency/gmd:result
/gmd:DQ\_ConformanceResult* element citing to the INSPIRE Generic Network Model.The *gmd:DQ\_ConformanceResult/gmd:specification/gmd:CI\_Citation/
gmd:title/gco:CharacterString* element shall have the value "INSPIRE Data Specifications - Base Models - Generic Network Model" regardless of the metadata language.The *gmd:DQ\_ConformanceResult/gmd:specification/gmd:CI\_Citation/ gmd:date/gmd:CI\_Date/gmd:date* shall contain the publication date of the  INSPIRE Generic Network Model document containing the geometry types used in the data set.The date type code element *gmd:DQ\_ConformanceResult/
gmd:specification/gmd:CI\_Citation/* gmd:date/gmd:CI\_Date/gmd:dateType/gmd:CI\_DateTypeCode shall be given and it shall point to the value "publication" of the ISO 19139 code list CI\_DateTypeCode.The value of the *gmd:DQ\_ConformanceResult/gmd:pass* element shall always be "false" in this element to indicate that the data set does not assure the centreline topology for the network.The multiplicity of *gmd:report/gmd:DQ\_TopologicalConsistency/gmd:result/
gmd:DQ\_ConformanceResult* elements as described above is 0..\*.The textual description of the results of the topological consistency check shall be given using the *gmd:DQ\_ConformanceResult/gmd:explanation* element. This element is a Non-empty Free Text Element.

` `REF \_Ref463969221 \h  \\* MERGEFORMAT Example 3.20 contains an example of the descriptive results of the topological consistency for a data set in the INSPIRE Transport networks theme.



NOTE	The value "true" of gmd:report/gmd:DQ\_TopologicalConsistency/gmd:result/ gmd:DQ\_ConformanceResult/gmd:pass shall not be used to indicate a successful passing of the topological consistency checks. Only gmd:report/gmd:DQ\_TopologicalConsistency/gmd:result/ gmd:DQ\_ConformanceResult elements with the value of gmd:pass equal "false" are considered as implementations of the descriptive results of the topological consistency as defined in [Regulation 1089/2010].



**/gmd:MD\_Metadata/gmd:dataQualityInfo/gmd:DQ\_DataQuality/gmd:report/gmd:DQ\_TopologicalConsistency:**

<gmd:DQ\_TopologicalConsistency>

`  `<gmd:nameOfMeasure>

`    `<gco:CharacterString>Network connectivity</gco:CharacterString>

`  `</gmd:nameOfMeasure>

`  `<gmd:evaluationMethodType>

`    `<gmd:DQ\_EvaluationMethodTypeCode

`      `codeList="http://standards.iso.org/iso/19139/resources/gmxCodelists.xml#DQ\_EvaluationMethodTypeCode"

`      `codeListValue="directInternal">Direct, internal</gmd:DQ\_EvaluationMethodTypeCode>

`  `</gmd:evaluationMethodType>

`  `<gmd:evaluationMethodDescription>

`    `<gco:CharacterString>Check that wherever a connection exists in a transport network, all connected link ends and the optional node that take part in this connection are positioned at a distance of less than the connectivity tolerance from each other. Check that link ends and nodes that are not connected are always separated by a distance that is greater than the connectivity tolerance. Check if in data sets where both transport links and nodes are presented, the relative position of nodes and link ends in relation to the specified connectivity tolerance corresponds to the associations that exist between them in the data set.</gco:CharacterString>

`  `</gmd:evaluationMethodDescription>

`  `<gmd:dateTime>

`    `<gco:DateTime>2015-04-01T16:20:00</gco:DateTime>

`  `</gmd:dateTime>

`  `<gmd:result>

`    `<gmd:DQ\_ConformanceResult>

`      `<gmd:specification>

`        `<gmd:CI\_Citation>

`          `<gmd:title>

`            `<gco:CharacterString>D2.10.1 INSPIRE Data Specifications - Base Models - Generic Network Model</gco:CharacterString>

`          `</gmd:title>

`          `<gmd:date>

`            `<gmd:CI\_Date>

`              `<gmd:date>

`                `<gco:Date>2013-04-05</gco:Date>

`              `</gmd:date>

`              `<gmd:dateType>

`                `<gmd:CI\_DateTypeCode 

`                  `codeList="http://standards.iso.org/iso/19139/resources/gmxCodelists.xml#CI\_DateTypeCode"

`                  `codeListValue="publication">publication</gmd:CI\_DateTypeCode>

`              `</gmd:dateType>

`            `</gmd:CI\_Date>

`          `</gmd:date>

`        `</gmd:CI\_Citation>

`      `</gmd:specification>

`      `<gmd:explanation>

`        `<gco:CharacterString>Topological consistency has been verified following the requirements of the INSPIRE Data Specification on Transport Networks - Technical Guidelines. No errors have been found.</gco:CharacterString>

`      `</gmd:explanation>

`      `<gmd:pass>

`        `<gco:Boolean>false</gco:Boolean>

`      `</gmd:pass>

`    `</gmd:DQ\_ConformanceResult>

`  `</gmd:result>

</gmd:DQ\_TopologicalConsistency> 


***Example  STYLEREF 1 \s 3. SEQ Example \\* ARABIC \s 1 20:** Topological consistency reported using the descriptive result of one measure "Network connectivity".*

# **Recommended theme-specific metadata elements**
The INSPIRE data specifications [TG DS] include a number of “recommended theme-specific metadata elements” in their sections 8.3. All of them are optional but recommended for certain INSPIRE annex themes. 

**TG Recommendation 2. seq Rec5: metadata/2.0/rec/isdss/recommended-theme-specific-md-elements**

The recommended metadata elements should be included to metadata describing a spatial dataset or spatial dataset series related to the annex themes specified for the relevant element in Annex  REF \_Ref465443971 \n \h C.7.

Many of these theme-specific metadata consider details of particular INSPIRE annex themes in definitions and examples. These are listed in Annex  REF \_Ref465443971 \n \h C.7.
# **Conformance Classes for Spatial Data Services**
# ***Baseline metadata for Spatial Data Services***
**Conformance Class 3: metadata/2.0/*sds***

**Title:** INSPIRE Spatial Data Service baseline metadata**Conformance subject**: Metadata records describing INSPIRE Spatial Data Services encoded in ISO 19139 based XML format.Metadata record fulfilling all the Requirements of this Conformance Class is compliant with the INSPIRE metadata Implementation Rules for Spatial Data Services as defined in [**Regulation 1205/2008**].This Conformance Class includes TG Requirements C.1 – C.22 and TG Requirements 3.1 – 3.8 of this specification.

This Conformance Class covers all the Technical Guidance Requirements concerning metadata contained in [TG SDS].



The metadata elements described in the section 4.1.1 are direct child elements of *gmd:MD\_Metadata* element. The metadata elements contained within elements *gmd:identificationInfo*, *gmd:distributionInfo* and *gmd:dataQualityInfo* are described in sections 4.1.2 - 4.1.4 correspondingly.
# **Direct properties of MD\_Metadata element**
# **Resource type**
This is the type of resource being described by the metadata and it is filled in with a value from a classification of the resource based on its scope.

The element for declaring the type of the resource is described in [Regulation 1205/2008], Part B, 1.3:


*1.3. Resource type*

*This is the type of resource being described by the metadata. The value domain of this metadata element is defined in Part D.1*


Table 2 contained in Part C of the same document defines the multiplicity of this element to exactly one for Spatial Data Services.

To comply with ISO 19115 the *hierarchyLevelName* element shall also be given, if the value of *hierarchyLevel* is not "dataset".



**TG Requirement 3.seq Req \r11: metadata/2.0/req/sds/resource-type**

Resource type shall be declared as "service" using *gmd:hierarchyLevel/gmd:MD\_ScopeCode* element[` `Attribute codeList with value "http://standards.iso.org/iso/19139/resources/gmxCodelists.xml#MD\\_ScopeCode" and the attribute codeListValue with value "service".
].Additionally the name of the hierarchy level shall be given using element *gmd:hierarchyLevelName* element with a Non-empty Free Text Element containing the term "service" in the language of the metadata.The multiplicity of both of these elements is 1.

` `REF \_Ref463969599 \h  \\* MERGEFORMAT Example 4.1 gives an example of the XML code for these elements.


**/gmd:MD\_Metadata/gmd:hierarchyLevel:**

``<gmd:hierarchyLevel>    <gmd:MD\_ScopeCode

`       `codeList="http://standards.iso.org/iso/19139/resources/gmxCodelists.xml#MD\_ScopeCode"

`       `codeListValue="service" />  

</gmd:hierarchyLevel>

<gmd:hierarchyLevelName>    <gco:CharacterString>Service</gco:CharacterString></gmd:hierarchyLevelName>

***Example  STYLEREF 1 \s 4. SEQ Example \\* ARABIC \s 1 1:** Resource type indicating a service given using gmd:hierarchyLevel and gmd:hierarchyLevelName properties.*

# **Identification info section**
The metadata elements described in this section are contained within the first *gmd:identificationInfo* property of the *gmd:MD\_Metadata* element.

**TG Requirement 3.seq Req2: metadata/2.0/req/sds/service-identification-element**

The first *gmd:identificationInfo* property of *gmd:MD\_Metadata* element shall contain a *srv:SV\_ServiceIdentification* element for identifying an INSPIRE Spatial Data Service.
# **Restriction on the spatial resolution**
Spatial resolution refers to the level of detail of the data set. It shall be expressed as a set of zero to many resolution distances (typically for gridded data and imagery-derived products) or equivalent scales (typically for maps or map-derived products).

The [Regulation 1205/2008], Part B 6.2 describes the element for expressing the spatial resolution of provided data sets:


*6.2. Spatial resolution*

*Spatial resolution refers to the level of detail of the data set. It shall be expressed as a set of zero to many resolution distances (typically for gridded data and imagery-derived products) or equivalent scales (typically for maps or map-derived products).* 

*An equivalent scale is generally expressed as an integer value expressing the scale denominator.*

*A resolution distance shall be expressed as a numerical value associated with a unit of length.*


The multiplicity of this element as defined in [Regulation 1205/2008], Part C, Table 2 is zero or more, with the following condition: "Mandatory when there is a restriction on the spatial resolution for this service".

For services, it is not possible to express the restriction of a service concerning the spatial resolution in using the ISO 19139 XML Schema. This problem has been solved in the [ISO 19115-3] standard expected to be published in summer 2016. This slightly inconvenient way of declaring the Spatial resolution for Spatial Data Services shall be used until this specification has been revised to comply with XML Schema rules of [ISO 19115-3].

**TG Requirement 3.seq Req3: metadata/2.0/req/sds/spatial-resolution**

For services with restriction on the spatial resolution, these restrictions shall be expressed in the *gmd:abstract* element with a Non-empty Free Text Element content.The spatial resolution restriction text shall include either an equivalent scale as integer valued scale denominator or a resolution distance using a numerical length value and with a unit of length.

**TG Recommendation 3. seq Rec \r11: metadata/2.0/rec/sds/spatial-resolution-interval**

If the spatial resolution is an interval, both bounding values of the interval should be given.
# **Spatial Data Service category keywords**
Each INSPIRE Spatial Data Service must be classified using ISO 19119 based list of categories and subcategories as defined in the [Regulation 1205/2008], Part D 4. This classification helps users in evaluating if the described service is useful in a particular use case. [INSPIRE Directive], Article 11(2)(b) requires this classification information to be provided also as search criteria in INSPIRE Discovery Services.

The element for giving this information is described in [Regulation 1205/2008], Part B 3:


*3. KEYWORD*

``*If the resource is a spatial data service, at least one keyword from Part D.4 shall be provided.*


**TG Requirement 3.seq Req4: metadata/2.0/req/sds/sds-category**

At least one Spatial Data Service category or subcategory for the described service shall be given using the language-neutral keyword values as defined in Part D 4 “Classification of Spatial Data Services” of [Regulation 1205/2008].

**TG Recommendation 3. seq Rec2: metadata/2.0/rec/sds/sds-category-cv**

To make the reference to the keywords values in [Regulation 1205/2008], Part D 4 clear, these keywords should be expressed as keywords from a controlled vocabulary and using *gmx:Anchor* elements with references to the *Classification of spatial data services* code list in the INSPIRE registry[` `<http://inspire.ec.europa.eu/metadata-codelist/SpatialDataServiceCategory> 
]. The *gmd:thesaurusName* element of the enclosing *gmd:MD\_Keywords* element should be added and it should contain the citation to the [Regulation 1205/2008], Part D 4 and its publication date  according to section 2.4.5.

**TG Recommendation 3. seq Rec3: metadata/2.0/rec/sds/additional-keywords**

In addition to the required keyword from the categories from part D 4 of the [Regulation 1205/2008], it is suggested to choose a minimum of two additional keywords describing the service or the data sets provided by it.

For an XML example, see  REF \_Ref463970137 \h  \\* MERGEFORMAT Example 4.2.

` `**/gmd:MD\_Metadata/gmd:identificationInfo/srv:SV\_ServiceIdentification/gmd:descriptiveKeywords/gmd:MD\_Keywords:**

<gmd:MD\_Keywords>

`  `<gmd:keyword>

`    `<gmx:Anchor xlink:href="http://inspire.ec.europa.eu/metadata-codelist/SpatialDataServiceCategory/humanCatalogueViewer">humanCatalogueViewer</gmx:Anchor>

`  `</gmd:keyword>

`  `<gmd:thesaurusName>

`    `<gmd:CI\_Citation>

`      `<gmd:title>

`        `<gco:CharacterString>COMMISSION REGULATION (EC) No 1205/2008 of 3 December 2008 implementing Directive 2007/2/EC of the European Parliament and of the Council as regards metadata, Part D 4, Classification of Spatial Data Services</gco:CharacterString>

`      `</gmd:title>

`      `<gmd:date>

`        `<gmd:CI\_Date>

`          `<gmd:date>

`            `<gco:Date>2008-12-03</gco:Date>

`          `</gmd:date>

`          `<gmd:dateType>

`            `<gmd:CI\_DateTypeCode

`		    `codeList="http://standards.iso.org/iso/19139/resources/gmxCodelists.xml#CI\_DateTypeCode"

`              `codeListValue="publication"/>

`          `</gmd:dateType>

`        `</gmd:CI\_Date>

`      `</gmd:date>

`    `</gmd:CI\_Citation>

`  `</gmd:thesaurusName>

</gmd:MD\_Keywords>

***Example  STYLEREF 1 \s 4. SEQ Example \\* ARABIC \s 1 2:** Declaring Spatial Data Service category or subcategory as a keyword.*

# **Spatial Data Service type**
The [Regulation 1205/2008], Part B 2.2 describes the element for providing a classification to assist in the search of available Spatial Data Services. 




*2.2. Spatial data service type*

*This is a classification to assist in the search of available spatial data services. A specific service shall be categorised in only one category.The value domain of this metadata element is defined in Part D.3.*



The list of language-neutral values as in Part D3 of the [Regulation 1205/2008].

NOTE	The value "invoke" should no longer be used, since the obligation to provide (network) “services allowing spatial data services to be invoked” is being fulfilled through the provision of the additional metadata elements defined in Annexes V-VII of [Regulation 1089/2010]. See [SDS TG, section 4.2.2] for further details.

The multiplicity of this element as defined in [Regulation 1205/2008], Part C, Table 2 is one.

**TG Requirement 3.seq Req5: metadata/2.0/req/sds/sds-type**

Spatial Data Service type shall be given using element *srv:serviceType*/*gco:LocalName*.The multiplicity of this element is 1.

The specific TG Requirements for the allowed Spatial Data Service type values are given in Requirement Classes for Network Services (section 4.2) and Invocable Spatial Data Services (section 4.3).


**/gmd:MD\_Metadata/gmd:identificationInfo/srv:SV\_ServiceIdentification/srv:serviceType:**

<srv:serviceType>  <gco:LocalName codeSpace="http://inspire.ec.europa.eu/metadata-codelist/SpatialDataServiceType">view</gco:LocalName></srv:serviceType>

***Example  STYLEREF 1 \s 4. SEQ Example \\* ARABIC \s 1 3:** Spatial Data Service type "view"*

NOTE	Since the value domain of this metadata element is restricted to the values defined in Part D3 and the multiplicity of the element is 1, it is not possible to provide a more detailed type for the service (e.g. OGC:WMS or OGC:WMTS for a view service). Such addirional information can be provided in several ways in the metadata, e.g. using keywords, the *srv:serviceTypeVersion* element or the *gmd:protocol* element nested inside the *gmd:transferOptions*.

# **Linking to provided data sets using coupled resource**
This metadata element refers to, where relevant, the target spatial data set(s) of the described service. It is implemented by reference, i.e. through a URL that points to the metadata record of the data on which the service operates. It helps therefore linking services to the relevant datasets.

The element for giving this information is described in [Regulation 1205/2008], Part B 1.6:




*1.6. Coupled resource*

*If the resource is a spatial data service, this metadata element identifies, where relevant, the target spatial data set(s) of the service through their unique resource identifiers (URI).*

*The value domain of this metadata element is a mandatory character string code, generally assigned by the data owner, and a character string namespace uniquely identifying the context of the identifier code (for example, the data owner).*


The multiplicity of this element as defined in [Regulation 1205/2008], Part C, Table 2 is zero or more, with the following condition: "Mandatory if linkage to data sets on which the service operates are available". According to [ISO 19119] the coupled resource is encoded using operatesOn property and it is value is the MD\_DataIdentification element of the data set.

**TG Requirement 3.seq Req6: metadata/2.0/req/sds/coupled-resource**

Links pointing to the online metadata descriptions of data sets provided by the described service shall be given using *srv:operatesOn* element.The multiplicity of this element is 0..n.This property shall be implemented by reference. The *xlink:href* attribute of each of the *srv:operatesOn* elements shall contain a URI pointing to the *gmd:MD\_DataIdentification* element of the metadata record of the provided the data set or data set series.

“Implementation by reference” means that the xlink:href attribute is pointing to an XML document that contains a *gmd:MD\_DataIdentification* object. 

The reference to the *gmd:MD\_DataIdentification* element can be implemented e.g. in the following ways: 

- Point to the *gmd:MD\_DataIdentification* elements using so called fragment identifiers added at the end of the URL address of the metadata document separated by a hash mark "#"[` `See IETF RFC 3986: Uniform Resource Identifier (URI): Generic Syntax, https://tools.ietf.org/html/rfc3986 
]. The value of the fragment identifier should either match the value of the *id* attribute of the referred *gmd:MD\_DataIdentification* element or be another valid XPointer expression referring to the *gmd:MD\_DataIdentification* element. This kind of URL forms a valid XPointer[` `W3C Recommendation: XPointer Framework, https://www.w3.org/TR/xptr-framework/
] that can be understood and resolved and verified precisely by clients. (see  REF \_Ref463974145 \h  \\* MERGEFORMAT Example 4.4 and  REF \_Ref463974148 \h  \\* MERGEFORMAT Example 4.5).Note that the *id* attribute of *gmd:MD\_DataIdentification* is optional, so it may not always exist in the referred metadata record. See TG Recommendation 1.1 for more info.

- Point to the *gmd:MD\_DataIdentification* element by using the Unique Resource Identifier of the target spatial dataset itself. The URI needs to resolve to the *gmd:MD\_DataIdentification* element, e.g. through a dedicated resolver service translating the URI into a CSW request. (see  REF \_Ref463974196 \h  \\* MERGEFORMAT Example 4.6).

NOTE	The INSPIRE metadata element 1.6 *Coupled resource* is not mapped to the *srv:coupledResource*/*srv:SV\_CoupledResource* element.




/gmd:MD\_Metadata/gmd:identificationInfo/srv:SV\_ServiceIdentification/srv:operatesOn:

<srv:operatesOn xlink:href="http://example.com/csw?SERVICE=CSW&VERSION=2.0.2&REQUEST=**GetRecordById**&**ID=f9ee6623-cf4c-11e1-9105-0017085a97ab**&OUTPUTSCHEMA=http://www.isotc211.org/2005/gmd&ELEMENTSETNAME=full#md-so-1002001"/>

***Example  STYLEREF 1 \s 4. SEQ Example \\* ARABIC \s 1 4:** Coupled resource link given using the srv:operatesOn element with URL containing a fragment identifier pointing to the gmd:MD\_DataIdentification element with the corresponding id attribute value "md-so-1002001".*

/gmd:MD\_Metadata/gmd:identificationInfo/srv:SV\_ServiceIdentification/srv:operatesOn:

<srv:operatesOn

`  `xlink:href=" http://example.com/csw?SERVICE=CSW&VERSION=2.0.2&STARTPOSITION=1&MAXRECORDS=10&REQUEST=**GetRecords**&RESULTTYPE=results&OUTPUTFORMAT=application/xml&OUTPUTSCHEMA=http://www.isotc211.org/2005/gmd&TYPENAMES=gmd:MD\_Metadata&ELEMENTSETNAME=brief&CONSTRAINT\_LANGUAGE\_VERSION=1.1.0&CONSTRAINTLANGUAGE=CQL\_TEXT&NAMESPACE=xmlns%28ogc=http://www.opengis.net/ogc%29,xmlns%28gml=http://www.opengis.net/gml%29,xmlns%28apiso=http://www.opengis.net/cat/csw/apiso/1.0%29,xmlns%28csw=http://www.opengis.net/cat/csw/2.0.2%29**&constraint=apiso:identifier%20Like%20%27%26{Identifier of the resource}%26%27&#MD\_DataIdentification**"/>

***Example  STYLEREF 1 \s 4. SEQ Example \\* ARABIC \s 1 5:** Coupled resource link given using the srv:operatesOn element with URL containing a CSW GetRecords request including a query for the resource identifier (shown as {Identifier of the resource}).*


/gmd:MD\_Metadata/gmd:identificationInfo/srv:SV\_ServiceIdentification/srv:operatesOn:

<srv:operatesOn xlink:href="**https://registry.gdi-de.org/id/de.nw/inspire-cp-alkis**"/>

***Example  STYLEREF 1 \s 4. SEQ Example \\* ARABIC \s 1 6:** Coupled resource link given using the Unique resource identifier URL of the referred data set as the value of the xlink:href attribute of srv:operatesOn element. The given URL automatically redirects to another URL[` `[http://gdk.gdi-de.org/gdi-de/srv/eng/csw?REQUEST=GetRecords&SERVICE=CSW&VERSION=2.0.2&OUTPUTSCHEMA=http://www.isotc211.org/2005/gmd&constraintLanguage=CQL\_TEXT&constraint=ResourceIdentifier+like+%27https://registry.gdi-de.org/id/de.nw/inspire-cp-alkis%27&constraint\_language\_version=1.1.0&
typenames=csw:Record&resulttype=results&elementsetname=full#xpointer%28//gmd:identificationInfo\[1\]/gmd:MD\_DataIdentification%29](http://gdk.gdi-de.org/gdi-de/srv/eng/csw?REQUEST=GetRecords&SERVICE=CSW&VERSION=2.0.2&OUTPUTSCHEMA=http://www.isotc211.org/2005/gmd&constraintLanguage=CQL\_TEXT&constraint=ResourceIdentifier+like+%27https://registry.gdi-de.org/id/de.nw/inspire-cp-alkis%27&constraint\_language\_version=1.1.0&typenames=csw:Record&resulttype=results&elementsetname=full#xpointer%28//gmd:identificationInfo[1]/gmd:MD\_DataIdentification%29) 
] returning the gmd:MD\_DataIdentification element*

# **Distribution info section**
The metadata elements described in this section are contained within the *gmd:distributionInfo/gmd:MD\_Distribution* child element of *gmd:MD\_Metadata* element.
# **Resource locator for services**
The Resource Locator for Spatial Data Services, if available, provides the access point of the service, that is an Internet-resolvable address containing a detailed description of a Spatial Data Service, including a list of endpoints to allow an automatic execution.

The [Regulation 1205/2008], Part B, 1.4 describes an element intended for this information:




*1.4. Resource locator*

*The resource locator defines the link(s) to the resource and/or the link to additional information about the resource.*

*The value domain of this metadata element is a character string, commonly expressed as uniform resource locator (URL).*


The multiplicity of this element as defined in [Regulation 1205/2008], Part C, Table 2 is zero or more, and it is "mandatory if linkage to the service is available".

**TG Requirement 3.seq Req7: metadata/2.0/req/sds/resource-locator**

A Resource locator linking to the described Spatial Data Service shall be given, if online access to this service is available.If no online access to the described Spatial Data Service is available, but there is a publicly available online resource providing additional information about the described service, the URL pointing to this resource shall be given instead.These links shall be encoded using *gmd:transferOptions*/*gmd:MD\_DigitalTransferOptions*/*gmd:onLine*/
*gmd:CI\_OnlineResource*/*gmd*:*linkage*/*gmd:URL* element.The multiplicity of this element is 0..n.

A Resource Locator encoded using the *gmd:CI\_OnlineResource* element may also include *gmd:name*, *gmd:description*, and *gmd:function* properties. 

**TG Recommendation 3. seq Rec4: metadata/2.0/rec/sds/resource-locator-additional-info**

It is recommended that in addition to the mandatory *gmd:linkage* element also *gmd:name*, *gmd:description*, and *gmd:function*/*gmd:CI\_OnLineFunctionCode* child elements of *gmd:CI\_OnlineResource* element are provided to give additional information about the provided URL link. The *gmd:name* and the *gmd:description* elements should contain Non-empty Free Text Elements.If provided, the *gmd:CI\_OnLineFunctionCode* element should point to one of the values of the ISO 19139 code list CI\_OnLineFunctionCode[` `Attribute codeList with value "http://standards.iso.org/iso/19139/resources/gmxCodelists.xml#CI\\_OnLineFunctionCode".
]*.*

***TG Recommendation 3. seq Rec5: metadata/2.0/rec/sds/resource-type-url-target***

The URL provided as the value of the *gmd:transferOptions*/*gmd:MD\_DigitalTransferOptions*/*gmd:onLine*/*gmd:CI\_OnlineResource*/*gmd*: *linkage*/*gmd:URL* element should point to one of following type of resources:- a service metadata (capabilities) document of described Spatial Data Service,- a service WSDL[` `W3C Web Services Description Language, https://www.w3.org/TR/wsdl
] document of the described Spatial Data Service (if SOAP[` `W3C Simple Object Access Protocol, or more recently, just SOAP, https://www.w3.org/TR/soap/
] binding is available), or - a web page with further instructions for accessing the described service.

**

**/gmd:MD\_Metadata/gmd:distributionInfo/gmd:MD\_Distribution/gmd:transferOptions:**

<gmd:transferOptions>  <gmd:MD\_DigitalTransferOptions>    <gmd:onLine>      <gmd:CI\_OnlineResource>        <gmd:linkage>

`          `**<gmd:URL>http://example.com/wfs?VERSION=2.0.0&amp;SERVICE=WFS&amp;REQUEST=GetCapabilities</gmd:URL>**        </gmd:linkage>

`        `<gmd:name>          <gco:CharacterString>WFS GetCapabilities request providing machine readable service metadata</gco:CharacterString>        </gmd:name>        <gmd:function>          **<gmd:CI\_OnLineFunctionCode codeList="http://standards.iso.org/iso/19139/resources/gmxCodelists.xml#CI\_OnLineFunctionCode" codeListValue="download" />**        </gmd:function>      </gmd:CI\_OnlineResource>    </gmd:onLine>  </gmd:MD\_DigitalTransferOptions></gmd:transferOptions>

***Example  STYLEREF 1 \s 4. SEQ Example \\* ARABIC \s 1 7:** Resource locator pointing to the GetCapabilities operation of the described WFS service.*

# **Data quality info section**
The metadata elements described in this section are contained within the *gmd:dataQualityInfo/gmd:DQ\_DataQuality* child element of *gmd:MD\_Metadata* element.
# **Scope**
**TG Requirement 3.seq Req8: metadata/2.0/req/sds/only-one-dq-element**

There shall be exactly one *gmd:dataQualityInfo/gmd:DQ\_DataQuality* element scoped to the entire described service.The scoping shall be encoded using *gmd:scope*/*gmd:DQ\_Scope*/*gmd:level*/*gmd:MD\_ScopeCode* element referring to value "service" of [ISO 19139] code list MD\_ScopeCode[` `Attribute codeList with value "http://standards.iso.org/iso/19139/resources/gmxCodelists.xml#MD\\_ScopeCode" and the attribute codeListValue with value "service".
].Additionally the level shall be named using element *gmd:scope/gmd:DQ\_Scope/gmd:levelDescription/gmd:MD\_ScopeDescription/gmd:other* element with a Non-empty Free Text Element containing the term "service" in the language of the metadata.



**/gmd:MD\_Metadata/gmd:dataQualityInfo/gmd:DQ\_DataQuality/gmd:scope/gmd:DQ\_Scope:**

<gmd:DQ\_Scope>  **<gmd:level>    <gmd:MD\_ScopeCode        codeList="http://standards.iso.org/iso/19139/resources/gmxCodelists.xml#MD\_ScopeCode"       codeListValue="service" />  </gmd:level>**  **<gmd:levelDescription>**    <gmd:MD\_ScopeDescription>      <gmd:other>        **<gco:CharacterString>Service</gco:CharacterString>**      </gmd:other>    </gmd:MD\_ScopeDescription>  **</gmd:levelDescription>**</gmd:DQ\_Scope>

***Example  STYLEREF 1 \s 4. SEQ Example \\* ARABIC \s 1 8:** Scope of the Data quality info is set to the entire described Spatial Data Service by giving both the code (gmd:level) and the corresponding description of the level (gmd:levelDescription).*


# ***Metadata for Network Services***
**Conformance Class 4: metadata/2.0/*ns***

**Title:** INSPIRE Network Services metadata**Conformance subject**: metadata record describing an INSPIRE Network Service encoded in ISO 19139 based XML format.Metadata record fulfilling all the Requirements of this Conformance Class is compliant with the INSPIRE metadata Implementation Rules for Spatial Data Services as defined in [**Regulation 1205/2008**].[` `The [Regulation 976/2009] containing Implementing Rules for Network services does not contain any additional requirements for metadata. The requirements in this Requirements Class originate from the Network Services specific parts of [Regulation 1205/2008].
]This Conformance Class includes TG Requirements C.1 – C.22, TG Requirements 3.1 – 3.8, and TG Requirement 4.1 of this specification.

Most of the metadata requirements for INSPIRE Network Services are contained in Conformance Class 3: INSPIRE Spatial Data Service baseline metadata. Though brief, this Conformance Class is added here to make clear which metadata requirements apply to Network Services.

The metadata elements contained within elements *gmd:identificationInfo* and *gmd:dataQualityInfo* are described in sections 4.2.1 and 4.2.2 correspondingly.
# **Identification info section**
The metadata elements described in this section are contained within the first *gmd:identificationInfo/srv:SV\_ServiceIdentification* child element of the *gmd:MD\_Metadata* element.
# **Spatial Data Service type**
**TG Requirement 4.seq Req \r11: metadata/2.0/req/ns/sds-type**

Spatial Data Service type shall be given encoded as specified in  REF req\_sds\_sds\_type \h  \\* MERGEFORMAT TG Requirement 3.5. The value for the element shall be "view", "download", "discovery" or "transformation" depending on the kind of the described Network Service.The multiplicity of the *srv:serviceType/gco:LocalName* element used for the above purpose is 1.

# **Data quality info section**
The metadata elements described in this section are contained within the *gmd:dataQualityInfo/gmd:DQ\_DataQuality* child element of *gmd:MD\_Metadata* element.
# **Conformity**
In conformance to [INSPIRE Directive], the metadata shall include a statement on the degree of conformity with the specifications against which its conformity has been evaluated.

**TG Recommendation 4. seq Rec \r11: metadata/2.0/rec/ns/conformity**

Metadata for an INSPIRE Network Services should declare the conformity to the Network Services Implementation Rules, and it should be encoded using *gmd:report*/*gmd:DQ\_DomainConsistency/gmd:result/
gmd:DQ\_ConformanceResult* element as specified in the  REF req\_common\_conformity \h  \\* MERGEFORMAT TG Requirement C.20[`  `REF req\\_common\\_conformity \h  \\\* MERGEFORMAT TG Requirement C.20: degree of conformity using \*gmd:DQ\\_ConformanceResult.\*
]. This element should contain a citation for the [Regulation 976/2009] encoded according to  REF req\_common\_conformity\_specification \h  \\* MERGEFORMAT TG Requirement C.21[`  `REF req\\_common\\_conformity\\_specification \h  \\\* MERGEFORMAT TG Requirement C.21: \*gmd:DQ\\_ConformanceResult\* shall include a citation of the specification document, ...
]. The degree of conformity should be encoded according to  REF req\_common\_conformity\_degree \h  \\* MERGEFORMAT TG Requirement C.22[`  `REF req\\_common\\_conformity\\_degree \h  \\\* MERGEFORMAT TG Requirement C.22: … \*gmd:DQ\\_ConformanceResult …\* shall also include the degree of declared conformity…
].The multiplicity of the *gmd:report*/*gmd:DQ\_DomainConsistency/gmd:result/
gmd:DQ\_ConformanceResult* element used for the above purpose is 1.

**TG Recommendation 4. seq Rec2: metadata/2.0/rec/ns/uri-for-regulation-976-2009**

If providing the specification title as an *gmx:Anchor* element (as recommended in  REF rec\_common\_anchors\_for\_specifications \h  \\* MERGEFORMAT TG Recommendation C.11), the following URI should be used to refer to [Regulation 976/2009]: <http://data.europa.eu/eli/reg/2009/976>. 

NOTE	A pre-defined XML fragment containing the corresponding *CI\_Citation* element for [Regulation 976/2009] will be provided at <http://inspire.ec.europa.eu/id/citation/ir/reg-976-2009>


**/gmd:MD\_Metadata/gmd:dataQualityInfo/gmd:DQ\_DataQuality/gmd:report/gmd:DQ\_DomainConsistency/gmd:result:**

<gmd:result>  <gmd:DQ\_ConformanceResult>    <gmd:specification xlink:href="http://inspire.ec.europa.eu/id/citation/ir/reg-976-2009">      <gmd:CI\_Citation>        <gmd:title>          <gmx:Anchor xlink:href="http://data.europa.eu/eli/reg/2009/976"> COMMISSION REGULATION (EC) No 976/2009 of 19 October 2009 implementing Directive 2007/2/EC of the European Parliament and of the Council as regards the Network Services</gmx:Anchor>        </gmd:title>        <gmd:date>          <gmd:CI\_Date>            <gmd:date>              <gco:Date>2010-12-08</gco:Date>            </gmd:date>            <gmd:dateType>              <gmd:CI\_DateTypeCode                codeList="http://standards.iso.org/iso/19139/resources/gmxCodelists.xml#CI\_DateTypeCode"                codeListValue="publication">publication</gmd:CI\_DateTypeCode>            </gmd:dateType>          </gmd:CI\_Date>        </gmd:date>      </gmd:CI\_Citation>    </gmd:specification>    <gmd:explanation>      <gco:CharacterString>This data set is conformant with the INSPIRE Implementing Rules for Network Services</gco:CharacterString>    </gmd:explanation>    <gmd:pass>      <gco:Boolean>true</gco:Boolean>    </gmd:pass>  </gmd:DQ\_ConformanceResult></gmd:result>

***Example  STYLEREF 1 \s 4. SEQ Example \\* ARABIC \s 1 9:** Conformity declaration against the [Regulation 976/2009].*

Metadata for an INSPIRE network services can also include additional declarations of conformity, in particular to the abstract test suites and conformance classes defined for the INSPIRE technical guidance documents.

**TG Recommendation 4. seq Rec3: metadata/2.0/rec/ns/uris-for-ats-and-cc**

If declaring conformity to an abstract test suite or a conformance class using an *gmx:Anchor* element (as recommended in  REF rec\_common\_anchors\_for\_specifications \h  \\* MERGEFORMAT TG Recommendation C.11), the URI identifying the abstract test suite or a conformance class should be used in the *xlink:href* attribute of the specification title element.

NOTE	It is not currently planned to provide pre-defined XML fragments containing the *CI\_Citation* elements for the INSPIRE TG documents in the <http://inspire.ec.europa.eu/id/citation/> namespace. However, such fragments can be added if this is deemed useful by INSPIRE data providers.


**/gmd:MD\_Metadata/gmd:dataQualityInfo/gmd:DQ\_DataQuality/gmd:report/gmd:DQ\_DomainConsistency/gmd:result:**

<gmd:result>  <gmd:DQ\_ConformanceResult>    <gmd:specification>      <gmd:CI\_Citation>        <gmd:title>          <gmx:Anchor xlink:href="http://inspire.ec.europa.eu/id/ats/download-service/3.1/wfs-pre-defined">Technical Guidance for Download Services, version 3.1 - Conformance class: Pre-defined WFS</gmx:Anchor>        </gmd:title>        <gmd:date>          <gmd:CI\_Date>            <gmd:date>              <gco:Date>2014-04-17</gco:Date>            </gmd:date>            <gmd:dateType>              <gmd:CI\_DateTypeCode                codeList="http://standards.iso.org/iso/19139/resources/gmxCodelists.xml#CI\_DateTypeCode"                codeListValue="publication">publication</gmd:CI\_DateTypeCode>            </gmd:dateType>          </gmd:CI\_Date>        </gmd:date>      </gmd:CI\_Citation>    </gmd:specification>    <gmd:explanation>      <gco:CharacterString>This data set is conformant with Conformance class: Pre-defined WFS of the INSPIRE Technical Guidance for Download Services, version 3.1</gco:CharacterString>    </gmd:explanation>    <gmd:pass>      <gco:Boolean>true</gco:Boolean>    </gmd:pass>  </gmd:DQ\_ConformanceResult></gmd:result>

***Example  STYLEREF 1 \s 4. SEQ Example \\* ARABIC \s 1 10:** Conformity declaration against a conformance class.*

# ***Metadata for Invocable Spatial Data Services***
**Conformance Class 5: metadata/2.0/sds-invocable**

**Title:** INSPIRE Invocable Spatial Data Services metadata**Conformance subject**: metadata record describing a Spatial Data Service encoded in ISO 19139 based XML format.Metadata record fulfilling all the Requirements of this Conformance Class is compliant with the INSPIRE metadata Implementation Rules for Spatial Data Services as defined in [**Regulation 1205/2008**], and the Article 14b "Interoperability arrangements and harmonisation requirements for invocable spatial data services" of amendment [Regulation 1312/2014] to [Regulation 1089/2010] adding its Annex V.This Conformance Class includes TG Requirements C.1 – C.22, TG Requirements 3.1 – 3.8, and TG Requirements 5.1 – 5.5 of this specification.

The metadata elements contained within elements *gmd:identificationInfo*, *gmd:distributionInfo* and *gmd:dataQualityInfo* are described in sections 4.3.1 - 4.3.3 correspondingly.

# **Identification info section**
The metadata elements described in this section are contained within the first *gmd:identificationInfo/srv:SV\_ServiceIdentification* child element of the *gmd:MD\_Metadata* element.
# **Spatial Data Service type**
**TG Requirement 5.seq Req \r11: metadata/2.0/req/sds-invocable/sds-type**

Spatial Data Service type shall be given encoded using element *srv:serviceType*/*gco:LocalName* as specified in TG Requirement 3.5. The value for the element shall be "other" for all Invocable Spatial Data Services.

# **Distribution info section**
# **Resource locator** 
This Conformance Class extends the requirements in section 4.1.3.1 by requiring explicit declarations of the access points of the Spatial Data Service. The [Regulation 1312/2014], Annex I, Part D 1 describes these additional requirements:


*1. Resource Locator*
\*


*The Resource Locator metadata element set out in Regulation (EC) No 1205/2008 shall also contain all access points from the spatial data service provider and these access points shall be unambiguously identified as such.* 



**TG Requirement 5.seq Req2: metadata/2.0/req/sds-invocable/access-point**

Each access point of the described Invocable Spatial Data Service shall be described in the metadata record using a *gmd:transferOptions/gmd:MD\_DigitalTransferOptions/gmd:onLine/
gmd:CI\_OnlineResource* element.The *gmd:linkage/gmd:URL* child element of *gmd:CI\_OnlineResource* shall contain the URL of the described access point containing a detailed description of a spatial data service, including a list of end points to allow its execution.The *gmd:linkage/gmd:description* child element *gmd:CI\_OnlineResource* shall contain a *gmx:Anchor* element pointing to the value "accessPoint" of the code list OnLineDescriptionCode in the INSPIRE Registry[` `Attribute xlink:href with value "http://inspire.ec.europa.eu/metadata-codelist/OnLineDescriptionCode/accessPoint"
].The multiplicity of the *gmd:transferOptions/gmd:MD\_DigitalTransferOptions/gmd:onLine/
gmd:CI\_OnlineResource* element used for the above purpose is 1..\*.

**TG Recommendation 5. seq Rec4: metadata/2.0/rec/sds-invocable/access-point-additional-info**

It is recommended that in addition to the mandatory *gmd:linkage* and *gmd:description* elements, also the *gmd:name*, the *gmd:function*/*gmd:CI\_OnLineFunctionCode* child elements of *gmd:CI\_OnlineResource* element are provided to give additional information about the provided URL link. The *gmd:name* element should contain a Non-empty Free Text Element.If provided, the *gmd:CI\_OnLineFunctionCode* element should point to value "information" of the ISO 19139 code list CI\_OnLineFunctionCode[` `Attribute codeList with value "http://standards.iso.org/iso/19139/resources/gmxCodelists.xml#CI\\_OnLineFunctionCode" and the attribute codeListValue with "information".
]*.*


**/gmd:MD\_Metadata/gmd:distributionInfo/gmd:MD\_Distribution/gmd:transferOptions:**

<gmd:transferOptions>  <gmd:MD\_DigitalTransferOptions>    <gmd:onLine>      <gmd:CI\_OnlineResource>        <gmd:linkage>

`			  `<gmd:URL>http://www.dinoservices.nl:80/geo3dmodelwebservices-1/Geo3DModelService?wsdl</gmd:URL>

`        `</gmd:linkage>

`			`<gmd:description>				  <gmx:Anchor

`             `xlink:href="http://inspire.ec.europa.eu/metadata-codelist/OnLineDescriptionCode/accessPoint">accessPoint</gmx:Anchor>				</gmd:description>		   <gmd:function>			  <gmd:CI\_OnLineFunctionCode

`            `codeList="http://standards.iso.org/iso/19139/resources/gmxCodelists.xml#CI\_OnLineFunctionCode"

`            `codeListValue="information">information</gmd:CI\_OnLineFunctionCode>			</gmd:function>      </gmd:CI\_OnlineResource>    </gmd:onLine>  </gmd:MD\_DigitalTransferOptions></gmd:transferOptions>

***Example  STYLEREF 1 \s 4. SEQ Example \\* ARABIC \s 1 11**: Resource locator pointing the access point of the described Invocable Spatial Data Service.*

# **Data quality info section**
The metadata elements described in this section are contained within the *gmd:dataQualityInfo/gmd:DQ\_DataQuality* child element of *gmd:MD\_Metadata* element.
# **Conformity to INSPIRE Implementation Rules**
Invocable Spatial Data Services shall declare conformity to the [Regulation 1089/2010].

**TG Requirement 5.seq Req3: metadata/2.0/req/sds-invocable/conformity**

Metadata for an INSPIRE Invocable Spatial Data Services shall declare the conformity to the Implementing Rules for interoperability of spatial data sets and services, and it shall be encoded using *gmd:report*/*gmd:DQ\_DomainConsistency/gmd:result/
gmd:DQ\_ConformanceResult* element as specified in  REF req\_common\_conformity \h  \\* MERGEFORMAT **TG Requirement C.20** REF req\_common\_conformity \h  \\* MERGEFORMAT **TG Requirement C.20** REF req\_common\_conformity \h  \\* MERGEFORMAT TG Requirement C.20[`  `REF req\\_common\\_conformity \h  \\\* MERGEFORMAT TG Requirement C.20: degree of conformity using \*gmd:DQ\\_ConformanceResult.\*
]. This element shall contain citation of the [Regulation 1089/2010] encoded according to  REF req\_common\_conformity\_specification \h  \\* MERGEFORMAT TG Requirement C.21[`  `REF req\\_common\\_conformity\\_specification \h  \\\* MERGEFORMAT TG Requirement C.21: \*gmd:DQ\\_ConformanceResult\* shall include a citation of the specification document, ...
]. The degree of conformity shall be encoded as according to  REF req\_common\_conformity\_degree \h  \\* MERGEFORMAT TG Requirement C.22[`  `REF req\\_common\\_conformity\\_degree \h  \\\* MERGEFORMAT TG Requirement C.22: … \*gmd:DQ\\_ConformanceResult …\* shall also include the degree of declared conformity…
].

``The multiplicity of the *gmd:report*/*gmd:DQ\_DomainConsistency/gmd:result/
gmd:DQ\_ConformanceResult* element used for the above purpose is 1.

**TG Recommendation 5. seq Rec5: metadata/2.0/rec/sds-invocable/uri-for-regulation-1089-2010**

If providing the specification title as an *gmx:Anchor* element (as recommended in  REF rec\_common\_anchors\_for\_specifications \h  \\* MERGEFORMAT TG Recommendation C.11), the following URI should be used to refer to [Regulation 1089/2010]: <http://data.europa.eu/eli/reg/2010/1089>.

NOTE	A pre-defined XML fragment containing the corresponding *CI\_Citation* element for [Regulation 1089/2010] will be provided at <http://inspire.ec.europa.eu/id/citation/ir/reg-1089-2010>.



**/gmd:MD\_Metadata/gmd:dataQualityInfo/gmd:DQ\_DataQuality/gmd:report/gmd:DQ\_DomainConsistency/gmd:result:**

<gmd:result>  <gmd:DQ\_ConformanceResult>    <gmd:specification xlink:href="http://inspire.ec.europa.eu/id/citation/ir/reg-1089-2010">

`      `<gmd:CI\_Citation>        <gmd:title>          <gmx:Anchor xlink:href="http://data.europa.eu/eli/reg/2010/1089">COMMISSION REGULATION (EU) No 1089/2010 of 23 November 2010 implementing Directive 2007/2/EC of the European Parliament and of the Council as regards interoperability of spatial data sets and services</gmx:Anchor>        </gmd:title>        <gmd:date>          <gmd:CI\_Date>            <gmd:date>              <gco:Date>2010-12-08</gco:Date>            </gmd:date>            <gmd:dateType>              <gmd:CI\_DateTypeCode                codeList="http://standards.iso.org/iso/19139/resources/gmxCodelists.xml#CI\_DateTypeCode"                codeListValue="publication">publication</gmd:CI\_DateTypeCode>            </gmd:dateType>          </gmd:CI\_Date>        </gmd:date>      </gmd:CI\_Citation>    </gmd:specification>    <gmd:explanation>      <gco:CharacterString>This Spatial Data Service set is conformant with the INSPIRE Implementing Rules for the interoperability of spatial data sets and services</gco:CharacterString>    </gmd:explanation>    <gmd:pass>      <gco:Boolean>true</gco:Boolean>    </gmd:pass>  </gmd:DQ\_ConformanceResult></gmd:result>

***Example  STYLEREF 1 \s 4. SEQ Example \\* ARABIC \s 1 12:** Conformity declaration against the [Regulation 1089/2010].*


Metadata for Invocable Spatial Data Services can also include additional declarations of conformity, in particular to the abstract test suites and conformance classes defined for the INSPIRE technical guidance documents.

**TG Recommendation 5. seq Rec6: metadata/2.0/rec/datasets-and-series/uris-for-ats-and-cc**

If declaring conformity to an abstract test suite or a conformance class using an *gmx:Anchor* element (as recommended in  REF rec\_common\_anchors\_for\_specifications \h  \\* MERGEFORMAT TG Recommendation C.11), the URI identifying the abstract test suite or a conformance class should be used in the *xlink:href* attribute of the specification title element. 

NOTE	It is not currently planned to provide pre-defined XML fragments containing the *CI\_Citation* elements for the INSPIRE TG documents in the <http://inspire.ec.europa.eu/id/citation/> namespace. However, such fragments can be added if this is deemed useful by INSPIRE data providers.

# **Category of the Spatial Data Service**
To discover the harmonisation level of the described Invocable Spatial Data Service, the users must able to find out if the service fulfils the additional requirements specified for an Interoperable or a Harmonised Spatial Data Service. The Category element for providing information is described in [Regulation 1312/2014], Annex I, Part B 1:


*1. Category*

*This is a citation of the status of the spatial data service versus invocability. The value domain of this metadata element is as follows:* 

*1.1. Invocable (invocable)*

*The spatial data service is an invocable spatial data service.*

*1.2. Interoperable (interoperable)*

*The invocable spatial data service is an interoperable spatial data service.*

*1.3. Harmonised (harmonised)*

*The interoperable spatial data service is a harmonised spatial data service.*


In Table 1 of [Regulation 1312/2014], Annex I, Part C, the element is defined as mandatory for an invocable spatial data services.

The Category element is mapped in to [ISO 19139] using the *gmd:DQ\_DomainConsistency* and *gmd:DQ\_ConformanceResult* elements citing the Conformance Classes for the Invocable Spatial Data Service categories mentioned above.

**TG Requirement 5.seq Req4: metadata/2.0/req/sds-invocable/sds-category**

The category of the Invocable Spatial Data Service shall be given. It shall be encoded using the *gmd:report*/*gmd:DQ\_DomainConsistency/gmd:result/gmd:DQ\_ConformanceResult* element as specified in  REF req\_common\_conformity \h  \\* MERGEFORMAT TG Requirement C.20[`  `REF req\\_common\\_conformity \h  \\\* MERGEFORMAT TG Requirement C.20: degree of conformity using \*gmd:DQ\\_ConformanceResult.\*
]. This element shall contain a citation for one of the three Conformance Classes for Invocable Spatial Data Service categories, and it shall be encoded according to  REF req\_common\_conformity\_specification \h  \\* MERGEFORMAT TG Requirement C.21[`  `REF req\\_common\\_conformity\\_specification \h  \\\* MERGEFORMAT TG Requirement C.21: \*gmd:DQ\\_ConformanceResult\* shall include a citation of the specification document, ...
]. 

``The title of the cited Conformance Class shall be encoded using the *gmd:DQ\_ConformanceResult/gmd:specification/gmd:CI\_Citation/gmd:title/gmx:Anchor* element. The attribute *xlink:href* of this element shall contain the permanent unique identifier of the Conformance Class, and the textual content of the *gmx:Anchor* element shall contain the corresponding language-neutral name of the category. The language-neutral names and the permanent unique identifiers are given in Table 5.1.

The degree of conformity as specified by  REF req\_common\_conformity\_degree \h  \\* MERGEFORMAT TG Requirement C.22[`  `REF req\\_common\\_conformity\\_degree \h  \\\* MERGEFORMAT TG Requirement C.22: … \*gmd:DQ\\_ConformanceResult …\* shall also include the degree of declared conformity…
] shall indicate that the service is fully conformant with the cited Conformance Class[` `Element gmd:DQ\\_ConformanceResult/gmd:pass/gco:Boolean shall have value "true".
].

The multiplicity of the *gmd:report*/*gmd:DQ\_DomainConsistency/gmd:result/gmd:DQ\_ConformanceResult* element used for the above purpose is 1.

**

***Table  STYLEREF 1 \s 4. SEQ Table \\* ARABIC \s 1 1:** The language-neutral names and the URIs of the Invocable Spatial Data Service categories.*

|**Language-neutral name**|**Permanent unique identifier of the Requirements Class**|
| :- | :- |
|invocable|http://inspire.ec.europa.eu/id/ats/metadata/2.0/sds-invocable|
|interoperable|http://inspire.ec.europa.eu/id/ats/metadata/2.0/sds-interoperable|
|harmonised|http://inspire.ec.europa.eu/id/ats/metadata/2.0/sds-harmonised|



**/gmd:MD\_Metadata/gmd:dataQualityInfo/gmd:DQ\_DataQuality/gmd:report/gmd:DQ\_DomainConsistency/gmd:result:**

<gmd:result>  <gmd:DQ\_ConformanceResult>    <gmd:specification>      <gmd:CI\_Citation>        <gmd:title>         <gmx:Anchor

`            `xlink:href=" http://inspire.ec.europa.eu/id/ats/metadata/2.0/sds-invocable"

`            `xlink:title="INSPIRE Invocable Spatial Data Services metadata">invocable</gmx:Anchor>        </gmd:title>        <gmd:date>          <gmd:CI\_Date>            <gmd:date>              <gco:Date>2016-05-01</gco:Date>            </gmd:date>            <gmd:dateType>              <gmd:CI\_DateTypeCode                codeList="http://standards.iso.org/iso/19139/resources/gmxCodelists.xml#CI\_DateTypeCode"                codeListValue="publication">publication</gmd:CI\_DateTypeCode>            </gmd:dateType>          </gmd:CI\_Date>        </gmd:date>      </gmd:CI\_Citation>    </gmd:specification>    <gmd:explanation>      <gco:CharacterString>This Spatial Data Service set is conformant with the INSPIRE requirements for Invocable Spatial Data Services</gco:CharacterString>    </gmd:explanation>    <gmd:pass>      <gco:Boolean>true</gco:Boolean>    </gmd:pass>  </gmd:DQ\_ConformanceResult></gmd:result>

***Example  STYLEREF 1 \s 4. SEQ Example \\* ARABIC \s 1 13:** Conformity declaration against the Requirements Class "INSPIRE Invocable Spatial Data Services metadata".*

# **Conformity to technical specifications**
The requirement of declaring conformity not only to the INSPIRE Implementation Rules, but also to technical specifications, including the INSPIRE Technical Guidelines, is made more explicit for the Invocable Spatial Data Services in [Regulation 1312/2014], Annex I, Part D 2:




*2. Specification*

*The Specification metadata element set out in Regulation (EC) No 1205/2008 shall also refer to or contain technical specifications (such as INSPIRE technical guidance but not only), to which the invocable spatial data service fully conforms, providing all the necessary technical elements (human, and wherever relevant, machine readable) to allow its invocation.*


The mentioned Specification element together with the Degree element form the Conformity element as defined in [Regulation 1205/2008], Part B 7. The [ISO 19139] mapping for this element is defined in section 2.5.1 of this specification.

The specification metadata element described above and the access point given as the resource locator element (see section 4.3.2.1) together shall to provide sufficient information to actually invoke the service and enable its usage. If the specification metadata element does not refer to or contain at least one technical specification to which the Invocable Spatial Data Service fully conforms, providing all the necessary technical elements, the service is not considered an INSPIRE Invocable Spatial Data Service.

**TG Requirement 5.seq Req5: metadata/2.0/req/sds-invocable/conformity-to-technical-specifications**

An Invocable Spatial Data Service shall declare full compliance with at least one technical specification providing all the necessary technical elements to actually invoke the service and enable its usage. This declaration shall be encoded using *gmd:report*/*gmd:DQ\_DomainConsistency/gmd:result/
gmd:DQ\_ConformanceResult* element as specified in  REF req\_common\_conformity \h  \\* MERGEFORMAT TG Requirement C.20[`  `REF req\\_common\\_conformity \h  \\\* MERGEFORMAT TG Requirement C.20: degree of conformity using \*gmd:DQ\\_ConformanceResult.\*
]. This element shall contain a citation for the technical specification encoded according to  REF req\_common\_conformity\_specification \h  \\* MERGEFORMAT TG Requirement C.21[`  `REF req\\_common\\_conformity\\_specification \h  \\\* MERGEFORMAT TG Requirement C.21: \*gmd:DQ\\_ConformanceResult\* shall include a citation of the specification document, ...
]. 

``The degree of conformity as specified by  REF req\_common\_conformity\_degree \h  \\* MERGEFORMAT TG Requirement C.22[`  `REF req\\_common\\_conformity\\_degree \h  \\\* MERGEFORMAT TG Requirement C.22: … \*gmd:DQ\\_ConformanceResult …\* shall also include the degree of declared conformity…
] shall indicate that the service is fully conformant with the given specification[` `Element gmd:DQ\\_ConformanceResult/gmd:pass/gco:Boolean shall have value "true".
].

``The multiplicity of the *gmd:report*/*gmd:DQ\_DomainConsistency/gmd:result/gmd:DQ\_ConformanceResult* element used for the above purpose is 1..\*.

**TG Recommendation 5. seq Rec7: metadata/2.0/rec/sds-invocable/specification-title-anchor**

In order to be machine readable, the specification title element should be provided using the *gmx:Anchor* element referring to an official publication URL address of the particular specification. The text content of this element should contain the official title of the referred technical specification.



**/gmd:MD\_Metadata/gmd:dataQualityInfo/gmd:DQ\_DataQuality/gmd:report/gmd:DQ\_DomainConsistency/gmd:result:**

<gmd:result>  <gmd:DQ\_ConformanceResult>    <gmd:specification>      <gmd:CI\_Citation>        <gmd:title>         <gmx:Anchor

`            `xlink:href="http://www.iso.org/iso/iso\_catalogue/catalogue\_tc/catalogue\_detail.htm?csnumber=32546">EN ISO 19128:2005(E): Geographic information — Web map server interface</gmx:Anchor>        </gmd:title>        <gmd:date>          <gmd:CI\_Date>            <gmd:date>              <gco:Date>2005-12-01</gco:Date>            </gmd:date>            <gmd:dateType>              <gmd:CI\_DateTypeCode                codeList="http://standards.iso.org/iso/19139/resources/gmxCodelists.xml#CI\_DateTypeCode"                codeListValue="publication">publication</gmd:CI\_DateTypeCode>            </gmd:dateType>          </gmd:CI\_Date>        </gmd:date>      </gmd:CI\_Citation>    </gmd:specification>    <gmd:explanation>      <gco:CharacterString>This Spatial Data Service set is conformant with the ISO 19128:2005 specification</gco:CharacterString>    </gmd:explanation>    <gmd:pass>      <gco:Boolean>true</gco:Boolean>    </gmd:pass>  </gmd:DQ\_ConformanceResult></gmd:result>

***Example  STYLEREF 1 \s 4. SEQ Example \\* ARABIC \s 1 14:** Conformity declaration against the Web Map Service specification (ISO 19128:2005).*

# ***Metadata for Interoperable Spatial Data Services***
**Conformance Class 6: metadata/2.0/sds-interoperable**

**Title:** INSPIRE Interoperable Spatial Data Services metadata**Conformance subject**: metadata record describing a Spatial Data Service encoded in ISO 19139 based XML format.Metadata record fulfilling all the Requirements of this Conformance Class is compliant with the INSPIRE metadata Implementation Rules for Spatial Data Services as defined in [**Regulation 1205/2008**], and the Article 14b "Interoperability arrangements and harmonisation requirements for invocable spatial data services" of amendment [Regulation 1312/2014] to [Regulation 1089/2010] adding its Annex VI.This Conformance Class includes TG Requirements C.1 – C.22, TG Requirements 3.1 – 3.8, TG Requirements 5.1 – 5.5, and TG Requirements 6.1 – 6.5 of this specification.

The metadata elements described in section  REF \_Ref469906154 \r \h 4.4.1 are direct child elements of *gmd:MD\_Metadata* element. The metadata elements contained within elements *gmd:identificationInfo* and *gmd:dataQualityInfo* are described in sections  REF \_Ref469906159 \r \h 4.4.2 –  REF \_Ref469906162 \r \h 4.4.3 correspondingly.
# **Direct properties of MD\_Metadata element**
# **Coordinate Reference System Identifier**
It is mandatory for Interoperable Spatial Data Services indicate the coordinate reference system identifiers supported by the service. The element for describing this information is given in 

[Regulation1312/2014], Annex II, Part B 3:


*3. Coordinate Reference System Identifier*

*Where appropriate, this is the list of coordinate reference systems supported by the spatial data service.*

*Each supported coordinate reference system shall be expressed using an identifier.* 


**TG Requirement 6.seq Req \r11: metadata/2.0/req/sds-interoperable/crs**

The coordinate reference system(s) supported by the described Spatial Data Service shall be given using element *gmd:referenceSystemInfo/gmd:MD\_ReferenceSystem/
gmd:referenceSystemIdentifier/gmd:RS\_Identifier*.The multiplicity of this element is 1..\*.The *gmd:code* child element of *gmd:RS\_Identifier* is mandatory. The *gmd:codeSpace* child element shall be used if the code alone does not uniquely identify the referred coordinate reference system. Both *gmd:code* and *gmd:codeSpace* element (if given) shall contain Non-empty Free Text Elements.Only the coordinate reference system identifiers specified in a well-known common register shall be used.

**TG Requirement 6.seq Req2: metadata/2.0/req/sds-interoperable/crs-http-uris**

If the coordinate reference system is listed in the table Default Coordinate Reference System Identifiers in Annex  REF \_Ref465002404 \n \h D.4, the value of the HTTP URI Identifier column shall be used as the value of *gmd:referenceSystemInfo/gmd:MD\_ReferenceSystem/
gmd:referenceSystemIdentifier/gmd:RS\_Identifier/gmd:code* element.The *gmd:codeSpace* element shall not be used in this case.

# **Identification info section**
The metadata elements described in this section are contained within the first *gmd:identificationInfo/srv:SV\_ServiceIdentification* child element of the *gmd:MD\_Metadata* element.
# **Conditions applying to access and use – technical restrictions**
In addition to the generic, often policy and licensing based restrictions discussed in section 2.4.7, also possible technical restrictions applying to the access and use of the Spatial Data Services shall be declared in the metadata for Interoperable Spatial Data Services, as described in [Regulation1312/2014], Annex II, Part A 1:


*1. Conditions applying to access and use*

*The technical restrictions applying to the access and use of the spatial data service shall be documented in the metadata element “CONSTRAINT RELATED TO ACCESS AND USE” set out in Regulation (EC) No 1205/2008.* 


**TG Requirement 6.seq Req3: metadata/2.0/req/sds-interoperable/conditions-applying-to-access-and-use**

The technical restrictions applying to access and use of an Interoperable Spatial Data Service shall be given in the metadata. This information shall be encoded as described in the  REF req\_common\_limitations\_access\_and\_use \h  \\* MERGEFORMAT TG Requirement C.18.The multiplicity of the *gmd:resourceConstraints/gmd:MD\_LegalConstraints* element used for the above purpose is 1..\*.This information may be combined within the same *gmd:resourceConstraints* element used for describing the non-technical conditions applying to access and use of the Spatial Data Service.


# **Responsible party – custodian**
In addition to the information about the organisation responsible for the establishment, management, maintenance and distribution described in section 2.4.3, the metadata for Interoperable Spatial Data Service shall contain the information about the responsible party for the service in the role of the custodian. A custodian accepts accountability and responsibility for the resource and ensures appropriate care and maintenance of the resource. This additional requirement is described in [Regulation1312/2014], Annex II, Part A 2:




*2. Responsible party*

*The responsible party set out in Regulation (EC) No 1205/2008 shall at least describe the custodian responsible organisation, corresponding to the Custodian responsible party role set out in Regulation (EC) No 1205/2008.*  


**TG Requirement 6.seq Req4: metadata/2.0/req/sds-interoperable/responsible-party**

The responsible party for the Interoperable Spatial Data Service in the role of the custodian shall be given. This element shall be encoded as described in  REF req\_common\_responsible\_organisation \h  \\* MERGEFORMAT TG Requirement C.10.The value of *gmd:pointOfContact*/*gmd:CI\_ResponsibleParty*/*gmd:role*/
*gmd:CI\_RoleCode* shall point to the value "custodian" of ISO 19139 code list CI\_RoleCode[` `Attribute codeList shall be "http://standards.iso.org/iso/19139/resources/gmxCodelists.xml#CI\\_RoleCode" and the attribute codeListValue shall be "custodian".
]The multiplicity of the *gmd:pointOfContact/gmd:CI\_ResponsibleParty* element used for the above purpose is 1..\*.

In the TG Requirement C.9 the freedom of selecting the best fitting code for the responsible party role is left to the metadata provider. In cases when the responsible organisation responsible for the establishment, management, maintenance and distribution of the Spatial Data Service, is also responsible for the service in the role of the custodian, it may be sufficient to use the same responsible party element with only the role code custodian to represent the responsible party for both roles. Note that if it is desirable to express all of the distinct roles, a separate *gmd:pointOfContact/gmd:CI\_ResponsibleParty* element must be used for each role as only one *gmd:role* child element is allowed for *gmd:CI\_ResponsibleParty by the [ISO 19139] XML Schema*.
# **Data quality info section**
The metadata elements described in this section are contained within the *gmd:dataQualityInfo/gmd:DQ\_DataQuality* child element of *gmd:MD\_Metadata* element.
# **Minimum estimated Quality of Service**
The minimum Quality of Service criteria values for the Interoperable Spatial Data Service shall be given in the metadata. These criteria are described in [Regulation1312/2014], Annex II, Part B 4:


*4.1. Criteria*

*These are the criteria to which the measurements refer. The value domain of this metadata element is as follows:*

*4.1.1. Availability (availability)It describes the percentage of time the service is available.*

*4.1.2. Performance (performance)*

*It describes how fast a request to the spatial data service can be completed.*

*4.1.3. Capacity (capacity)*

*It describes the maximum number of simultaneous requests that can be completed with the declared performance.* 

*4.2. Measurement*

*4.2.1. Description*

*It describes the measurement for each criterion.* 

*The value domain of this metadata element is free text.*

*4.2.2. Value (value)*

*It describes the value of the measurement for each criterion.*

*The value domain of this metadata element is free text.*

*4.2.3. Unit (unit)*

*It describes the Unit of the measurement for each criterion.*

*The value domain of this metadata element is free text.*


In Table 1 of [Regulation 1312/2014], Annex II, Part C, the multiplicity for the quality of service elements is defined as 3..\*.

**TG Requirement 6.seq Req5: metadata/2.0/req/sds-interoperable/quality-of-service**

The minimum values for each of the Quality of Service criteria given in Table 6.1 shall be given in the metadata. They shall be encoded using one *gmd:report/gmd:DQ\_ConceptualConsistency* element within the *gmd:DQ\_DataQuality* element scoped for the entire service.The value of *gmd:DQ\_ConceptualConsistency/gmd:nameOfMeasure* shall be shall be an *gmx:Anchor* element referring to the code list value for the criterion in the INSPIRE Registry[` `Attribute xlink:href with URL value starting with "http://inspire.ec.europa.eu/metadata-codelist/QualityOfServiceCriteria/" and postfixed with one of values of code list QualityOfServiceCriteria, see Annex D.4
] and expressing the name of the criterion in the language of the metadata.

The description of the measurement of the criterion shall be encoded using the *gmd:DQ\_ConceptualConsistency/gmd:measureDescription* element.

` `The value of the measurement of the criterion shall be encoded using the *gmd:DQ\_ConceptualConsistency/gmd:result/gmd:DQ\_QuantitativeResult* element.The *gmd:valueUnit* child element shall describe the unit of measure of the criteria as given in Table 6.1. The numerical value of the criteria shall be encoded using the *gmd:value/gco:Record* element. The value type of shall be declared using the *xsi:type* attribute of the *gco:Record* element as given in the Table 6.1.

The purpose of these quality of service metadata elements is to describe the minimum provided service level for the given Spatial Data Service over a long period of time. These values are not intended to be used for publishing the real-time or short-term results of measured quality of service criteria for the service. They should however reflect the true Quality of Service of the particular service evaluated in realistic test scenarios rather than the expected goals to reach for these criteria.

***Table  STYLEREF 1 \s 4. SEQ Table \\* ARABIC \s 1 2:** The Quality of Service criteria for Interoperable Spatial Data Services.*

|Minimum availability|Definition|Lower limit of the percentage of time the service is estimated to be available on a yearly basis.|
| :- | :- | :- |
||Identifier URI|<http://inspire.ec.europa.eu/metadata-codelist/QualityOfServiceCriteria/availability>   |
||Value type|xsi:double between 0..100|
||Unit of measure|urn:ogc:def:uom:OGC::percent|
|Minimum performance|Definition|The maximum response time within which a typical request to the Spatial Data Service can be carried out in a normal situation, by returning at least the initial part of the response. The normal situation represents periods out of peak load. It is set at 90% of the time.|
||Identifier URI|<http://inspire.ec.europa.eu/metadata-codelist/QualityOfServiceCriteria/performance> |
||Value type|xsi:double|
||Unit of measure|<http://www.opengis.net/def/uom/SI/second> |
|Minimum capacity|Definition|Lower limit of the maximum number of simultaneous requests that can be completed within the limits of the declared performance.|
||Identifier URI|<http://inspire.ec.europa.eu/metadata-codelist/QualityOfServiceCriteria/capacity> |
||Value type|xsi:integer|
||Unit of measure|<http://www.opengis.net/def/uom/OGC/1.0/unity> |


**/gmd:MD\_Metadata/gmd:dataQualityInfo/gmd:DQ\_DataQuality/gmd:report:**

<gmd:report>

`  `<gmd:DQ\_ConceptualConsistency>

`    `<gmd:nameOfMeasure> 

`      `<gmx:Anchor

`        `xlink:href="http://inspire.ec.europa.eu/metadata-codelist/QualityOfServiceCriteria/performance">performance</gmx:Anchor>

`    `</gmd:nameOfMeasure>

`    `<gmd:measureDescription>

`      `<gco:CharacterString>The maximum time in which a typical request to the Spatial Data Service can be carried out in a off-peak load situation</gco:CharacterString>

`    `</gmd:measureDescription>

`    `<gmd:result>

`      `<gmd:DQ\_QuantitativeResult>

`        `<gmd:valueUnit xlink:href="http://www.opengis.net/def/uom/SI/second"/> 

`        `<gmd:value> 

`          `<gco:Record xmlns:xs="http://www.w3.org/2001/XMLSchema"

`            `xsi:type="xs:double">1.56</gco:Record>

`        `</gmd:value>

`      `</gmd:DQ\_QuantitativeResult>

`    `</gmd:result>

`  `</gmd:DQ\_ConceptualConsistency>

</gmd:report>

***Example  STYLEREF 1 \s 4. SEQ Example \\* ARABIC \s 1 15:** Declared Quality of Service for the criteria minimum performance. Similar gmd:report elements shall be given also for the other criteria minimum availability and minimum capacity. The type of the gco:Record element has been defined as a double precision floating point number using the local typing (xsi:type attribute).*



# ***Metadata for Harmonised Spatial Data Services***
**Conformance Class 7: metadata/2.0/sds-harmonised**

**Title:** INSPIRE Harmonised Spatial Data Services metadata**Conformance subject**: metadata record describing a Spatial Data Service encoded in ISO 19139 based XML format.Metadata record fulfilling all the Requirements of this Conformance Class is compliant with the INSPIRE metadata Implementation Rules for Spatial Data Services as defined in [**Regulation 1205/2008**], and the Article 14b "Interoperability arrangements and harmonisation requirements for invocable spatial data services" of amendment [Regulation 1312/2014] to [Regulation 1089/2010] adding its Annex VII.This Conformance Class includes TG Requirements C.1 – C.22, TG Requirements 3.1 – 3.8, TG Requirements 5.1 – 5.5, TG Requirements 6.1 – 6.5, and TG Requirements 7.1 – 7.3 of this specification.

The metadata elements described in the section 4.5.1 are direct child elements of *gmd:MD\_Metadata* element.
# **Identification info section**
The metadata elements described in this section are contained within the first *gmd:identificationInfo/srv:SV\_ServiceIdentification* child element of the *gmd:MD\_Metadata* element.
# **Invocation metadata**
A harmonised spatial data service shall have well documented interfaces and list the end points for each operation to enable machine to machine communication. This invocation metadata element is described in [Regulation1312/2014], Annex III, Part B 3:


*3. Invocation metadataThe invocation metadata element documents the interfaces of the harmonised spatial data service and lists the end points to enable machine-to machine communication.* 


**TG Requirement 7.seq Req \r11: metadata/2.0/req/sds-harmonised/invocation-metadata**

The invocation metadata shall be given for Harmonised Spatial Data Services. This information shall be encoded using one of the following two options:**Option 1**: All operations and the list of end points for them along with the information about the required and optional parameters for each operation shall be provided within the metadata record using the *srv:containsOperations/srv:SV\_OperationMetadata/srv:connectPoint* element. This element shall be the same as the element describing the access point (see  REF req\_sds\_sds\_invocable\_access\_point \h  \\* MERGEFORMAT TG Requirement 5.2). In this option the information provided by calling the access point together with the information about the conformity with the technical specifications described according to  REF req\_sds\_sds\_invocable\_conformity\_specs \h  \\* MERGEFORMAT TG Requirement 5.5 shall fulfil the invocation metadata requirements.**Option 2**: All operations and the list of end points for them along with the information about the required and optional parameters for each operation shall be provided within the metadata record using one *srv:containsOperations/srv:SV\_OperationMetadata* element for each provided operation. The contents of these element shall be given according to [ISO 19119, Section C.2].When the metadata record contains at least one *srv:containsOperations/srv:SV\_OperationMetadata* element, it is assumed that the option 2 has been chosen, otherwise it is assumed that the option 1 has been chosen.

**TG Requirement 7.seq Req2: metadata/2.0/req/sds-harmonised/operation-metadata**

If the metadata contains at least one the *srv:containsOperations/srv:SV\_OperationMetadata* element the invocation metadata within shall be encoded using at least the following child elements*:srv:operationName* element shall contain a unique identifier for interface described by the *srv:SV\_OperationMetadata* element. The value of this element is a Non-empty Free Text Element. The multiplicity of this element is 1.*srv:DCP/srv:DCPList* shall contain a reference to the Distributed Computing Platform on which the operation has been implemented. The multiplicity of this element is 1..\*.*srv:parameters/srv:SV\_Parameter* shall contain a description of a single request parameter to be used in invoking the operation. The content for this element shall be encoded as described in TG Requirement 7.3. The multiplicity of this element is 0..\*, and it is mandatory for all required and optional parameters provided by the operation.*srv:connectPoint/gmd:CI\_OnlineResource/gmd:URL* shall contain an end point URL to be used for accessing the service for executing the operation. The multiplicity of the element is 1..\*.

**TG Requirement 7.seq Req3: metadata/2.0/req/sds-harmonised/operation-metadata-parameters**

For all the required and optional request parameters of all the operations described using *srv:containsOperations/srv:SV\_OperationMetadata* elements, the following child elements of s*rv:parameters/srv:SV\_Parameter* element shall be given*:srv:name/gco:aName* shall contain the name of the parameter as used by the service. The content of this element is a Non-empty Free Text Element. The element *srv:name/gco:attributeType* shall contain the record or the type part of the attribute name. The multiplicity of the *srv:name* element is 1.*srv:optionality* shall contain information about whether the attribute is required or optional. The content of this element is a Non-empty Free Text Element. The multiplicity of this element is 1.srv:repeatability/gco:Boolean shall contain indicate whether the attribute can be given more than once in one operation. The value "true" shall be used indicate that the attribute may be repeated, "false" that only it may be given only once.*srv:valueType/gco:TypeName/gco:Name* shall indicate the data type of the attribute.



1. # **Abstract Test Suites**
This Annex only contains the structure of the Abstract Test Suites and the contained Conformance Classes for testing the metadata records against the requirements of this specification. The Test Cases for the Conformance Classes are provided in a separate repository[` `At the time of writing, the test cases for these Conformance Classes were not yet published. The repository for the Conformance Classes will be made available at <http://inspire.ec.europa.eu/id/ats/metadata/2.0>.
].

# ***ATS: Metadata for INSPIRE datasets and data set series***
# **Conformance Class 1: Baseline metadata for data sets and data set series**
This section contains test cases covering all the TG Requirements of Conformance Class 1: INSPIRE data sets and data set series baseline metadata (<http://inspire.ec.europa.eu/id/ats/metadata/2.0/datasets-and-series>).
# **Conformance Class 2: Interoperability metadata for data sets and data set series**
This section contains test cases covering all the TG Requirements of Conformance Class 2: INSPIRE data sets and data set series interoperability metadata (<http://inspire.ec.europa.eu/id/ats/metadata/2.0/isdss>).

# ***ATS: Metadata for INSPIRE Spatial Data Services***
# **Conformance Class 3: Baseline metadata for Spatial Data Services**
This section contains test cases covering all the TG Requirements of Conformance Class 3: INSPIRE Spatial Data Service baseline metadata (<http://inspire.ec.europa.eu/id/ats/metadata/2.0/sds>).
# **Conformance Class 4: Metadata for INSPIRE Network Services**
This section contains test cases covering all the TG Requirements of Conformance Class 4: INSPIRE Network Services metadata (<http://inspire.ec.europa.eu/id/ats/metadata/2.0/ns>).
# **Conformance Class 5: Metadata for Invocable Spatial Data Services**
This section contains test cases covering all the TG Requirements of Conformance Class 5: INSPIRE Invocable Spatial Data Services metadata (<http://inspire.ec.europa.eu/id/ats/metadata/2.0/sds-invocable>).
# **Conformance Class 6: Metadata for Interoperable Spatial Data Services**
This section contains test cases covering all the TG Requirements of Conformance Class 6: INSPIRE Interoperable Spatial Data Services metadata (<http://inspire.ec.europa.eu/id/ats/metadata/2.0/sds-interoperable>).
# **Conformance Class 7: Metadata for Harmonised Spatial Data Services**
This section contains test cases covering all the TG Requirements of Conformance Class 7: INSPIRE Harmonised Spatial Data Services metadata (<http://inspire.ec.europa.eu/id/ats/metadata/2.0/sds-harmonised>).
# **Mapping of ISO 19115:2003 Core elements and INSPIRE Implementing Rules for metadata (informative)**
# ***Spatial dataset and spatial dataset series***
The table below compares the core elements of ISO 19115 (see Table 3 in 6.5 of EN ISO 19115:2003) to the requirements of INSPIRE for spatial dataset and spatial dataset series as defined in the Implementing Rules for metadata.


|ISO 19115 Core|INSPIRE Implementing Rules for Metadata|Comments|
| :- | :- | :- |
|Dataset title (M)|Part B 1.1 Resource Title|-|
|Dataset reference date (M)|Part B 5 Temporal Reference|ISO 19115 is more demanding. The metadata shall contain a date of publication, revision or creation of the resource, while in INSPIRE the Temporal Reference can also be expressed through Temporal Extent. |
|Dataset responsible party (O)|Part B 9 Responsible organisation|INSPIRE is more demanding by mandating both the name of the organisation, and a contact e-mail address |
|Geographic location of the dataset (C)|Part B 4.1 Geographic Bounding Box|INSPIRE is more restrictive. A Geographic bounding box is mandated|
|Dataset language (M)|Part B 1.7 Resource Language|ISO 19115 is more demanding. It mandates the dataset language, even if the resource does not include any textual information. The ISO 19115 Dataset language is defaulted to the Metadata language.|
|Dataset character set (C)|-|<p>ISO 19115 is more demanding. The dataset character set has to be documented in ISO 19115 when ISO 10646-1 is not used. </p><p>The ISO 19115 element maps to the conditional “Character Encoding” metadata element defined in Art. 13(5) of the Implementing Rules on interoperability of spatial data sets and services. This element is mandatory only if an encoding is used that is not based on UTF-8 (the dominant encoding of ISO 10646-1).</p>|
|Dataset topic category (M)|Part B 2.1 Topic Category|-|
|Spatial resolution of the dataset (O)|Part B 6.2 Spatial Resolution|-|
|Abstract describing the dataset (M)|Part B 1.2 Resource abstract|-|
|Distribution format (O)|-|The ISO 19115 element maps to the mandatory “Encoding” metadata element defined in Art. 13(3) of the Implementing Rules on interoperability of spatial data sets and services.|
|Additional extent information for the dataset (vertical and temporal) (O)|Part B 5.1 Temporal extent|INSPIRE is more demanding. A temporal reference is mandated, and can be expressed as a temporal extent.|
|Spatial representation type (O)|-|The ISO 19115 element maps to the mandatory “Spatial Representation Type” metadata element defined in Art. 13(6) of the Implementing Rules on interoperability of spatial data sets and services.|
|Reference system (O)|-|The ISO 19115 element maps to the mandatory “Coordinate Reference System” and the conditional “Temporal Reference System” metadata elements defined in Art. 13(1) and (2) of the Implementing Rules on interoperability of spatial data sets and services set.|
|Lineage (O)|Part B 6.1 Lineage|INSPIRE is more demanding. A general lineage statement is mandated.|
|On-line resource (O)|Part B 1.4 Resource Locator|-|
|Metadata file identifier (O)|-|-|
|Metadata standard name (O)|-|-|
|Metadata standard version (O)|-|-|
|Metadata language (C)|Part B 10.3 Metadata Language|INSPIRE is more demanding. The metadata language is mandated even if it is defined by the encoding.|
|Metadata character set (C)|-|ISO 19115 is more demanding. The metadata character set has to be documented in ISO 19115 when ISO 10646-1 is not used. |
|Metadata point of contact (M)|Part B 10.1 Metadata point of contact|INSPIRE is more demanding by mandating both the name of the organisation, and a contact e-mail address.|
|Metadata date stamp (M)|Part B 10.2 Metadata Date|ISO is more restrictive because this element shall contain the “date that the metadata was created” and INSPIRE may contain the “date when the metadata record was created or updated |
|-|Part B 1.3 Resource Type|INSPIRE is more demanding|
||Part B 1.5 Unique Resource Identifier|INSPIRE is more demanding|
||Part B 3 Keyword|INSPIRE is more demanding|
|-|Part B 7 Conformity|INSPIRE is more demanding|
|-|Part B 8.1 Conditions for access and use|INSPIRE is more demanding|
|-|Part B 8.2 Limitations on public access|INSPIRE is more demanding|
# ***Services***
The table below compares the core requirements of ISO 19115 (see Table 3 in 6.5 of ISO 19115:2003) to the requirements of INSPIRE for services as defined in the Implementing Rules for metadata. The greyed lines correspond to core metadata elements not applicable to services.


|ISO 19115 Core|INSPIRE|Comments|
| :- | :- | :- |
|Dataset title (M)|Part B 1.1 Resource Title|-|
|Dataset reference date (M)|Part B 5 Temporal Reference |ISO 19115 is more demanding. Despite its name, this ISO 19115 Core metadata element applies to services. A reference date of the service (date of publication, revision or creation …) is mandated.|
|Dataset responsible party (O)|Part B 9 Responsible organisation|-|
|Geographic location of the dataset (C)|-|See INSPIRE Geographic Bounding Box|
|-|Part B 4.1 Geographic Bounding Box|The Geographic Bounding Box is handled in ISO 19119 with a different metadata element from the one corresponding to “Geographic location of the dataset”|
|Dataset language (M)|-|Not applicable to services|
|Dataset character set (C)|-|Not applicable to services|
|Dataset topic category (M)|-|Not applicable to services|
|Spatial resolution of the dataset (O)|Part B 6.2 Spatial Resolution|In the current version of ISO 19119, it is not possible to express the restriction of a service concerning the spatial resolution|
|Abstract describing the dataset (M)|Part B 1.2 Resource abstract|-|
|Distribution format (O)|-|-|
|Additional extent information for the dataset (O)|- |-|
|Spatial representation type (O)|-|-|
|Reference system (O)|-|-|
|Lineage (O)|-|-|
|On-line resource (O)|Part B 1.4 Resource Locator|-|
|Metadata file identifier (O)|-|-|
|Metadata standard name (O)|-|-|
|Metadata standard version (O)|-|-|
|Metadata language (C)|Part B 10.3 Metadata Language|INSPIRE is more demanding. The metadata language is mandated.|
|Metadata character set (C)|-|ISO 19115 is more demanding. The metadata character set has to be documented in ISO 19115 when ISO 10646-1 is not used. |
|Metadata point of contact (M)|Part B 10.1 Metadata point of contact|-|
|Metadata date stamp (M)|Part B 10.2 Metadata Date|ISO is more restrictive because this element shall contain the “date that the metadata was created” and INSPIRE may contain the “date when the metadata record was created or updated |
|-|Part B 1.3 Resource Type|INSPIRE is more demanding|
|-|Part B 1.6 Coupled Resource|Optional in INSPIRE|
|-|Part B 2.2 Spatial Data Service Type|INSPIRE is more demanding|
||Part B 3 Keyword|INSPIRE is more demanding|
|-|Part B 7 Conformity|INSPIRE is more demanding|
|-|Part B 8.1 Conditions for access and use|INSPIRE is more demanding|
|-|Part B 8.2 Limitations on public access|INSPIRE is more demanding|

# ***Conclusion***

- The conformance of an ISO 19115 metadata set to the ISO 19115 Core does not guarantee the conformance to INSPIRE;
- The use of these guidelines to create INSPIRE metadata ensures that the metadata is not in conflict with ISO 19115. However, full conformance to ISO 19115 implies the provision of additional metadata elements which are not required by the INSPIRE Implementing Rule on Metadata.



# **INSPIRE metadata element catalog (informative)**
The following tables describe the mapping between the metadata elements of INSPIRE, as defined in the [Regulation 1205/2008] and [Regulation 1089/2010] (including its amendments [Regulation 1253/2013] and [Regulation 1312/2014]) and ISO 19115/ISO 19119. For each of the INSPIRE Metadata element, the mapping is composed of the main characteristics of the metadata element as they are defined in the INSPIRE implementing rules (IR) for metadata and the main characteristics of the corresponding metadata element of ISO 19115 or ISO 19119:

- The metadata element name as used in the INSPIRE implementing rules;
- The reference to the paragraph of the INSPIRE implementing rules describing the metadata element;
- The definition, which gives the current ISO 19115 or ISO 19119 terms for describing the metadata element (Annex B of ISO 19115 standard: Data Dictionary for geographic metadata or Annex C of ISO 19119: Data dictionary for geographic service metadata);
- The number and the name that identifies the metadata element inside tables in ISO 19115 (or ISO 19119) published standard;
- An XPath expression indicating the metadata element within the ISO 19115 / ISO 19119 UML model (see 2.1.1);
- The INSPIRE obligation/condition applicable to the metadata element;
- The INSPIRE multiplicity of the metadata element;
- The Data Type and the Domain required by the metadata element; 
- An example that illustrates the description of the metadata element by providing a concrete case
- Some comments, which give more information about the metadata element 

Apart from the tables collecting the main significant aspects, additional information is provided regarding: the description of the metadata element, advices on its fulfilment and important requirements and recommendations.

The first section C.1 gives a list of all INSPIRE metadata elements for spatial data sets and data set series as well as for Spatial Data Services as described in the INSPIRE Implementing Rules [Regulation 1205/2008] and [Regulation 1089/2010] (including its amendments [Regulation 1253/2013] and [Regulation 1312/2014]). Details of each elements as well as its mapping to [ISO 19115] or [ISO 19119] and [ISO 19139] is given in sections C.2 - C.6.

Section C.7 contains a collection of theme-specific metadata elements described in the INSPIRE Data Specifications.

# ***Overview of the required INSPIRE metadata elements***
# **Spatial data sets and data sets series**


|Implementing rule|Section / article|Element name|INSPIRE multiplicity|INSPIRE obligation / condition / note|
| :- | :- | :- | :- | :- |
|[Regulation 1205/2008]|Part B 1.1|Resource title|1|Mandatory|
|[Regulation 1205/2008]|Part B 1.2|Resource abstract|1|Mandatory|
|[Regulation 1205/2008]|Part B 1.3|Resource type|1|Mandatory|
|[Regulation 1205/2008]|Part B 1.4|Resource locator|0..\*|Mandatory if a URL is available to obtain more information on the resources and/or access related services.|
|[Regulation 1205/2008]|Part B 1.5|Unique resource identifier|1..\*|Mandatory|
|[Regulation 1205/2008]|Part B 1.7|Resource language|0..\*|Mandatory if the resource includes textual information.|
|[Regulation 1205/2008]|Part B 2.1|Topic category|1..\*|Mandatory|
|[Regulation 1205/2008]|Part B 3.1|Keyword value|1..\*|Mandatory|
|[Regulation 1205/2008]|Part B 3.2|Originating controlled vocabulary|0..1|Conditional: Mandatory for each keyword if the keyword value originates from a controlled vocabulary|
|[Regulation 1205/2008]|Part B 4.1|Geographic bounding box|1..\*|Mandatory|
|[Regulation 1205/2008]|Part B 5|Temporal reference||At least one of Temporal extent, Date of publication, Date of last revision or Date of creation must be given|
|[Regulation 1205/2008]|Part B 5.1|Temporal extent|0..\*|Conditional|
|[Regulation 1205/2008]|Part B 5.2|Date of publication|0..\*|Conditional|
|[Regulation 1205/2008]|Part B 5.3|Date of last revision|0..1|Conditional|
|[Regulation 1205/2008]|Part B 5.4|Date of creation|0..1|Conditional|
|[Regulation 1205/2008]|Part B 6.1|Lineage|1|Mandatory|
|[Regulation 1205/2008]|Part B 6.2|Spatial resolution|0..\*|Mandatory if an equivalent scale or a resolution distance can be specified|
|[Regulation 1205/2008]|Part B 7|Conformity|1..\*|Mandatory|
|[Regulation 1205/2008]|Part B 7.1|Specification|1|Mandatory for each conformity statement|
|[Regulation 1205/2008]|Part B 7.2|Degree|1|Mandatory for each conformity statement|
|[Regulation 1205/2008]|Part B 8.1|Conditions applying to access and use|1..\*|Special values for unknown conditions or no applying conditions may be used|
|[Regulation 1205/2008]|Part B 8.2|Limitations on public access|1..\*|Special value for no limitations may be used|
|[Regulation 1205/2008]|Part B 9|Responsible organisation|1..\*|Mandatory|
|[Regulation 1205/2008]|` `Part B 9.1|Responsible party|1|Mandatory for each responsible organisation|
|[Regulation 1205/2008]|` `Part B 9.2|Responsible party role|1|Mandatory for each responsible organisation|
|[Regulation 1205/2008]|Part B 10.1|Metadata point of contact|1..\*|Mandatory|
|[Regulation 1205/2008]|Part B 10.2|Metadata date|1|Mandatory|
|[Regulation 1205/2008]|Part B 10.3|Metadata language|1|Mandatory|
|[Regulation 1089/2010]|Article 13, clause 1|Coordinate Reference System|1..\*|Mandatory to comply with [Regulation 1089/2010]|
|[Regulation 1089/2010]|Article 13, clause 2|Temporal Reference System|0..\*|Mandatory for compliance with [Regulation 1089/2010] only if a non-default temporal reference system (i.e. Gregorian Calendar or the Coordinated Universal Time) is used|
|[Regulation 1089/2010]|Article 13, clause 3|Encoding|1..\*|Mandatory to comply with [Regulation 1089/2010]|
|[Regulation 1089/2010]|Article 13, clause 4|Topological consistency|0..\*|Mandatory for compliance with [Regulation 1089/2010] only if the data set includes types from the Generic Network Model and does not assure centreline topology (connectivity of centrelines) for the network|
|[Regulation 1089/2010]|Article 13, clause 5|Character Encoding|0..\*|<p>Mandatory for compliance with [Regulation 1089/2010] only if the data set is not using UTF-8 encoding</p><p></p>|
|[Regulation 1089/2010] amended by [Regulation 1253/2013]|Article 13, clause 6|Spatial representation type|1..\*|Mandatory to comply with [Regulation 1089/2010]|

# **Spatial Data Services**

|Implementing rule|Section / article|Element name|INSPIRE multiplicity|INSPIRE obligation / condition / note|
| :- | :- | :- | :- | :- |
|[Regulation 1205/2008]|Part B 1.1|Resource title|1|Mandatory|
|[Regulation 1205/2008]|Part B 1.2|Resource abstract|1|Mandatory|
|[Regulation 1205/2008]|Part B 1.3|Resource type|1|Mandatory|
|[Regulation 1205/2008]|Part B 1.4|Resource locator|0..\*|Conditional, mandatory if linkage to service is available|
|[Regulation 1205/2008]|Part B 1.6|Coupled resource|0..\*|Conditional, mandatory if linkage to data sets on which the service operates are available.|
|[Regulation 1205/2008]|Part B 2.2|Spatial data service type|1|Mandatory|
|[Regulation 1205/2008]|Part B 3.1|Keyword value|1..\*|Mandatory|
|[Regulation 1205/2008]|Part B 3.2|Originating controlled vocabulary|0..1|Conditional, mandatory for each keyword if the keyword value originates from a controlled vocabulary|
|[Regulation 1205/2008]|Part B 4.1|Geographic bounding box|0..\*|Conditional, mandatory for services with an explicit geographic extent.|
|[Regulation 1205/2008]|Part B 5|Temporal reference||At least one of Temporal extent, Date of publication, Date of last revision or Date of creation must be given|
|[Regulation 1205/2008]|Part B 5.1|Temporal extent|0..\*|Conditional|
|[Regulation 1205/2008]|Part B 5.2|Date of publication|0..\*|Conditional|
|[Regulation 1205/2008]|Part B 5.3|Date of last revision|0..1|Conditional|
|[Regulation 1205/2008]|Part B 5.4|Date of creation|0..1|Conditional|
|[Regulation 1205/2008]|Part B 6.2|Spatial resolution|0..\*|Mandatory when there is a restriction on the spatial resolution for this service|
|[Regulation 1205/2008]|Part B 7|Conformity|1..\*|Mandatory|
|[Regulation 1205/2008]|Part B 7.1|Specification|1|Mandatory for each conformity statement|
|[Regulation 1205/2008]|Part B 7.2|Degree|1|Mandatory for each conformity statement|
|[Regulation 1205/2008]|Part B 8.1|Conditions applying to access and use|1..\*|Special values for unknown conditions or no applying conditions may be used|
|[Regulation 1205/2008]|Part B 8.2|Limitations on public access|1..\*|Special value for no limitations may be used|
|[Regulation 1205/2008]|Part B 9|Responsible organisation|1..\*|Mandatory|
|[Regulation 1205/2008]|` `Part B 9.1|Responsible party|1|Mandatory for each responsible organisation|
|[Regulation 1205/2008]|` `Part B 9.2|Responsible party role|1|Mandatory for each responsible organisation|
|[Regulation 1205/2008]|Part B 10.1|Metadata point of contact|1..\*|Mandatory|
|[Regulation 1205/2008]|Part B 10.2|Metadata date|1|Mandatory|
|[Regulation 1205/2008]|Part B 10.3|Metadata language|1|Mandatory|
|[Regulation 1089/2010], Annex V, (Invocable SDS)|Part B 1|Category|0..1|Conditional, mandatory for an Invocable Spatial Data Service in order to comply with Annex V of [Regulation 1089/2010]|
|[Regulation 1089/2010], Annex VI, (Interoperable SDS)|Part B 3|Coordinate Reference System Identifier|1..\*|Mandatory if relevant for an Interoperable Spatial Data Service in order to comply with Annex VI of [Regulation 1089/2010]|
|[Regulation 1089/2010], Annex VI, (Interoperable SDS)|Part B 4|Quality of service|3..\*|Mandatory for an Interoperable Spatial Data Service. Three criteria for minimum quality of service shall be given to comply with Annex VI of [Regulation 1089/2010]: Availability, Performance and Capacity|
|[Regulation 1089/2010], Annex VII, (Harmonised SDS)|Part B 3|Invocation metadata |1..\*|Mandatory for a Harmonised Spatial Data Service in order to comply with Annex VII of [Regulation 1089/2010]|


# ***INSPIRE Implementing Rules for metadata (regulation 1205/2008)***
# **Resource title**

|Metadata element name|Resource title|
| :- | :- |
|Reference|Part B 1.1|
|Definition|Name by which the cited resource is known|
|ISO 19115 number and name|360. title|
|ISO/TS 19139 path |identificationInfo[1]/\*/citation/\*/title|
|INSPIRE obligation / condition|Mandatory|
|INSPIRE multiplicity|[1]|
|Data type (and ISO 19115 no.) |CharacterString|
|Domain|Free text|
|Example|SPI: Standardized Precipitation Index|
|Comments||

# **Resource abstract**

|Metadata element name|Resource abstract|
| :- | :- |
|Reference|Part B 1.2|
|Definition|Brief narrative summary of the content of the resource(s)|
|ISO 19115 number and name|25. abstract|
|ISO/TS 19139 path |identificationInfo[1]/\*/abstract|
|INSPIRE obligation / condition|Mandatory|
|INSPIRE multiplicity|[1]|
|Data type (and ISO 19115 no.) |CharacterString|
|Domain|Free text|
|Example|The Standardized Precipitation Index (SPI-n) is a statistical indicator comparing the total precipitation received at a particular location during a period of n months with the long-term rainfall distribution for the same period of time at that location. SPI is calculated on a monthly basis for a moving window of n months, where n indicates the rainfall accumulation period, which is typically 1, 3, 6, 9, 12, 24 or 48 months. The corresponding SPIs are denoted as SPI-1, SPI-3, SPI-6, etc. In order to allow for the statistical comparison of wetter and drier climates, SPI is based on a transformation of the accumulated precipitation into a standard normal variable with zero mean and variance equal to one. SPI results are given in units of standard deviation from the long-term mean of the standardized distribution. In 2010 WMO selected the SPI as a key meteorological drought indicator to be produced operationally by meteorological services|
|Comments||

# **Resource type**

|Metadata element name|Resource type|
| :- | :- |
|Reference|Part B 1.3|
|Definition|Scope to which metadata applies|
|ISO 19115 number and name|6. hierarchyLevel|
|ISO/TS 19139 path |hierarchyLevel|
|INSPIRE obligation / condition|Mandatory|
|INSPIRE multiplicity|[1]|
|Data type (and ISO 19115 no.) |MD\_ScopeCode|
|Domain|CodeList (see annex B.5.25 of ISO 19115)|
|Example|dataset|
|Comments||


# **Resource locator**

|Metadata element name|Resource locator|
| :- | :- |
|Reference|Part B 1.4|
|Definition|Location (address) for on-line access using a Uniform Resource Locator address or similar addressing scheme|
|ISO 19115 number and name|397. linkage|
|ISO/TS 19139 path |distributionInfo/\*/transferOptions/\*/onLine/\*/linkage|
|INSPIRE obligation / condition|- Conditional for spatial dataset and spatial dataset series: Mandatory if a URL is available to obtain more information on the resources and/or access related services.|
|INSPIRE multiplicity|[0..\*] |
|Data type (and ISO 19115 no.) |URL|
|Domain|URL (IETF RFC1738 and IETF RFC 2056)|
|Example|<p>http://edo.jrc.ec.europa.eu/chm/ows.php?VERSION=1.3.0&SERVICE=WMS&REQUEST=GetCapabilities</p><p>http://www.eea.europa.eu/data-and-maps/data/wise-river-basin-districts-rbds-1</p>|
|Comments|<p>A Resource Locator could be described, moreover, by other additional elements as a Title, a Description and a Function. In that case, the Title and the Description shall be free text and the Function shall be filled by the CI\_OnLineFunctionCode (ISO 19115 code list). </p><p>Examples of Resource Locator with these additional elements:</p><p>- JRC EDO (European Drought Observatory) - Drought Indexes WMS</p><p>&emsp;- Linkage: http://edo.jrc.ec.europa.eu/chm/ows.php?VERSION=1.3.0&SERVICE=WMS&REQUEST=GetCapabilities</p><p>&emsp;- Title: JRC EDO (European Drought Observatory) - Drought Indexes WMS</p><p>&emsp;- Description: WMS delivering maps of drought indexes provided by the European Drought Observatory (EDO). </p><p>&emsp;- Function: information</p><p>- WISE River basin districts (RBDs)</p><p>&emsp;- Linkage: http://www.eea.europa.eu/data-and-maps/data/wise-river-basin-districts-rbds-1</p><p>&emsp;- Title: WISE River basin districts (RBDs)</p><p>&emsp;- Description: Version 1.4 (06/2011) - River Basin Districts (RBDs) and/or their subunits (RBDSUs) are the main units for the management of river basins and have been delineated by Member States under Article 3 and updated by reporting to Article 13 of the Water Framework Directive. </p><p>&emsp;- Function: information</p>|

# **Unique resource identifier**

|Metadata element name|Unique resource identifier|
| :- | :- |
|Reference|Part B 1.5|
|Definition|Value uniquely identifying an object within a namespace|
|ISO 19115 number and name|365. identifier|
|ISO/TS 19139 path |identificationInfo[1]/\*/citation/\*/identifier|
|INSPIRE obligation / condition|Mandatory for dataset and dataset series|
|INSPIRE multiplicity|[1..\*] for dataset and series|
|Data type (and ISO 19115 no.) |205. MD\_Identifier |
|Domain|URI (IETF RFC 3986)|
|Example|<p>The Unique resource identifier semantically consisting of</p><p>namespace: **https://example.org/** </p><p>and identifier: **ab749859**</p><p></p><p>and is provided together in element *code:* </p><p>https://example.org/ab749859</p>|
|Comments|The unique resource identifier is needed to provide a queryable information when following data-service-coupling (see also  REF \_Ref461283412 \r \h 4.1.2.4). Therefore it is necessary to have the identifier itself together with the namespace in element code. The use of RS\_Identifier (with a separate element codeSpace) is not suitable here|

# **Coupled resource**

|Metadata element name|Coupled resource |
| :- | :- |
|Reference|Part B 1.6|
|Definition|Provides information about the datasets that the service operates on.|
|ISO 19119 number and name|9 of table C.1. operatesOn|
|ISO/TS 19139 path |identificationInfo[1]/\*/operatesOn|
|INSPIRE obligation / condition|<p>- Not applicable to dataset and dataset series</p><p>- Conditional to services: Mandatory if linkage to datasets on which the service operates are available.</p>|
|INSPIRE multiplicity|<p>[0] for datasets and series</p><p>[0..\*] for services</p>|
|Data type (and ISO 19115 no.) |36. MD\_DataIdentification|
|Domain|A unique resource identifier or locator (URL) of the MD\_DataIdentification object|
|Example|<http://vap-xgeodev.jrc.ec.europa.eu/geonetwork/srv/eng/csw?SERVICE=CSW&VERSION=2.0.2&REQUEST=GetRecordById&ID=f9ee6623-cf4c-11e1-9105-0017085a97ab&OUTPUTSCHEMA=http://www.isotc211.org/2005/gmd&ELEMENTSETNAME=full#lakes>|
|Comments|<p>The implementation of this element by reference means that the xlink:href element are pointing to a metadatarecord that contains a MD\_DataIdentification object. The reference to the MD\_DataIdentification object is done using the xpointer reference using the #-sign. The example above points to #lakes which is the ID of this object. Check example on xml encoding in section  REF \_Ref461283642 \r \h  \\* MERGEFORMAT 0.</p><p></p><p>The Unique Resource Identifier for the can be explicilty defined for the target dataset using the optional uuidref.attribute.</p>|

# **Resource language**

|Metadata element name|Resource language|
| :- | :- |
|Reference|Part B 1.7|
|Definition|Language(s) used within the datasets|
|ISO 19115 number and name|39. language|
|ISO/TS 19139 path |identificationInfo[1]/\*/language|
|INSPIRE obligation / condition|<p>- Conditional for spatial dataset and spatial dataset series: Mandatory if the resource includes textual information.</p><p>- Not applicable to services </p>|
|INSPIRE multiplicity|<p>[0..\*] for datasets and series</p><p>[0] for services</p>|
|Data type (and ISO 19115 no.) |LanguageCode (ISO/TS 19139)|
|Domain|<p>Codelist (See ISO/TS 19139) based on alpha-3 codes of ISO 639-2. Use only three-letter codes from in ISO 639-2/B (bibliographic codes), </p><p></p><p>The list of codes for the 24 official EU languages is:</p><p>Bulgarian – bul 	Irish – gle</p><p>Croatian – hrv	Italian – ita</p><p>Czech – cze	Latvian – lav</p><p>Danish – dan	Lithuanian – lit</p><p>Dutch – dut	Maltese – mlt</p><p>English – eng	Polish – pol</p><p>Estonian – est	Portuguese – por</p><p>Finnish – fin	Romanian – rum</p><p>French – fre	Slovak – slo</p><p>German – ger	Slovenian – slv</p><p>Greek – gre	Spanish – spa</p><p>Hungarian – hun	Swedish – swe</p><p></p><p>The list of all the codes is defined at <http://www.loc.gov/standards/iso639-2/> </p><p>Regional languages also are included in this list.</p><p></p>|
|Example|eng|
|Comments||

# **Topic category**

|Metadata element name|Topic category|
| :- | :- |
|Reference|Part B 2.1|
|Definition|Main theme(s) of the dataset|
|ISO 19115 number and name|41. topicCategory|
|ISO/TS 19139 path |identificationInfo[1]/\*/topicCategory|
|INSPIRE obligation / condition|<p>- Mandatory for datasets and dataset series </p><p>- Not applicable to services</p>|
|INSPIRE multiplicity|<p>[1..\*] for datasets and dataset series</p><p>[0] for services</p>|
|Data type (and ISO 19115 no.) |MD\_TopicCategory|
|Domain|Enumeration (See B.5.27 of ISO 19115 or Part D 2 of [Regulation 1205/2008])|
|Example|climatologyMeteorologyAtmosphere|
|Comments|The topic categories defined in Part D 2 of [Regulation 1205/2008] are derived directly from the topic categories defined in MD\_TopicCategoryCode (B.5.27 of ISO 19115)|

# **Spatial data service type**

|Metadata element name|Spatial data service type|
| :- | :- |
|Reference|Part B 2.2|
|Definition|A service type name from a registry of services|
|ISO 19119 number and name|1 of table C.1. serviceType|
|ISO/TS 19139 path |identificationInfo[1]/\*/serviceType|
|INSPIRE obligation / condition|<p>- Not applicable to datasets and dataset series </p><p>- Mandatory for services</p><p></p>|
|INSPIRE multiplicity|<p>[1] for services</p><p>[0] for datasets and dataset series</p>|
|Data type (and ISO 19115 no.) |GenericName|
|Domain|Code list. See Part D 3 of [Regulation 1205/2008]|
|Example|view|
|Comments||

# **Keyword value**

|Metadata element name|Keyword value|
| :- | :- |
|Reference|Part B 3.1|
|Definition|Commonly used word(s) or formalised word(s) or phrase(s) used to describe the subject|
|ISO 19115 number and name|53. keyword|
|ISO/TS 19139 path |identificationInfo[1]/\*/descriptiveKeywords/\*/keyword|
|INSPIRE obligation / condition|Mandatory|
|INSPIRE multiplicity|[1..\*]|
|Data type (and ISO 19115 no.) |CharacterString|
|Domain|Free text|
|Example|<p>Atmospheric conditions (INSPIRE Spatial Data Theme)</p><p>humanCatalogueViewer (spatial data service subcategory)</p><p>water springs (AGROVOC)</p><p>rain water (GEMET Concepts)</p>|
|Comments|Each instance of ISO 19115 keyword may originate from a controlled vocabulary described through the thesaurusName property of the instance of descriptiveKeywords to which the keyword pertains|

# **Originating controlled vocabulary**

|Metadata element name|Originating controlled vocabulary|
| :- | :- |
|Reference|Part B 3.2|
|Definition|Name of the formally registered thesaurus or a similar authoritative source of keywords|
|ISO 19115 number and name|55. thesaurusName|
|ISO/TS 19139 path |identificationInfo[1]/\*/descriptiveKeywords/\*/thesaurusName|
|INSPIRE obligation / condition|Conditional: Mandatory if the keyword value originates from a controlled vocabulary|
|INSPIRE multiplicity|[0..1] relative to a single Keyword, but there may be many keywords originating from different controlled vocabularies|
|Data type (and ISO 19115 no.) |CI\_Citation|
|Domain|<p>The following properties are expected:</p><p>- Title (characterString and free text)</p><p>- Reference date (CI\_Date):</p><p>&emsp;- dateType: creation, publication or revision</p><p>&emsp;- date: an effective date</p>|
|Example|<p>Identification for a keyword originating from GEMET- INSPIRE themes:</p><p>- title: GEMET - INSPIRE themes, version 1.0</p><p>- date:</p><p>&emsp;- dateType: publication</p><p>&emsp;- date: 2008-06-01</p><p></p><p>Identification for a keyword originating from GEMET - Concepts:</p><p>- title: GEMET - Concepts, version 2.4</p><p>- date: </p><p>&emsp;- dateType: publication</p><p>&emsp;- date: 2010-01-13</p><p></p><p>Identification for a keyword originating from AGROVOC:</p><p>- title: AGROVOC</p><p>- date: </p><p>&emsp;- dateType: publication</p><p>&emsp;- date: 2008-04-14</p><p></p>|
|Comments||

# **Geographic bounding box**

|Metadata element name|Geographic bounding box|
| :- | :- |
|Reference|Part B 4.1|
|Definition|<p>Western-most coordinate of the limit of the dataset extent, expressed in longitude in decimal degrees (positive east).</p><p>Eastern-most coordinate of the limit of the dataset extent, expressed in longitude in decimal degrees (positive east)</p><p>Northern-most coordinate of the limit of the dataset extent, expressed in latitude in decimal degrees (positive north)</p><p>Southern-most coordinate of the limit of the dataset extent, expressed in latitude in decimal degrees (positive north).</p>|
|ISO 19115 number and name|<p>344. westBoundLongitude</p><p>345. eastBoundLongitude</p><p>346. southBoundLatitude</p><p>347. northBoundLatitude</p>|
|ISO/TS 19139 path |<p>identificationInfo[1]/\*/extent/\*/geographicElement/\*/westBoundLongitude</p><p>identificationInfo[1]/\*/extent/\*/geographicElement/\*/eastBoundLongitude</p><p>identificationInfo[1]/\*/extent/\*/geographicElement/\*/southBoundLatitude</p><p>identificationInfo[1]/\*/extent/\*/geographicElement/\*/northBoundLatitude</p>|
|INSPIRE obligation / condition|<p>- Mandatory for datasets and spatial dataset series </p><p>- Conditional for spatial services: mandatory for services with an explicit geographic extent</p><p></p>|
|INSPIRE multiplicity|<p>[1..\*] for spatial data sets and spatial dataset series</p><p>[0..\*] for spatial data services</p>|
|Data type (and ISO 19115 no.) |Decimal|
|Domain|<p>-180.00 ≤ westBoundLongitude ≤ 180.00</p><p>-180.00 ≤ eastBoundLongitude ≤ 180.00</p><p>-90.00 ≤ southBoundingLatitude ≤ 90.00</p><p>-90.00 ≤ northBoundingLatitude ≤ 90.00</p>|
|Example|<p>-15.00 (westBoundLongitude )</p><p>45.00 (eastBoundLongitude )</p><p>35.00 (southBoundLatitude)</p><p>72.00 (northBoundLatitude)</p>|
|Comments|<p>- There may be as many bounding boxes defining the geographic location of the resource as instances of identificationInfo[1]/\*/extent/\*/geographicElement having the westBoundLongitude, eastBoundLongitude, southBoundLatitude and northBoundLatitude properties. The four coordinates of the bounding box originate from the same instance.</p><p>- If the bounding box crosses the 180 meridian, then the value of the westBoundLongitude will be greater than the eastBoundLongitude value.</p><p></p>|

# **Temporal extent**

|Metadata element name|Temporal extent|
| :- | :- |
|Reference|Part B 5.1|
|Definition|Time period covered by the content of the dataset|
|ISO 19115 number and name|351. extent|
|ISO/TS 19139 path |identificationInfo[1]/\*/extent/\*/temporalElement/\*/extent|
|INSPIRE obligation / condition|Conditional: At least one temporal reference is required|
|INSPIRE multiplicity|[0..\*] for temporal extent but at least one temporal reference is required|
|Data type (and ISO 19115 no.) |TM\_Primitive|
|Domain|As described in ISO 19108|
|Example|From 2008-01-01T11:45:30 to 2008-12-31T09:10:00 |
|Comments|The overall time period covered by the content of the resource may be composed of one or many instances|

# **Date of publication**

|Metadata element name|Date of publication|
| :- | :- |
|Reference|Part B 5.2|
|Definition|Reference date for the cited resource - publication|
|ISO 19115 number and name|362. date|
|ISO/TS 19139 path |identificationInfo[1]/\*/citation/\*/date[./\*/dateType/\*/text()='publication']/\*/date|
|INSPIRE obligation / condition|Conditional: at least one date of publication / date of creation / date of revision is required |
|INSPIRE multiplicity|[0..\*] but at least one date of publication / date of creation / date of revision or one temporal extent is required|
|Data type (and ISO 19115 no.) |393. CI\_Date|
|Domain|Described in ISO 19108 and ISO 8601|
|Example|<p>2009-03-15</p><p>2009-03-15T11:15:00</p>|
|Comments||

# **Date of last revision**

|Metadata element name|Date of last revision|
| :- | :- |
|Reference|Part B 5.3|
|Definition|Reference date for the cited resource - revision|
|ISO 19115 number and name|362. date|
|ISO/TS 19139 path |identificationInfo[1]/\*/citation/\*/date[./\*/dateType/\*/text()='publication']/\*/date|
|INSPIRE obligation / condition|Conditional: at least one date of publication / date of creation / date of revision is required |
|INSPIRE multiplicity|[0..1] but at least one date of publication / date of creation / date of revision or one temporal extent is required|
|Data type (and ISO 19115 no.) |393. CI\_Date|
|Domain|Described in ISO 19108 and ISO 8601|
|Example|<p>2009-04-15</p><p>2009-04-15T11:15:00</p>|
|Comments|There may be more than one revision date provided in an ISO 19115 metadata, but INSPIRE will consider as date of last revision the more recent one|

# **Date of creation**

|Metadata element name|Date of creation|
| :- | :- |
|Reference|Part B 5.4|
|Definition|Reference date for the cited resource - creation|
|ISO 19115 number and name|362. date|
|ISO/TS 19139 path |identificationInfo[1]/\*/citation/\*/date[./\*/dateType/\*/text()='publication']/\*/date|
|INSPIRE obligation / condition|Conditional: at least one date of publication / date of creation / date of revision is required |
|INSPIRE multiplicity|[0..1] but at least one date of publication / date of creation / date of revision or one temporal extent is required|
|Data type (and ISO 19115 no.) |393. CI\_Date|
|Domain|Described in ISO 19108 and ISO 8601|
|Example|<p>2009-02-15</p><p>2009-02-15T11:15:00</p>|
|Comments||

# **Lineage**

|Metadata element name|Lineage|
| :- | :- |
|Reference|Part B 6.1|
|Definition|General explanation of the data producer’s knowledge about the lineage of a dataset|
|ISO 19115 number and name|83. statement|
|ISO/TS 19139 path |dataQualityInfo/\*/lineage/\*/statement|
|INSPIRE obligation / condition|<p>- Mandatory for spatial dataset and spatial dataset series.</p><p>- Not applicable to services.</p>|
|INSPIRE multiplicity|<p>[1] for datasets and data set series</p><p>[0] for spatial data services</p>|
|Data type (and ISO 19115 no.) |CharacterString|
|Domain|Free text|
|Example|Computation of the SPI involves fitting a probability density function to a given frequency distribution of precipitation totals for a station or grid point and for an accumulation period. We use the gamma probability density function. The statistics for the frequency distribution are calculated on the basis of a reference period of at least 30 years. The parameters of the probability density function are then used to find the cumulative probability of the observed precipitation for the required month and temporal scale. This cumulative probability is then transformed to the standardised normal distribution with mean zero and variance one, which results in the value of the SPI. The SPI values are computed using the so-called MARS weather stations as rainfall input data. Refer the MARS weather catalogue for characteristics of the quality and quantity of these data. We only rely on the rainfall data input|
|Comments||

# **Spatial resolution**

|Metadata element name|Spatial resolution|
| :- | :- |
|Reference|Part B 6.2|
|Definition|<p>- Equivalent scale: level of detail expressed as the scale denominator of a comparable hardcopy map or chart</p><p>- Distance: ground sample distance</p>|
|ISO 19115 number and name|<p>- 60. equivalentScale</p><p>- 61. distance</p>|
|ISO/TS 19139 path |<p>- identificationInfo[1]/\*/spatialResolution/\*/equivalentScale/\*/denominator (equivalent scale)</p><p>- identificationInfo[1]/\*/spatialResolution/\*/distance (distance)</p>|
|INSPIRE obligation / condition|<p>- Conditional: Mandatory if an equivalent scale or a resolution distance can be specified.</p><p>- Conditional: Mandatory when there is a restriction on the spatial resolution for service.</p>|
|INSPIRE multiplicity|[0..\*] |
|Data type (and ISO 19115 no.) |<p>- Integer (equivalent scale)</p><p>- Distance (distance)</p>|
|Domain|<p>- positive integer (equivalent scale)</p><p>- number expressing the distance value and a unit of measure of the distance value (distance)</p>|
|Example|<p>50000 (e.g. 1:50000 scale map)</p><p>0.25 (degrees)</p>|
|Comments|For services, it is not possible to express the restriction of a service concerning the spatial resolution in the current version of ISO 19119. While the problem is addressed by the standardization community, spatial resolution restrictions for services shall be expressed in the Abstract|

# **Specification**

|Metadata element name|Specification|
| :- | :- |
|Reference|Part B 7.1|
|Definition|Citation of the product specification or user requirement against which data is being evaluated|
|ISO 19115 number and name|130. specification|
|ISO/TS 19139 path |dataQualityInfo/\*/report/\*/result/\*/specification|
|INSPIRE obligation / condition|Mandatory|
|INSPIRE multiplicity|[1] understood in the context of a conformity statement when reported in the metadata – there may be more than one conformity statement|
|Data type (and ISO 19115 no.) |359. CI\_Citation|
|Domain|<p>The following properties are expected:</p><p>- Title (characterString and free text)</p><p>- Reference date (CI\_Date):</p><p>&emsp;- dateType: creation, publication or revision</p><p>date: an effective date</p>|
|Example|<p>- title: COMMISSION REGULATION (EU) No 1089/2010 of 23 November 2010 implementing Directive 2007/2/EC of the European Parliament and of the Council as regards interoperability of spatial data sets and services</p><p>- date:</p><p>&emsp;- dateType: publication</p><p>&emsp;- date: 2010-12-08</p>|
|Comments||

# **Degree**

|Metadata element name|Degree|
| :- | :- |
|Reference|Part B 7.2|
|Definition|Indication of the conformance result|
|ISO 19115 number and name|132. pass|
|ISO/TS 19139 path |dataQualityInfo/\*/report/\*/result/\*/pass|
|INSPIRE obligation / condition|Mandatory |
|INSPIRE multiplicity|[1] understood in the context of a conformity statement when reported in the metadata – there may be more than one conformity statement|
|Data type (and ISO 19115 no.) |Boolean|
|Domain|<p>- true if conformant</p><p>- false if not conformant</p><p>- null (with nilReason = “unknown”) if not evaluated</p>|
|Example|true|
|Comments||

# **Conditions applying to access and use**

|Metadata element name|Conditions applying to access and use|
| :- | :- |
|Reference|Part B 8.1|
|Definition|Restrictions on the access of a resource or metadata|
|ISO 19115 number and name|70. accessConstraints|
|ISO/TS 19139 path |identificationInfo[1]/\*/resourceConstraints/\*/accessConstraints |
|INSPIRE obligation / condition|Conditional. Mandatory if useConstraints is not documented.|
|INSPIRE multiplicity|[0..\*] for accessConstraints per instance of MD\_LegalConstraints|
|Data type (and ISO 19115 no.) |MD\_RestrictionCode|
|Domain|Codelist (strictly limited to the value defined in B.5.24 of ISO 19115)|
|Example|otherRestrictions (limitation not listed).|
|Comments||


|Metadata element name|Conditions applying to access and use (other constraints)|
| :- | :- |
|Reference|Part B 8.1|
|Definition|Other restrictions and legal prerequisites for accessing the resource or metadata|
|ISO 19115 number and name|72. otherConstraints|
|ISO/TS 19139 path |identificationInfo[1]/\*/resourceConstraints/\*/otherConstraints|
|INSPIRE obligation / condition|Conditional: referring to conditions applying to access. Mandatory if accessConstraints is set at the value “otherRestrictions”|
|INSPIRE multiplicity|[0..\*] for otherConstraints per instance of MD\_LegalConstraints|
|Data type (and ISO 19115 no.) |CharacterString|
|Domain|<p>Free text or if the values “no conditions apply” or “conditions unknown” is used then an Anchor to the code list <http://inspire.ec.europa.eu/metadata-codelist/ConditionsApplyingToAccessAndUse> </p><p>in the Inspire Registry should be used. See also Annex D.2 in this document for the code list.</p>|
|Example|<p>Example if no conditions apply:</p><p>[http://inspire.ec.europa.eu/metadata-codelist/ConditionsApplyingToAccessAndUse/NoConditionsApply](http://inspire.ec.europa.eu/registry/metadata-codelist/ConditionsApplyingToAccessAndUse/NoConditionsApply)</p><p>Example if there is information about restrictions:</p><p>Reproduction for non-commercial purposes is authorised, provided the source is acknowledged. Commercial use is not permitted without prior written consent of the JRC. Reports, articles, papers, scientific and non-scientific works of any form, including tables, maps, or any other kind of output, in printed or electronic form, based in whole or in part on the data supplied, must contain an acknowledgement of the form: Data re-used from the European Drought Observatory (EDO) http://edo.jrc.ec.europa.eu The SPI data were created as part of JRC's research activities. Although every care has been taken in preparing and testing the data, JRC cannot guarantee that the data are correct; neither does JRC accept any liability whatsoever for any error, missing data or omission in the data, or for any loss or damage arising from its use. The JRC will not be responsible for any direct or indirect use which might be made of the data. The JRC does not provide any assistance or support in using the data</p><p></p>|
|Comments|<p>``The domain of the metadata element otherConstraints is Free text. This makes it hard to unambiguous define some common values in all official languages in the Communiy.Therefore it is required to refer to code lists in the Inspire registry for some specific values like “no conditions apply” and “conditions unknown” (see TG Requirement 8).</p><p></p>|


|**Metadata element name**|**Conditions applying to use**|
| :- | :- |
|Reference|Part B 8.1|
|Definition|Restrictions on the use of a resource or metadata|
|ISO 19115 number and name|71. useConstraints|
|ISO/TS 19139 path |identificationInfo[1]/\*/resourceConstraints/\*/useConstraints |
|INSPIRE obligation / condition|Conditional. Mandatory if accessConstraints is not documented.|
|INSPIRE multiplicity|[0..\*] for useConstraints per instance of MD\_LegalConstraints|
|Data type (and ISO 19115 no.) |MD\_RestrictionCode|
|Domain|Codelist (strictly limited to the value defined in B.5.24 of ISO 19115)|
|Example|**otherRestrictions** (limitation not listed).|
|Comments||


|**Metadata element name**|**Conditions applying to use (other constraints)**|
| :- | :- |
|Reference|Part B 8.1|
|Definition|Other restrictions and legal prerequisites for accessing and using the resource or metadata|
|ISO 19115 number and name|72. otherConstraints|
|ISO/TS 19139 path |identificationInfo[1]/\*/resourceConstraints/\*/otherConstraints|
|INSPIRE obligation / condition|Conditional: referring to conditions applying to use. Mandatory if useConstraints is set at the value “otherRestrictions”|
|INSPIRE multiplicity|[0..\*] for otherConstraints per instance of MD\_LegalConstraints|
|Data type (and ISO 19115 no.) |CharacterString|
|Domain|Free text<br>or <br>if the values “no conditions apply” or “conditions unknown” is used then an Anchor to the codelist in the Inspire Registry should be used.|
|Example|<p>Example if no conditions apply:</p><p><http://inspire.ec.europa.eu/metadata-codelist/ConditionsApplyingToAccessAndUse/noConditionsApply>   </p><p>Example if there is information about restrictions:</p><p>**Reproduction for non-commercial purposes is authorised, provided the source is acknowledged. Commercial use is not permitted without prior written consent of the JRC. Reports, articles, papers, scientific and non-scientific works of any form, including tables, maps, or any other kind of output, in printed or electronic form, based in whole or in part on the data supplied, must contain an acknowledgement of the form: Data re-used from the European Drought Observatory (EDO) http://edo.jrc.ec.europa.eu The SPI data were created as part of JRC's research activities. Although every care has been taken in preparing and testing the data, JRC cannot guarantee that the data are correct; neither does JRC accept any liability whatsoever for any error, missing data or omission in the data, or for any loss or damage arising from its use. The JRC will not be responsible for any direct or indirect use which might be made of the data. The JRC does not provide any assistance or support in using the data**</p>|
|Comments|The domain of the metadata element otherConstraints is Free text. This makes it hard to unambiguous define some common values in all official languages in the Community.<br>Therefore it is required to refer to codelists in the Inspire registry for some specific values like “no conditions apply” and “conditions unknown” (see TG Requirement 8).|

# **Limitations on public access**

|Metadata element name|Limitations on public access (access constraints)|
| :- | :- |
|Reference|Part B 8.2|
|Definition|access constraints applied to assure the protection of privacy or intellectual property, and any special restrictions or limitations on obtaining the resource|
|ISO 19115 number and name|70. accessConstraints|
|ISO/TS 19139 path |identificationInfo[1]/\*/resourceConstraints/\*/accessConstraints |
|INSPIRE obligation / condition|Conditional: referring to limitations on public access. Mandatory if classification is not documented|
|INSPIRE multiplicity|[0..\*] for accessConstraints per instance of MD\_LegalConstraints|
|Data type (and ISO 19115 no.) |MD\_RestrictionCode|
|Domain|Codelist (strictly limited at the value defined in B.5.24 of ISO 19115)|
|Example|otherRestrictions|
|Comments||


|Metadata element name|Limitations on public access (other constraints)|
| :- | :- |
|Reference|Part B 8.2|
|Definition|Other restrictions and legal prerequisites for accessing and using the resource or metadata|
|ISO 19115 number and name|72. otherConstraints|
|ISO/TS 19139 path |identificationInfo[1]/\*/resourceConstraints/\*/otherConstraints|
|INSPIRE obligation / condition|Conditional: referring to limitations on public access. Mandatory if classification is not documented|
|INSPIRE multiplicity|[0..\*] for otherConstraints per instance of MD\_LegalConstraints|
|Data type (and ISO 19115 no.) |Gmx:anchor|
|Domain|A code list value from the code list at[ http://inspire.ec.europa.eu/metadata-codelist /LimitationsOnPublicAccess](%20http://inspire.ec.europa.eu/metadata-codelist%20/LimitationsOnPublicAccess)/. See also Annex D.1 of this document for this code list.|
|Example|<gmx:Anchor link:href=" http://inspire.ec.europa.eu/ metadata-codelist /LimitationsOnPublicAccess//NoLimitations"> no limitations</gmx:Anchor>		|
|Comments||

# **Responsible party**

|Metadata element name|Responsible party|
| :- | :- |
|Reference|Part B 9.1 |
|Definition|Identification of, and means of communication with, person(s) and organization(s) associated with the resource(s)|
|ISO 19115 number and name|29. pointOfContact|
|ISO/TS 19139 path |identificationInfo[1]/\*/pointOfContact|
|INSPIRE obligation / condition|<p>Mandatory </p><p></p>|
|INSPIRE multiplicity|[1] Relative to a responsible organisation, but there may be many responsible organisations for a single resource|
|Data type (and ISO 19115 no.) |374. CI\_ResponsibleParty|
|Domain|<p>The following properties are expected:</p><p>- organisationName (characterString and free text)</p><p>- contactInfo (CI\_Contact):</p><p>&emsp;- address:</p><p>&emsp;&emsp;- electronicMailAddress [1..\*] (characterString)</p><p></p>|
|Example|<p>- organisationName: European Commission, Joint Research Centre</p><p>- contactInfo:</p><p>&emsp;- address:</p><p>&emsp;&emsp;- electronicMailAddress: ies-contact@jrc.ec.europa.eu</p><p></p>|
|Comments||

# **Responsible party role**

|Metadata element name|Responsible party role|
| :- | :- |
|Reference|Part B 9.2 |
|Definition|Function performed by the responsible party|
|ISO 19115 number and name|379. role|
|ISO/TS 19139 path |identificationInfo[1]/\*/pointOfContact/\*/role|
|INSPIRE obligation / condition|Mandatory |
|INSPIRE multiplicity|[1] relative to a responsible organisation, but there may be many responsible organisations for a single resource|
|Data type (and ISO 19115 no.) |CI\_RoleCode|
|Domain|Codelist (see B.5.5 of ISO 19115)|
|Example|custodian|
|Comments|There is a direct mapping between the responsible party roles defined in Part D 6 of [Regulation 1205/2008] and the values of the CI\_RoleCode code list of ISO 19115|

# **Metadata point of contact**

|Metadata element name|Metadata point of contact|
| :- | :- |
|Reference|Part B 10.1|
|Definition|Party responsible for the metadata information|
|ISO 19115 number and name|8. contact|
|ISO/TS 19139 path |contact|
|INSPIRE obligation / condition|Mandatory|
|INSPIRE multiplicity|[1..\*] |
|Data type (and ISO 19115 no.) |374. CI\_ResponsibleParty|
|Domain|<p>The following properties are expected:</p><p>- organisationName (characterString and free text)</p><p>- contactInfo (CI\_Contact):</p><p>&emsp;- address:</p><p>&emsp;&emsp;- electronicMailAddress [1..\*] (characterString)</p><p></p>|
|Example|<p>- organisationName: European Commission, Joint Research Centre</p><p>- contactInfo:</p><p>&emsp;- address:</p><p>&emsp;&emsp;- electronicMailAddress: ies-contact@jrc.ec.europa.eu</p><p></p>|
|Comments||

# **Metadata date**

|Metadata element name|Metadata date|
| :- | :- |
|Reference|Part B 10.2|
|Definition|Date that the metadata was created|
|ISO 19115 number and name|9. dateStamp|
|ISO/TS 19139 path |dateStamp|
|INSPIRE obligation / condition|Mandatory|
|INSPIRE multiplicity|[1] |
|Data type (and ISO 19115 no.) |Date|
|Domain|ISO 8601|
|Example|2012-02-20|
|Comments||

# **Metadata language**

|Metadata element name|Metadata language|
| :- | :- |
|Reference|Part B 10.3|
|Definition|Language used for documenting metadata|
|ISO 19115 number and name|3. language|
|ISO/TS 19139 path |language|
|INSPIRE obligation / condition|Mandatory|
|INSPIRE multiplicity|[1]|
|Data type (and ISO 19115 no.) |LanguageCode (ISO/TS 19139)|
|Domain|<p>Codelist (See ISO/TS 19139) based on alpha-3 codes of ISO 639-2. Use only three-letter codes from in ISO 639-2/B (bibliographic codes), </p><p></p><p>The value domain for this element is limited to the official languages of the EU member states.</p><p>The list of valid codes for the 24 official EU languages is:</p><p>Bulgarian – bul 	Irish – gle</p><p>Croatian – hrv	Italian – ita</p><p>Czech – cze	Latvian – lav</p><p>Danish – dan	Lithuanian – lit</p><p>Dutch – dut	Maltese – mlt</p><p>English – eng	Polish – pol</p><p>Estonian – est	Portuguese – por</p><p>Finnish – fin	Romanian – rum</p><p>French – fre	Slovak – slo</p><p>German – ger	Slovenian – slv</p><p>Greek – gre	Spanish – spa</p><p>Hungarian – hun	Swedish – swe</p><p></p><p>These values are part of the list defined at <http://www.loc.gov/standards/iso639-2/> </p><p></p>|
|Example|Eng|
|Comments||


# ***Implementing Rules for interoperability of spatial data sets and services (regulations 1089/2010 and 1253/2013)***
# **Coordinate Reference System**

|Metadata element name|Coordinate Reference System|
| :- | :- |
|Reference|COMMISSION REGULATION (EU) No 1089/2010, article 13, clause 1 |
|Definition|Description of the coordinate reference system(s) used in the data set.|
|ISO 19115 number and name|13. referenceSystem|
|ISO/TS 19139 path|referenceSystemInfo|
|INSPIRE obligation / condition|<p>Mandatory for dataset and dataset series;</p><p>not applicable to Network services;</p><p></p>|
|INSPIRE multiplicity|<p>[1..\*] for dataset and dataset series;</p><p></p>|
|Data type (and ISO 19115 no.)|186. MD\_ReferenceSystem|
|Domain|<p>To identify the reference system, the referenceSystemIdentifier (RS\_Identifier) shall be provided.</p><p></p><p>RS\_Identifier itself is a complex type (lines 206-207 and 208.1-208.2 from ISO 19115). </p><p>At least the following element that is mandatory for ISO should be used (the multiplicity according to ISO 19115 is shown in parentheses): </p><p>- 207. code [1] / domain value: free text</p><p></p><p>TG Requirement 2 in INSPIRE Data specifications states that a URI identifier listed in a table provided there shall be used for referring to the Coordinate reference system. </p><p>This table is provided as Annex D.5 of this document.</p><p>If the code is given as an URI as shown above, the element codespace is not needed. The identifiers can be accessed via gmx:Anchor (see XML example).</p><p>For regions outside of continental Europe, Member States may define suitable coordinate reference systems</p>|
|Example|code: <http://www.opengis.net/def/crs/EPSG/0/4258>|
|Comments|ISO 19115 lists several elements which build MD\_ReferenceSystem. For the purpose of theme-specific metadata according to the INSPIRE Data specifications the element listed above is sufficient.|

# **Temporal Reference System**

|Metadata element name|Temporal Reference System|
| :- | :- |
|Reference|COMMISSION REGULATION (EU) No 1089/2010, article 13, clause 2|
|Definition|Description of the temporal reference system(s) used in the data set.|
|<p></p><p>ISO 19115 number and name</p>|13. referenceSystemInfo|
|ISO/TS 19139 path|referenceSystemInfo|
|INSPIRE obligation / condition|<p>Conditional for dataset and dataset series: Only required if a non-default temporal reference system (i.e. Gregorian Calendar or the Coordinated Universal Time) is used;</p><p>not applicable to services.</p>|
|INSPIRE multiplicity|[0..\*] for dataset and dataset series|
|Data type (and ISO 19115 no.)|186. MD\_ReferenceSystem|
|Domain|<p>No specific type is defined in ISO 19115 for temporal reference systems. Thus, the generic MD\_ReferenceSystem element and its referenceSystemIdentifier (RS\_Identifier) property shall be provided.</p><p></p><p>RS\_Identifier itself is a complex type (lines 206-207 and 208.1-208.2 from ISO 19115). </p><p>At least the following element that is mandatory for ISO should be used (the multiplicity according to ISO 19115 is shown in parentheses): </p><p>- 207. code [1] / domain value: free text</p>|
|Example|JulianCalendar|
|Comments|<p>The primary temporal reference system for use with geographic information is the Gregorian Calendar and 24 hour local or Coordinated Universal Time (UTC), but special applications may entail the use of alternative reference systems. So this element is mandatory only if the spatial data set contains temporal information that does not refer to the default temporal reference system.</p><p>ISO 19115 lists several elements which build MD\_ReferenceSystem. For the purpose of theme-specific metadata according to the INSPIRE Data specifications the element listed above is sufficient.</p><p></p><p>Further elements like authority, codeSpace and version are optional but may be included for completeness if required.</p>|

# **Encoding**

|Metadata element name|Encoding|
| :- | :- |
|Reference|COMMISSION REGULATION (EU) No 1089/2010, article 13, clause 3|
|Definition|Description of the computer language construct(s) specifying the representation of data objects in a record, file, message, storage device or transmission channel.|
|ISO 19115 number and name|271.distributionFormat|
|ISO/TS 19139 path|distributionInfo/MD\_Distribution/distributionFormat|
|INSPIRE obligation / condition|<p>Mandatory for dataset and dataset series;</p><p>not applicable to services</p>|
|INSPIRE multiplicity|[1..\*] for dataset and dataset series|
|Data type (and ISO 19115 no.)|284. MD\_Format|
|Domain|<p>This is a complex type (lines 285-290 from ISO 19115). </p><p>At least the following elements that are mandatory for ISO should be used (the multiplicity according to ISO 19115 is shown in parentheses): </p><p>- 285. name [1] / domain value: free text</p><p>- 286. version [1] / domain value: free text</p><p></p><p>Content for name could also be taken from INSIPRE Registry using the code list available here: <http://inspire.ec.europa.eu/media-types/> and can be accessed via gmx:Anchor (see XML example).</p>|
|Example|<p>name: GML</p><p>version: 3.2.1</p>|
|Comments|<p>ISO 19115 lists several elements which build MD\_Format. For the purpose of theme-specific metadata according to the INSPIRE Data specifications the elements listed above are sufficient.</p><p>Instead of using element specification here the documentation of the supported data scheme inside the distributed dataset (as mentioned in INSPIRE Data specification) can be given either in conformity statement (see [2.8](#Ref419875521)) or the maybe existing metadata element applicationSchemaInfo (see ISO 19115, B.2.1, No. 21).</p>|

# **Character Encoding**

|Metadata element name|Character Encoding|
| :- | :- |
|Reference|COMMISSION REGULATION (EU) No 1089/2010, article 13, clause 5|
|Definition|Full name of the character coding standard used for the dataset|
|ISO 19115 number and name|40. characterSet|
|ISO/TS 19139 path|identificationInfo[1]/\*/characterSet|
|INSPIRE obligation / condition|<p>Conditional for dataset and dataset series: mandatory if NOT using standard UTF-8 encoding;</p><p>not applicable to services</p>|
|INSPIRE multiplicity|[0..\*] for dataset and dataset series|
|Data type (and ISO 19115 no.)|MD\_CharacterSetCode|
|Domain|CodeList (see B.5.10 of ISO 19115)|
|Example|usAscii|
|Comments||

# **Spatial representation type**

|Metadata element name|Spatial representation type|
| :- | :- |
|Reference|COMMISSION REGULATION (EU) No 1089/2010, article 13, clause 6 (element added by amendment 1253/2013)|
|Definition|The method used to spatially represent geographic information|
|ISO 19115 number and name|37. SpatialRepresentationType|
|ISO/TS 19139 path|identificationInfo[1]/\*/spatialRepresentationType|
|INSPIRE obligation / condition|<p>Mandatory for dataset and dataset series;</p><p>not applicable to services</p>|
|INSPIRE multiplicity|[1..\*] for dataset and dataset series|
|Data type (and ISO 19115 no.)|MD\_SpatialRepresentation TypeCode|
|Domain|Codelist (see B.5.26 of ISO 19115), following INSPIRE Data specifications only vector, grid and tin should be used.|
|Example|vector|
|Comments|This element is used to broadly categorise a spatial data resource being described.|

# **Topological Consistency**

|Metadata element name|Topological Consistency – Quantitative results|
| :- | :- |
|Reference|COMMISSION REGULATION (EU) No 1089/2010, article 13, clause 4|
|Definition|Correctness of the explicitly encoded topological characteristics of the data set as described by the scope.|
|ISO 19115 number and name|80. report|
|ISO/TS 19139 path|dataQualityInfo/DQ\_DataQuality/report/|
|INSPIRE obligation / condition|<p>Conditional for dataset and dataset series: mandatory if the data set includes types from the Generic Network Model and does not assure centreline topology (connectivity of centrelines) for the network;</p><p>not applicable to services</p>|
|INSPIRE multiplicity|[0..\*] for dataset and dataset series|
|Data type (and ISO 19115 no.)|115. DQ\_TopologicalConsistency|
|Domain|<p>DQ\_TopologicalConsistency is a forming of the abstract complex type DQ\_Element. See B.2.4.3 in ISO 19115:2003 for further information.</p><p></p><p>The following ISO 19115 elements are the corresponding ones to express quantitative results of the data quality evaluation as given in INSPIRE Data specifications sections 8.3.2 which in fact focus on ISO 19157:</p><p>- 100. nameOfMeasure [0..\*]: name of the test applied to the data / domain value: free text</p><p>- 103. evaluationMethodType [0..1]: type of method used to evaluate quality of the dataset/ domain value: DQ\_EvaluationMethod TypeCode</p><p>- 104. evaluationMethodDescription [0..1]: description of the evaluation method / domain value: free text</p><p>- 106. dateTime [0..\*]: date or range of dates on which a data quality measure was applied / domain value: DateTime (ISO 19103)</p><p>- 107. result [1..2]: value (or set of values) obtained from applying a data quality measure or the outcome of evaluating the obtained value (or set of values) against a specified acceptable conformance quality level / domain value: DQ\_Result (abstract)</p><p>- 133. DQ\_QuantitativeResult, consisting of</p><p>- 137. value [1..\*]: quantitative value or values, content determined by the evaluation procedure used / domain value: Record (ISO 19103)</p><p>Due to making use of DQ\_QuantitativeResult subset there is a mandatory element in ISO 19115 to be considerer too:</p><p>- 135. valueUnit [1]</p>|
|Example||
|Comments|<p>ISO 19115 lists several elements which build DQ\_Element. For the purpose of theme-specific metadata according to the INSPIRE Data specifications the elements won by mapping from ISO 19157 are sufficient.</p><p>This element is mandatory only if the data set includes types from the Generic Network Model and does not assure centreline topology (connectivity of centrelines) for the network.</p>|


|Metadata element name|Topological Consistency – Descriptive results|
| :- | :- |
|Reference|COMMISSION REGULATION (EU) No 1089/2010, article 13, clause 4|
|Definition|Correctness of the explicitly encoded topological characteristics of the data set as described by the scope.|
|ISO 19115 number and name|80. report|
|ISO/TS 19139 path|dataQualityInfo/DQ\_DataQuality/report/|
|INSPIRE obligation / condition|<p>Conditional for dataset and dataset series: mandatory if the data set includes types from the Generic Network Model and does not assure centreline topology (connectivity of centrelines) for the network;</p><p>not applicable to services</p>|
|INSPIRE multiplicity|[0..\*] for dataset and dataset series|
|Data type (and ISO 19115 no.)|115. DQ\_TopologicalConsistency|
|Domain|<p>DQ\_TopologicalConsistency is a forming of the abstract complex type DQ\_Element. See B.2.4.3 in ISO 19115:2003 for further information.</p><p></p><p>To provide the descriptive results of Topological consistency evaluation DQ\_ConformanceResult containing the following elements should be used (the multiplicity according to ISO 19115 is shown in parentheses): </p><p>- 130. specification [1..1]: citation of product specification or user requirement against which data is being evaluated / domain value: CI\_Citation</p><p>- 131. explanation [1..1]: explanation of the meaning of conformance for this result / domain value: free text</p><p>- 132. pass [1..1]: indication of the conformance result / domain value: Boolean</p>|
|Example|<p>specification: INSPIRE Data Specifications - Base Models - Generic Network Model–</p><p>pass: false</p>|
|Comments|To provide the descriptive results of Topological consistency evaluation DQ\_ConformanceResult should be used because there is no well matching element for descriptive results at all. The specification to be cited in this case will be the Generic Network Model and pass will be FALSE. This is exactly the condition when to have this statement at all (see reference above).|


# ***Implementing Rules for Invocable Spatial Data Services (Regulation 1312/2014, Annex I)***
Metadata elements for Invocable Spatial Data Services in [Regulation 1089/2010], Annex V as added in amending [Regulation 1312/2014].
# **Category**

|Metadata element name|Category|
| :- | :- |
|Reference|COMMISSION REGULATION (EU) No 1089/2010, Annex V, Part B 1  |
|Definition|Citation of the product specification or user requirement against which data is being evaluated|
|ISO 19115 number and name|130. specification|
|ISO/TS 19139 path |dataQualityInfo/\*/report/\*/result/\*/specification|
|INSPIRE obligation / condition|Mandatory for invocable spatial data services|
|INSPIRE multiplicity|<p></p><p>[1] understood in the context of a conformity statement when reported in the metadata – there may be more than one conformity statement</p>|
|Data type (and ISO 19115 no.) |359. CI\_Citation|
|Domain|<p>invocable</p><p><http://inspire.ec.europa.eu/RequirementsClass/TG-Metadata/2.0/SDS-invocable> </p><p></p><p>interoperable <http://inspire.ec.europa.eu/RequirementsClass/TG-Metadata/2.0/SDS-interoperable></p><p></p><p>harmonized</p><p><http://inspire.ec.europa.eu/RequirementsClass/TG-Metadata/2.0/SDS-harmonised> </p>|
|Example|<**gmx:Anchor xlink:href=" http://inspire.ec.europa.eu/id/ats/metadata/2.0/sds-invocable"** xlink:title="conformanceClass\_Invocable">invocable</gmx:Anchor>|
|Comments||


|Metadata element name|Degree|
| :- | :- |
|Reference|COMMISSION REGULATION (EU) No 1089/2010, Annex V, Part B 1|
|Definition|Indication of the conformance result|
|ISO 19115 number and name|132. pass|
|ISO/TS 19139 path |dataQualityInfo/\*/report/\*/result/\*/pass|
|INSPIRE obligation / condition|Mandatory for invocable spatial data services|
|INSPIRE multiplicity|[1] understood in the context of a conformity statement when reported in the metadata – there may be more than one conformity statement|
|Data type (and ISO 19115 no.) |Boolean|
|Domain|- true if conformant|
|Example|true|
|Comments|If conformant, the domain in this case can only have the value **true**|

# **Resource locator** 

|Metadata element name|Resource locator|
| :- | :- |
|Reference|COMMISSION REGULATION (EU) No 1089/2010, Annex V, Part D 1|
|Definition|Location (address) for on-line access using a Uniform Resource Locator address or similar addressing scheme|
|ISO 19115 number and name|397. linkage|
|ISO/TS 19139 path |distributionInfo/\*/transferOptions/\*/onLine/\*/linkage|
|INSPIRE obligation / condition|Mandatory for invocable spatial data services|
|INSPIRE multiplicity|[1..\*] |
|Data type (and ISO 19115 no.) |URL|
|Domain|URL (IETF RFC1738 and IETF RFC 2056)|
|Example|http://www.dinoservices.nl/geo3dmodelwebservices-1/Geo3DModelService|
|Comments||


|Metadata element name|Function|
| :- | :- |
|Reference|COMMISSION REGULATION (EU) No 1089/2010, Annex V, Part D 1|
|Definition|Detailed text description of what the online resource is/does|
|ISO 19115 number and name|401. description|
|ISO/TS 19139 path |distributionInfo/\*/transferOptions/\*/onLine/\*/description|
|INSPIRE obligation / condition|Mandatory for invocable spatial data services|
|INSPIRE multiplicity|[1] |
|Data type (and ISO 19115 no.) |Free text|
|Domain|The *gmd:linkage/gmd:description* child element *gmd:CI\_OnlineResource* shall contain a *gmx:Anchor* element pointing to the value "accessPoint" of the code list OnLineDescriptionCode in the INSPIRE Registry.|
|Example|<gmx:Anchor xlink:href="http://inspire.ec.europa.eu /metadata-codelist/OnLineDescriptionCode/accessPoint">accessPoint</gmx:Anchor>	|
|Comments||
# **Specification**

|Metadata element name|Specification|
| :- | :- |
|Reference|COMMISSION REGULATION (EU) No 1089/2010, Annex V, Part D 2|
|Definition|Citation of the product specification or user requirement against which data is being evaluated|
|ISO 19115 number and name|130. specification|
|ISO/TS 19139 path |dataQualityInfo/\*/report/\*/result/\*/specification|
|INSPIRE obligation / condition|Mandatory for invocable spatial data services|
|INSPIRE multiplicity|[1..\*] understood in the context of a conformity statement when reported in the metadata – there may be more than one conformity statement|
|Data type (and ISO 19115 no.) |359. CI\_Citation|
|Domain|<p>The following properties are expected:</p><p>- Title (characterString and free text)</p><p>- Reference date (CI\_Date):</p><p>&emsp;- dateType: creation, publication or revision</p><p>date: an effective date</p>|
|Example|<p>- title: EN ISO 19128:2005(E) : Geographic information — Web map server interface</p><p>- date:</p><p>&emsp;- dateType: publication</p><p>&emsp;- date: 2005-12-01</p>|
|Comments||


|Metadata element name|Degree|
| :- | :- |
|Reference|COMMISSION REGULATION (EU) No 1089/2010, Annex V, Part D 2|
|Definition|Indication of the conformance result|
|ISO 19115 number and name|132. pass|
|ISO/TS 19139 path |dataQualityInfo/\*/report/\*/result/\*/pass|
|INSPIRE obligation / condition|Mandatory for invocable spatial data services|
|INSPIRE multiplicity|[1] understood in the context of a conformity statement when reported in the metadata – there may be more than one conformity statement|
|Data type (and ISO 19115 no.) |Boolean|
|Domain|- true if conformant|
|Example|true|
|Comments|If conformant, the domain in this case can only have the value **true**|

# ***Implementing Rules for Interoperable Spatial Data Services (Regulation 1312/2014, Annex II)***
Metadata elements for Interoperable Spatial Data Services in [Regulation 1089/2010], Annex VI as added in amending [Regulation 1312/2014].
# **Coordinate Reference System**

|Metadata element name|Coordinate Reference System|
| :- | :- |
|Reference|COMMISSION REGULATION (EU) No 1089/2010, Annex VI, Part B 3|
|Definition|Description of the coordinate reference system(s) used in the data set.|
|ISO 19115 number and name|13. referenceSystem|
|ISO/TS 19139 path|referenceSystemInfo|
|INSPIRE obligation / condition|Mandatory if  relevant for interoperable spatial data services |
|INSPIRE multiplicity|[0..\*] |
|Data type (and ISO 19115 no.)|186.MD\_ReferenceSystem|
|Domain|<p>To identify the reference system, the referenceSystemIdentifier</p><p></p><p>(RS\_Identifier) shall be provided.</p>|
|Example|code: <http://www.opengis.net/def/crs/EPSG/0/4258>|
|Comments|Despite the definition of the ISO element, this is used to provide the CRS of the service|
# **Criteria**

|Metadata element name|Criteria|
| :- | :- |
|Reference|COMMISSION REGULATION (EU) No 1089/2010, Annex VI Part B 4.1|
|Definition|Name of the test applied to the data|
|ISO 19115 number and name|100. nameOfMeasure|
|ISO/TS 19139 path |dataQualityInfo/\*/report/DQ\_ConceptualConsistency/nameOfMeasure|
|INSPIRE obligation / condition|Mandatory for interoperable spatial data services|
|INSPIRE multiplicity|<p></p><p>[1] For each criteria</p>|
|Data type (and ISO 19115 no.) |Free text|
|Domain|<p>Availability (availability)  </p><p>Performance (performance)  </p><p>Capacity (capacity)  </p>|
|Example|availability|
|Comments|The identifier of the measure is enough to retrieve all information about the quality measure. This element enable direct understanding of the metadata|
# **Measurement**

|Metadata element name|Description |
| :- | :- |
|Reference|COMMISSION REGULATION (EU) No 1089/2010, Annex VI Part B 4.2.1|
|Definition|Code identifying a registered standard procedure|
|ISO 19115 number and name|101.  measureIdentification|
|ISO/TS 19139 path |dataQualityInfo/\*/report/DQ\_ConceptualConsistency/measureIdentification|
|INSPIRE obligation / condition|Mandatory for interoperable spatial data services|
|INSPIRE multiplicity|[1] For each criteria|
|Data type (and ISO 19115 no.) |MD\_Identifier/code|
|Domain|<p><http://inspire.ec.europa.eu/metadata-codelist/QualityOfServiceCriteria/availability> </p><p></p>|
|Example|INSPIRE QoS2|
|Comments||


|Metadata element name|Value|
| :- | :- |
|Reference|COMMISSION REGULATION (EU) No 1089/2010, Annex VI Part B 4.2.2|
|Definition|Quantitative value or values, content determined by the evaluation procedure used|
|ISO 19115 number and name|137. value|
|ISO/TS 19139 path |dataQualityInfo/\*/report/DQ\_ConceptualConsistency/result/DQ\_QuantitativeResult/value|
|INSPIRE obligation / condition|Mandatory for interoperable spatial data services|
|INSPIRE multiplicity|[1..\*] for each criteria|
|Data type (and ISO 19115 no.) |As defined for each measure in the quality measure tables|
|Domain||
|Example|1|
|Comments||


|Metadata element name|Unit|
| :- | :- |
|Reference|COMMISSION REGULATION (EU) No 1089/2010, Annex VI Part B 4.2.3|
|Definition|Value unit for reporting a data quality result.|
|ISO 19115 number and name|135. valueUnit|
|ISO/TS 19139 path |dataQualityInfo/\*/report/DQ\_ConceptualConsistency/result/DQ\_QuantitativeResult/valueUnit|
|INSPIRE obligation / condition|Mandatory for interoperable spatial data services|
|INSPIRE multiplicity|[1] for each criteria|
|Data type (and ISO 19115 no.) |UnitOfMeasure|
|Domain|Value unit for the measure as described in the quality measure tables|
|Example|<p>second </p><p>(implemented by reference in XML : <gmd:valueUnit xlink:href=" <http://www.opengis.net/def/uom/SI/second>"/>)</p>|
|Comments||


# ***Implementing Rules for Harmonised Spatial Data Services (Regulation 1312/2014, Annex III)***
Metadata elements for Harmonised Spatial Data Services in [Regulation 1089/2010], Annex VII as added in amending [Regulation 1312/2014].
# **Invocation metadata**

|Metadata element name|operationName|
| :- | :- |
|Reference|COMMISSION REGULATION (EU) No 1089/2010, Annex VII Part B 3|
|Definition|A unique identifier for this interface|
|ISO 19119 number and name|Table C2 1. operationName|
|CSW ISO Metadata AP path |identificationInfo[1]/\*/containsOperations/\*/operationName	|
|INSPIRE obligation / condition|Mandatory for harmonised spatial data services|
|INSPIRE multiplicity|[1]|
|Data type (and ISO 19115 no.) |CharacterString|
|Domain||
|Example|GetSampleColumn|
|Comments||


|Metadata element name|DCP|
| :- | :- |
|Reference|COMMISSION REGULATION (EU) No 1089/2010, Annex VII Part B 3|
|Definition|Distributed computing platforms on which the operation has been implemented.|
|ISO 19119 number and name|Table C2 2. DCP|
|CSW ISO Metadata AP path |identificationInfo[1]/\*/containsOperations/\*/DCP	|
|INSPIRE obligation / condition|Mandatory for harmonised spatial data services|
|INSPIRE multiplicity|[1..\*]|
|Data type (and ISO 19115 no.) |DCPlist|
|Domain|XML, CORBA, JAVA, COM, SQL, WebServices|
|Example|WebServices|
|Comments||


|Metadata element name|connectPoint|
| :- | :- |
|Reference|COMMISSION REGULATION (EU) No 1089/2010, Annex VII Part B 3|
|Definition|Handle for accessing the service interface.|
|ISO 19119 number and name|Table C2 6. connectPoint|
|CSW ISO Metadata AP path |identificationInfo[1]/\*/containsOperations/\*/connectPoint/\*/linkage	|
|INSPIRE obligation / condition|Mandatory for harmonised spatial data services|
|INSPIRE multiplicity|[1..\*]|
|Data type (and ISO 19115 no.) |<p>CI\_OnlineResource </p><p></p>|
|Domain|IETF RFC1738 and IETF RFC 2056|
|Example|http://www.dinoservices.nl:80/geo3dmodelwebservices-1/Geo3DModelService|
|Comments||

# ***Theme-specific metadata elements from INSPIRE Data Specifications***
This section describes the details on the “recommended theme-specific metadata elements” included in sections 8.3 of INSPIRE Data specifications. All of them are optional but recommended for certain INSPIRE annex themes. 

Many of these theme-specific metadata consider details of particular INSPIRE annex themes in definitions and examples. These are listed in the following sub-sections. 

The tables below gives an overview of the INSPIRE theme-specific metadata in combination with the INSPIRE annex themes they are recommended for.



![](Aspose.Words.bef9e791-4ef2-43dc-ae9d-769f51fa1525.007.png)

![](Aspose.Words.bef9e791-4ef2-43dc-ae9d-769f51fa1525.008.png)

# **Maintenance information**

|Metadata element name|Maintenance information|
| :- | :- |
|Reference|INSPIRE Data specifications, sections 8.3.1|
|Definition|Information about the scope and frequency of updating|
|ISO 19115 number and name|30. resourceMaintenance|
|ISO/TS 19139 path|identificationInfo[1]/MD\_DataIdentification/resourceMaintenance/|
|INSPIRE obligation / condition|<p>optional for dataset and dataset series;</p><p>not applicable to services</p>|
|**Recommended for themes**|**all**|
|INSPIRE multiplicity|[0..1] for dataset and dataset series|
|Data type (and ISO 19115 no.)|142. MD\_MaintenanceInformation|
|Domain|<p>This is a complex type (lines 143-148 from ISO 19115). </p><p>At least the following element should be used (the multiplicity according to ISO 19115 is shown in parentheses): </p><p>- 143. maintenanceAndUpdateFrequency [1]: frequency with which changes and additions are made to the resource after the initial resource is completed / domain value: MD\_MaintenanceFrequencyCode</p><p>In addition the following elements are recommended, but in contrast to ISO each of them should not appear multiple but single only:</p><p>- 146. updateScope [0..\*]: scope of data to which maintenance is applied / domain value: MD\_ScopeCode </p><p>- 148. maintenanceNote [0..\*]: information regarding specific requirements for maintaining the resource / domain value: free text </p>|
|Example|<p>maintenanceAndUpdateFrequency: annually</p><p>updateScope: dataset</p>|
|Comments|ISO 19115 lists several elements which build MD\_MaintenanceInformation. For the purpose of theme-specific metadata according to the INSPIRE Data specifications the three elements listed above are sufficient.|

# **Spatial representation information**

|Metadata element name|Spatial representation information|
| :- | :- |
|Reference|INSPIRE Data specifications, sections 8.3.x|
|Definition|Digital representation of spatial information in the dataset|
|ISO 19115 number and name|12. spatialRepresentationInfo|
|ISO/TS 19139 path|spatialRepresentationInfo/|
|INSPIRE obligation / condition|<p>optional for dataset and dataset series;</p><p>not applicable to services</p>|
|INSPIRE multiplicity|[0..\*] for dataset and dataset series|
|**Recommended for themes**|**Elevation**|
|Data type (and ISO 19115 no.)|156. MD\_SpatialRepresentation|
|Domain|<p>MD\_SpatialRepresentation is an abstract complex type and has to be expressed as MD\_GridSpatialRepresentation, MD\_Georectified, MD\_Georeferenceable or MD\_VectorSpatialRepresentation.</p><p>See B.2.6 in ISO 19115:2003 for further information.</p>|
|Example||
|Comments|This metadata information is only applicable to vector and grid spatial representations. Hence it should be informed only when the data set adopt any of these spatial representation types.|

# **Supplemental information**

|Metadata element name|Supplemental information|
| :- | :- |
|Reference|INSPIRE Data specifications, sections 8.3.x|
|Definition|Any other descriptive information about the dataset|
|ISO 19115 number and name|46. supplementalInformation|
|ISO/TS 19139 path|identificationInfo[1]/MD\_DataIdentification/supplementalInformation|
|INSPIRE obligation / condition|<p>optional for dataset and dataset series;</p><p>not applicable to services</p>|
|INSPIRE multiplicity|[0..1] for dataset and dataset series|
|**Recommended for themes**|**Elevation**|
|Data type (and ISO 19115 no.)|CharacterString|
|Domain|Free text|
|Example||
|Comments on theme ELEVATION|<p>This metadata element is recommended to concisely describe general properties of the spatial data set which should be traced here. As illustration, depending on the spatial representation types of the data set: </p><p>Vector </p><p>- Contour line vertical intervals (i.e. equidistance parameters), indicating in which geographic areas and/or conditions they are used (if any) within the data set. </p><p>Grid or Tin </p><p>- Interpolation method recommended by the data provider in order to calculate the elevation values at any direct position within the DEM extent (either a grid coverage or TIN surface. The calculation involves the interpolation of the elevation values known for the grid coverage range set points or TIN control points, respectively). The values defined for the CV\_InterpolationType code list defined in ISO 19123:2005 should be re-used where possible. </p><p>- Description of the geographic features that are included (measured) within the DEM surface. Organizations very often have discrepancies to what it is considered as a pure DTM or DSM. Data providers should explain here any existing deviations from the concepts of pure DTM / DSM. As illustration, declaration of any known dynamic features included within the DEM surface, limitations due to the data capture process (e.g. trees or bridges not included within a DSM), if water body surfaces have been flattened or not, etc.</p>|
# **Process step**

|Metadata element name|Process step|
| :- | :- |
|Reference|INSPIRE Data specifications, sections 8.3.x|
|Definition|Information about an event or transformation in the life of a dataset including the process used to maintain the dataset|
|ISO 19115 number and name|84. processStep|
|ISO/TS 19139 path|dataQualityInfo/DQ\_DataQuality/lineage/LI\_Lineage/processStep/|
|INSPIRE obligation / condition|<p>optional for dataset and dataset series;</p><p>not applicable to services</p>|
|INSPIRE multiplicity|[0..\*] for dataset and dataset series|
|**Recommended for themes**|**Elevation, Orthoimagery**|
|Data type (and ISO 19115 no.)|86. LI\_ProcessStep |
|Domain|<p>This is a complex type (lines 87-91 from ISO 19115).</p><p>The description (87., free text) property shall be provided.</p>|
|Example||
|Comments|<p>ISO 19115 lists several elements which build LI\_ProcessStep. For the purpose of theme-specific metadata according to the INSPIRE Data specifications the element listed above is sufficient.</p><p>Note that the path for dataQualityInfo/DQ\_DataQuality/lineage/ will already exist in metadata because of being used for carrying information about lineage itself (see [2.7.1](#Ref419892471)). Therefore an addition of these information into the same entity of LI\_Lineage may be useful.</p>|
|Comments on theme ELEVATION|<p>This metadata element aims to supplement the *Lineage* metadata element defined in Regulation 1205/2008/EC with a precise description of a process or operation that has been applied to the elevation dataset. </p><p>As illustration, the following processing steps may be traced here: </p><p>- Data acquisition. </p><p>- Data editing. </p><p></p><p>For vector data: </p><p>- Aero-triangulation. </p><p>- Stereo-plotting. </p><p></p><p>For grid data: </p><p>- Grid calculation / sampling. </p><p></p><p>Note that such information may convey, most often implicitly, supplementary indications of the expected quality of a dataset, which often depends on the nature of the production process. </p><p></p><p>In the case of the data acquisition process it is important to highlight any known limitations which may lead to quality problems, for example the description of the geographical areas where the reliability of geographic information is reduced or limited due to limitations of the data capture technology used. Information relative to the geometry of low reliability areas (e.g. links to elsewhere such geometries may be obtained) can be particularly helpful to assess the accuracy and the reliability of the elevation data set. </p>|
|Comments on theme ORTHOIMAGERY|<p>This metadata element aims to supplement the *Lineage* metadata element defined in Regulation 1205/2008/EC with a precise description of a process or operation that has been applied to the orthoimagery dataset. </p><p></p><p>For example, the following processing steps, which are common in orthoimagery, may be traced here: </p><p>- data acquisition </p><p>- aero/spatio-triangulation </p><p>- orthorectification </p><p>- mosaicking </p><p>- radiometric correction </p><p></p><p>Note that such information may convey, most often implicitly, supplementary indications of the expected quality of a dataset (e.g. the radiometric aspect of a mosaic), which often depends on the nature of the production process. </p>|

# **Data source**

|Metadata element name|Data source|
| :- | :- |
|Reference|INSPIRE Data specifications, sections 8.3.x|
|Definition|Information about the source data used in creating the data specified by the scope|
|ISO 19115 number and name|85. source|
|ISO/TS 19139 path|dataQualityInfo/DQ\_DataQuality/lineage/LI\_Lineage/source/|
|INSPIRE obligation / condition|<p>optional for dataset and dataset series;</p><p>not applicable to services</p>|
|INSPIRE multiplicity|[0..\*] for dataset and dataset series|
|**Recommended for themes**|**Elevation, Orthoimagery**|
|Data type (and ISO 19115 no.)|92. LI\_Source |
|Domain|<p>This is a complex type (lines 93-98 from ISO 19115).</p><p>Either the description (93., free text) or the sourceExtent (97., EX\_Extent) elements shall be provided.</p>|
|Example||
|Comments|<p>ISO 19115 lists several elements which build LI\_Source. For the purpose of theme-specific metadata according to the INSPIRE Data specifications the elements listed above are sufficient.</p><p>Note that the path for dataQualityInfo/DQ\_DataQuality/lineage/ will already exist in metadata because of being used for carrying information about lineage itself (see [2.7.1](#Ref419892607)). Therefore an addition of these information into the same entity of LI\_Lineage may be useful.</p>|
|Comments on theme ELEVATION|<p>This metadata element aims to supplement the *Lineage* metadata element defined in Regulation 1205/2008/EC with a precise description of data sources that have been used as input to generate the elevation dataset. </p><p>For example, the following data sources may be described and referenced here: </p><p>- image sources and orientations </p><p>- calibration data </p><p>- control data (e.g. aero-triangulation control points) </p><p>- data sources used to infer break lines </p><p></p><p>Metadata on data sources may as well include any specifications available and the conditions of data acquisition (e.g. sensors characteristics, data properties like image overlaps, known lacks of source data, etc). </p>|
|Comments on theme ORTHOIMAGERY|<p>This metadata element aims to supplement the *Lineage* metadata element defined in Regulation 1205/2008/EC with a precise description of data sources that have been used as input to generate the orthoimagery dataset. </p><p>For example, the following data sources may be described and referenced here: </p><p>- image sources </p><p>- calibration data </p><p>- control data (e.g. control points) </p><p>- image positions and orientations </p><p>- elevation data </p><p>- seamlines used to build the mosaic elements </p><p></p><p>Metadata on image sources may as well include the specifications and the conditions of data acquisition (e.g. sensors characteristics, image overlap, solar elevation, et.). </p><p></p><p>Concerning elevation data, it is recommended to provide information about the following basic characteristics of the Digital Elevation Models (DEM) used to rectify images: </p><p>- structure (grid or TIN data) </p><p>- for grid data: surface type (Digital Terrain Model or Digital Surface Model) </p><p>- for grid data: DTM/DSM spacing (distance) </p><p>- for grid data: water bodies flattened (yes/no) </p><p>- for DSM: modelling of buildings (yes/no) </p><p>- for DSM: modelling of trees (yes/no) </p><p>- additional breaklines (yes/no) </p><p>- vertical datum information </p><p>- vertical accuracy (rmse) </p><p>- positional accuracy (rmse) </p><p></p><p>Information relative to the seamlines carrying the geometry of the mosaic elements can be particularly helpful to assess the accuracy and the reliability of the acquisition times provided through these mosaic elements. Seamlines may have been slightly generalized, so that the exact race between adjoining pixels from neighbouring images is lost. Or feathering may have been applied to mosaick images, so that some range values in the mosaic can be defined as a combination of values stemming from several input images with different capture time. </p>|

# **Browse graphic information**

|Metadata element name|Browse graphic information|
| :- | :- |
|Reference|INSPIRE Data specifications, sections 8.3.x|
|Definition|Graphic that provides an illustration of the dataset (should include a legend for the graphic)|
|ISO 19115 number and name|31. graphicOverview|
|ISO/TS 19139 path|identificationInfo[1]/MD\_DataIdentification/graphicOverview/|
|INSPIRE obligation / condition|<p>optional for dataset and dataset series;</p><p>not applicable to services</p>|
|INSPIRE multiplicity|[0..\*] for dataset and dataset series|
|**Recommended for themes**|**Elevation, Orthoimagery**|
|Data type (and ISO 19115 no.)|48. MD\_BrowseGraphic |
|Domain|<p>This is a complex type (lines 49-51 from ISO 19115). </p><p>The following element is mandatory (the multiplicity according to ISO 19115 is shown in brackets): </p><p>- 49. filename [1]: name of the file that contains a graphic that provides an illustration of the dataset / domain value: free text </p>|
|Example||
|Comments|ISO 19115 lists several elements which build MD\_BrowseGraphic. For the purpose of theme-specific metadata according to the INSPIRE Data specifications the element listed above is sufficient.|

# **Image description**

|Metadata element name|Image description|
| :- | :- |
|Reference|INSPIRE Data specifications, sections 8.3.x|
|Definition|Information about an image‘s suitability for use|
|ISO 19115 number and name|16. contentInfo |
|ISO/TS 19139 path|contentInfo/|
|INSPIRE obligation / condition|<p>optional for dataset and dataset series;</p><p>not applicable to services</p>|
|INSPIRE multiplicity|[0..\*] for dataset and dataset series|
|**Recommended for themes**|**Orthoimagery**|
|Data type (and ISO 19115 no.)|243. MD\_ImageDescription |
|Domain|<p>This is a complex type (lines 244-255 and 249-242 from ISO 19115). </p><p>At least the following element should be used: </p><p>- 248. cloudCoverPercentage [1]: area of the dataset obscured by clouds, expressed as a percentage of the spatial extent/ domain value: Real</p><p>ISO 19115 itself demands two mandatory elements in MD\_ImageDescription:</p><p>- 240. attributeDescription [1]</p><p>- 241. contentType [1]</p>|
|Example||
|Comments|ISO 19115 lists several elements that build MD\_ImageDescription. For the purpose of theme-specific metadata according to the INSPIRE Data specifications the elements listed above are sufficient.|

# **Content information**

|Metadata element name|Content information|
| :- | :- |
|Reference|INSPIRE Data specifications, sections 8.3.x|
|Definition|Description of the content of a dataset|
|ISO 19115 number and name|16. contentInfo |
|ISO/TS 19139 path|contentInfo/|
|INSPIRE obligation / condition|<p>optional for dataset and dataset series;</p><p>not applicable to services</p>|
|INSPIRE multiplicity|[0..1] for dataset and dataset series|
|**Recommended for themes**|**Buildings**|
|Data type (and ISO 19115 no.)|233. MD\_FeatureCatalogueDescription |
|Domain|<p>This is a complex type (lines 234-238 from ISO 19115). </p><p>Data specification on Buildings does not give a minimum element.</p><p>ISO 19115 itself demands two mandatory elements in MD\_ FeatureCatalogueDescription:</p><p>- 236. includedWithDataset [1]</p><p>- 238. featureCatalogueCitation [1]</p>|
|Example||
|Comments|ISO 19115 lists several elements that build MD\_ FeatureCatalogueDescription. For the purpose of theme-specific metadata according to the INSPIRE Data specifications the elements listed above are sufficient.|
|Comments on theme BUILDINGS|<p>The purpose of this metadata element is to inform the user about the feature types and properties that are populated in the data set. </p><p>This has to be done by a reference to a feature catalogue including only the populated feature types and properties. It may be done by referencing the tables supplied **in annex E of data specification** for additional information once they have been filled by the data producer, just by ticking the populated features and properties. </p>|

# **Digital transfer options information**

|Metadata element name|Digital transfer options information|
| :- | :- |
|Reference|INSPIRE Data specifications, sections 8.3.x|
|Definition|Technical means and media by which a resource is obtained from the distributor|
|ISO 19115 number and name|273. transferOptions|
|ISO/TS 19139 path|distributionInfo/MD\_Distribution/transferOptions/|
|INSPIRE obligation / condition|<p>optional for dataset and dataset series;</p><p>not applicable to services</p>|
|INSPIRE multiplicity|[0..\*] for dataset and dataset series|
|**Recommended for themes**|**Hydrography, Elevation, Orthoimagery**|
|Data type (and ISO 19115 no.)|274. MD\_DigitalTransferOptions|
|Domain|<p>This is a complex type (lines 275-278 from ISO 19115). </p><p>At least the following elements should be used (the multiplicity according to ISO 19115 is shown in parentheses): </p><p>For Elevation and Orthoimagery:</p><p>- 275. unitsOfDistribution [0..1]: tiles, layers, geographic areas, etc., in which data is available / domain value: free text </p><p>- 278. offLine [0..1]: information about offline media on which the resource can be obtained / domain value: MD\_Medium </p><p>For Hydrography:</p><p>- 276. transferSize [0..1]: estimated size of a unit in the specified transfer format, expressed in megabytes. The transfer size is > 0.0/ domain value: Real </p>|
|Example||
|Comments|<p>ISO 19115 lists several elements that build MD\_DigitalTransferOptions. For the purpose of theme-specific metadata according to the INSPIRE Data specifications the elements listed above are sufficient.</p><p>Note that the path for distributionInfo/MD\_Distribution/transferOptions/ may already exist in metadata if being used for carrying information about online access (277. online, see  REF \_Ref461298717 \r \h 3.1.3). Therefore an addition of these information into the same entity of MD\_DigitalTransferOptions may be useful.</p>|

# **Extent**

|Metadata element name|Identification - Extent|
| :- | :- |
|Reference|INSPIRE Data specifications, sections 8.3.x|
|Definition|Extent information including the bounding box, bounding polygon, vertical, and temporal extent of the dataset|
|ISO 19115 number and name|45. extent |
|ISO/TS 19139 path|identificationInfo[1]/MD\_DataIdentification/extent|
|INSPIRE obligation / condition|<p>optional for dataset and dataset series;</p><p>not applicable to services</p>|
|INSPIRE multiplicity|[0..\*] for dataset and dataset series|
|**Recommended for themes**|**Hydrography**|
|Data type (and ISO 19115 no.)|334. EX\_Extent |
|Domain|<p>This is a complex type (lines 335-338 from ISO 19115). </p><p>In addition to the Geographic bounding box (see  REF \_Ref461298822 \r \h 2.3.8) the following element should be used to provide a common "name" for the extent (the multiplicity according to ISO 19115 is shown in parentheses): </p><p>- 335. description [0..1]: spatial and temporal extent for the referring object/ domain value: free text </p>|
|Example|<p>Use e.g. NAME\_ENGL and EUCD\_RBD values like </p><p>description: "East Estonia, A6018" or </p><p>description: "Rhine, A5001"</p>|
|Comments|ISO 19115 lists several elements that build EX\_Extent. For the purpose of theme-specific metadata according to the INSPIRE Data specifications the element listed above is sufficient in addition to the geographic extent.|
|Comments on theme HYDROGRAPHY|<p>Use e.g. WISE River basin districts (RBDs) </p><p>Use the terms provided here: </p><p><http://dataservice.eea.europa.eu/dataservice/metadetails.asp?id=1041></p><p></p><p>In future the use of a common register (gazetteer) of e.g. river names is expected to be useful </p>|

# **Data Quality**

|Metadata element name|Data Quality – Quantitative results|
| :- | :- |
|Reference|INSPIRE Data specifications, sections 8.3.2|
|Definition|Several, theme specific aspects of Data Quality - See corresponding Data Specfication for further information|
|ISO 19115 number and name|80. report|
|ISO/TS 19139 path|dataQualityInfo/DQ\_DataQuality/report/|
|INSPIRE obligation / condition|<p>optional for dataset and dataset series;</p><p>not applicable to services</p>|
|INSPIRE multiplicity|[0..\*] for dataset and dataset series|
|Data type (and ISO 19115 no.)|99. DQ\_Element|
|Domain|<p>DQ\_Element is an abstract complex type and has to be expressed by a corresponding DQ\_xxx subelement concerning the particular data quality issue e.g. DQ\_ConceptualConsistency.</p><p>See B.2.4.3 in ISO 19115:2003 for further information.</p><p></p><p>The following ISO 19115 elements are the corresponding ones to express quantitative results of the data quality evaluation as given in INSPIRE Data specifications sections 8.3.2 which in fact focus on ISO 19157:</p><p>- 100. nameOfMeasure [0..\*]: name of the test applied to the data / domain value: free text</p><p>- 103. evaluationMethodType [0..1]: type of method used to evaluate quality of the dataset/ domain value: DQ\_EvaluationMethod TypeCode</p><p>- 104. evaluationMethodDescription [0..1]: description of the evaluation method / domain value: free text</p><p>- 106. dateTime [0..\*]: date or range of dates on which a data quality measure was applied / domain value: DateTime (ISO 19103)</p><p>- 107. result [1..2]: value (or set of values) obtained from applying a data quality measure or the outcome of evaluating the obtained value (or set of values) against a specified acceptable conformance quality level / domain value: DQ\_Result (abstract)</p><p>- 133. DQ\_QuantitativeResult, consisting of</p><p>- 137. value [1..\*]: quantitative value or values, content determined by the evaluation procedure used / domain value: Record (ISO 19103)</p><p>Due to making use of DQ\_QuantitativeResult subset there is a mandatory element in ISO 19115 to be considerer too:</p><p>- 135. valueUnit [1]</p>|
|Example||
|Comments|ISO 19115 lists several elements which build DQ\_Element. For the purpose of theme-specific metadata according to the INSPIRE Data specifications the elements won by mapping from ISO 19157 are sufficient. |


# **Referenced code lists and code list values**
# ***Limitations on public access***
Code list URI: <http://inspire.ec.europa.eu/metadata-codelist/LimitationsOnPublicAccess> 


|**Code value**|**Label**|**Definition**|
| :- | :- | :- |
|INSPIRE\_Directive\_Article13\_1a|public access limited according to Article 13(1)(a) of the INSPIRE Directive|Public access to spatial data sets and services would adversely affect the confidentiality of the proceedings of public authorities, where such confidentiality is provided for by law.|
|INSPIRE\_Directive\_Article13\_1b|public access limited according to Article 13(1)(b) of the INSPIRE Directive|Public access to spatial data sets and services would adversely affect international relations, public security or national defence.|
|INSPIRE\_Directive\_Article13\_1c|public access limited according to Article 13(1)(c) of the INSPIRE Directive|Public access to spatial data sets and services would adversely affect the course of justice, the ability of any person to receive a fair trial or the ability of a public authority to conduct an enquiry of a criminal or disciplinary nature.|
|INSPIRE\_Directive\_Article13\_1d|public access limited according to Article 13(1)(d) of the INSPIRE Directive|Public access to spatial data sets and services would adversely affect the confidentiality of commercial or industrial information, where such confidentiality is provided for by national or Community law to protect a legitimate economic interest, including the public interest in maintaining statistical confidentiality and tax secrecy.|
|INSPIRE\_Directive\_Article13\_1e|public access limited according to Article 13(1)(e) of the INSPIRE Directive|Public access to spatial data sets and services would adversely affect intellectual property rights.|
|INSPIRE\_Directive\_Article13\_1f|public access limited according to Article 13(1)(f) of the INSPIRE Directive|Public access to spatial data sets and services would adversely affect the confidentiality of personal data and/or files relating to a natural person where that person has not consented to the disclosure of the information to the public, where such confidentiality is provided for by national or Community law.|
|INSPIRE\_Directive\_Article13\_1g|public access limited according to Article 13(1)(g) of the INSPIRE Directive|Public access to spatial data sets and services would adversely affect the interests or protection of any person who supplied the information requested on a voluntary basis without being under, or capable of being put under, a legal obligation to do so, unless that person has consented to the release of the information concerned.|
|INSPIRE\_Directive\_Article13\_1h|public access limited according to Article 13(1)(h) of the INSPIRE Directive|Public access to spatial data sets and services would adversely affect the protection of the environment to which such information relates, such as the location of rare species.|
|noLimitations|no limitations to public access|There are no limitations on public access to spatial data sets and services|


# ***Conditions Applying To Access And Use***
Code list URI: <http://inspire.ec.europa.eu/metadata-codelist/ConditionsApplyingToAccessAndUse>


|**Code value**|**Label**|**Definition**|
| :- | :- | :- |
|noConditionsApply|no conditions to access and use|No conditions apply to access and use.|
|conditionsUnknown|conditions to access and use unknown|The conditions applying to access and use are unknown|

# ***Quality of Service criteria code***
Code list URI: <http://inspire.ec.europa.eu/metadata-codelist/QualityOfServiceCriteria>


|**Code Value**|**Label**|**Definition**|
| :- | :- | :- |
|availability|availability|The percentage of time the service is available.|
|performance|performance|How fast a request to the spatial data service can be completed.|
|capacity|capacity|The maximum number of simultaneous requests that can be completed with the declared performance.|

# ***Default Coordinate Reference Systems***
This list of default coordinate reference system identifiers is included here as specified in the INSPIRE Data Specification on Coordinate Reference Systems, version 3.2, Table 1 in section 5.5 Identifiers. In the case that this set of identifiers should be changed or corrected in the later versions of the INSPIRE Data Specification on Coordinate Reference Systems, the changed version of the identifier set should be preferred over the one provided here. 


|**Description**|**Short name**|**HTTP URI Identifier**|
| :- | :- | :- |
|<p>3D Cartesian in ETRS89</p><p>(X,Y,Z)</p>|ETRS89-XYZ|http://www.opengis.net/def/crs/EPSG/0/4936|
|3D geodetic in ETRS89 on GRS80 (Latitude, Longitude, Ellipsoidal height)|ETRS89-GRS80h |http://www.opengis.net/def/crs/EPSG/0/4937|
|2D geodetic in ETRS89 on GRS80 (Latitude, Longitude)|ETRS89-GRS80 |http://www.opengis.net/def/crs/EPSG/0/4258|
|2D LAEA projection in ETRS89 on GRS80 (Y,X)|ETRS89-LAEA|http://www.opengis.net/def/crs/EPSG/0/3035|
|2D LCC projection in ETRS89 on GRS80 (N,E)|ETRS89-LCC |http://www.opengis.net/def/crs/EPSG/0/3034|
|2D TM projection in ETRS89 on GRS80, zone 26N (30°W to 24°W) (N,E)|ETRS89-TM26N|http://www.opengis.net/def/crs/EPSG/0/3038|
|2D TM projection in ETRS89 on GRS80, zone 27N (24°W to 18°W) (N,E)|ETRS89-TM27N|http://www.opengis.net/def/crs/EPSG/0/3039|
|2D TM projection in ETRS89 on GRS80, zone 28N (18°W to 12°W) (N,E)|ETRS89-TM28N|http://www.opengis.net/def/crs/EPSG/0/3040|
|2D TM projection in ETRS89 on GRS80, zone 29N (12°W to 6°W) (N,E)|ETRS89-TM29N|http://www.opengis.net/def/crs/EPSG/0/3041|
|2D TM projection in ETRS89 on GRS80, zone 30N (6°W to 0°) (N,E)|ETRS89-TM30N|http://www.opengis.net/def/crs/EPSG/0/3042|
|2D TM projection in ETRS89 on GRS80, zone 31N (0° to 6°E) (N,E)|ETRS89-TM31N|http://www.opengis.net/def/crs/EPSG/0/3043|
|2D TM projection in ETRS89 on GRS80, zone 32N (6°E to 12°E) (N,E)|ETRS89-TM32N|http://www.opengis.net/def/crs/EPSG/0/3044|
|2D TM projection in ETRS89 on GRS80, zone 33N (12°E to 18°E) (N,E)|ETRS89-TM33N|http://www.opengis.net/def/crs/EPSG/0/3045|
|2D TM projection in ETRS89 on GRS80, zone 34N (18°E to 24°E) (N,E)|ETRS89-TM34N|http://www.opengis.net/def/crs/EPSG/0/3046|
|2D TM projection in ETRS89 on GRS80, zone 35N (24°E to 30°E) (N,E)|ETRS89-TM35N|http://www.opengis.net/def/crs/EPSG/0/3047|
|2D TM projection in ETRS89 on GRS80, zone 36N (30°E to 36°E) (N,E)|ETRS89-TM36N|http://www.opengis.net/def/crs/EPSG/0/3048|
|2D TM projection in ETRS89 on GRS80, zone 37N (36°E to 42°E) (N,E)|ETRS89-TM37N|http://www.opengis.net/def/crs/EPSG/0/3049|
|2D TM projection in ETRS89 on GRS80, zone 38N (42°E to 48°E) (N,E)|ETRS89-TM38N|http://www.opengis.net/def/crs/EPSG/0/3050|
|2D TM projection in ETRS89 on GRS80, zone 39N (48°E to 54°E) (N,E)|ETRS89-TM39N|http://www.opengis.net/def/crs/EPSG/0/3051|
|Height in EVRS (H)|EVRS|http://www.opengis.net/def/crs/EPSG/0/5730|
|Depth referred to LAT (D) |LAT|http://www.opengis.net/def/crs/EPSG/0/5861|
|Depth referred to MSL (D)|MSL|http://www.opengis.net/def/crs/EPSG/0/5715|
|Pressure coordinate in the free atmosphere (ICAO international standard atmosphere) (P)|ISA|http://codes.wmo.int/grib2/codeflag/4.2/\_0-3-3|
|3D compound: 2D geodetic in ETRS89 on GRS80, and EVRS height(Latitude, Longitude, H)|ETRS89-GRS80- EVRS |http://www.opengis.net/def/crs/EPSG/0/7409|

# ***Online Description Code***
Code list URI: <http://inspire.ec.europa.eu/metadata-codelist/OnLineDescriptionCode>


|**Code value**|**Label**|**Definition**|
| :- | :- | :- |
|endPoint|end point|An internet address containing a detailed description of a spatial data service, including a list of end points to allow its execution.|
|accessPoint|access point|The internet address used to directly call an operation provided by a spatial data service.|



# **Mapping between IR element numbers and TG Requirements**


|**Implementing rule**|**Section / article**|**Element name**|**TG Requirement(s)**|**Sections**|
| :- | :- | :- | :- | :- |
|[Regulation 1205/2008]|Part B 1.1|Resource title|` `REF req\_common\_title \h  \\* MERGEFORMAT TG Requirement C.8|` `REF \_Ref476232845 \r \h  \\* MERGEFORMAT 2.3.1|
|[Regulation 1205/2008]|Part B 1.2|Resource abstract|` `REF req\_common\_abstract \h  \\* MERGEFORMAT TG Requirement C.9|` `REF \_Ref476232855 \r \h  \\* MERGEFORMAT 2.3.2|
|[Regulation 1205/2008]|Part B 1.3|Resource type|` `REF req\_data\_resource\_type \h  \\* MERGEFORMAT TG Requirement 1.1,  REF req\_sds\_resource\_type \h  \\* MERGEFORMAT TG Requirement 3.1|<p>` `REF \_Ref476232875 \r \h  \\* MERGEFORMAT 3.1.1.1, </p><p>` `REF \_Ref476232886 \r \h  \\* MERGEFORMAT 4.1.1.1</p>|
|[Regulation 1205/2008]|Part B 1.4|Resource locator|` `REF req\_data\_resource\_locator \h  \\* MERGEFORMAT TG Requirement 1.8,  REF req\_sds\_resource\_locator \h  \\* MERGEFORMAT TG Requirement 3.7|<p>` `REF \_Ref476232939 \r \h  \\* MERGEFORMAT 3.1.3.1, </p><p>` `REF \_Ref476232964 \r \h  \\* MERGEFORMAT 4.1.3.1</p>|
|[Regulation 1205/2008]|Part B 1.5|Unique resource identifier|` `REF req\_data\_dataset\_uid \h  \\* MERGEFORMAT TG Requirement 1.3|` `REF \_Ref476232985 \r \h  \\* MERGEFORMAT 3.1.2.1|
|[Regulation 1205/2008]|Part B 1.7|Resource language|` `REF req\_data\_resource\_language \h  \\* MERGEFORMAT TG Requirement 1.6|` `REF \_Ref476232994 \r \h  \\* MERGEFORMAT 3.1.2.4|
|[Regulation 1205/2008]|Part B 1.6|Coupled resource|` `REF req\_sds\_sds\_coupled\_resource \h  \\* MERGEFORMAT TG Requirement 3.6|` `REF \_Ref476233005 \r \h  \\* MERGEFORMAT 4.1.2.4|
|[Regulation 1205/2008]|Part B 2.1|Topic category|` `REF req\_data\_topic\_category \h  \\* MERGEFORMAT TG Requirement 1.7|` `REF \_Ref476233014 \r \h  \\* MERGEFORMAT 3.1.2.5|
|[Regulation 1205/2008]|Part B 2.2|Spatial data service type|` `REF req\_sds\_sds\_type \h  \\* MERGEFORMAT TG Requirement 3.5,  REF req\_ns\_sds\_type \h  \\* MERGEFORMAT TG Requirement 4.1,  REF req\_sds\_invocable\_sds\_type \h  \\* MERGEFORMAT TG Requirement 5.1|<p>` `REF \_Ref476233024 \r \h  \\* MERGEFORMAT 4.1.2.3, </p><p>` `REF \_Ref476233035 \r \h  \\* MERGEFORMAT 4.2.1.1, </p><p>` `REF \_Ref476233047 \r \h  \\* MERGEFORMAT 4.3.1.1</p>|
|[Regulation 1205/2008]|Part B 3.1|Keyword value|` `REF req\_data\_theme\_keyword \h  \\* MERGEFORMAT TG Requirement 1.4,  REF req\_sds\_sds\_category \h  \\* MERGEFORMAT TG Requirement 3.4|<p>` `REF \_Ref476233085 \r \h  \\* MERGEFORMAT 3.1.2.2, </p><p>` `REF \_Ref476233094 \r \h  \\* MERGEFORMAT 4.1.2.2</p>|
|[Regulation 1205/2008]|Part B 3.2|Originating controlled vocabulary|` `REF req\_common\_keyword\_originating\_cv \h  \\* MERGEFORMAT TG Requirement C.15|` `REF \_Ref476233132 \r \h  \\* MERGEFORMAT 2.3.5|
|[Regulation 1205/2008]|Part B 4.1|Geographic bounding box|` `REF req\_common\_bounding\_box \h  \\* MERGEFORMAT TG Requirement C.19|` `REF \_Ref476233152 \r \h  \\* MERGEFORMAT 2.3.8|
|[Regulation 1205/2008]|Part B 5|Temporal reference|` `REF req\_common\_temporal\_reference \h  \\* MERGEFORMAT TG Requirement C.11,  REF req\_common\_max\_1\_date\_creation \h  \\* MERGEFORMAT TG Requirement C.12,  REF req\_common\_max\_1\_date\_last\_revision \h  \\* MERGEFORMAT TG Requirement C.13|` `REF \_Ref476233162 \r \h  \\* MERGEFORMAT 2.3.4|
|[Regulation 1205/2008]|Part B 5.1|Temporal extent|` `REF req\_common\_temporal\_extent \h  \\* MERGEFORMAT TG Requirement C.14|` `REF \_Ref476233162 \r \h  \\* MERGEFORMAT 2.3.4|
|[Regulation 1205/2008]|Part B 5.2|Date of publication|` `REF req\_common\_temporal\_reference \h  \\* MERGEFORMAT TG Requirement C.11|` `REF \_Ref476233162 \r \h  \\* MERGEFORMAT 2.3.4|
|[Regulation 1205/2008]|Part B 5.3|Date of last revision|` `REF req\_common\_temporal\_reference \h  \\* MERGEFORMAT TG Requirement C.11,  REF req\_common\_max\_1\_date\_last\_revision \h  \\* MERGEFORMAT TG Requirement C.13|` `REF \_Ref476233162 \r \h  \\* MERGEFORMAT 2.3.4|
|[Regulation 1205/2008]|Part B 5.4|Date of creation|` `REF req\_common\_temporal\_reference \h  \\* MERGEFORMAT TG Requirement C.11,  REF req\_common\_max\_1\_date\_creation \h  \\* MERGEFORMAT TG Requirement C.12|` `REF \_Ref476233162 \r \h  \\* MERGEFORMAT 2.3.4|
|[Regulation 1205/2008]|Part B 6.1|Lineage|` `REF req\_data\_lineage \h  \\* MERGEFORMAT TG Requirement 1.11|` `REF \_Ref476233234 \r \h  \\* MERGEFORMAT 3.1.4.3|
|[Regulation 1205/2008]|Part B 6.2|Spatial resolution|` `REF req\_data\_spatial\_resolution \h  \\* MERGEFORMAT TG Requirement 1.5,  REF req\_sds\_spatial\_resolution \h  \\* MERGEFORMAT TG Requirement 3.3|<p>` `REF \_Ref476233248 \r \h  \\* MERGEFORMAT 3.1.2.3, </p><p>` `REF \_Ref476233260 \r \h  \\* MERGEFORMAT 4.1.2.1</p>|
|[Regulation 1205/2008]|Part B 7|Conformity|` `REF req\_common\_conformity \h  \\* MERGEFORMAT TG Requirement C.20,  REF req\_common\_conformity\_degree \h  \\* MERGEFORMAT TG Requirement C.22,  REF req\_common\_conformity\_specification \h  \\* MERGEFORMAT TG Requirement C.21,  REF req\_data\_conformity \h  \\* MERGEFORMAT TG Requirement 1.10,  REF req\_sds\_invocable\_conformity \h  \\* MERGEFORMAT TG Requirement 5.3,  REF req\_sds\_sds\_invocable\_conformity\_specs \h  \\* MERGEFORMAT TG Requirement 5.5|<p>` `REF \_Ref476233291 \r \h  \\* MERGEFORMAT 2.4.1, </p><p>` `REF \_Ref476233304 \r \h  \\* MERGEFORMAT 3.1.4.2, </p><p>` `REF \_Ref476233316 \r \h  \\* MERGEFORMAT 4.2.2.1, </p><p>` `REF \_Ref476233332 \r \h  \\* MERGEFORMAT 4.3.3.1, </p><p>` `REF \_Ref476233341 \r \h  \\* MERGEFORMAT 4.3.3.3</p>|
|[Regulation 1205/2008]|Part B 7.1|Specification|` `REF req\_common\_conformity \h  \\* MERGEFORMAT TG Requirement C.20,  REF req\_common\_conformity\_degree \h  \\* MERGEFORMAT TG Requirement C.22,  REF req\_common\_conformity\_specification \h  \\* MERGEFORMAT TG Requirement C.21,  REF req\_data\_conformity \h  \\* MERGEFORMAT TG Requirement 1.10,  REF req\_sds\_invocable\_conformity \h  \\* MERGEFORMAT TG Requirement 5.3,  REF req\_sds\_sds\_invocable\_conformity\_specs \h  \\* MERGEFORMAT TG Requirement 5.5|<p>` `REF \_Ref476233291 \r \h  \\* MERGEFORMAT 2.4.1, </p><p>` `REF \_Ref476233304 \r \h  \\* MERGEFORMAT 3.1.4.2, </p><p>` `REF \_Ref476233316 \r \h  \\* MERGEFORMAT 4.2.2.1, </p><p>` `REF \_Ref476233332 \r \h  \\* MERGEFORMAT 4.3.3.1, </p><p>` `REF \_Ref476233341 \r \h  \\* MERGEFORMAT 4.3.3.3</p>|
|[Regulation 1205/2008]|Part B 7.2|Degree|` `REF req\_common\_conformity \h  \\* MERGEFORMAT TG Requirement C.20,  REF req\_common\_conformity\_degree \h  \\* MERGEFORMAT TG Requirement C.22,  REF req\_common\_conformity\_specification \h  \\* MERGEFORMAT TG Requirement C.21,  REF req\_data\_conformity \h  \\* MERGEFORMAT TG Requirement 1.10,  REF req\_sds\_invocable\_conformity \h  \\* MERGEFORMAT TG Requirement 5.3,  REF req\_sds\_sds\_invocable\_conformity\_specs \h  \\* MERGEFORMAT TG Requirement 5.5|<p>` `REF \_Ref476233291 \r \h  \\* MERGEFORMAT 2.4.1,</p><p>` `REF \_Ref476233304 \r \h  \\* MERGEFORMAT 3.1.4.2, </p><p>` `REF \_Ref476233316 \r \h  \\* MERGEFORMAT 4.2.2.1, </p><p>` `REF \_Ref476233332 \r \h  \\* MERGEFORMAT 4.3.3.1, </p><p>` `REF \_Ref476233341 \r \h  \\* MERGEFORMAT 4.3.3.3</p>|
|[Regulation 1205/2008]|Part B 8.1|Conditions applying to access and use|` `REF req\_common\_limitations\_access\_and\_use \h  \\* MERGEFORMAT TG Requirement C.18|` `REF \_Ref476233390 \r \h  \\* MERGEFORMAT 2.3.7|
|[Regulation 1205/2008]|Part B 8.2|Limitations on public access|` `REF req\_common\_limitations\_public\_access \h  \\* MERGEFORMAT TG Requirement C.17|` `REF \_Ref476233397 \r \h  \\* MERGEFORMAT 2.3.6|
|[Regulation 1205/2008]|Part B 9|Responsible organisation|` `REF req\_common\_responsible\_organisation \h  \\* MERGEFORMAT TG Requirement C.10|` `REF \_Ref476233406 \r \h  \\* MERGEFORMAT 2.3.3|
|[Regulation 1205/2008]|` `Part B 9.1|Responsible party|` `REF req\_common\_responsible\_organisation \h  \\* MERGEFORMAT TG Requirement C.10|` `REF \_Ref476233415 \r \h  \\* MERGEFORMAT 2.3.3|
|[Regulation 1205/2008]|` `Part B 9.2|Responsible party role|` `REF req\_common\_responsible\_organisation \h  \\* MERGEFORMAT TG Requirement C.10|` `REF \_Ref476233415 \r \h  \\* MERGEFORMAT 2.3.3|
|[Regulation 1205/2008]|Part B 10.1|Metadata point of contact|` `REF req\_common\_md\_point\_of\_contact \h  \\* MERGEFORMAT TG Requirement C.6|` `REF \_Ref476233448 \r \h  \\* MERGEFORMAT 2.2.3|
|[Regulation 1205/2008]|Part B 10.2|Metadata date|` `REF req\_common\_md\_date \h  \\* MERGEFORMAT TG Requirement C.7|` `REF \_Ref476233455 \r \h  \\* MERGEFORMAT 2.2.4|
|[Regulation 1205/2008]|Part B 10.3|Metadata language|` `REF req\_common\_md\_language \h  \\* MERGEFORMAT TG Requirement C.5|` `REF \_Ref476233462 \r \h  \\* MERGEFORMAT 2.2.2|
|[Regulation 1089/2010]/[Regulation 1089/2010], Annex VI|Article 13, clause 1/ Part B 3|Coordinate Reference System (Identifier)|` `REF req\_isdss\_crs \h  \\* MERGEFORMAT TG Requirement 2.1,  REF req\_isdss\_crs\_id \h  \\* MERGEFORMAT TG Requirement 2.2,  REF req\_sds\_interoperable\_crs \h  \\* MERGEFORMAT TG Requirement 6.1,  REF req\_sds\_interoperable\_crs\_uris \h  \\* MERGEFORMAT TG Requirement 6.2|<p>` `REF \_Ref476233480 \r \h  \\* MERGEFORMAT 3.2.1.1, </p><p>` `REF \_Ref476233491 \r \h  \\* MERGEFORMAT 4.4.1.1</p>|
|[Regulation 1089/2010]|Article 13, clause 2|Temporal Reference System|` `REF req\_isdss\_temporal\_rs \h  \\* MERGEFORMAT TG Requirement 2.3|` `REF \_Ref476233504 \r \h  \\* MERGEFORMAT 3.2.1.2|
|[Regulation 1089/2010]|Article 13, clause 3|Encoding|` `REF req\_isdss\_data\_encoding \h  \\* MERGEFORMAT TG Requirement 2.6|` `REF \_Ref476233513 \r \h  \\* MERGEFORMAT 3.2.3.1|
|[Regulation 1089/2010]|Article 13, clause 4|Topological consistency|` `REF req\_isdss\_topo\_consistency\_quantitative \h  \\* MERGEFORMAT TG Requirement 2.7,  REF req\_isdss\_topo\_consistency\_descriptive \h  \\* MERGEFORMAT TG Requirement 2.8|` `REF \_Ref476233521 \r \h  \\* MERGEFORMAT 3.2.4.1|
|[Regulation 1089/2010]|Article 13, clause 5|Character Encoding|` `REF req\_isdss\_character\_encoding \h  \\* MERGEFORMAT TG Requirement 2.5|` `REF \_Ref476233527 \r \h  \\* MERGEFORMAT 3.2.2.2|
|[Regulation 1089/2010] amended by [Regulation 1253/2013]|Article 13, clause 6|Spatial representation type|` `REF req\_isdss\_spatial\_representation\_type \h  \\* MERGEFORMAT TG Requirement 2.4|` `REF \_Ref476233536 \r \h  \\* MERGEFORMAT 3.2.2.1|
|[Regulation 1089/2010], Annex V, (Invocable SDS)|Part B 1|Category|` `REF req\_sds\_sds\_category \h  \\* MERGEFORMAT TG Requirement 3.4,  REF req\_sds\_invocable\_sds\_category \h  \\* MERGEFORMAT TG Requirement 5.4|<p>` `REF \_Ref476300263 \r \h 4.1.2.2,</p><p>` `REF \_Ref476233546 \r \h  \\* MERGEFORMAT 4.3.3.2</p>|
|[Regulation 1089/2010], Annex VI, (Interoperable SDS)|Part B 4|Quality of service|` `REF req\_sds\_interoperable\_qos \h  \\* MERGEFORMAT TG Requirement 6.5|` `REF \_Ref476233557 \r \h  \\* MERGEFORMAT 4.4.3.1|
|[Regulation 1089/2010], Annex VII, (Harmonised SDS)|Part B 3|Invocation metadata |` `REF req\_sds\_harmonised\_invocation\_md \h  \\* MERGEFORMAT TG Requirement 7.1,  REF req\_sds\_harmonised\_operation\_md \h  \\* MERGEFORMAT TG Requirement 7.2,  REF req\_sds\_harmonised\_operation\_md\_params \h  \\* MERGEFORMAT TG Requirement 7.3|` `REF \_Ref476233564 \r \h  \\* MERGEFORMAT 4.5.1.1|

# **Mapping for Requirements in previous TG versions**


|**Originating document & requirement**|**TG Metadata 2.0 requirement**|**TG Metadata 2.0 section**|
| :- | :- | :- |
|TG Metadata 1.3, TG Requirement 1|` `REF req\_data\_resource\_type \h  \\* MERGEFORMAT TG Requirement 1.1|` `REF \_Ref476299479 \r \h  \\* MERGEFORMAT 3.1.1.1|
|TG Metadata 1.3, TG Requirement 2|` `REF req\_data\_resource\_type \h  \\* MERGEFORMAT TG Requirement 1.1, <br>` `REF req\_sds\_resource\_type \h  \\* MERGEFORMAT TG Requirement 3.1|<p>` `REF \_Ref476299479 \r \h  \\* MERGEFORMAT 3.1.1.1, </p><p>` `REF \_Ref476299498 \r \h  \\* MERGEFORMAT 4.1.1.1</p>|
|TG Metadata 1.3, TG Requirement 3|` `REF req\_data\_resource\_locator \h  \\* MERGEFORMAT TG Requirement 1.8|` `REF \_Ref476299536 \r \h  \\* MERGEFORMAT 3.1.3.1|
|TG Metadata 1.3, TG Requirement 4|` `REF req\_sds\_resource\_locator \h  \\* MERGEFORMAT TG Requirement 3.7|` `REF \_Ref476299562 \r \h  \\* MERGEFORMAT 4.1.3.1|
|TG Metadata 1.3, TG Requirement 5|` `REF req\_data\_dataset\_uid \h  \\* MERGEFORMAT TG Requirement 1.3|` `REF \_Ref476232985 \r \h  \\* MERGEFORMAT 3.1.2.1|
|TG Metadata 1.3, TG Requirement 6|-||
|TG Metadata 1.3, TG Requirement 7|` `REF req\_sds\_sds\_coupled\_resource \h  \\* MERGEFORMAT TG Requirement 3.6|` `REF \_Ref476233005 \r \h  \\* MERGEFORMAT 4.1.2.4|
|TG Metadata 1.3, TG Requirement 8|` `REF req\_data\_resource\_language \h  \\* MERGEFORMAT TG Requirement 1.6|` `REF \_Ref476232994 \r \h  \\* MERGEFORMAT 3.1.2.4|
|TG Metadata 1.3, TG Requirement 9|` `REF req\_data\_resource\_language \h  \\* MERGEFORMAT TG Requirement 1.6|` `REF \_Ref476232994 \r \h  \\* MERGEFORMAT 3.1.2.4|
|TG Metadata 1.3, TG Requirement 10|` `REF req\_data\_topic\_category \h  \\* MERGEFORMAT TG Requirement 1.7|` `REF \_Ref476233014 \r \h  \\* MERGEFORMAT 3.1.2.5|
|TG Metadata 1.3, TG Requirement 11|-||
|TG Metadata 1.3, TG Requirement 12|<p>` `REF req\_sds\_sds\_type \h  \\* MERGEFORMAT TG Requirement 3.5, </p><p>` `REF req\_ns\_sds\_type \h  \\* MERGEFORMAT TG Requirement 4.1,</p><p>` `REF req\_sds\_invocable\_sds\_type \h  \\* MERGEFORMAT TG Requirement 5.1</p>|<p>` `REF \_Ref476233024 \r \h  \\* MERGEFORMAT 4.1.2.3, </p><p>` `REF \_Ref476233035 \r \h  \\* MERGEFORMAT 4.2.1.1, </p><p>` `REF \_Ref476233047 \r \h  \\* MERGEFORMAT 4.3.1.1</p>|
|TG Metadata 1.3, TG Requirement 13|<p>` `REF req\_data\_theme\_keyword \h  \\* MERGEFORMAT TG Requirement 1.4,</p><p>` `REF req\_sds\_sds\_category \h  \\* MERGEFORMAT TG Requirement 3.4</p>|<p>` `REF \_Ref476233085 \r \h  \\* MERGEFORMAT 3.1.2.2, </p><p>` `REF \_Ref476233094 \r \h  \\* MERGEFORMAT 4.1.2.2</p>|
|TG Metadata 1.3, TG Requirement 14|<p>` `REF req\_data\_theme\_keyword \h  \\* MERGEFORMAT TG Requirement 1.4,</p><p>` `REF req\_sds\_sds\_category \h  \\* MERGEFORMAT TG Requirement 3.4</p>|<p>` `REF \_Ref476233085 \r \h  \\* MERGEFORMAT 3.1.2.2, </p><p>` `REF \_Ref476233094 \r \h  \\* MERGEFORMAT 4.1.2.2</p>|
|TG Metadata 1.3, TG Requirement 15|<p>` `REF req\_data\_theme\_keyword \h  \\* MERGEFORMAT TG Requirement 1.4,</p><p>` `REF req\_sds\_sds\_category \h  \\* MERGEFORMAT TG Requirement 3.4</p>|<p>` `REF \_Ref476233085 \r \h  \\* MERGEFORMAT 3.1.2.2, </p><p>` `REF \_Ref476233094 \r \h  \\* MERGEFORMAT 4.1.2.2</p>|
|TG Metadata 1.3, TG Requirement 16|` `REF req\_common\_keyword\_originating\_cv \h  \\* MERGEFORMAT TG Requirement C.15|` `REF \_Ref476233132 \r \h  \\* MERGEFORMAT 2.3.5|
|TG Metadata 1.3, TG Requirement 17|` `REF req\_common\_keyword\_originating\_cv \h  \\* MERGEFORMAT TG Requirement C.15|` `REF \_Ref476233132 \r \h  \\* MERGEFORMAT 2.3.5|
|TG Metadata 1.3, TG Requirement 18|` `REF req\_common\_keyword\_originating\_cv \h  \\* MERGEFORMAT TG Requirement C.15|` `REF \_Ref476233132 \r \h  \\* MERGEFORMAT 2.3.5|
|TG Metadata 1.3, TG Requirement 19|` `REF req\_common\_group\_keywords\_by\_cv \h  \\* MERGEFORMAT TG Requirement C.16|` `REF \_Ref476233132 \r \h  \\* MERGEFORMAT 2.3.5|
|TG Metadata 1.3, TG Requirement 20|` `REF req\_common\_bounding\_box \h  \\* MERGEFORMAT TG Requirement C.19|` `REF \_Ref476299914 \r \h 2.3.8|
|TG Metadata 1.3, TG Requirement 21|` `REF req\_common\_bounding\_box \h  \\* MERGEFORMAT TG Requirement C.19|` `REF \_Ref476299917 \r \h 2.3.8|
|TG Metadata 1.3, TG Requirement 22|` `REF req\_common\_temporal\_reference \h  \\* MERGEFORMAT TG Requirement C.11|` `REF \_Ref476233162 \r \h  \\* MERGEFORMAT 2.3.4|
|TG Metadata 1.3, TG Requirement 23|` `REF req\_common\_temporal\_reference \h  \\* MERGEFORMAT TG Requirement C.11|` `REF \_Ref476233162 \r \h  \\* MERGEFORMAT 2.3.4|
|TG Metadata 1.3, TG Requirement 24|` `REF req\_common\_temporal\_reference \h  \\* MERGEFORMAT TG Requirement C.11|` `REF \_Ref476233162 \r \h  \\* MERGEFORMAT 2.3.4|
|TG Metadata 1.3, TG Requirement 25|` `REF req\_common\_max\_1\_date\_creation \h  \\* MERGEFORMAT TG Requirement C.12|` `REF \_Ref476233162 \r \h  \\* MERGEFORMAT 2.3.4|
|TG Metadata 1.3, TG Requirement 26|` `REF req\_data\_lineage \h  \\* MERGEFORMAT TG Requirement 1.11|` `REF \_Ref476233234 \r \h  \\* MERGEFORMAT 3.1.4.3|
|TG Metadata 1.3, TG Requirement 27|<p>` `REF req\_data\_spatial\_resolution \h  \\* MERGEFORMAT TG Requirement 1.5, </p><p>` `REF req\_sds\_spatial\_resolution \h  \\* MERGEFORMAT TG Requirement 3.3</p>|<p>` `REF \_Ref476233248 \r \h  \\* MERGEFORMAT 3.1.2.3, </p><p>` `REF \_Ref476233260 \r \h  \\* MERGEFORMAT 4.1.2.1</p>|
|TG Metadata 1.3, TG Requirement 28|<p>` `REF req\_common\_conformity \h  \\* MERGEFORMAT TG Requirement C.20, </p><p>` `REF req\_common\_conformity\_specification \h  \\* MERGEFORMAT TG Requirement C.21,</p><p>` `REF req\_common\_conformity\_degree \h  \\* MERGEFORMAT TG Requirement C.22,</p><p>` `REF req\_data\_conformity \h  \\* MERGEFORMAT TG Requirement 1.10,</p><p>` `REF req\_sds\_invocable\_conformity \h  \\* MERGEFORMAT TG Requirement 5.3</p>|<p>` `REF \_Ref476233291 \r \h  \\* MERGEFORMAT 2.4.1, </p><p>` `REF \_Ref476233304 \r \h  \\* MERGEFORMAT 3.1.4.2, </p><p>` `REF \_Ref476233316 \r \h  \\* MERGEFORMAT 4.2.2.1, </p><p>` `REF \_Ref476233332 \r \h  \\* MERGEFORMAT 4.3.3.1, </p><p>` `REF \_Ref476233341 \r \h  \\* MERGEFORMAT 4.3.3.3</p>|
|TG Metadata 1.3, TG Requirement 29|<p>` `REF req\_common\_conformity \h  \\* MERGEFORMAT TG Requirement C.20, </p><p>` `REF req\_common\_conformity\_specification \h  \\* MERGEFORMAT TG Requirement C.21,</p><p>` `REF req\_common\_conformity\_degree \h  \\* MERGEFORMAT TG Requirement C.22,</p><p>` `REF req\_data\_conformity \h  \\* MERGEFORMAT TG Requirement 1.10,</p><p>` `REF req\_sds\_invocable\_conformity \h  \\* MERGEFORMAT TG Requirement 5.3</p>|<p>` `REF \_Ref476233291 \r \h  \\* MERGEFORMAT 2.4.1, </p><p>` `REF \_Ref476233304 \r \h  \\* MERGEFORMAT 3.1.4.2, </p><p>` `REF \_Ref476233316 \r \h  \\* MERGEFORMAT 4.2.2.1, </p><p>` `REF \_Ref476233332 \r \h  \\* MERGEFORMAT 4.3.3.1, </p><p>` `REF \_Ref476233341 \r \h  \\* MERGEFORMAT 4.3.3.3</p>|
|TG Metadata 1.3, TG Requirement 30|<p>` `REF req\_common\_limitations\_public\_access \h  \\* MERGEFORMAT TG Requirement C.17,</p><p>` `REF req\_common\_limitations\_access\_and\_use \h  \\* MERGEFORMAT TG Requirement C.18</p>|<p>` `REF \_Ref476233397 \r \h  \\* MERGEFORMAT 2.3.6,</p><p>` `REF \_Ref476233390 \r \h  \\* MERGEFORMAT 2.3.7</p>|
|TG Metadata 1.3, TG Requirement 31|<p>` `REF req\_common\_limitations\_public\_access \h  \\* MERGEFORMAT TG Requirement C.17,</p><p>` `REF req\_common\_limitations\_access\_and\_use \h  \\* MERGEFORMAT TG Requirement C.18</p>|<p>` `REF \_Ref476233397 \r \h  \\* MERGEFORMAT 2.3.6,</p><p>` `REF \_Ref476233390 \r \h  \\* MERGEFORMAT 2.3.7</p>|
|TG Metadata 1.3, TG Requirement 32|` `REF req\_common\_limitations\_public\_access \h  \\* MERGEFORMAT TG Requirement C.17|` `REF \_Ref476233397 \r \h  \\* MERGEFORMAT 2.3.6|
|TG Metadata 1.3, TG Requirement 33|` `REF req\_common\_limitations\_access\_and\_use \h  \\* MERGEFORMAT TG Requirement C.18|` `REF \_Ref476233390 \r \h  \\* MERGEFORMAT 2.3.7|
|TG Metadata 1.3, TG Requirement 34|` `REF req\_common\_limitations\_access\_and\_use \h  \\* MERGEFORMAT TG Requirement C.18|` `REF \_Ref476233390 \r \h  \\* MERGEFORMAT 2.3.7|
|TG Metadata 1.3, TG Requirement 35|` `REF req\_common\_responsible\_organisation \h  \\* MERGEFORMAT TG Requirement C.10|` `REF \_Ref476233406 \r \h  \\* MERGEFORMAT 2.3.3|
|TG Metadata 1.3, TG Requirement 36|` `REF req\_common\_responsible\_organisation \h  \\* MERGEFORMAT TG Requirement C.10|` `REF \_Ref476233406 \r \h  \\* MERGEFORMAT 2.3.3|
|TG Metadata 1.3, TG Requirement 37|` `REF req\_common\_md\_point\_of\_contact \h  \\* MERGEFORMAT TG Requirement C.6|` `REF \_Ref476233448 \r \h  \\* MERGEFORMAT 2.2.3|
|TG Metadata 1.3, TG Requirement 38|` `REF req\_common\_md\_point\_of\_contact \h  \\* MERGEFORMAT TG Requirement C.6|` `REF \_Ref476233448 \r \h  \\* MERGEFORMAT 2.2.3|
|TG Metadata 1.3, TG Requirement 39|` `REF req\_common\_md\_language \h  \\* MERGEFORMAT TG Requirement C.5|` `REF \_Ref476233462 \r \h  \\* MERGEFORMAT 2.2.2|
|TG SDS 3.1, Implementation Requirement 1|` `REF req\_sds\_invocable\_sds\_category \h  \\* MERGEFORMAT TG Requirement 5.4|` `REF \_Ref476233546 \r \h  \\* MERGEFORMAT 4.3.3.2|
|TG SDS 3.1, Implementation Requirement 2|` `REF req\_sds\_sds\_invocable\_access\_point \h  \\* MERGEFORMAT TG Requirement 5.2|` `REF \_Ref476300344 \r \h 4.3.2.1|
|TG SDS 3.1, Implementation Requirement 3|` `REF req\_sds\_sds\_invocable\_access\_point \h  \\* MERGEFORMAT TG Requirement 5.2|` `REF \_Ref476300344 \r \h 4.3.2.1|
|TG SDS 3.1, Implementation Requirement 4|` `REF req\_sds\_sds\_invocable\_conformity\_specs \h  \\* MERGEFORMAT TG Requirement 5.5|` `REF \_Ref476300396 \r \h 4.3.3.3|
|TG SDS 3.1, Implementation Requirement 5|` `REF req\_sds\_invocable\_conformity \h  \\* MERGEFORMAT TG Requirement 5.3|` `REF \_Ref476300412 \r \h 4.3.3.1|
|TG SDS 3.1, Implementation Requirement 6|<p>` `REF req\_sds\_interoperable\_crs \h  \\* MERGEFORMAT TG Requirement 6.1,</p><p>` `REF req\_sds\_interoperable\_crs\_uris \h  \\* MERGEFORMAT TG Requirement 6.2</p>|` `REF \_Ref476300419 \r \h 4.4.1.1|
|TG SDS 3.1, Implementation Requirement 7|<p>` `REF req\_sds\_interoperable\_crs \h  \\* MERGEFORMAT TG Requirement 6.1,</p><p>` `REF req\_sds\_interoperable\_crs\_uris \h  \\* MERGEFORMAT TG Requirement 6.2</p>|` `REF \_Ref476300419 \r \h 4.4.1.1|
|TG SDS 3.1, Implementation Requirement 8|` `REF req\_sds\_interoperable\_qos \h  \\* MERGEFORMAT TG Requirement 6.5|` `REF \_Ref476300432 \r \h 4.4.3.1|
|TG SDS 3.1, Implementation Requirement 9|` `REF req\_sds\_interoperable\_qos \h  \\* MERGEFORMAT TG Requirement 6.5|` `REF \_Ref476300432 \r \h 4.4.3.1|
|TG SDS 3.1, Implementation Requirement 10|` `REF req\_sds\_interoperable\_qos \h  \\* MERGEFORMAT TG Requirement 6.5|` `REF \_Ref476300432 \r \h 4.4.3.1|
|TG SDS 3.1, Implementation Requirement 11|` `REF req\_sds\_interoperable\_responsible\_party \h  \\* MERGEFORMAT TG Requirement 6.4|` `REF \_Ref476300460 \r \h 4.4.2.2|
|TG SDS 3.1, Implementation Requirement 12|` `REF req\_sds\_interoperable\_cond\_access\_use \h  \\* MERGEFORMAT TG Requirement 6.3|` `REF \_Ref476300467 \r \h 4.4.2.1|
|TG SDS 3.1, Implementation Requirement 13|[Not relevant to metadata]|-|
|TG SDS 3.1, Implementation Requirement 14|[Not relevant to metadata]|-|
|TG SDS 3.1, Implementation Requirement 15|<p>` `REF req\_sds\_harmonised\_invocation\_md \h  \\* MERGEFORMAT TG Requirement 7.1,</p><p>` `REF req\_sds\_harmonised\_operation\_md \h  \\* MERGEFORMAT TG Requirement 7.2</p>|` `REF \_Ref476300474 \r \h 4.5.1.1|
|TG SDS 3.1, Implementation Requirement 16|[Not relevant to metadata]|-|
|TG SDS 3.1, Implementation Requirement 17|` `REF req\_sds\_sds\_invocable\_conformity\_specs \h  \\* MERGEFORMAT TG Requirement 5.5|` `REF \_Ref476300482 \r \h 4.3.2.1|
|TG SDS 3.1, Implementation Requirement 18|[Not relevant to metadata]|-|


# **Examples of complete INSPIRE metadata records**
A web site with examples of complete metadata records compliant with this technical guidance is available at <http://inspire.ec.europa.eu/id/document/tg/metadata-iso19139/2.0/examples>.
