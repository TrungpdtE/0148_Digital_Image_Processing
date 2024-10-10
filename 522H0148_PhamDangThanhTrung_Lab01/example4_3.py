import numpy as np
import cv2
# Creating a black screen image using numpy.zeros function
Img = np.zeros((512, 512, 3), dtype='uint8')
# Start coordinate, here (100, 100). It represents the top left corner of image
start_point = (100, 100)
# End coordinate, here (450, 450). It represents the bottom right corner of the image according to resolution
end_point = (450, 450)
# White color in BGR
color = (255, 250, 255)
# Line thickness of 9 px
thickness = 9
# Using cv2.line() method to draw a diagonal green line with thickness of 9 px
image = cv2.line(Img, start_point, end_point, color, thickness)
# Display the image
cv2.imshow('Drawing_Line', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
