import cv2
import numpy as np 

image = cv2.imread("lab3_img1.png")
mask = np.zeros(image.shape[:2], dtype="uint8")

# creating a rectangle on the mask
# where the pixels are valued at 255
cv2.circle(mask, (145, 200), 100, 255, -1)
cv2.imshow("Mask", mask)

cv2.circle(mask, (431, 179), 100, 255, -1)
cv2.imshow("Mask", mask)

cv2.circle(mask, (704, 248), 100, 255, -1)
cv2.imshow("Mask", mask)

# performing a bitwise_and with the image and the mask
masked = cv2.bitwise_and(image, image, mask=mask)
cv2.imshow("Mask applied to Image", masked)
cv2.waitKey(0)