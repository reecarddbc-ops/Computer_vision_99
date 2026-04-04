import cv2 as cv

capture = cv.VideoCapture("dog.mp4")

while True:
    isTrue, frame = capture.read()

    if not isTrue:
        break  # stop when video ends

    cv.imshow('dog', frame)

    if cv.waitKey(20) & 0xFF == ord('d'):
        break  # press 'd' to exit

capture.release()   # frre memory and close the window
cv.destroyAllWindows()