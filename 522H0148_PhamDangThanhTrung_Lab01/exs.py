import cv2 as cv
import numpy as np

#img = cv.imread(r'E:\Backup2023\XLA\Theory\EXERCISES\T1.png', 1)

#ret,thresh = cv.threshold(img,70,255,0)
print("\n")
#print(img)
#print("\ndtype = ", img.dtype)
#cv.imwrite( r'E:\Backup2023\XLA\Theory\EXERCISES\ex1_bw.jpg', thresh)
#cv.imwrite( r'E:\Backup2023\XLA\Theory\EXERCISES\ex1_gray.jpg', img)
#cv.imwrite( r'E:\Backup2023\XLA\Theory\EXERCISES\ex1_rgb.jpg', img)


dip00_1 = np.array([
					[ [0, 0, 255], [0, 255, 0], [255, 0, 0] ],
					[ [255, 0, 0], [255, 0, 255], [0, 0, 255] ]
				   ]
				   
				, dtype=np.uint8)

print("\n")
print(dip00_1)

cv.imwrite( r'C:\Users\Admin\Downloads\dip00_1.png', dip00_1)

##-----------------------------------------------
dip00_2 = np.array([
					[ 0, 0, 0, 0, 0 ],
					[ 0, 255, 255, 255, 0 ],
					[ 0, 255, 255, 255, 0 ],
					[ 0, 0, 0, 0, 0 ]
				   ]
				   
				, dtype=np.uint8)

print("\n")
print(dip00_2)

cv.imwrite( r'C:\Users\Admin\Downloads\dip00_2.jpg', dip00_2)

##-----------------------------------------------
dip00_5 = np.array([
					[ 0, 255, 255, 255, 0 ],
					[ 0, 190, 190, 190, 0 ],
					[ 0, 127, 127, 127, 0 ],
					[ 0, 0, 0, 0, 0 ]
				   ]
				   
				, dtype=np.uint8)

#print("\n", dip00_5)
#cv.imwrite( r'E:\Backup2023\XLA\Theory\EXERCISES\dip00_5.png', dip00_5)

##-----------------------------------------------
#b,g,r = cv.split(dip00_1)

#print("\n", b)
#print("\n", g)
#print("\n", r)

#dip00_1 = cv.cvtColor(dip00_1, cv.COLOR_BGR2CMYK )
#print("\n", dip00_1)

##-----------------------------------------------

dip03_1 = np.array([
					[ 0, 255, 255, 255, 255, 255, 55, 55, 55 ],
					[ 0, 190, 190, 190, 190, 190, 85, 85, 85 ],
					[ 0, 127, 127, 127, 127, 127, 255, 255, 255],
					[ 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
					[ 0, 190, 190, 190, 190, 190, 85, 85, 85 ],
					[ 0, 255, 255, 255, 255, 255, 55, 55, 55 ]
				   ]
				   
				, dtype=np.uint8)

# print("dip03_1=\n\n", dip03_1)
# ath = cv.adaptiveThreshold(dip03_1,255,cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY,3,2)

# print("\n ath=\n", ath)

# #kernel = np.ones((3,3),np.uint8)
# kernel = cv.getStructuringElement(cv.MORPH_CROSS,(3,3))
# erosion = cv.dilate(ath, kernel, iterations = 1)
# print("\n erosion=\n", erosion)

 

#cv.imwrite( r'E:\Backup2023\XLA\Theory\EXERCISES\dip03_1.png', dip03_1)

##-----------------------------------------------

dip05_1 = np.array([
					[ 1, 2, 3 ],
					[ 4, 5, 6 ],
					[ 8, 9, 10 ]
					
				   ]
				   
				, dtype=np.uint8)

#k51 = np.ones((3, 3), np.float32)/9
k51 = np.array(
	[
		[0, -1, 0],
		[-1, 5, -1],
		[0, -1, 0]
	]
)

print("dip05_1=\n\n", dip05_1)
print("filter=\n", cv.filter2D(src = dip05_1, ddepth=-1, kernel = k51))

#cv.imshow("dip00_1", dip00_1)
cv.waitKey(0)
