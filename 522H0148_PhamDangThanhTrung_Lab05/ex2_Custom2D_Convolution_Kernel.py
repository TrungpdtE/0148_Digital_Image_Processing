import cv2
import numpy as np

image = cv2.imread('lena.png')
'''
Apply blurring kernel
'''
kernel2 = np.ones((5, 5), np.float32) / 25

img = cv2.filter2D(src=image, ddepth=-1, kernel=kernel2)

cv2.imshow('Original', image) 
cv2.imshow('Kernel Blur', img)

cv2.waitKey() 
cv2.imwrite('blur_kernel.jpg', img)

cv2.destroyAllWindows()