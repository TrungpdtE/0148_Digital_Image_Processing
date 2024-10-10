# Python program to explain cv2.line() method 
 
# importing cv2 
import cv2 
 
# path 
path = r'C:\Users\admin\Downloads\hoa.png'
 
# Reading an image in grayscale mode
image = cv2.imread(path, 0)
 
# Window name in which image is displayed
window_name = 'Image'

# Start coordinate, here (225, 0)
# represents the top right corner of image
start_point = (225, 0)

# End coordinate, here (0, 225)
# represents the bottom left corner of image
end_point = (0, 225)

# Black color in BGR
color = (0, 0, 0)

# Line thickness of 5 px
thickness = 5

# Using cv2.line() method
# Draw a diagonal black line with thickness of 5 px
image = cv2.line(image, start_point, end_point, color, thickness)

# Displaying the image 
cv2.imshow(window_name, image) 
cv2.waitKey(0)
cv2.destroyAllWindows()