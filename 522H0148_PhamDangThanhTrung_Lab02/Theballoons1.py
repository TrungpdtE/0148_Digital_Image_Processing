import numpy as np
import cv2 as cv

img = cv.imread('lab02_ex.png')

#tach kenh mau
b, g, r = cv.split(img)

#Hien thi color channel
cv.imshow('B:', b)
cv.imshow('G:', g)
cv.imshow('R:', r)

#Tao anh ket hop tu cac kenh(gan nhu anh goc)
merged_img = cv.merge((b, g, r))
cv.imshow('Merged Image', merged_img)

cv.waitKey(0)
cv.destroyAllWindows()
