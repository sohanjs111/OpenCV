# Import the libraries
import cv2


# Read the image
image_path = "../Photos/Schweinfurt.jpg"
im = cv2.imread(image_path)
img = cv2.resize(im, (960, 540))

# Extract Border
row, col = img.shape[:2]
bottom = img[row-2:row, 0:col]
mean = cv2.mean(bottom)[0]

# Define the border
border_size = 5
border = cv2.copyMakeBorder(
    img,
    top=border_size,
    bottom=border_size,
    left=border_size,
    right=border_size,
    borderType=cv2.BORDER_CONSTANT,
    value=[mean, mean, mean]
)

# Display  the images
cv2.imshow('image', img)
cv2.imshow('bottom', bottom)
cv2.imshow('border', border)
cv2.waitKey(0)
