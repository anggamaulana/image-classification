import skimage.io as io
from skimage import data_dir
from skimage.color import rgb2gray

import numpy as np


x=np.array([1,2,3],ndmin=3)

ic = io.ImageCollection('class1/*jpg')
gray_image = rgb2gray(ic[0])
print gray_image.shape

x=np.append(x,gray_image)
print x

# print ic.shape
print ic[0].shape