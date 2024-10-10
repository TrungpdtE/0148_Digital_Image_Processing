import cv2 
import numpy as np 
	

# Reading an image in default mode 
Img = np.zeros((512, 512, 3), np.uint8) 
	
# Window name in which image is displayed 
window_name = 'Image'
	
# Center coordinates 
center_coordinates = (220, 150) 

# Radius of circle 
radius = 100
	
# Red color in BGR 
color = (255, 133, 233) 
	
# Line thickness of -1 px 
thickness = -1
	
# Using cv2.circle() method 
# Draw a circle of red color of thickness -1 px 
image = cv2.circle(Img, center_coordinates, radius, color, thickness) 
	
# Displaying the image 
cv2.imshow(window_name, image) 
cv2.waitKey(0) 
cv2.destroyAllWindows()
