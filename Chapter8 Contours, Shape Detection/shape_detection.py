import cv2
import numpy as np

# def the image path
path = '../Photos/shapes.png'

# Stacking Images
def stackImages(scale,imgArray):
    rows = len(imgArray)
    cols = len(imgArray[0])
    rowsAvailable = isinstance(imgArray[0], list)
    width = imgArray[0][0].shape[1]
    height = imgArray[0][0].shape[0]
    if rowsAvailable:
        for x in range(0, rows):
            for y in range(0, cols):
                if imgArray[x][y].shape[:2] == imgArray[0][0].shape[:2]:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (0, 0), None, scale, scale)
                else:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (imgArray[0][0].shape[1], imgArray[0][0].shape[0]), None, scale, scale)
                if len(imgArray[x][y].shape) == 2: imgArray[x][y]= cv2.cvtColor( imgArray[x][y], cv2.COLOR_GRAY2BGR)
        imageBlank = np.zeros((height, width, 3), np.uint8)
        hor = [imageBlank]*rows
        hor_con = [imageBlank]*rows
        for x in range(0, rows):
            hor[x] = np.hstack(imgArray[x])
        ver = np.vstack(hor)
    else:
        for x in range(0, rows):
            if imgArray[x].shape[:2] == imgArray[0].shape[:2]:
                imgArray[x] = cv2.resize(imgArray[x], (0, 0), None, scale, scale)
            else:
                imgArray[x] = cv2.resize(imgArray[x], (imgArray[0].shape[1], imgArray[0].shape[0]), None,scale, scale)
            if len(imgArray[x].shape) == 2: imgArray[x] = cv2.cvtColor(imgArray[x], cv2.COLOR_GRAY2BGR)
        hor= np.hstack(imgArray)
        ver = hor
    return ver


# Define getContour function
def getContours(img):
    contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    for cnt in contours:
        # area of each contours
        area = cv2.contourArea(cnt)
        print(area)
        cv2.drawContours(imgBlank, cnt, -1, (255, 0, 0), 4)
        if area > 500:
            cv2.drawContours(imgContour, cnt, -1, (255, 0, 0), 3)
            # finding the Contour Perimeter
            peri = cv2.arcLength(cnt, True)
            print(peri)
            # finding the Contour Approximation
            approx = cv2.approxPolyDP(cnt, 0.02 * peri, True)
            print(len(approx))
            # object Corners
            obj_cor = len(approx)
            x, y, w, h = cv2.boundingRect(approx)
            if obj_cor == 3:
                object_type = "Tri"
            elif obj_cor == 4:
                asp_ratio = w / float(h)
                if asp_ratio > 0.98 and asp_ratio < 1.03:
                    object_type = "Square"
                else:
                    object_type = "Rectangle"
            elif obj_cor > 4:
                object_type = "Circles"
            else:
                object_type = "None"

            cv2.rectangle(imgContour, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv2.putText(imgContour, object_type,
                        (x + (w // 2) - 10, y + (h // 2) + 20), cv2.FONT_HERSHEY_COMPLEX, 0.7,(0, 0, 0), 2)

# Read the image
img = cv2.imread(path)

# copy the original image
imgContour = img.copy()

# Create a White blank image
imgBlank = np.zeros((img.shape[1], img.shape[0], 3), np.uint8)
imgBlank[:] = 255, 255, 255

# Grayscale image
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# Blur the gray image
imgBlur = cv2.GaussianBlur(imgGray, (7, 7), 1)
# Canny the blur image
imgCanny = cv2.Canny(imgBlur, 50, 50)
# Call getContour function for canny image
getContours(imgCanny)

# Stack the image
imgStack = stackImages(0.65, ([img, imgGray, imgBlur], [imgCanny, imgBlank, imgContour]))

# Display the Stacked Image
cv2.imshow("Stack", imgStack)
cv2.waitKey(0)