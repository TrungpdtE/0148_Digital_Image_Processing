import cv2 as cv
import numpy as np

# Chuyen doi RGB sang CMY
def rgb_to_cmy(rgb_image):
    # Chuan hoa gia tri RGB (tu khoang 0-255 sang khoang 0-1)
    rgb_image_normalized = rgb_image / 255.0
    
    # Chuyen doi CMY: C = 1 - R, M = 1 - G, Y = 1 - B
    cmy_image= 1 - rgb_image_normalized
    
    # Chuyen doi lai sang khoang 0-255
    cmy_image= (cmy_image * 255).astype(np.uint8)
    return cmy_image

# Chuyen doi CMY sang RGB
def cmy_to_rgb(cmy_image):
    # Chuan hoa gia tri CMY (tu khoang 0-255 sang khoang 0-1)
    cmy_image_normalized= cmy_image / 255.0
    
    # Chuyen doi RGB: R = 1 - C, G = 1 - M, B = 1 - Y
    rgb_image= 1 - cmy_image_normalized
    
    # Chuyen doi lai sang khoang 0-255
    rgb_image= (rgb_image * 255).astype(np.uint8)
    return rgb_image

# Mang anh RGB mau mau (ban co the tai anh su dung cv.imread thay the)
dip00_1= np.array([[[0, 0, 255], [0, 255, 0], [255, 0, 0]], 
                    [[255, 0, 0], [255, 0, 255], [0, 0, 255]]], dtype=np.uint8)

# Chuyen doi tu RGB sang CMY
cmy_image= rgb_to_cmy(dip00_1)
print("Anh CMY:\n", cmy_image)

# Chuyen doi tu CMY ve lai RGB
rgb_image_converted= cmy_to_rgb(cmy_image)
print("Anh RGB (sau khi chuyen doi):\n", rgb_image_converted)
