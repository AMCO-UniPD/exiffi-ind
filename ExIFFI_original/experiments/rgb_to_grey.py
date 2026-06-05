"""
Python script to convert an image from RGB to greyscale
"""

from PIL import Image

img = Image.open("02-04-2026_11-12-13_multi_syn_data.png").convert("L")
img.save("02-04-2026_11-12-13_multi_syn_data_greyscale.png")
