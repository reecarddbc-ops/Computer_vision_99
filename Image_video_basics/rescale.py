import cv2 as cv 

pic = cv.imread("cat_large.jpg")


cv.imshow('cat',pic)
cv.waitKey(0)


def rescaleFrame(frame,scale=0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)


    dimensions = (width,height)
    return cv.resize(frame,dimensions,interpolation=cv.INTER_AREA)


capture = cv.VideoCapture("dog.mp4")

while True:
    isTrue, frame = capture.read()

    frame_resized=rescaleFrame(frame)

    if not isTrue:
        break  # stop when video ends

    cv.imshow('dog', frame)
    cv.imshow('dog-resized',frame_resized)

    if cv.waitKey(20) & 0xFF == ord('d'):
        break  # press 'd' to exit

capture.release()   # frre memory and close the window
cv.destroyAllWindows()


cv.waitKey(0)