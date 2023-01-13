@echo off

set argC=0
for %%x in (%*) do Set /A argC+=1

if %argC% NEQ 2 (
    echo Usage: %~nx0 DEST_FOLDER FILE_TYPE>&2
	echo This commands convert intermediate files to post-processed asciidoc file.>&2
	echo.>&2
	echo Parameters:>&2
	echo DEST_FOLDER : The folder containing the intermediate files>&2
	echo FILE_TYPE : The file type to elaborate. Could be "metadata", "services" or "data">&2
	echo.>&2
    exit 1
)

cls
xcopy /y attributes.adoc %1attributes.adoc
cd %1
python ..\post_pandoc.py md_2_pandoc.adoc md_2_styles.md attributes.adoc %2
cd ..