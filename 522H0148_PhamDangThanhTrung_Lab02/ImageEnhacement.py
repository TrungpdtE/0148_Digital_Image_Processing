import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('dog.png')

if img is None:
    print("Failed to load image")
    exit()

#BGR sang RGB
image_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

#tang do sang
brightness_increased = cv2.convertScaleAbs(image_rgb, alpha=1, beta=50)

# Global histogram equalization
gray_image = cv2.cvtColor(image_rgb, cv2.COLOR_RGB2GRAY)
global_eq = cv2.equalizeHist(gray_image)

# Adaptive histogram equalization
clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
clahe_eq = clahe.apply(gray_image)

fig, axs = plt.subplots(2, 2, figsize=(10, 10))

axs[0, 0].imshow(image_rgb)
axs[0, 0].set_title('Original Image')
axs[0, 0].axis('off')

#tang do sang
axs[0, 1].imshow(brightness_increased)
axs[0, 1].set_title('Brightness Increased')
axs[0, 1].axis('off')

#global histogram equalization
axs[1, 0].imshow(global_eq, cmap='gray')
axs[1, 0].set_title('Global Histogram Equalization')
axs[1, 0].axis('off')

#adaptive histogram equalization
axs[1, 1].imshow(clahe_eq, cmap='gray')
axs[1, 1].set_title('Adaptive Histogram Equalization (CLAHE)')
axs[1, 1].axis('off')

plt.tight_layout()
plt.show()
