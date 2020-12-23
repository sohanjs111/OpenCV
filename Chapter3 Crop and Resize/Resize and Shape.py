# Import the libraries
import cv2

# Read the image
image_path = "../Photos/view.jpg"
img = cv2.imread(image_path)
print(img.shape)                                # (height, width, channel)

# Resize
imgResize = cv2.resize(img, (800, 530))         # (width, height)
print(imgResize.shape)

# Cropping
imgCropped = imgResize[120:400, 350:620]        # (height, width)

# Display image
cv2.imshow("Image", img)
cv2.imshow("Image Resize", imgResize)
cv2.imshow("Image Cropped", imgCropped)
cv2.waitKey(0)
