'''                 Working with images
PIL stands for   PYTHON IMAGING LIBRARY
PILLOW is a Python library for processing images. It is an updated version of PIL.
PILLOW allows me to manipulate images.

                    IMAGE MANIPULATION  # 30
Convert an image to grayscale.
Convert image to another image type
Resize an image.
Rotate an image.
'''
# # Load and show on image with Pillow
# from pillow import Image

# # Load the image
# img = Image.open("Puppies/pup1.jpg")

# # Get basic details about the image
# print(img.format)
# print(img.mode)
# print(img.size)

# #  Show Image

# img.show




                    # IMAGE MANIPULATION
# Load and show on image with Pillow
from pillow import image

# Load the image
img = Image.open("Puppies/pup1.jpg") .convert('L')

# Get basic details about the image
print(img.format)
print(img.mode)
print(img.size)

#  Show Image
img.show

# save image
img.save('Puppies/pup2_gs.jpg')  #  _gs.jpg  == saves to greyscale.

