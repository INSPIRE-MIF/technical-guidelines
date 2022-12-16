from .common import *

package_name = "view_services"

# docData init skeleton with default configuration
docData = {
    "default": {
        "execution": {},
        "settings": {}
    }
}

# execution order of elements in process, comment to exclude an element from execution
docData["default"]["execution"]["execution_order"] = [
    "cleaning",
    "centering",
    # "sections",
    "sections_light",
    "styles",
    "styles_data",
    "xml_block",
    # "quotes",
]

# verify if centering is active in process. Useful for in-method specific optimizations
docData["default"]["settings"]["is_centering_active"] = \
    "centering" in docData["default"]["execution"]["execution_order"]

# doStyles list of elements to convert
docData["default"]["settings"]["doStiles"] = [
    ['Requirement', r'\*\*Implementation Requirement', '__', 'IMPORTANT'],
    ['Recommendation', r'\*\*Implementation Recommendation', '__', 'TIP']
]

# xml translation settings
docData["default"]["settings"]["xml_block"] = {
    "xml_caption_has_prefix": True,
    "xml_caption_has_suffix": False
}

# select default configuration
myDocData = docData["default"]


def process(adoc, md):
    """Execute conversion process from adoc and md to processed adoc, using context and pure functions"""
    context = {
        "adoc": adoc,
        "md": md,
        "docData": myDocData
    }

    for task in docData["default"]["execution"]["execution_order"]:
        print("-----------------------------------------\nCurrent task: " + task)
        if task == "cleaning":
            context = do_cleaning(context)
        elif task == "centering":
            context = do_centering(context)
        elif task == "sections":
            context = do_sections(context)
        elif task == "sections_light":
            context = do_sections_light(context)
        elif task == "styles":
            for styles in myDocData["settings"]["doStiles"]:
                context = do_styles(context, styles[0], styles[1], styles[2], styles[3], 1)
        elif task == "styles_data":
            context = do_styles_data(context)
        elif task == "xml_block":
            context = do_xml(context, myDocData["settings"]["xml_block"]["xml_caption_has_prefix"],
                             myDocData["settings"]["xml_block"]["xml_caption_has_suffix"])
            context = do_xml(context, myDocData["settings"]["xml_block"]["xml_caption_has_prefix"],
                             myDocData["settings"]["xml_block"]["xml_caption_has_suffix"], True)
        elif task == "quotes":
            context = do_quotes(context)

    return context["adoc"]
