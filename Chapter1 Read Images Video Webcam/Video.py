# Import the libraries
import cv2

# Read the video
cap = cv2.VideoCapture("../Photos/outside.mp4")

# Display video
while True:
    success, img = cap.read()
    cv2.imshow("Video", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

