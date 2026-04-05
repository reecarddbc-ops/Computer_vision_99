import cv2 as cv
import numpy as np # used to handle arrays (labels, image data)

# 🔹 Load Haar Cascade
face_cascade = cv.CascadeClassifier(
    cv.data.haarcascades + 'haarcascade_frontalface_default.xml'
)

# 🔹 Step 1: Load your image
img = cv.imread('myface.jpeg')

if img is None:
    print("Image not found ❌")
    exit()
else:
    print("Image loaded ✅")

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY) # Face detection works better on single channel

# 🔹 Step 2: Detect face in image
faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=3) #scaleFactor=Helps detect different face sizes

print("Faces detected:", len(faces)) #Print number of faces

features = [] #will store face images
labels = [] #will store IDs

# 🔹 Step 3: Extract face
for (x, y, w, h) in faces:
    face_roi = gray[y:y+h, x:x+w]
    features.append(face_roi)
    labels.append(0)   # only one person

# 🔹 Safety check
if len(features) == 0:
    print("No face found in image ❌")
    exit()

labels = np.array(labels)

# 🔹 Step 4: Train model
model = cv.face.LBPHFaceRecognizer_create()
model.train(features, labels)

print("Model trained ✅")

# 🔹 Step 5: Start webcam
cap = cv.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, 1.1, 4)

    for (x, y, w, h) in faces:
        face_roi = gray[y:y+h, x:x+w]

        label, confidence = model.predict(face_roi)

        # 🔹 Recognition logic
        if confidence < 70:
            text = "YOU"
        else:
            text = "Unknown"

        # 🔹 Display result
        cv.putText(frame, f'{text} ({int(confidence)})',
                   (x, y-10), cv.FONT_HERSHEY_SIMPLEX,
                   1, (0,255,0), 2)

        cv.rectangle(frame, (x,y), (x+w,y+h), (0,255,0), 2)

    cv.imshow("Face Recognition", frame)

    if cv.waitKey(10) == ord('q'):
        break

cap.release()
cv.destroyAllWindows()