import re, copy

from bs4 import BeautifulSoup


def find_nth(content, item, n):
    """Search the n-th occurrence of item in content"""

    start = content.find(item)
    while start >= 0 and n > 1:
        start = content.find(item, start + len(item))
        n -= 1
    return start


def fix_arabic_adoc(old_context):
    """Fixes arabic content as each arabic has is own point item, with the right numerations"""

    # old_context has to be immutable
    context = copy.deepcopy(old_context)

    adoc = context["adoc"]

    adoc_orig = ""
    regex_arabic = r'(\[arabic, start=([0-9]+)\]\n\.((?:(?!\n\n)).)*?\n\.)'
    while adoc_orig != adoc:
        adoc_orig = adoc
        for req in re.finditer(regex_arabic, adoc, re.DOTALL):
            number = str(int(req.group(2)) + 1)
            adoc = adoc.replace(req.group(1), req.group(0)[:-2] + "\n\n[arabic, start=" + number + "]\n.")

    context["adoc"] = adoc
    return context


def fix_styles_md(old_context, style, title_re, adoc_content, new_content):
    """Convert edge case adoc admonitions working on fixes into MD styles"""

    # old_context has to be immutable
    context = copy.deepcopy(old_context)

    context = fix_arabic_adoc(context)

    context["md"] = re.sub(fr'\n([0-9a-zA-Z]+)\.[ ]*::: {{custom-style="{style}"}}',
                           fr'\n admonition start\n\n    ::: {{custom-style="{style}"}}\n    **{new_content} \g<1>**\n    :::\n	\n    ::: {{custom-style="{style}"}}',
                           context["md"], 0, re.DOTALL)

    md_regex = fr'[ ]*::: {{custom-style="{style}"}}\n[ ]*{title_re} ([0-9a-zA-Z]+).*?:::\s*::: {{custom-style="{style}"}}\n((?!{title_re}).*?)\n[ ]*:::\n'
    found = 0
    for req in re.finditer(md_regex, context["md"], re.DOTALL):
        found += 1
        index = req.group(1)
        content = req.group(2).lstrip()

        # print("AAA"+req.group(0)+"bbb("+index+")")

        # simple dirty md to adoc conversion, ideally Pandoc could be used for this purpose
        content = content.replace('***', '*|||||').replace('**', '|||||').replace('\\*', '|||||') \
            .replace(r"\'", "'").replace('\\#', '#').replace("*", "_").replace('|||||', '*') \
            .replace(r'\[', '[').replace(r'\]', ']').replace(r'\<', '<').replace(r'\>', '>').replace('--', '–') \
            .replace('__', '_').replace(r'\"', '"').replace("\\", ' +')

        # remove internal Hyperlink style
        content = re.sub('(\[\[(.*?)\]{custom-style="Hyperlink"}\]\((.*?)\))', 'link:\g<3>[\g<2>]', content)

        # remove internal Hyperlink style
        content = re.sub('(\[(.*?){custom-style="Hyperlink"}\])', r'\g<2>', content)

        # ignore anchors
        content = re.sub('\[\]{(#_Toc[0-9]+) .anchor}', '[\g<1> .anchor]##', content)

        arabic = adoc_content.replace('##index##', index)
        new_arabic = '*' + new_content + ' ' + index + '*\n\n'

        # print("CCC"+arabic+content+"DDD")

        context["adoc"] = context["adoc"].replace(arabic + content, new_arabic + content)

    print('Fix ' + style + ' ' + str(found))
    print('-----------------------------------------')

    return context


