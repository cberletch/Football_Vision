import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
from skimage.filters import threshold_local
import imutils 
from skimage import measure
import tensorflow as tf

img = cv.imread("images\QBView1.png")

RGB_img = cv.cvtColor(img, cv.COLOR_BGR2RGB)

plt.imshow(RGB_img)

plt.waitforbuttonpress()
plt.close('all')


