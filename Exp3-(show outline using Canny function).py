import cv2
import numpy as np
image = cv2.imread('A1.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
gray_blurred = cv2.GaussianBlur(gray, (5, 5), 0)
edges = cv2.Canny(gray_blurred, threshold1=30, threshold2=100)
cv2.imshow('Original Image', image)
cv2.imshow('Edges', edges)
cv2.waitKey(0)
cv2.destroyAllWindows()
 
