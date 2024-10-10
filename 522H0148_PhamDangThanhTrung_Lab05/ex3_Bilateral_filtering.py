import cv2
import numpy as np

image = cv2.imread('lena.png')
'''
Apply Bilateral Filtering
'''
# Using the function bilateralFilter() where d is diameter of each... ...pixel neighborhood that is used during filtering.

#sigmaColor is used to filter sigma in the color space.

#sigmaSpace is used to filter sigma in the coordinate space. 
bilateral_filter = cv2.bilateralFilter (src=image, d=9, sigmaColor=75, sigmaSpace=75)
cv2.imshow('Original', image) 
cv2.imshow('Bilateral Filtering', bilateral_filter)

cv2.waitKey(0)

cv2.imwrite('bilateral_filtering.jpg', bilateral_filter) 
cv2.destroyAllWindows ()