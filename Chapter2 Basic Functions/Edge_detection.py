# Import the libraries
import cv2
import numpy as np

# Read the image
im = cv2.imread("../Photos/Schweinfurt.jpg")
img = cv2.resize(im, (960, 540))       # Resize image

# Kernel size
kernel = np.ones((3, 3), np.uint8)

# Edge Detector
imgCanny = cv2.Canny(img, 200, 220)
imgDilation = cv2.dilate(imgCanny, kernel, iterations=1)
imgEroded = cv2.erode(imgDilation, kernel, iterations=1)

# Display image
cv2.imshow("Canny Image", imgCanny)
cv2.imshow("Dilated Image", imgDilation)
cv2.imshow("Eroded Image", imgEroded)
cv2.waitKey(0)
