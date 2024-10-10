import cv2
import numpy as np

# Buoc 1: Doc anh dau vao
input_image = cv2.imread('input_image.jpg')

# Buoc 2: Chuyen anh sang anh xam
gray_image = cv2.cvtColor(input_image, cv2.COLOR_BGR2GRAY)

# Buoc 3: Ap dung nguong de nhi phan hoa anh
_, binary_image = cv2.threshold(gray_image, 1, 255, cv2.THRESH_BINARY)

# Buoc 4: Tim duong vien trong anh
contours, _ = cv2.findContours(binary_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Buoc 5: Loc duong vien de xac dinh cac so va tach chung ra
number_images = []
for contour in contours:
    x, y, w, h = cv2.boundingRect(contour)
    if w > 10 and h > 10:  # Loc bo cac duong vien nho khong phai la so
        number_image = input_image[y:y+h, x:x+w]
        number_images.append(number_image)

# Buoc 6: Luu moi so thanh mot anh rieng biet
for idx, number_image in enumerate(number_images):
    cv2.imwrite(f'number_{idx}.png', number_image)