def do_styles(old_context, style, title_re, star_replacement, admonition, title_rows):
    """Make as admonition every Requirement, Recomendation, etc... based on regex"""

    # old_context has to be immutable
    context = copy.deepcopy(old_context)

    req_count = 0
    found_count = 0
    position = 0
    output = ''
    regex = fr'[ ]*::: {{custom-style="{style}"}}\n[ ]*{title_re}.*?:::(\s*::: {{custom-style="{style}"}}\n(?!{title_re}).*?:::\n+)*'

    # loop through special sections identified with regex in md with style annotations
    for req in re.finditer(regex, context["md"], re.DOTALL):
        req_count += 1

        # print("AAA"+req.group(0)+"BBB")

        # remove style annotation
        req = re.sub(r':::.*\n', '', req.group(0))
        req = re.sub(r'^[ ]*', '', req)
        req = re.sub(r'\n[ ]*', '\n', req)

        # print("AAA"+req+"BBB")

        # find title line
        title = req[0:find_nth(req, "\n", title_rows)]

        # find number of lines
        lines = req.count('\n')

        # simple dirty md to adoc conversion, ideally Pandoc could be used for this purpose
        title = title.replace('***', '*|||||').replace('**', '|||||').replace('\\*', '|||||') \
            .replace(r"\'", "'").replace('\\#', '#').replace('*', star_replacement).replace('|||||', '*') \
            .replace(r'\[', '[').replace(r'\]', ']').replace(r'\<', '<').replace(r'\>', '>').replace('--', '–') \
            .replace('__', '_').replace(r'\"', '"').replace("\\", ' +')

        # remove internal Hyperlink style
        title = re.sub('(\[\[(.*?)\]{custom-style="Hyperlink"}\]\((.*?)\))', 'link:\g<3>[\g<2>]', title)

        # remove internal Hyperlink style
        title = re.sub('(\[(.*?){custom-style="Hyperlink"}\])', r'\g<2>', title)

        # ignore anchors
        title = re.sub('\[\]{(#_Toc[0-9]+) .anchor}', '[\g<1> .anchor]##', title)

        # find title by using only truncated part before footnote, if footnote exists
        title_ = re.findall("(.*?)\[\^[0-9]+\]", title)
        if (len(title_) > 0):
            title = title_[0]

        # print("TITLE|"+title)

        # find the same section in adoc
        start = context["adoc"].find(title, position)
        if start >= 0:
            found_count += 1
            end = start
            for i in range(0, lines):
                end = context["adoc"].find('\n', end + 1)

            # Pandoc conversion has errors, such as missing newlines, here we try to fix them in adoc (in special sections that are dealt with here)
            fixed = re.sub(r'(?<=[A-Za-z0-9\]\)])\.(?=[A-Z])', '.\n\n', context["adoc"][start:end])
            fixed = re.sub(r'(?<=[A-Za-z0-9\]\)])(?=\*\*Conformance subject\*\*)', '.\n\n', fixed)

            print(title.replace("\n", " - ") + "(" + str(lines) + ")")

            # create admonition section in adoc
            output += context["adoc"][position:start] + '[' + admonition + ']\n====\n' + fixed + '\n====\n'
            position = end
        else:
            print("TITLE NOT FOUND: |" + title)

    output += context["adoc"][position:]

    print(style + ' ' + str(req_count) + ' ' + str(found_count))
    # print(regex)
    print('-----------------------------------------')

    context["adoc"] = output
    return context


