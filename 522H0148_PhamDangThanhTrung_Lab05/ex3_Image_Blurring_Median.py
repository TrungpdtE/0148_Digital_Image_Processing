import cv2
import numpy as np

image = cv2.imread('lena.png')

'''
Apply Median blur
'''



# medianBlur() is used to apply Median blur to image

#ksize is the kernel size

median = cv2.medianBlur (src=image, ksize=5)

cv2.imshow('Original', image)

cv2.imshow('Median Blurred', median)

cv2.waitKey()

cv2.imwrite('median_blur.jpg', median)

cv2.destroyAllWindows()