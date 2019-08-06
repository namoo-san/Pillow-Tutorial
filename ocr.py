from PIL import Image
import sys
import glob

import pyocr
import pyocr.builders

# OCR

tools = pyocr.get_available_tools()
if len(tools) == 0:
    print("No OCR tool found")
    sys.exit(1)

# OCR tool
tool = tools[0]
print("OCR tool '%s'" % (tool.get_name()))

# File list
files = glob.glob("./result/*")
for file in files:
    txt = tool.image_to_string(
        Image.open(file),
        lang="jpn",
        builder=pyocr.builders.TextBuilder(tesseract_layout=3)
    )
    print (txt)
