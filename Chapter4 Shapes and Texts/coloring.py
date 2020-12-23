# Import the libraries
import cv2
import numpy as np

#  Create Plain Image
img = np.zeros((512, 512, 3), np.uint8)

# Coloring
print(img)
img[:] = 255, 0, 0                  # whole image
img[200:300, 100:300] = 0, 255, 0    # specific part

# Display image
cv2.imshow("Output", img)
cv2.waitKey(0)
