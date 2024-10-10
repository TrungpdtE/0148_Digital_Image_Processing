import cv2 as cv
import numpy as np

def luminosity_method(img):
    img= cv.imread(img)
    
    if img is None:
        print("Failed to load image")
        exit()
    
    #pp Luminosity
    gray_luminosity= (0.299*img[:, :, 2] + 0.587 * img[:, :, 1] + 0.114 * img[:, :, 0]).astype('uint8')
    
    cv.imwrite('page38_Luminosity_Method.png', gray_luminosity)
    
    cv.imshow('page38_Luminosity_Method', gray_luminosity)
    cv.waitKey(0)
    cv.destroyAllWindows()

img = 'lab02_ex.png'
luminosity_method(img)
