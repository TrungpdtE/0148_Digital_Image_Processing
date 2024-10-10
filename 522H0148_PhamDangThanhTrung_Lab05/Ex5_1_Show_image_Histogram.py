import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the grayscale image
image = cv2.imread('ex5.jpg', cv2.IMREAD_GRAYSCALE)

# Show original histogram
plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
plt.title('Original Histogram')
plt.hist(image.ravel(), bins=256, range=[0, 256], color='gray')
plt.xlim([0, 256])

# Histogram Equalization
equalized_image = cv2.equalizeHist(image)

# Show equalized histogram
plt.subplot(1, 2, 2)
plt.title('Equalized Histogram')
plt.hist(equalized_image.ravel(), bins=256, range=[0, 256], color='gray')
plt.xlim([0, 256])

# Show images
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.title('Original Image')
plt.imshow(image, cmap='gray')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.title('Equalized Image')
plt.imshow(equalized_image, cmap='gray')
plt.axis('off')

plt.show()
