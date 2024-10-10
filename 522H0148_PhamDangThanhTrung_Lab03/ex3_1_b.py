import cv2
src=cv2.imread("threshold.png",cv2.IMREAD_GRAYSCALE)

thresh=180
maxValue=0
dst=src.copy()
#th,dst=cv2.threshold(src, thresh,maxValue, cv2.THRESH_BINARY)
#co cach khac dung for
#cv2.imwrite("opencv-threshold-example.jpg", dst); 

height = src.shape[0]
weight = src.shape[1]

for i in range(0,height):
    for j in range(0,weight):
        if src[i,j] < thresh:
            dst[i,j]=maxValue
        else:
            dst[i,j]=255
cv2.imwrite("ex3_2_b.jpg", dst); 