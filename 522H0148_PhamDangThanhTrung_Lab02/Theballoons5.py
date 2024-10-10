import cv2
import numpy as np

img = cv2.imread('lab02_ex.png')

#chuyen sang hsv
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

#dinh nghia mau
lower_yellow = np.array([20, 100, 100])
upper_yellow = np.array([30, 255, 255])

mask = cv2.inRange(hsv, lower_yellow, upper_yellow)

result = cv2.bitwise_and(img, img, mask=mask)

cv2.imshow('Original Image', img)
cv2.imshow('Mask', mask)
cv2.imshow('Result', result)

cv2.waitKey(0)
cv2.destroyAllWindows()
