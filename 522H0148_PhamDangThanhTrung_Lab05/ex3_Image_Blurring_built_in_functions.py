import cv2
import numpy as np

image = cv2.imread('lena.png')

'''
Apply blur using 'blur() function
'''
img_blur = cv2.blur(src=image, ksize=(5,5)) 
#image where ksize is the kernel size

# Display using cv2.imshow() 

cv2.imshow('Original', image) 
cv2.imshow('Blurred', img_blur)

cv2.waitKey()

cv2.imwrite('blur.jpg', img_blur)

cv2.destroyAllWindows()