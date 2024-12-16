import cv2 as cv

img = cv.imread('Photos/park.jpg')

#Grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

#BLUR
blur = cv.GaussianBlur(img, (9,9), cv.BORDER_DEFAULT)
cv.imshow('Blur', blur)

#Edge Cascade
canny = cv.Canny(blur, 125, 175) #Apply more blur to remove more edges.
cv.imshow('Canny', canny)

#Dilating
dilated = cv.dilate(canny, (3,3), iterations=3)
cv.imshow('Dilated', dilated)


#Eroding
eroded = cv.erode(dilated, (3,3), iterations=1)
cv.imshow('Eroded', eroded)

#Resize
resized = cv.resize(img, (500,500), interpolation=cv.INTER_AREA) #For increasing size of image use INTER_LINEAR
cv.imshow('Resized', resized)

#Cropping 
cropped = img[50:200, 200:400]
cv.imshow('Cropped', cropped)

cv.waitKey(0)