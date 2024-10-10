import cv2
import numpy as np 

src1 = cv2.imread("lab3_img1.png")
src2 = cv2.imread("lab3_img2.png")

#must be same size
#src1.shape[-1::-1] => c,d,r but src1.shape[1::-1] => d,r 
#https://stackoverflow.com/questions/71443071/opencv-transform-image-shape-transformation-into-a-given-contour
#https://medium.com/featurepreneur/blending-images-using-opencv-bfc9ab3697b7
#src2 = cv2.resize(src2,(750,750))
src2 = cv2.resize(src2,src1.shape[1::-1])
dst = cv2.addWeighted(src1, 0.5, src2, 0.5, 0)
cv2.imwrite('BLEND_image.jpg', dst)
