import cv2
import numpy as np
image = cv2.imread('A1.jpg', cv2.IMREAD_GRAYSCALE)
gradient_x = cv2.Sobel(image, cv2.CV_64F, 1, 0, ksize=3)
gradient_y = cv2.Sobel(image, cv2.CV_64F, 0, 1, ksize=3)
gradient_magnitude = cv2.magnitude(gradient_x, gradient_y)
cv2.imshow('Original Image', image)
cv2.imshow('Gradient Masking', gradient_magnitude)
cv2.waitKey(0)
cv2.destroyAllWindows()
