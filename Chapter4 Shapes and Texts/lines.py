# Import the libraries
import cv2
import numpy as np

#  Create Plain Image
img = np.zeros((512, 512, 3), np.uint8)

# drawing a diagonals
cv2.line(img, (0, 0), (img.shape[1], img.shape[0]), (0, 255, 255), 3)       # yellow
cv2.line(img, (0, img.shape[0]), (img.shape[1], 0), (255, 0, 0), 3)         # blue

# Display image
cv2.imshow("Output", img)
cv2.waitKey(0)
