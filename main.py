#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 20 13:33:18 2019

@author: hsuan
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

img = mpimg.imread('licensePlate.jpg',0) #read image
plt.imshow(img) #show image

gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY) #
plt.imshow(gray, cmap = 'gray')

ret , binary = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)
plt.imshow(binary, cmap= 'gray')

cv2.imwrite('binary.jpg', binary) #store binary image

low_threshold = 1
high_threshold = 10
kernel_size = 9 #input odd number only

blur_gray = cv2.GaussianBlur(binary, (kernel_size, kernel_size), 0)
edges = cv2.Canny(blur_gray, low_threshold, high_threshold)

plt.imshow(edges)
cv2.imwrite('edges.jpg', edges) #store edges image