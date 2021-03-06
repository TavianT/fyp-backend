import json
import requests
import cv2
import numpy as np

IMAGE_SHAPE = (224, 224)
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

img = cv2.imread('rose.jpg')
resized_img = cv2.resize(img, IMAGE_SHAPE)
resized_img = resized_img.reshape(1,224,224,3)
resized_img = np.array(resized_img)
resized_img = resized_img / 255

api_url = "http://flowermodel.ukwest.azurecontainer.io:8501/v1/models/adv_new_model:predict" 


data = json.dumps({"signature_name": "serving_default", "instances": resized_img.tolist()})
headers = {"content-type": "application/json"} 
json_response = requests.post(api_url, data=data, headers=headers) 
predictions = json.loads(json_response.text)['predictions']
predicted = np.argmax(predictions, axis=1)

print(list(flowers_labels_dict.keys())[list(flowers_labels_dict.values()).index(predicted[0])])
