import cv2
image = cv2.imread('nature.jpg')
if image is not None:
    blurred_image = cv2.GaussianBlur(image, (5, 5), 0)
    cv2.imshow('Blurred Image', blurred_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print('Failed to load the image.')
