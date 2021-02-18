import cv2
from predict import predict

# predicting function for image as an input
# This is currently not functioning
def image(img):
    faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    while True:
        frame = cv2.imread('pic2.jpg', cv2.IMREAD_GRAYSCALE)

        # rectangle around face
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = faceCascade.detectMultiScale(gray, 1.3, 5)
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

            # predicting
            result = predict(gray[x:x + w, y:y + h])

            font = cv2.FONT_HERSHEY_SIMPLEX

            cv2.putText(frame,
                        result,
                        (x, y),
                        font, h / 150,
                        (0, 0, 255),
                        2,
                        cv2.LINE_AA)
        cv2.imshow('Demo video', frame)
