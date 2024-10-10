# Python program to explain cv2.putText() method
  
# importing cv2
import cv2
  
# path
path = r'C:\Users\admin\Downloads\hoa.png'
  
# Reading an image in default mode
image = cv2.imread(path)
  
# Window name in which image is displayed
window_name = 'hoa.png'

# text
text = 'HEHE'

# font
font = cv2.FONT_HERSHEY_SIMPLEX

# org
org = (00, 185)

# fontScale
fontScale = 1
 
# Red color in BGR
color = (0, 0, 255)

# Line thickness of 2 px
thickness = 2
 
# Using cv2.putText() method
image = cv2.putText(image, text, org, font, fontScale, 
                 color, thickness, cv2.LINE_AA, False)

# Using cv2.putText() method
image = cv2.putText(image, text, org, font, fontScale,
                  color, thickness, cv2.LINE_AA, True) 

# Displaying the image
cv2.imshow(window_name, image) 
cv2.waitKey(0)
cv2.destroyAllWindows()