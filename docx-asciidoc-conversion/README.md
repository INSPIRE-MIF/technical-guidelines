# docx-asciidoc-conversion

### Introduction

The objective of the project is to convert the INSPIRE Metadata Technical Guidance 2.0 document from MS Word docx format to AsciiDoc format to facilitate its access and maintenance in a GitHub repository. AsciiDoc was selected over the more common Markdown format because AsciiDoc supports many advanced document features, such as automatic section numbering, that Markdown does not support. 

An important issue encountered is that it is not possible for a generic docx to AsciiDoc converter (such as Pandoc used here) to convert all the document content as required, which is mostly due to sections with special formatting, such as TG Requirements, TG Recommendations, Conformance Classes, XML Examples or quotes. To address this issue, a Python script was developed that applies custom styling to relevant sections of AsciiDoc version of the document (obtained using Pandoc converter) based on additional style information included in a Markdown version of the document (obtained using Pandoc as well). Additionally, the Python script fixes other minor issues with the AsciiDoc document, such as section headings, numbering, TOC, etc. Moreover, some of the styles, used to identify relevant sections, are not applied consistently in the docx, so this needs to be corrected in MS Word before the conversion.  

### Prerequisites

- [Pandoc](https://pandoc.org/), version 2.14.0.3 used
- Python 3, version 3.8.3 used
- [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/) Python library, version 4.9.3 used

### Conversion Procedure

1. Correct the original docx document, save as `md_2_fixed.docx`:
   - apply *XML Example* style to all XML examples (about 7 cases were found in `md_2_0_1.docx` where this fix was required)
   - remove paragraph breaks from inside footnotes (two cases were found in `md_2_0_1.docx` where this fix was required)

2. Convert the corrected docx document to *AsciiDoc* using Pandoc, save as `md_2_pandoc.adoc`, extract images to `media` folder:
    ```shell
    pandoc md_2_fixed.docx -f docx -t asciidoc -o md_2_pandoc.adoc --wrap=none --extract-media=. --markdown-headings=atx
    ```
    
1. Convert the corrected docx document to *Markdown* using Pandoc, enabling the [styles extension](https://pandoc.org/MANUAL.html#ext-styles), save as `md_2_styles.md`:
    ```shell
    pandoc md_2_fixed.docx -f docx+styles -t markdown -o md_2_styles.md --wrap=none --markdown-headings=atx
    ```
    
4. Run the `post_pandoc.py` Python script with 3 arguments: adoc file from 2., md file from 3. and `attributes.adoc` file, it will create `md_2_final.adoc` file:
    ```shell
    python post_pandoc.py md_2_pandoc.adoc md_2_styles.md attributes.adoc
    ```
    
    The script applies AsciiDoc admonitions to TG Requirement, TG Recommendation and Conformance Class sections, source blocks to XML Examples and blockquotes to quote sections of `md_2_pandoc.adoc` based on additional style information included in`md_2_styles.md`. It also corrects initial (unnumbered) section headings, removes manual TOC entries, inserts automatic TOC. AsciiDoc does not yet support custom section numbering (see [this issue](https://github.com/asciidoctor/asciidoctor/issues/3311)), therefore 'Annex X' text is inserted in relevant headings by the script.
    
5. Replace `image1.wmf` image with a *png* version in the `media` folder.

### Included Files

`md_2_0_1.docx` original docx MS Word, Metadata Technical Guidance 2.0 document, used in 1.

`md_2_fixed.docx` corrected docx MS Word, Metadata Technical Guidance 2.0 document, created in 1., used in 2. and 3. 

`md_2_final.adoc` final AsciiDoc , Metadata Technical Guidance 2.0 document, created in 4.

`attributes.adoc` attributes to include in the AsciiDoc document, used in 4.

`post_pandoc.py` Python script, used in 4.

`media` folder containing images extracted from docx document by Pandoc, created in 4., modified in 5.
