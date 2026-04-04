import numpy as np
import cv2 as cv


blank = np.zeros((500,500,3),dtype='uint8') # 500 height,500 width,3 color channels BGR
cv.rectangle(blank,(50,50),(200,200),(0,255,0),thickness=2)# image to draw on ,top lft coner,bootom right conr,color,border thikness
cv.circle(blank,(250,250),50,(255,0,0), thickness=-1) #img,center,radius,color,thickness

cv.imshow('shapes',blank)
cv.waitKey(0)





