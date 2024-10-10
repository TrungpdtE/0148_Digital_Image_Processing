import numpy as np
import cv2 as cv

image = cv.imread('lab02_ex.png')
output = image.copy()

#Chuyen doi anh sang khong gian mau HSV
hsv = cv.cvtColor(image, cv.COLOR_BGR2HSV)


colors = {
    "Red": [(0, 100, 100), (10, 255, 255)],
    "Green": [(40, 100, 100), (80, 255, 255)],
    "Blue": [(100, 100, 100), (140, 255, 255)], 
    "Yellow": [(20, 100, 100), (30, 255, 255)] 
}

#Duyet qua tung mau de phat hien bong
for color_name, (lower, upper) in colors.items():
    mask = cv.inRange(hsv, np.array(lower), np.array(upper))
    
    contours, _ = cv.findContours(mask, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)

    for contour in contours:
        x, y, w, h = cv.boundingRect(contour)
        
        cv.rectangle(output, (x, y), (x + w, y + h), (255, 0, 0), 2)
        

cv.imshow('OUTPUT', output)
cv.waitKey(0)
cv.destroyAllWindows()
