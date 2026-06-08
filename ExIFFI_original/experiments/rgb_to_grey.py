"""
Python script to convert an image from RGB to greyscale
"""

import ipdb
import os
import argparse
from PIL import Image

parser = argparse.ArgumentParser(description="RGB to greyscale converter")

parser.add_argument(
    "--image_path",
    type=str,
    default="experiments",
    help="path to the image"
)

args = parser.parse_args()

paper_image_dirpath = os.path.join(
    os.getcwd(),
    "paper_images",
    "rgb"
)

paper_gey_image_dirpath = os.path.join(
    os.getcwd(),
    "paper_images",
    "grey"
)

for image_path in os.listdir(paper_image_dirpath):

    image_name = os.path.splitext(os.path.basename((image_path)))[0]
    image_path = os.path.join(paper_image_dirpath,image_path)
    greyscale_image_path = os.path.join(paper_gey_image_dirpath,f"{image_name}_greyscale.png")

    if os.path.exists(greyscale_image_path):

        print("-"*50)
        print(f"Image {image_name} already converted in grey scale, skipping it")
        print("-"*50)

        continue

    else:

        print("-"*50)
        print(f"Processing image {image_name} at path {image_path}")
        print("-"*50)

        img = Image.open(image_path).convert("L")
        img.save(greyscale_image_path)

        print("-"*50)
        print(f"Greyscale image saved at {greyscale_image_path}")
        print("-"*50)
