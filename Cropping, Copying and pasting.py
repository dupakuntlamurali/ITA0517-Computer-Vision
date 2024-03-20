import cv2
import numpy as np
image = cv2.imread('nature.jpg', cv2.IMREAD_GRAYSCALE)
if image is None:
    print("Error: Image not loaded. Check the file path.")
else:
    sobel_x = cv2.Sobel(image, cv2.CV_64F, 1, 0, ksize=3)
    sobel_y = cv2.Sobel(image, cv2.CV_64F, 0, 1, ksize=3)
    gradient_magnitude = cv2.magnitude(sobel_x, sobel_y)
    gradient_magnitude = np.uint8(gradient_magnitude)
    cv2.imshow('Boundary Image', gradient_magnitude)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