def do_xml(old_context, caption_prefix, caption_suffix, negative=False):
    """Find each XML block with his own caption and fixes content indentation where is possible"""

    # old_context has to be immutable
    context = copy.deepcopy(old_context)

    adoc = context["adoc"]
    is_centering_active = context["docData"]["settings"]["is_centering_active"]

    if (caption_prefix and caption_suffix):
        raise Exception("Cannot enable simultaneously caption_prefix and caption suffix")

    req_count = 0
    found_count = 0
    position = 0
    output = ''
    # regex_caption = fr'(::: {{custom-style="[cC]aption.?"}}\n(?:(?!:::).)*?:::\s*)?'
    regex_caption = fr'(::: {{custom-style="[cC]aption.?"}}\n(?:(?!:::).)*?:::)?'
    # regex_caption_sure = fr'(::: {{custom-style="[cC]aption.?"}}\n(?:(?!:::).)*?:::)'
    # regex_xml = fr'(::: {{custom-style="(XML Example|XML Highlight)"}}\n(?:(?!:::).)*?:::\s*)+'
    regex_xml = fr'(::: {{custom-style="(XML Example|XML Highlight)"}}\n(?:(?!:::).)*?:::\s*)*(::: {{custom-style="(XML Example|XML Highlight)"}}\n(?:(?!:::).)*?:::)'
    regex = regex_xml

    if (caption_prefix):
        regex = regex_caption + "\s*" + regex
    if (caption_suffix):
        regex = regex + "\s*" + regex_caption

    # loop through XML sections identified with regex in md with style annotations
    for req in re.finditer(regex, context["md"], re.DOTALL):
        # print("AAA"+req.group(0)+"BBB")

        title = next(re.finditer(regex_caption, req.group(0), re.DOTALL), [''])[0]
        title = re.sub(r'::: {custom-style="[cC]aption.?"}\n((?:(?!:::).)*?)\n:::', r'\g<1>', title, 0, re.DOTALL)
        title = title.replace('***', '*|||||').replace('**', '|||||').replace('\\*', '|||||') \
            .replace(r"\'", "'").replace('\\#', '#').replace('|||||', '*') \
            .replace(r'\[', '[').replace(r'\]', ']').replace(r'\<', '<').replace(r'\>', '>').replace('--', '–') \
            .replace('__', '_').replace(r'\"', '"').replace("\\", ' +')
        title = re.sub(r'\[\]{#_Toc[0-9]+ .anchor}', '', title)

        if (not negative and not title or negative and title):
            continue

        req_count += 1

        content = next(re.finditer(regex_xml, req.group(0), re.DOTALL))[0].replace(u'\xa0', u' ')

        # if ("Conditions for access and use" in title):
        #    print("AAA"+content+"BBB")

        # remove style annotation, but persist highlight
        # req = re.sub(r':::.*\n', '', req.group(0))
        req = re.sub(r'::: {custom-style="XML Example"}\n((?:(?!:::).)*?)\n:::', r'\g<1>', content, 0, re.DOTALL)
        req = re.sub(r'::: {custom-style="XML Highlight"}\n((?:(?!:::).)*?)\n:::', r'\g<1>', req, 0, re.DOTALL)

        # if ("Conditions for access and use" in title):
        #    print("CCC"+req+"DDD")

        # find intresting lines
        clean_content = req[:]
        clean_content = clean_content.replace('***', '*|||||').replace('**', '|||||').replace('\\*', '|||||') \
            .replace(r"\'", "'").replace('\\#', '#').replace('|||||', '*') \
            .replace(r'\[', '[').replace(r'\]', ']').replace(r'\<', '<').replace(r'\>', '>').replace('--', '–') \
            .replace('__', '_').replace(r'\"', '"').replace("\\", ' +')

        # if ("Conditions for access and use" in title):
        #    print("CCC"+clean_content+"DDD")
        evids = re.findall(r'<evid>(.*?)</evid>', clean_content)
        clean_content = clean_content.replace(r'<evid>', '').replace(r'</evid>', '')

        firstline = clean_content.lstrip().splitlines()[0]
        firstline_count = clean_content.count(firstline)
        # print("FIRTLINE|"+str(firstline_count)+"|"+firstline)

        lastline = clean_content.rstrip().splitlines()[-1]
        lastline_count = clean_content.count(lastline)
        # print("LASTLINE|"+str(lastline_count)+"|"+lastline)

        # find the same XML section in adoc
        # end = adoc.find(title.replace('**', '*'), position)
        # end = adoc.find(lastline, position)+len(lastline)+1 # +1 is the next \n
        end = position
        last_endline = ''
        for line in clean_content.splitlines():
            if line:
                end_find = adoc.find(line, end)
                end = end_find + len(line) + 1 if end_find > 0 else end
                last_endline = line
        if (last_endline != lastline):
            print("LASTLINE ERROR|" + lastline)
        start = end
        for i in range(firstline_count):
            start = adoc.rfind(firstline, position, start)
        if end >= 0 and start >= 0 and end >= start:
            found_count += 1
            # start = end
            # for i in range(0, lines):
            #    start = adoc.rfind('\n', 0, start)
            # start += 1

            # fix long lines that are split, remove stars
            xml = adoc[start:end].replace(' +\n', '').replace('/*/', '|||||').replace('*', '').replace('|||||', '/*/')
            # xml = re.sub(r'(?<!/)\*(?!/)', '', xml)
            xml = xml + "\n"

            # print(len(evids))
            for evid in evids:
                # print(evid)
                xml = xml.replace(evid, '<evid>' + evid + '</evid>')

            # if ("Conditions for access and use" in title):
            #    print("XML|"+xml)
            # print("XML|"+xml)

            # prettify XML
            soup = BeautifulSoup(xml, "html.parser")
            pretty = soup.prettify(formatter=None)

            # increase indent, as it cannot be customized in BS
            indent = re.compile(r'^(\s*)', re.MULTILINE)
            pretty = re.sub(indent, r'\1\1', pretty)

            # fix first line
            pretty = re.sub(r'^(/.*)\n', r'**\1**\n\n', pretty)

            pretty = re.sub(r'[ ]*<evid>\n', '##', pretty)
            pretty = re.sub(r'\n[ ]*</evid>', '##', pretty)
            pretty = pretty + "\n" if pretty[-1] != "\n" else pretty

            if (not negative):
                print(title)
            # print(title+"|"+pretty)

            header_text = '[source,xml,subs="+quotes"]\n----\n'
            if (is_centering_active):
                header_text = '[source,xml,subs="+quotes",align=center]\n----\n'

            intercontent = adoc[position:start]

            if (title and is_centering_active):
                intercontent = ("[.text-center]\n" + title).join(intercontent.rsplit(title, 1))

            # create source section in adoc, subs="+quotes" should allow for bold formatting but does not seem to work in GitHub
            output += intercontent + header_text + pretty + '----\n'
            position = end
        else:
            print("TITLE NOT FOUND: |" + title)
            print("FIRTLINE DEBUG|" + str(firstline_count) + "|" + firstline)
            print("LASTLINE DEBUG|" + str(lastline_count) + "|" + lastline)

    output += adoc[position:]

    if (not negative):
        print('XML Example ' + str(req_count) + ' ' + str(found_count))
    else:
        print('XML without Caption ' + str(req_count) + ' ' + str(found_count))
    print('-----------------------------------------')

    # print(regex)

    context["adoc"] = output
    return context


