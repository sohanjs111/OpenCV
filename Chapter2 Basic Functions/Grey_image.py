# Import the libraries
import cv2

# Read the image
im = cv2.imread("../Photos/Schweinfurt.jpg")
img = cv2.resize(im, (960, 540))                    # Resize image

# Gray Image
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Print the shape
print(imgGray.shape)

# Display image
cv2.imshow("Gray Image", imgGray)
cv2.waitKey(0)

