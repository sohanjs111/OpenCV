# Import the libraries
import cv2
import numpy as np

#  Create Plain Image
img = np.zeros((512, 512, 3), np.uint8)

# Insert Text
cv2.putText(img, "OpenCV", (int(img.shape[1]*0.125), (int(img.shape[0]*0.5))),
            cv2.FONT_HERSHEY_SIMPLEX, 3, (0, 0, 255), 2)

# Display image
cv2.imshow("Output", img)
cv2.waitKey(0)
