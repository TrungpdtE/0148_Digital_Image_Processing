# Python program to explain cv2.rectangle() method 
  
# importing cv2 
import cv2 
  
# path 
path = r'C:\Users\admin\Downloads\hoa.png'
  
# Reading an image in grayscale mode
image = cv2.imread(path, 0)
  
# Window name in which image is displayed
window_name = 'Image'
 
# Start coordinate, here (100, 50)
# represents the top left corner of rectangle
start_point = (100, 50)
 
# Ending coordinate, here (125, 80)
# represents the bottom right corner of rectangle
end_point = (125, 80)
 
# Black color in BGR
color = (0, 0, 0)
 
# Line thickness of -1 px
# Thickness of -1 will fill the entire shape
thickness = -1
 
# Using cv2.rectangle() method
# Draw a rectangle of black color of thickness -1 px
image = cv2.rectangle(image, start_point, end_point, color, thickness)
 
# Displaying the image 
cv2.imshow(window_name, image) 
cv2.waitKey(0) 
cv2.destroyAllWindows()
