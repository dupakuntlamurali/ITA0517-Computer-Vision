import cv2
video_capture = cv2.VideoCapture('vc.mp4')
if not video_capture.isOpened():
    print("Error: Couldn't open the video file")
    exit()
while True:
    ret, frame = video_capture.read()
    if not ret:
        break
    cv2.imshow('Slow Motion Video', frame)
    if cv2.waitKey(50) & 0xFF == 27:
        break
    cv2.imshow('Fast Motion Video', frame)
    if cv2.waitKey(25) & 0xFF == 27: 
        break

video_capture.release()
cv2.destroyAllWindows()
