# Python program to explain cv2.imwrite() method

# importing cv2 
import cv2

# importing os module  
import os

# Image path
image_path = r'C:\Users\admin\Downloads\hoa.png'

# Image directory
directory = r'C:\Users\admin\Downloads'

# Using cv2.imread() method
# to read the image
img = cv2.imread(image_path)

# Change the current directory 
# to specified directory 

os.chdir(directory)

# List files and directories  
# in 'C:/Users/Rajnish/Desktop/GeeksforGeeks'  
print("Before saving image:")  
print(os.listdir(directory))  

# Filename
filename = 'savedImage.jpg'

# Using cv2.imwrite() method
# Saving the image
cv2.imwrite(filename, img)

# List files and directories  
# in 'C:/Users / Rajnish / Desktop / GeeksforGeeks'  
print("After saving image:")  
print(os.listdir(directory))

print('Successfully saved')