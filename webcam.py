import cv2
from predict import predict

faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(1)

if not cap.isOpened():
    cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Cannot open webcam")

while True:
    ret, frame = cap.read()  # read image from video

    # rectangle around face
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(gray, 1.1, 4)
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        # predicting emotion
        result = predict(gray[x:x + w, y:y + h])

        font = cv2.FONT_HERSHEY_SIMPLEX

        cv2.putText(frame,
                    result,
                    (50, 50),
                    font, 2,
                    (0, 0, 255),
                    2,
                    cv2.LINE_AA)
    cv2.imshow('Demo video', frame)

    if cv2.waitKey(2) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()