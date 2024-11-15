import cv2
import numpy as np

def preprocess_image(image_path):
    """
    Preprocess the input image by converting it to grayscale,
    applying Gaussian Blur, and detecting edges.
    """
    # Load the image
    img = cv2.imread(image_path)
    
    # Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    # Apply Gaussian blur to reduce noise
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    
    # Detect edges using the Canny edge detector
    edges = cv2.Canny(blurred, 50, 150, apertureSize=3)
    
    return img, edges

def detect_lines(edges_image):
    """
    Detect lines in the edge-detected image using the Hough Line Transform.
    """
    # Apply Hough Line Transform to detect lines
    lines = cv2.HoughLinesP(edges_image, 1, np.pi / 180, threshold=100, minLineLength=100, maxLineGap=10)
    
    return lines

def draw_detected_lines(image, lines):
    """
    Draw the detected lines on the original image.
    """
    img_copy = image.copy()
    
    if lines is not None:
        for line in lines:
            x1, y1, x2, y2 = line[0]
            cv2.line(img_copy, (x1, y1), (x2, y2), (0, 0, 255), 2)
    
    return img_copy

def sudoku_grabber(image_path):
    """
    Main function to grab Sudoku puzzle grid using Hough Line Transform.
    """
    # Preprocess the image
    img, edges = preprocess_image(image_path)
    
    # Detect lines in the edge-detected image
    lines = detect_lines(edges)
    
    # Draw the detected lines on the original image
    result_img = draw_detected_lines(img, lines)
    
    # Show the resulting image with the detected grid
    cv2.imshow("Detected Sudoku Grid", result_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Run the Sudoku Grabber
image_path = "sudoku-original.jpg"  # Provide the path to your Sudoku image here
sudoku_grabber(image_path)
