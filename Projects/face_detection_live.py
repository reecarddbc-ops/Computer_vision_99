import cv2 as cv

face_capture=cv.CascadeClassifier("C:/Users/REECARD/AppData/Local/Python/pythoncore-3.14-64/Lib/site-packages/cv2/data/haarcascade_frontalface_default.xml")
cam = cv.VideoCapture(0)

while True:
    isture,video=cam.read()
    col = cv.cvtColor(video, cv.COLOR_BGR2GRAY)
    faces = face_capture.detectMultiScale(
        col,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30,30),
        flags=cv.CASCADE_SCALE_IMAGE
    )

    for(x,y,w,h) in faces:
        cv.rectangle(video,(x,y),(x+w,y+h),(0,255,0),2)


    cv.imshow('face_detect',video)

    if cv.waitKey(10) == ord('a'):
        break

cam.release()
cv.destroyAllWindows()





