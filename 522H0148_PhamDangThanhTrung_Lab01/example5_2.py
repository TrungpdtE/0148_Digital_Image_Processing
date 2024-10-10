# Python program to explain cv2.arrowedLine() method 

# importing cv2 
import cv2 

# path 
path = r'C:\Users\admin\Downloads\hoa.png'

# Reading an image in default mode 
image = cv2.imread(path) 

# Window name in which image is displayed 
window_name = 'Image'

# Start coordinate, here (225, 0) 
# represents the top right corner of image 
start_point = (225, 0) 

# End coordinate 
end_point = (0, 90) 

# Red color in BGR 
color = (0, 0, 255) 

# Line thickness of 9 px 
thickness = 9

# Using cv2.arrowedLine() method 
# Draw a red arrow line 
# with thickness of 9 px and tipLength = 0.5 
image = cv2.arrowedLine(image, start_point, end_point, 
					color, thickness, tipLength = 0.5) 

# Displaying the image 
cv2.imshow(window_name, image) 
cv2.waitKey(0)
cv2.destroyAllWindows()