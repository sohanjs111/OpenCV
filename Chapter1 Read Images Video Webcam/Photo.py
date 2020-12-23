# Import the libraries
import cv2

# Read the image
im = cv2.imread("../Photos/Schweinfurt.jpg")

# Display image
img = cv2.resize(im, (960, 540))                    # Resize image
cv2.imshow("Output", img)
cv2.waitKey(0)
