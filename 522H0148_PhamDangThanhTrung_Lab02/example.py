import numpy as np
import cv2 as cv
img = cv.imread('lab02_ex.png')

# accessing only blue pixel
blue = img[100,100,0]
print( blue )

px = img[100,100]
print(px)

img[100,100] = [255,255,255]
print( img[100,100] )

# accessing RED value
img.item(10,10,2)
# modifying RED value
#img.itemset((10,10,2),100)
img.item(10,10,2)


x = np.uint8([250])
y = np.uint8([10])
print( cv.add(x,y) ) # 250+10 = 260 => 255
print( x+y ) # 250+10 = 260 % 256 = 4




print( img.shape )
print( img.size )
print( img.dtype )