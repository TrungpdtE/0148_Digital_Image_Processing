import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the image
image = cv2.imread('ex5.jpg')

# 1. Sharpening using addWeighted
def sharpen_with_weighted(image, alpha=1.5, beta=-0.5):
    blurred = cv2.GaussianBlur(image, (5, 5), 0)
    sharpened = cv2.addWeighted(image, alpha, blurred, beta, 0)
    return sharpened

sharpened_weighted = sharpen_with_weighted(image)

# 2. Sharpening using filter2D
def sharpen_with_filter2D(image):
    # Sharpening kernel
    kernel = np.array([[0, -1, 0],
                       [-1, 5, -1],
                       [0, -1, 0]])
    sharpened = cv2.filter2D(image, -1, kernel)
    return sharpened

sharpened_filter2D = sharpen_with_filter2D(image)

# Display the results
plt.figure(figsize=(12, 6))
plt.subplot(1, 3, 1)
plt.title('Original Image')
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.axis('off')

plt.subplot(1, 3, 2)
plt.title('Sharpened (addWeighted)')
plt.imshow(cv2.cvtColor(sharpened_weighted, cv2.COLOR_BGR2RGB))
plt.axis('off')

plt.subplot(1, 3, 3)
plt.title('Sharpened (filter2D)')
plt.imshow(cv2.cvtColor(sharpened_filter2D, cv2.COLOR_BGR2RGB))
plt.axis('off')

plt.tight_layout()
plt.show()
