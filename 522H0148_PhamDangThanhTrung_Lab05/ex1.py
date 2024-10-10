import cv2
import numpy as np

# Load the grayscale image
gray_img = cv2.imread(r"lena.png", 0)

# Initialize noise image with zeros
noise_img = np.zeros(gray_img.shape, dtype=np.uint8)

# Fill the image with random numbers in the range [0, 256)
cv2.randu(noise_img, 0, 256)

# Add noise to the existing image
noisy_gray = cv2.add(gray_img, np.array(0.2 * noise_img, dtype=np.uint8))

# Display the noise image
cv2.imshow("Noise", noise_img)

# Display the gray image with noise
cv2.imshow("Gray Image with Noise", noisy_gray)

# Wait for a key press and close the image windows
cv2.waitKey(0)
cv2.destroyAllWindows()
