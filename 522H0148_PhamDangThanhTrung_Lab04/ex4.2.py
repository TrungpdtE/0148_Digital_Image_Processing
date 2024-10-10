import cv2
import numpy as np

# Tai anh xam
image_path = 'input_image.jpg'  # Thay bang duong dan anh cua ban
image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

# Chuyen doi thanh anh nhi phan su dung nguong
_, binary_image = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY_INV)

# Ap dung cac phep toan hinh thai hoc de ket noi cac chu so cua moi so
kernel = np.ones((5, 5), np.uint8)  # Dieu chinh kich thuoc kernel neu can thiet
morph_image = cv2.morphologyEx(binary_image, cv2.MORPH_CLOSE, kernel)

# Tim cac duong vien trong anh nhi phan
contours, _ = cv2.findContours(morph_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Ve cac hop bao quanh moi duong vien
output_image = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)  # Chuyen doi sang BGR de ve mau
for contour in contours:
    x, y, w, h = cv2.boundingRect(contour)
    cv2.rectangle(output_image, (x, y), (x + w, y + h), (0, 255, 0), 2)

# Hien thi anh ket qua
cv2.imshow('Bounding Boxes', output_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Luu anh ket qua
cv2.imwrite('bounding_boxes.jpg', output_image)