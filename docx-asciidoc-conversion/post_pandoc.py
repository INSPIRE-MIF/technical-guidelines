import re, sys
from bs4 import BeautifulSoup

def do_styles(style, title_re, star_replacement, admonition):
    req_count = 0
    found_count = 0
    position = 0
    output = ''
    regex = fr'::: {{custom-style="{style}"}}\n{title_re}.*?(::: {{custom-style="{style}"}}\n(?!{title_re}).*?:::\n+)+'

    # loop through special sections identified with regex in md with style annotations
    for req in re.finditer(regex, md, re.DOTALL):
        req_count += 1

        # remove style annotation
        req = re.sub(r':::.*\n', '', req.group(0))

        # find title line
        title = req[0:req.find('\n')]

        # find number of lines
        lines = req.count('\n')

        # simple dirty md to adoc conversion, ideally Pandoc could be used for this purpose
        title = title.replace('***', '*|||||').replace('**', '|||||').replace('\\*', '|||||')\
            .replace('\\<', '<').replace('\\#', '#').replace('*', star_replacement).replace('|||||', '*')

        # find the same section in adoc
        start = adoc.find(title, position)
        if start >= 0:
            found_count += 1
            end = start
            for i in range(0, lines):
                end = adoc.find('\n', end + 1)

            # Pandoc conversion has errors, such as missing newlines, here we try to fix them in adoc (in special sections that are dealt with here)
            fixed = re.sub(r'(?<=[A-Za-z0-9\]\)])\.(?=[A-Z])', '.\n\n', adoc[start:end])
            fixed = re.sub(r'(?<=[A-Za-z0-9\]\)])(?=\*\*Conformance subject\*\*)', '.\n\n', fixed)

            print(title)
            
            # create admonition section in adoc
            output += adoc[position:start] + '[' + admonition + ']\n====\n' + fixed + '====\n'
            position = end

    output += adoc[position:]

    print(style + ' ' + str(req_count) + ' ' + str(found_count))
    print('-----------------------------------------')

    return output

def do_xml():
    req_count = 0
    found_count = 0
    position = 0
    output = ''
    regex = fr'::: {{custom-style="XML Example"}}\n.*?::: {{custom-style="[cC]aption.?"}}\n.*?\n:::\n'

    # loop through XML sections identified with regex in md with style annotations 
    for req in re.finditer(regex, md, re.DOTALL):
        req_count += 1

        # remove style annotation
        req = re.sub(r':::.*\n', '', req.group(0))

        # find caption line
        title_start = req.find('**Example')
        title_end = req.find(':', title_start) + 1
        title = req[title_start:title_end]

        # find number of lines
        lines = req.count('\n')

        # find the same XML section in adoc 
        end = adoc.find(title.replace('**', '*'), position)
        if end >= 0:
            found_count += 1
            start = end
            for i in range(0, lines):
                start = adoc.rfind('\n', 0, start)
            start += 1

            # fix long lines that are split, remove stars
            xml = adoc[start:end].replace(' +\n', '').replace('/*/', '|||||').replace('*', '').replace('|||||', '/*/')
            #xml = re.sub(r'(?<!/)\*(?!/)', '', xml)

            # prettify XML
            soup = BeautifulSoup(xml, "html.parser")
            pretty = soup.prettify()

            # increase indent, as it cannot be customized in BS
            indent = re.compile(r'^(\s*)', re.MULTILINE)
            pretty = re.sub(indent, r'\1\1', pretty)

            # fix first line
            pretty = re.sub(r'^(/.*)\n', r'**\1**\n\n', pretty)

            print(title)

            # create source section in adoc, subs="+quotes" should allow for bold formatting but does not seem to work in GitHub
            output += adoc[position:start] + '[source,xml,subs="+quotes"]\n----\n' + pretty + '----\n'
            position = end

    output += adoc[position:]

    print('XML Example ' + str(req_count) + ' ' + str(found_count))
    print('-----------------------------------------')

    return output

