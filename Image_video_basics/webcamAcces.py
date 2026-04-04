import cv2 as cv

cam = cv.VideoCapture(0)

while True:
    istrue,frame=cam.read()

    if not istrue:
        break

    cv.imshow('cam',frame)

    if cv.waitKey(20) & 0xFF == ord('d'):
        break


cam.release()
cv.destroyAllWindows()