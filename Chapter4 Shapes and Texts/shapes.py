# Import the libraries
import cv2
import numpy as np

#  Create Plain Image
img = np.zeros((512, 512, 3), np.uint8)

# drawing a rectangle
cv2.rectangle(img, (int(img.shape[1]*0.125), int((img.shape[0])*0.125)), (int((img.shape[1])*0.875), int((img.shape[0])*0.875)), (0, 255, 0), 2)
# rectangle filled color
cv2.rectangle(img, (int(img.shape[1]*0.25), int((img.shape[0])*0.25)), (int((img.shape[1])*0.75), int((img.shape[0])*0.75)), (0, 255, 255), cv2.FILLED)

# drawing a circle
cv2.circle(img, (int(img.shape[1]*0.5), int((img.shape[0])*0.5)), int((img.shape[0])*0.25), (0, 0, 255), 2)

# Display image
cv2.imshow("Output", img)
cv2.waitKey(0)
