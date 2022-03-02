import json
import requests
from PIL import Image
import numpy as np
import os

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



def classify_image(img_path):
    img = Image.open(img_path)
    resized_img = img.resize(IMAGE_SHAPE)
    resized_img = np.array(resized_img)
    resized_img = resized_img.reshape([-1, 224 ,224, 3])
    resized_img = resized_img / 255

    api_url = "http://flowermodel.ukwest.azurecontainer.io:8501/v1/models/adv_new_model:predict" 


    data = json.dumps({"signature_name": "serving_default", "instances": resized_img.tolist()})
    headers = {"content-type": "application/json"} 
    json_response = requests.post(api_url, data=data, headers=headers) 
    predictions = json.loads(json_response.text)['predictions']
    predicted = np.argmax(predictions, axis=1)
    print(list(flowers_labels_dict.keys())[list(flowers_labels_dict.values()).index(predicted[0])])
    # print(f'acc: {np.max(score) * 100}')
    if os.path.exists(img_path):
        os.remove(img_path)
    classification = {
        'flower': list(flowers_labels_dict.keys())[list(flowers_labels_dict.values()).index(predicted[0])]
        # 'accuracy': str(round(np.max(score) * 100, 2))
    }
    return classification
