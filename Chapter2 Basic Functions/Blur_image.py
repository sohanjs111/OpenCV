# Import the libraries
import cv2

# Read the image
image_path = "../Photos/Schweinfurt.jpg"
im = cv2.imread(image_path)
img = cv2.resize(im, (960, 540))                    # Resize image

# Blur Image
imgBlur7 = cv2.GaussianBlur(img, (7, 7), 0)        # k size is odd number
imgBlur3 = cv2.GaussianBlur(img, (3, 3), 0)        # k size is odd number

# Display image
cv2.imshow("Without Blur Image", img)
cv2.imshow("3*3 Blur Image", imgBlur3)
cv2.imshow("7*7 Blur Image", imgBlur7)
cv2.waitKey(0)
