## Generate rotated samples of images
# Arun Aniyan, Kshitij Thorat
# Multispectral analysis project
# SKA SA/ RATT
# arun@ska.ac.za
# 02-05-2016

import sys
import os
import numpy as np
from scipy.misc import imsave,imread
from scipy import ndimage

#Load input image
arg = sys.argv

fname = arg[1]

step = int(float(arg[2]))

out = arg[3]
# Filename without extension
name = os.path.splitext(fname)[0]
base = os.path.basename(name)

print(fname)

# Center Crop Image
def cut_rot(image,new_width):
    new_img = image.copy()
    new_height = new_width
    width = image.shape[0]
    height = image.shape[1]
    left = int((width - new_width)/2.0)
    top = int((height - new_height)/2.0)
    right = int((width + new_width)/2.0)
    bottom = int((height + new_height)/2.0)
    new_img = new_img[left:right,top:bottom]
    return new_img

# Load Image
image_data = imread(fname)

# Make a copy
img = np.copy(image_data)


# Generate rotated versions
for i in range(0,359,step):
    rot = ndimage.rotate(img,i, reshape=False)
    fname1 = os.path.join(out,base) +'-'+str(i)+'.png'
    rot = cut_rot(rot, 256)
    imsave(fname1,rot)

