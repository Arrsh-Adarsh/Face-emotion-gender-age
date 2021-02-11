import cv2
import numpy as np
# import tensorflow as tf
from tensorflow import keras
from keras.models import load_model


def predict_emotion(img):
    model = load_model('model/emotion.h5')
    emotion_label = {0: 'Angry',
                     1: 'Disgust',
                     2: 'Fear',
                     3: 'Happy',
                     4: 'Sad',
                     5: 'Surprise',
                     6: 'Neutral'
                     }
    result = np.argmax(model.predict(img), axis=1)[0]
    emotion = emotion_label[result]
    return emotion


def predict_age(img):
    model = load_model('model/age.h5')
    # return np.argmax(model.predict(img), axis=1)[0]
    return model.predict(img)


def predict_gender(img):
    model = load_model('model/gender.h5')
    a = {1: 'male',
         0: 'female'}
    return a[np.argmax(model.predict(img), axis=1)[0]]


def predict(img):
    # final_img = np.expand_dims(np.expand_dims(np.asarray(cv2.resize(img, (48, 48))), 0), -1)
    emotion = predict_emotion(np.expand_dims(np.expand_dims(np.asarray(cv2.resize(img, (48, 48))), 0), -1))
    # age = predict_age(np.expand_dims(np.expand_dims(np.asarray(cv2.resize(img, (96, 96))), 0), -1))
    gender = predict_gender(np.expand_dims(np.expand_dims(np.asarray(cv2.resize(img, (96, 96))), 0), -1))
    return str(emotion) + ' | ' + str(gender)