@echo off

set argC=0
for %%x in (%*) do Set /A argC+=1

if %argC% NEQ 1 (
    echo Usage: $0 DEST_FOLDER>&2
	echo This commands convert the .docx present into DEST_FOLDER to intermediate files of .adoc final conversion.>&2
	echo.>&2
	echo Parameters:>&2
	echo DEST_FOLDER : The folder containing the .docx file to convert. It will contain intermediate files also
	echo.>&2
	echo Files created are:>&2
	echo - md_2_pandoc.adoc: the intermediate conversion of .docx file to asciidoc file>&2
	echo - md_2_styles.md: the intermediate conversion of .docx file to markdown file>&2
	echo.>&2
	echo NOTE: If you have an old .doc or .docx document format you have to update it to latest version using Microsoft Word>&2
	echo.>&2
    exit 1
)

cd %1
for %%f in (*.docx) do (
    if "%%~xf"==".docx" (
		echo %%f
		pandoc %%f -f docx -t asciidoc -o md_2_pandoc.adoc --wrap=none --extract-media=. --markdown-headings=atx
		pandoc %%f -f docx+styles -t markdown -o md_2_styles.md --wrap=none --markdown-headings=atx
	)
)
cd ..