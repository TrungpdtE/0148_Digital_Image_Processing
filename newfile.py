import cv2
import numpy as np

frame = cv2.imread("lab02_ex.png")

#Color range HSV: https://elearning.tdtu.edu.vn/mod/url/view.php?id=370148
#Lab2. Q5. Extract the yellow balloon automatically by using HSV color space
hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
     
# Threshold of yellow in HSV space
lower_yellow = np.array([25, 50, 70])
upper_yellow = np.array([35, 255, 255])
 
# preparing the mask to overlay
mask = cv2.inRange(hsv, lower_yellow, upper_yellow)
result = cv2.bitwise_and(frame, frame, mask = mask)
cv2.imshow('Lab2 Q5 - yellow balloon', result)

#Lab2. Q6.	Re-paint the yellow balloon by replacing the pixels of yellow by green
greenBalloon = frame.copy()
greenBalloon[mask > 0] = (0, 255, 0)
cv2.imshow('Lab2 Q6 - yellow to green balloon', greenBalloon)

#greenBalloon[mask > 0] += np.array([45, 0, 0], dtype = np.uint8)
#cv2.imshow('green balloon', cv2.cvtColor(greenBalloon, cv2.COLOR_HSV2BGR))
#---------------------------------------------------------------------------------

#Lab3. Q3. Thresholding
src = cv2.imread("threshold.png", cv2.IMREAD_GRAYSCALE); 

_, dst180black = cv2.threshold(src,179, 255, cv2.THRESH_BINARY_INV)
cv2.imshow("Lab3 Q3.1a", dst180black)

_, dst = cv2.threshold(src,179, 255, cv2.THRESH_TOZERO_INV)
_, dst = cv2.threshold(dst,4, 255, cv2.THRESH_BINARY)
cv2.imshow("Lab3 Q3.1b", dst)

_, dst = cv2.threshold(src,128, 255, cv2.THRESH_TOZERO_INV)
_, dst = cv2.threshold(dst,127, 128, cv2.THRESH_BINARY)
cv2.imshow("Lab3 Q3.2", dst)
#---------------------------------------------------------------------------------

#Lab4. Q2
img = cv2.imread('threshold.png')
img_gray = cv2.imread('threshold.png',0)
ret, thresh = cv2.threshold(img_gray, 0, 255, cv2.THRESH_BINARY)

kernel = np.ones((27,27),np.uint8)
dillation = cv2.dilate(thresh, kernel,iterations = 1)

# detect the contours on the binary image using cv2.CHAIN_APPROX_NONE
contours, hierarchy = cv2.findContours(image=dillation, mode=cv2.RETR_TREE, 
							method=cv2.CHAIN_APPROX_NONE)  

# draw contours on the original image
image_copy = img.copy()
cv2.drawContours(image=image_copy, contours=contours, contourIdx=-1, 
				color=(0, 0, 255), thickness=2, lineType=cv2.LINE_AA)

for cnt in contours:
	x,y,w,h = cv2.boundingRect(cnt)
	cv2.rectangle(image_copy,(x,y),(x+w,y+h),(0,255,0),2)

cv2.imshow('Lab4. Q2 Dillation', dillation)
cv2.imshow('Lab4. Q2 Drawed contours', image_copy)

#Lab4. Q3
# img = cv2.imread('4_digits.png')
# img_gray = cv2.imread('4_digits.png',0)

# th1 = cv2.adaptiveThreshold(...)
# Invert color: black to white, white to black 
	# by	 bitwise_not(...) or use threhold(THRESH_BINARY_INV)
	
# img_lotNoise = th1[...] #Extract the region which have a lot of noise


# Opening, Closing

# contours, hierarchy  = cv2.findContours(...)
# for cnt in contours:
    # if(len(cnt) > < ...):
        # x,y,w,h = cv2.boundingRect(cnt)
        # cv2.rectangle(...)

                         

cv2.waitKey(0)
cv2.destroyAllWindows()