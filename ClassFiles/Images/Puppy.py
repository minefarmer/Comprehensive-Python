'''                 Working with images
PIL stands for   PYTHON IMAGING LIBRARY
PILLOW is a Python library for processing images. It is an updated version of PIL.
PILLOW allows me to manipulate images.





'''
# Load and show on image with Pillow
from PIL import Image

# Load the image
img = Image.open("Puppies/pup1jpg")

# Get basic details about the image
print(img.format)
print(img.mode)
print(img.size)

#  Show Image

img.show
