"""                  Working with Images in Python
                            What is Pul?
PIL stands for Python Imaging Library
PIL allows me to manipulate images.
PILLOW is a Python library for proccessing images. It is an update version of PIL.

                    INSTALLING PILLOW
Best to install Pillow inside a virtual environment.
See lesson 103 for details.

                    Loading Images & Details
Get information about image format.
Get information about image mode.
Get information about image size.
Display Image




"""
# Load and show an image with Pillow
from PIL import Image

# Load the image.
img = Image.open(Puppies/pup1.jpg)

# Get basic details about the image
print("img.format")
print("img.mode")
print("img.size")


