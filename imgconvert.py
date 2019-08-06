from PIL import Image, ImageFilter, ImageDraw, ImageFont
import sys
import glob
import pyocr
import pyocr.builders

# Image files convert to grayscale

def convert ():
    lists = glob.glob("./img/*", recursive=True)
    for cv_img in lists:
        print(cv_img)
        filename = cv_img.replace('img', 'result')
        print(filename)
        img = Image.open(cv_img)
        img.convert('L').save(filename),

if __name__ == "__main__" :
    convert()