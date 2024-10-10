import cv2 as cv
import numpy as np

# Ham chuyen doi RGB sang CMY
def rgb_to_cmy(rgb_image):
    # Chuan hoa gia tri RGB (tu khoang 0-255 ve khoang 0-1)
    rgb_image_normalized = rgb_image / 255.0
    
    # Chuyen doi CMY: C = 1 - R, M = 1 - G, Y = 1 - B
    cmy_image = 1 - rgb_image_normalized
    
    # Chuyen ve khoang 0-255
    cmy_image = (cmy_image * 255).astype(np.uint8)
    return cmy_image

# Chuyen doi CMY sang RGB
def cmy_to_rgb(cmy_image):
    # Chuan hoa gia tri CMY (tu khoang 0-255 ve khoang 0-1)
    cmy_image_normalized = cmy_image / 255.0
    
    # Chuyen doi RGB: R = 1 - C, G = 1 - M, B = 1 - Y
    rgb_image = 1 - cmy_image_normalized
    
    # Chuyen ve khoang 0-255
    rgb_image = (rgb_image * 255).astype(np.uint8)
    return rgb_image

# Doc anh RGB tu file
img = cv.imread('lab02_ex.png')

if img is None:
    print("Khong the tai anh")
    exit()

cv.imshow('Anh RGB goc', img)

# Chuyen doi tu RGB sang CMY
cmy_image = rgb_to_cmy(img)
print("Anh CMY:\n", cmy_image)

# Chuyen doi tu CMY ve RGB
rgb_image_converted = cmy_to_rgb(cmy_image)
print("Anh RGB (sau khi chuyen doi):\n", rgb_image_converted)

# Hien thi anh CMY va RGB sau khi chuyen doi
cv.imshow('Anh CMY', cmy_image)
cv.imshow('Anh RGB (sau khi chuyen doi)', rgb_image_converted)

cv.waitKey(0)
cv.destroyAllWindows()
