import cv2
import numpy as np
image = cv2.imread('A1.jpg')
original_points = np.float32([[50, 50], [200, 50], [50, 200], [200, 200]])
transformed_points = np.float32([[0, 0], [300, 0], [0, 300], [300, 300]])
homography_matrix, _ = cv2.findHomography(original_points, transformed_points)
homography_image = cv2.warpPerspective(image, homography_matrix, (image.shape[1], image.shape[0]))
cv2.imshow('Homography Transformed Image', homography_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
