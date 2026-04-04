import cv2 as cv


def rescale(frame,scale=0.75):
    height=int(frame.shape[0] * scale) 
    width=int(frame.shape[0] * scale) 
    return cv.resize(frame,(width,height))

img = cv.imread("cat.jpg")

resized = rescale(img)

cv.imshow('img_cat',resized)
cv.waitKey(0)