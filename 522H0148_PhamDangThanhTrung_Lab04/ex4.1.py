import cv2
import numpy as np
from matplotlib import pyplot as plt

# Tai anh xam
image_path = '4_sudoku.png'  # Thay bang duong dan anh cua ban
image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

# Nguong don gian
_, simple_thresh = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)

# Nguong thich nghi
adaptive_thresh = cv2.adaptiveThreshold(image, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                        cv2.THRESH_BINARY, 11, 2)

# Nguong Otsu
_, otsu_thresh = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

# Hien thi cac anh
titles = ['Anh goc', 'Nguong don gian', 'Nguong thich nghi', 'Nguong Otsu']
images = [image, simple_thresh, adaptive_thresh, otsu_thresh]

for i in range(4):
    plt.subplot(2, 2, i + 1)
    plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()

# Luu cac anh da nhi phan hoa
cv2.imwrite('simple_threshold.jpg', simple_thresh)
cv2.imwrite('adaptive_threshold.jpg', adaptive_thresh)
cv2.imwrite('otsu_threshold.jpg', otsu_thresh)