def do_quotes():
    req_count = 0
    found_count = 0
    position = 0
    output = ''
    adoc_adj = adoc.replace('“', '"').replace('”', '"')
    regex = fr'(::: {{custom-style="IR quote"}}\n.*?:::\n+)+'

    # loop through quote sections identified with regex in md with style annotations
    for req in re.finditer(regex, md, re.DOTALL):
        req_count += 1

        # remove style annotation
        req = re.sub(r':::.*\n', '', req.group(0))

        # find title line
        first = req[0:req.find('\n')].replace('\\', '')

        # find number of lines
        lines = req.count('\n')

        # find the first line in adoc 
        start = adoc_adj.find(first, position)
        if start >= 0:
            found_count += 1
            end = start
            for i in range(0, lines):
                end = adoc.find('\n', end + 1)

            print(first)

            # create blockquote section in adoc
            output += adoc[position:start] + '\n____\n' + adoc[start:end] + '____\n'
            position = end

    output += adoc[position:]

    print('Quote ' + str(req_count) + ' ' + str(found_count))
    print('-----------------------------------------')

    return output

# fix sections, TOC, misc fixes
def do_sections():
    # section numbering starting from first '==' Pandoc heading
    output = adoc.replace('\n== ', '\n:sectnums:\n\n== ', 1)

    # fix initial (unnumbered) section headings 
    output = re.sub(r'\[(#_\S*)(.*)\]####(.*)\n', r'== \3', output)

    # insert 'Annex X' in relevant headings
    output = output.replace('\n== Abstract Test Suites', 
        '\n== Annex A Abstract Test Suites')
    output = output.replace('\n== Mapping of ISO 19115:2003 Core elements and INSPIRE Implementing Rules for metadata', 
        '\n== Annex B Mapping of ISO 19115:2003 Core elements and INSPIRE Implementing Rules for metadata')
    output = output.replace('\n== INSPIRE metadata element catalog', 
        '\n== Annex C INSPIRE metadata element catalog')
    output = output.replace('\n== Referenced code lists and code list values', 
        '\n== Annex D Referenced code lists and code list values')
    output = output.replace('\n== Mapping between IR element numbers and TG Requirements', 
        '\n== Annex E Mapping between IR element numbers and TG Requirements')
    output = output.replace('\n== Mapping for Requirements in previous TG versions', 
        '\n== Annex F Mapping for Requirements in previous TG versions')
    output = output.replace('\n== Examples of complete INSPIRE metadata records', 
        '\n== Annex G Examples of complete INSPIRE metadata records')

    # remove manual TOC
    output = re.sub(r'\nlink:#.*\]\n', '', output)

    # insert automatic TOC
    output = output.replace('\n== Table of Contents', '\n== Table of Contents\ntoc::[]\n')
    #sections = fr'\[(#_\S*)(.*)\]####(.*)\n'
    #for sect in re.finditer(regex, adoc):
    #    print(sect.group(3))
    #    title = sect.group(3).lower().replace(' ', '-')
    #    output = output.replace('link:' + sect.group(1), 'link:#' + title).replace('[' + sect.group(1) + sect.group(2) + ']####', '== ')
    
    # remove all blockquotes (unwanted, inserted by Pandoc), adjust 'NOTE' text to prevent rendering as admonition
    output = output.replace('____', '').replace('NOTE:', 'NOTE')

    # insert newline after images, change image1 to png
    output = re.sub(r'(image:.*\[.*\])(\S)', r'\1\n\2', output)\
        .replace('image:.\media/image1.wmf', 'image:.\media/image1.png')

    # document title, [discrete] hides the title from TOC
    output = output.replace('*Technical Guidance for the implementation of INSPIRE dataset and service metadata based on ISO/TS 19139:2007*', 
        '[discrete]\n= Technical Guidance for the implementation of INSPIRE dataset and service metadata based on ISO/TS 19139:2007')

    # remove newline
    output = output.replace('**INSPIRE**\n\n*Infrastructure for Spatial Information in Europe*', 
        '**INSPIRE**\n*Infrastructure for Spatial Information in Europe*')

    # remove other Pandoc garbage
    output = output.replace('* +\n*\n', '')

    return output       

with open(sys.argv[3], 'r', encoding='utf8') as inAttributes:
    adoc = inAttributes.read()
with open(sys.argv[2], 'r', encoding='utf8') as inStyles:
    md = inStyles.read()
with open(sys.argv[1], 'r', encoding='utf8') as inTarget:
    adoc += inTarget.read()

adoc = do_sections()
adoc = do_styles('TG Requirement', r'\*\*TG Requirement', '__', 'IMPORTANT')
adoc = do_styles('TG Recommendation', r'\*\*TG Recommendation', '__', 'TIP')
adoc = do_styles('Conformance class', r'\*\*Conformance Class', '_', 'NOTE')
adoc = do_xml()
adoc = do_quotes()

with open('md_2_final.adoc', 'w', encoding='utf8') as output:
    output.write(adoc)
