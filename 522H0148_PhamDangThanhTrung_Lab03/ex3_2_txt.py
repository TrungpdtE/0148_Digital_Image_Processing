import cv2
import numpy as np

# Đọc hình ảnh ở chế độ grayscale
src = cv2.imread("input_image.jpg", cv2.IMREAD_GRAYSCALE)

# Mở tệp văn bản để ghi
with open("ex3_2_txt.txt", "w") as file:
    # Lặp qua từng hàng của hình ảnh
    for row in src:
        # Lặp qua từng pixel trong hàng
        for pixel in row:
            # Ghi giá trị pixel vào tệp, cách nhau bởi dấu cách
            file.write(f"{pixel} ")
        # Ghi ký tự xuống dòng sau mỗi hàng
        file.write("\n")
