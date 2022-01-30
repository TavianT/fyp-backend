import cv2
import tensorflow as tf
from tensorflow import keras
import numpy as np

IMAGE_SHAPE = (224, 224)

model = keras.models.load_model('adv_new_model')

flowers_labels_dict = {
    'roses': 0,
    'daisy': 1,
    'dandelion': 2,
    'sunflowers': 3,
    'tulips': 4,
    'carnations': 5,
    'daffodils': 6,
    'poppies': 7,
}



def classify_image(img_path):
    img = cv2.imread(img_path)
    resized_img = cv2.resize(img, IMAGE_SHAPE)
    resized_img = resized_img.reshape(1,224,224,3)
    resized_img = np.array(resized_img)
    resized_img = resized_img / 255
    predicted = model.predict(resized_img)
    score = tf.nn.softmax(predicted[0])
    predicted = np.argmax(predicted, axis=1)
    print(list(flowers_labels_dict.keys())[list(flowers_labels_dict.values()).index(predicted[0])])
    print(f'acc: {np.max(score) * 100}')

    classification = {
        'flower': list(flowers_labels_dict.keys())[list(flowers_labels_dict.values()).index(predicted[0])],
        'accuracy': str(round(np.max(score) * 100, 2))
    }
    return classification
