import cv2 as cv
import numpy as np

def desaturation_method(img):
    img= cv.imread(img)
    
    if img is None:
        print("Failed to load image")
        exit()
    
    #pp Desaturation
    gray_desaturation= ((np.max(img, axis=2) + np.min(img, axis=2)) / 2).astype('uint8')
    
    cv.imwrite('page38_Desaturation_Method.png',gray_desaturation)
    
    cv.imshow('page38_Desaturation_Method',gray_desaturation)
    cv.waitKey(0)
    cv.destroyAllWindows()


img = 'lab02_ex.png'
desaturation_method(img)
