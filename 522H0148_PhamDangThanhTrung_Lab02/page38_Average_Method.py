import cv2 as cv
import numpy as np

def average_method(img):
    img= cv.imread(img)
    
    if img is None:
        print("Failed to load image")
        exit()
    
    #pp Average
    gray_avg= np.mean(img,axis=2).astype('uint8')
    
    cv.imwrite('page38_Average_Method.png',gray_avg)
    
    cv.imshow('page38_Average_Method',gray_avg)
    cv.waitKey(0)
    cv.destroyAllWindows()

img = 'lab02_ex.png'
average_method(img)
