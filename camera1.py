import cv2
cap = cv2.VideoCapture('rtsp://admin:brandon@1@192.168.1.108/0')

while True:
	ret, frame = cap.read()
	cv2.imshow('frame',frame)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break
cap.release()
cv2.destroyAllWindows()
