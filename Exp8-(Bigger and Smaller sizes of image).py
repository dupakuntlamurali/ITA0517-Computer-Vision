import cv2
image = cv2.imread('A1.jpg')
bigger_scale = 2.0
smaller_scale = 0.5 
bigger_image = cv2.resize(image, None, fx=bigger_scale, fy=bigger_scale, interpolation=cv2.INTER_LINEAR)
smaller_image = cv2.resize(image, None, fx=smaller_scale, fy=smaller_scale, interpolation=cv2.INTER_LINEAR)
cv2.imshow('Original Image', image)
cv2.imshow('Bigger Image', bigger_image)
cv2.imshow('Smaller Image', smaller_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
