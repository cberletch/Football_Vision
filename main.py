import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread("images\QBView1.png")

RGB_img = cv.cvtColor(img, cv.COLOR_BGR2RGB)

plt.imshow(RGB_img)

plt.waitforbuttonpress()
plt.close('all')