import cv2
import numpy as np
input_image = cv2.imread('A1.jpg')
gray_image = cv2.cvtColor(input_image, cv2.COLOR_BGR2GRAY)
blurred_image = cv2.GaussianBlur(gray_image, (5, 5), 0)
k = 1.5 
high_boost_filter = gray_image - blurred_image
sharpened_image = gray_image + k * high_boost_filter
sharpened_image = cv2.cvtColor(sharpened_image, cv2.COLOR_GRAY2BGR)
cv2.imshow('Sharpened Image', sharpened_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
