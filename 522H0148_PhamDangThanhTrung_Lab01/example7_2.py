# Python program to explain cv2.circle() method 
	
# importing cv2 
import cv2 
	
# path 
path = r'C:\Users\admin\Downloads\hoa.png'
	
# Reading an image in default mode 
image = cv2.imread(path) 
	
# Window name in which image is displayed 
window_name = 'Image'

# Center coordinates 
center_coordinates = (120, 100) 

# Radius of circle 
radius = 30

# Red color in BGR 
color = (0, 0, 255) 

# Line thickness of -1 px 
thickness = -1

# Using cv2.circle() method 
# Draw a circle of red color of thickness -1 px 
image = cv2.circle(image, center_coordinates, radius, color, thickness) 

# Displaying the image 
cv2.imshow(window_name, image) 
cv2.waitKey(0)
cv2.destroyAllWindows()
