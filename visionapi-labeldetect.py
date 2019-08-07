# Reference : Google Quickstart tutorial script
import io
import os
import glob

from google.cloud import vision
from google.cloud.vision import types

# Instantiates a client
client = vision.ImageAnnotatorClient()

files = glob.glob("./img/*")

for file_name in files:
    # The name of the image file to annotate
    # file_name = os.path.join(
    #     os.path.dirname(__file__),
    #     'img/151.png')

    # Loads the image into memory
    with io.open(file_name, 'rb') as image_file:
        content = image_file.read()

    image = types.Image(content=content)


    response = client.text_detection(image=image)
    texts = response.text_annotations

    for text in texts:
        print("{}".format(text.description))