from PIL import Image, ImageFilter, ImageDraw, ImageFont
import sys
import glob
import pyocr
import pyocr.builders

# tools = pyocr.get_avilable_tools()

def init ():
    if len(tools) == 0:
        print("OCR tool not found.")
        sys.exit(1)

def convert ():
    lists = glob.glob("./img/*", recursive=True)
    for cv_img in lists:
        print(cv_img)
        img = Image.open(cv_img)
        img.convert('L').save('test.png'),

def ocr ():
    init

    tool = tools[0]
    print("OCR is '%s'" % (tools.get_name()))

    lists = glob.glob("./result/*")
    for file in lists:
        result = tool.image_to_string(
            Image.open(file),
            lang="jpn",
            builder=pyocr.builders.TextBuilder(tesseract_layout=3)
        )
        print (result)


if __name__ == "__main__" :
    convert()