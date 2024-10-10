import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the image
image = cv2.imread('ex5.jpg')

# Add Gaussian noise
def add_gaussian_noise(image):
    noise = np.random.normal(0, 25, image.shape).astype(np.uint8)
    noisy_image = cv2.add(image, noise)
    return noisy_image

# Add noise to the image
noisy_image = add_gaussian_noise(image)

# Blur the image using different techniques
# 1. Average Blurring
average_blur = cv2.blur(noisy_image, (5, 5))

# 2. Gaussian Blurring
gaussian_blur = cv2.GaussianBlur(noisy_image, (5, 5), 0)

# 3. Median Blurring
median_blur = cv2.medianBlur(noisy_image, 5)

# 4. Bilateral Filtering
bilateral_blur = cv2.bilateralFilter(noisy_image, 9, 75, 75)

# 5. Motion Blurring
kernel = np.ones((1, 5), np.float32) / 5
motion_blur = cv2.filter2D(noisy_image, -1, kernel)

# Display the results
plt.figure(figsize=(15, 10))
plt.subplot(2, 3, 1)
plt.title('Original Image')
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.axis('off')

plt.subplot(2, 3, 2)
plt.title('Noisy Image')
plt.imshow(cv2.cvtColor(noisy_image, cv2.COLOR_BGR2RGB))
plt.axis('off')

plt.subplot(2, 3, 3)
plt.title('Average Blur')
plt.imshow(cv2.cvtColor(average_blur, cv2.COLOR_BGR2RGB))
plt.axis('off')

plt.subplot(2, 3, 4)
plt.title('Gaussian Blur')
plt.imshow(cv2.cvtColor(gaussian_blur, cv2.COLOR_BGR2RGB))
plt.axis('off')

plt.subplot(2, 3, 5)
plt.title('Median Blur')
plt.imshow(cv2.cvtColor(median_blur, cv2.COLOR_BGR2RGB))
plt.axis('off')

plt.subplot(2, 3, 6)
plt.title('Bilateral Blur')
plt.imshow(cv2.cvtColor(bilateral_blur, cv2.COLOR_BGR2RGB))
plt.axis('off')

plt.tight_layout()
plt.show()
