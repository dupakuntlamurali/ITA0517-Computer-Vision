 import cv2

image = cv2.imread('cv1.jpg')

if image is not None:
    grayscale_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    cv2.imwrite('grayscale_  image.jpg', grayscale_image)

    cv2.imshow('Grayscale Image', grayscale_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print('Failed to load the image.')
