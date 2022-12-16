# Conversion from docx to asciidoc format

### Introduction

The objective of the procedure is to convert the INSPIRE Technical Guidance documents from MS Word docx format to AsciiDoc format to facilitate its access and maintenance in a GitHub repository. AsciiDoc was selected over the more common Markdown format because AsciiDoc supports many advanced document features, such as automatic section numbering, that Markdown does not support.

An important issue encountered is that it is not possible for a generic docx to AsciiDoc converter (such as Pandoc used here) to convert all the document content as required, which is mostly due to sections with special formatting, such as TG Requirements, TG Recommendations, Conformance Classes, XML Examples or quotes. To address this issue, a Python script was developed that applies custom styling to relevant sections of AsciiDoc version of the document (obtained using Pandoc converter) based on additional style information included in a Markdown version of the document (obtained using Pandoc as well). Additionally, the Python script fixes other minor issues with the AsciiDoc document, such as section headings, numbering, TOC, etc. Moreover, some of the styles, used to identify relevant sections, are not applied consistently in the docx, so this needs to be corrected in MS Word before the conversion.

The procedure was initially developed and tested using the INSPIRE Metadata Technical Guidance 2.0 and successively tested on different types of TGs (Network Services and Data Specifications). Due to the different MS Word formats used in these documents, the development of dedicated Python scripts was to automate as much as possible the conversion of all MS Word syntax. It has been verified that, in any case, a final manual revision is always needed due to the complexity of the MS Word documents.
 

### Prerequisites

- [Pandoc](https://pandoc.org/), version 2.14.0.3 used
- Python 3, version 3.8.3 used
- [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/) Python library, version 4.9.3 used

### Conversion Procedure

1. Create a new folder with the name of the document to convert:
   ```shell
    mkdir my_example_data_specifications_EX
    ```

2. Copy the Microsoft Word document into the new folder. Convert the Microsoft Word document into the last .docx format:
    ```shell
    From Microsoft Word document: File -> Informations -> Convert
    ```
    
3. Launch the preliminary folder script from main folder. This script contains instructions for the first conversion to asciidoc.:
    ```shell
    .\pandoc-folder.bat .\my_example_data_specifications_EX
    ```
    
4. Launch the conversion script from the main folder, using the correct data format between *metadata*, *services* and *data*. In fact, if a specific modification is required for a type of document, it will be possible to specifically modify one of the three libraries:
    ```shell
    .\pandoc-postpy.bat .\my_example_data_specifications_EX data
    ```
    
    The script applies AsciiDoc admonitions to TG Requirement, TG Recommendation and Conformance Class sections, source blocks to XML Examples and blockquotes to quote sections of  md_2_pandoc.adoc based on additional style information included in md_2_styles.md. 
    
5. Check the result document, named as the folder (e.g. my_example_data_specifications_EX.adoc). It always requires a manual revision to fix some possible conversion errors.
	A sample list of common issues to be manually fixed is the following:
  
	- Replace the image1.wmf image with a png version in the media folder and change the image filename in the adoc file  
	-	Replace all the .emf images with a png version in the media folder and change the related image filenames in the adoc file
	-	Delete flat TOC and add the code for the automatic generation:
	  ```shell
		= Table of Contents
		toc::[]
    ```
	-	Fix formatting of nested tables
	-	Add page break (<<<) support if the adoc is exported in PDF
	-	Add code for stopping the numbering of sections for which it is not required (e.g. Bibliography):
	  ```shell
		:sectnums!:
		== Bibliography
    ```
