import cv2 as cv

img = cv.imread("cat.jpg")

edges=cv.Canny(img,100,200)
cv.imshow('border',edges)
cv.waitKey(0)