def do_quotes(old_context):
    """Translate work IR Quotes style into corresponding adoc notation"""

    # old_context has to be immutable
    context = copy.deepcopy(old_context)

    req_count = 0
    found_count = 0
    position = 0
    output = ''
    adoc_adj = context["adoc"].replace('“', '"').replace('”', '"')
    regex = fr'(::: {{custom-style="IR quote"}}\n.*?:::\n+)+'

    # loop through quote sections identified with regex in md with style annotations
    for req in re.finditer(regex, context["md"], re.DOTALL):
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
                end = context["adoc"].find('\n', end + 1)

            print(first)

            # create blockquote section in adoc
            output += context["adoc"][position:start] + '\n____\n' + context["adoc"][start:end] + '____\n'
            position = end

    output += context["adoc"][position:]

    print('Quote ' + str(req_count) + ' ' + str(found_count))
    print('-----------------------------------------')

    context["adoc"] = output
    return context


# fix sections, TOC, misc fixes
def do_sections(old_context):
    """Many fixes on sections, relative on TOC, annex, etc... (contains also specific metadata code)"""

    # old_context has to be immutable
    context = copy.deepcopy(old_context)

    # section numbering starting from first '==' Pandoc heading
    output = context["adoc"].replace('\n== ', '\n:sectnums:\n\n== ', 1)

    output = context["adoc"].replace("\n==", "\n<<<\n==")

    # fix initial (unnumbered) section headings
    output = re.sub(r'\[(#_\S*)(.*)\]####(.*)\n', r'== \3', output)

    # insert 'Annex X' in relevant headings
    req_count = 0

    regex = '# (.+) {#.+ \.Annex}'
    # loop through quote sections identified with regex in md with style annotations
    for req in re.finditer(regex, context["md"]):
        req_count += 1
        annexName = req.group(1)
        print("* ANNEX:", annexName)
        output = output.replace('\n== ' + annexName,
                                '\n[appendix]\n== ' + annexName)

    print('Annex TOC ' + str(req_count))
    print('-----------------------------------------')

    # remove manual TOC
    output = re.sub(r'\nlink:#.*\]\n', '', output)

    # insert automatic TOC
    output = output.replace('\n== Table of Contents', '\n== Table of Contents\ntoc::[]\n')
    # sections = fr'\[(#_\S*)(.*)\]####(.*)\n'
    # for sect in re.finditer(regex, adoc):
    #    print(sect.group(3))
    #    title = sect.group(3).lower().replace(' ', '-')
    #    output = output.replace('link:' + sect.group(1), 'link:#' + title).replace('[' + sect.group(1) + sect.group(2) + ']####', '== ')

    # remove all blockquotes (unwanted, inserted by Pandoc), adjust 'NOTE' text to prevent rendering as admonition
    output = output.replace('____', '').replace('NOTE:', 'NOTE')

    # insert newline after images, change image1 to png
    output = re.sub(r'(image:.*\[.*\])(\S)', r'\1\n\2', output) \
        .replace('image:.\media/image1.wmf', 'image:.\media/image1.png')

    # document title, [discrete] hides the title from TOC
    output = output.replace(
        '*Technical Guidance for the implementation of INSPIRE dataset and service metadata based on ISO/TS 19139:2007*',
        '[discrete]\n= Technical Guidance for the implementation of INSPIRE dataset and service metadata based on ISO/TS 19139:2007')

    # remove newline
    output = output.replace('**INSPIRE**\n\n*Infrastructure for Spatial Information in Europe*',
                            '**INSPIRE**\n*Infrastructure for Spatial Information in Europe*')

    # remove other Pandoc garbage
    output = output.replace('* +\n*\n', '')

    context["adoc"] = output

    return context


