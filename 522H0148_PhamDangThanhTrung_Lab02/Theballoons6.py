import cv2
import numpy as np

img = cv2.imread('lab02_ex.png')

#numpy array [[]]
#mask M [[]] => 0,255
#A[mask>0]=[0,255,0]
#=> dung lai mat na cau 5

#chuyen sang hsv
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

lower_yellow = np.array([20, 100, 100])
upper_yellow = np.array([30, 255, 255])

mask = cv2.inRange(hsv, lower_yellow, upper_yellow)

output_img = img.copy()

#dinh nghia xanh la
green_color = [0, 255, 0]

output_img[mask > 0] = green_color

cv2.imwrite('yellow_Cto_green.png', output_img)
cv2.imshow('Repainted Balloon', output_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
