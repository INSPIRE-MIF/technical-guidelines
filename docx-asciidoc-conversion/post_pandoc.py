import os,sys

from pathlib import Path

import mylib.metadata as lib_metadata
import mylib.viewservices as lib_viewservices
import mylib.viewdata as lib_viewdata

if len(sys.argv) < 5:
    error_text = "Usage: %s ADOC_FILE STYLES_FILE ATTRIBUTES_FILE TYPE"%(os.path.basename(sys.argv[0]))
    raise SystemError(error_text)

type_param = sys.argv[4]

lib = None

if type_param== "metadata":
    lib = lib_metadata
elif type_param=="services":
    lib = lib_viewservices
elif type_param=="data":
    lib = lib_viewdata
else:
    error_text = "Unreconized type parameter '" + type_param + "'. Admitted types are 'metadata', 'services', 'data'."
    raise SystemError(error_text)

print("Selected %s package library as adoc processor!"%(lib.package_name))

future_filename = Path(os.getcwd()).name + ".adoc"

print("Converting document %s"%(future_filename))

with open(sys.argv[3], 'r', encoding='utf8') as inAttributes:
    adoc = inAttributes.read()
with open(sys.argv[1], 'r', encoding='utf8') as inTarget:
    adoc += inTarget.read()
with open(sys.argv[2], 'r', encoding='utf8') as inStyles:
    md = inStyles.read()

post_adoc = lib.process(adoc, md)

with open(future_filename, 'w', encoding='utf8') as output:
    output.write(post_adoc)