def do_sections_light(old_context):
    """Minor fixes to sections"""

    # old_context has to be immutable
    context = copy.deepcopy(old_context)

    # section numbering starting from first '==' Pandoc heading
    context["adoc"] = context["adoc"].replace('\n== ', '\n:sectnums:\n\n== ', 1)

    return context


def do_cleaning(old_context):
    """Clean adoc from dirty contents"""

    # old_context has to be immutable
    context = copy.deepcopy(old_context)

    adoc_tmp = re.sub(r'== \+\+\+([a-zA-Z0-9 ]+)\+\+\+', '== \g<1>', context["adoc"])
    adoc_tmp = re.sub(r'\[#_Toc[0-9]+ .anchor\]####Example', 'Example', adoc_tmp)
    adoc_tmp = re.sub(r'\[#_Toc[0-9]+ .anchor\]####Table', 'Table', adoc_tmp)
    adoc_tmp = re.sub(r'\[#_Toc[0-9]+ .anchor\]####Figure', 'Figure', adoc_tmp)
    adoc_tmp = adoc_tmp.replace('“', '"').replace('”', '"').replace("‘", "'").replace("’", "'").replace("…", "...")\
        .replace("\n======= \n", "").replace("\n> ", "\n").replace("+", "").replace('NOTE:', 'NOTE')\
        .replace("[arabic]\n.", "[arabic, start=1]\n.")

    context["adoc"] = adoc_tmp
    return context


def do_centering(old_context):
    """Center captions and objects into adoc document"""

    # old_context has to be immutable
    context = copy.deepcopy(old_context)

    adoc_tmp = re.sub(r'(\[image,width=[0-9]+,height=[0-9]+)\]\n', r'\g<1>, align=center]\n\n[.text-center]',
                      context["adoc"])
    adoc_tmp = re.sub(r'\n(\[#_Toc[0-9]+ .anchor]####Table (?:(?!width=").)+)width="100%",cols=',
                      r'\n[.text-center]\n\g<1>align=center,width="100%",cols=', adoc_tmp, 0, re.DOTALL)
    adoc_tmp = re.sub(r'\n(Table (?:(?!width=").)+)width="100%",cols=',
                      r'\n[.text-center]\n\g<1>align=center,width="100%",cols=', adoc_tmp, 0, re.DOTALL)

    context["adoc"] = adoc_tmp
    return context


def do_styles_data(old_context):
    """Alternative method to make admonition for specific edge case"""

    # old_context has to be immutable
    context = copy.deepcopy(old_context)

    context["adoc"] = context["adoc"].replace("____\n*IR Requirement", "[IMPORTANT]\n====\n*IR Requirement") \
        .replace("____\n*TG Requirement", "[TIP]\n====\n*TG Requirement") \
        .replace("____\n*Recommendation", "[NOTE]\n====\n*Recommendation") \
        .replace("____", "====")

    return context
