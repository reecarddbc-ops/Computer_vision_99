import cv2 as cv
img = cv.imread("cat.jpg")

gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)

cv.imshow('gray',gray)
cv.waitKey(0)