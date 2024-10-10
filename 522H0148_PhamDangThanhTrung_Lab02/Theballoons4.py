import cv2 as cv
import numpy as np

img = cv.imread('lab02_ex.png')

#chuyen doi sang khong gian mau HSV
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)

#dinh nghia nguong mau( co the chinh lai duoc)
lower_yellow = np.array([20, 100, 100])
upper_yellow = np.array([30, 255, 255])

# tao mask cho mau vang
mask = cv.inRange(hsv, lower_yellow, upper_yellow)

#lay vung bong tu anh goc
yellow_balloon = cv.bitwise_and(img, img, mask=mask)

cv.imwrite('yellow_balloon.png', yellow_balloon)
cv.imshow('Yellow Balloon', yellow_balloon)
cv.waitKey(0)
cv.destroyAllWindows()
