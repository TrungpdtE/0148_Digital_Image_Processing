# Python program to explain cv2.ellipse() method 
	
# importing cv2 
import cv2 
	
# path 
path = r'C:\Users\admin\Downloads\hoa.png'
	
# Reading an image in default mode 
image = cv2.imread(path) 
	
# Window name in which image is displayed 
window_name = 'Image'

center_coordinates = (120, 100) 

axesLength = (100, 50) 

angle = 0

startAngle = 0

endAngle = 360

# Red color in BGR 
color = (0, 0, 255) 

# Line thickness of 5 px 
thickness = 5

# Using cv2.ellipse() method 
# Draw a ellipse with red line borders of thickness of 5 px 
image = cv2.ellipse(image, center_coordinates, axesLength, 
		angle, startAngle, endAngle, color, thickness) 

# Displaying the image 
cv2.imshow(window_name, image) 
cv2.waitKey(0)
cv2.destroyAllWindows()