
import cv2
import numpy as np
img = cv2.imread("A1.jpg", cv2.IMREAD_GRAYSCALE)
kernel = np.ones((5,5), np.uint8)
opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
cv2.imshow("opening", opening)
cv2.waitKey(0)
cv2.destroyAllWindows()
