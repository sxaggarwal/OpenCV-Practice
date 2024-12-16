import cv2 as cv 
import numpy as np


img = cv.imread('Photos/cats.jpg')
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Cats', gray)

blank = np.zeros(img.shape, dtype='uint8')
cv.imshow('Blank', blank)

blur = cv.GaussianBlur(gray, (5,5) , cv.BORDER_DEFAULT)
cv.imshow('Blur', blur)

# canny = cv.Canny(blur, 125, 175)
# cv.imshow('Canny Edges', canny)

ret, thresh  = cv.threshold(gray,125,255, cv.THRESH_BINARY) 

contours, heirarchies = cv.findContours(thresh, cv.RETR_LIST, cv.CHAIN_APPROX_NONE)


cv.drawContours(blank, contours, -1, (0,0,255), 1)
cv.imshow('Contour Drawn', blank)
print(len(contours))
cv.waitKey(0)

#Use canny and then contour is preferrable 