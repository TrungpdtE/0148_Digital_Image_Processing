# load the required packages
import cv2
import numpy as np
# load the image into system memory
image = cv2.imread('lena.png', flags=cv2.IMREAD_COLOR)
# display the image to the screen
cv2.imshow('AV CV- Winter Wonder', image)
kernel = np.array([[0, -1, 0],
[-1, 5,-1],
[0, -1, 0]])
image_sharp = cv2.filter2D(src=image, ddepth=-1, kernel=kernel)
cv2.imshow('AV CV- Winter Wonder Sharpened', image_sharp)
cv2.waitKey()
cv2.destroyAllWindows()