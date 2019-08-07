
from PIL import Image, ImageFilter, ImageDraw, ImageFont, ImageOps
import sys
import glob
import pyocr
import pyocr.builders

tools = pyocr.get_available_tools()

def main ():
    lists = glob.glob("./img/*", recursive=True)
    for cv_img in lists:
        print(cv_img)
        filename = cv_img.replace('img', 'result')
        print(filename + " convert to grayscale...")
        img = Image.open(cv_img)
        grayscale = img.convert('L')
        twocolor = grayscale.point(lambda x: 0 if x < 230 else x)
        savefile = twocolor.save(filename)
        savefile
        print (filename + " convert successful.")

    tool = tools[0]

    lists = glob.glob("./result/*")
    for file in lists:
        result = tool.image_to_string(
            Image.open(file),
            lang="jpn",
            builder=pyocr.builders.TextBuilder(tesseract_layout=3)
        )
        print (result.replace(' ',''))

if __name__ == "__main__" :
    main()