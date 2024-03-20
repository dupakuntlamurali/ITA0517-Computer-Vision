import cv2
import numpy as np
image=cv2.imread('A1.jpg')
original_points=np.float32([[56, 65], [100,24], [28, 320], [156, 390]])
transformed_points = np.float32([[0, 0], [300, 0], [0, 300], [300, 300]])
perspective_matrix=cv2.getPerspectiveTransform(original_points,transformed_points)
perspective_image=cv2.warpPerspective(image,perspective_matrix,(400,400))
cv2.imshow('Perspective Transformed Image', perspective_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
