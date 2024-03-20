import cv2
import numpy as np
image = cv2.imread('nature.jpg')
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
laplacian = cv2.Laplacian(gray_image, cv2.CV_64F, ksize=3)
laplacian = cv2.convertScaleAbs(laplacian)
sharpened_image = cv2.addWeighted(image, 1.5, laplacian, -0.5, 0)
cv2.imshow('Sharpened Image', sharpened_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
