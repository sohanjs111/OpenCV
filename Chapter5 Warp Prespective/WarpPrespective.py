# Import the libraries
import cv2
import numpy as np

# Read the image
image_path = "../Photos/cards.jpg"
img = cv2.imread(image_path)

width, height = 250, 350
# determined the points using paint
pts1 = np.float32([[520, 25], [606, 215], [254, 148], [340, 333]])
pts2 = np.float32([[0, 0], [width, 0], [0, height], [width, height]])
matrix = cv2.getPerspectiveTransform(pts1, pts2)
imgOutput = cv2.warpPerspective(img, matrix, (width, height))

# Display image
cv2.imshow("Image", img)
cv2.imshow("Output", imgOutput)
cv2.waitKey(0)
