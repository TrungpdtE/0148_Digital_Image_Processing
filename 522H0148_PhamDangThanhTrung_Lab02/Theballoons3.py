import numpy as np
import cv2 as cv

# Đọc ảnh
image = cv.imread('lab02_ex.png')
output = image.copy()

# Chuyển đổi ảnh sang không gian màu HSV
hsv = cv.cvtColor(image, cv.COLOR_BGR2HSV)

# Định nghĩa các khoảng màu cho từng quả bóng
colors = {
    "Red": [(0, 100, 100), (10, 255, 255)],
    "Green": [(40, 100, 100), (80, 255, 255)],
    "Blue": [(100, 100, 100), (140, 255, 255)],
    "Yellow": [(20, 100, 100), (30, 255, 255)],
    "Purple": [(130, 100, 100), (160, 255, 255)]
}

# Duyệt qua từng màu để phát hiện quả bóng
for color_name, (lower, upper) in colors.items():
    # Tạo mặt nạ cho màu
    mask = cv.inRange(hsv, np.array(lower), np.array(upper))
    
    # Tìm các đường viền trong mặt nạ
    contours, _ = cv.findContours(mask, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)

    for contour in contours:
        # Tính toán hình chữ nhật bao quanh
        x, y, w, h = cv.boundingRect(contour)
        
        # Vẽ hình chữ nhật bao quanh quả bóng
        cv.rectangle(output, (x, y), (x + w, y + h), (255, 0, 0), 2)
        
        # Thêm tên màu ở phía trên hình chữ nhật
        cv.putText(output, color_name, (x, y - 10), 
                    cv.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2, cv.LINE_AA)

# Hiển thị ảnh kết quả
cv.imshow('Detected Balloons', output)
cv.waitKey(0)
cv.destroyAllWindows()
