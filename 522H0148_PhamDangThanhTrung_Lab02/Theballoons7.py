import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('lab02_ex.png')

#BGR sang RGB
image_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

#xoay
center = (image_rgb.shape[1] // 2, image_rgb.shape[0] // 2)  
angle = 20  
scale = 1 

rotation_matrix = cv2.getRotationMatrix2D(center, angle, scale)

rotated_image = cv2.warpAffine(image_rgb, rotation_matrix, (image_rgb.shape[1], image_rgb.shape[0]))

fig, axs = plt.subplots(1, 2, figsize=(10, 5))

axs[0].imshow(image_rgb)
axs[0].set_title('Original Image')

axs[1].imshow(rotated_image)
axs[1].set_title('Rotated Image (20 degrees)')

for ax in axs:
    ax.set_xticks([])
    ax.set_yticks([])

plt.tight_layout()
plt.show()
