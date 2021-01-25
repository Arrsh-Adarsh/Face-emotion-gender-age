import cv2
import numpy as np
from keras.models import load_model


def predict_emotion(img):
    model = load_model('emotion.h5')
    emotion_label = {0: 'Angry',
                     1: 'Disgust',
                     2: 'Fear',
                     3: 'Happy',
                     4: 'Sad',
                     5: 'Surprise',
                     6: 'Neutral'
                     }

    final_img = np.expand_dims(np.expand_dims(np.asarray(cv2.resize(img, (48, 48))), 0), -1)
    result = np.argmax(model.predict(final_img), axis=1)[0]
    emotion = emotion_label[result]
    return emotion
