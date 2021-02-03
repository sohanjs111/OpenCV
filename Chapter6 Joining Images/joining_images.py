# Import the libraries
import cv2
import numpy as np

# Read the image
image_path = "../Photos/view.jpg"
img = cv2.imread(image_path)

# Horizontal joining
imgHor = np.hstack((img, img))

# Vertical joining
imgVer = np.vstack((img, img))

# Display image
cv2.imshow("Horizontal", imgHor)
cv2.imshow("Vertical", imgVer)
cv2.waitKey(0)
