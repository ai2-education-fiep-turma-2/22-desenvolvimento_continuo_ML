import requests
import json
import numpy as np
from PIL import Image
import cv2

img_array = cv2.imread('blusa1.jpeg', cv2.IMREAD_GRAYSCALE)
img_pil = Image.fromarray(img_array)
img_28x281 = np.array(img_pil.resize((28, 28), Image.ANTIALIAS))

img_28x28 = img_28x281.reshape(1, 28, 28, 1)

data = json.dumps({"signature_name": "serving_default", "instances": img_28x28.tolist()})


headers = {"content-type": "application/json"}
json_response = requests.post('http://localhost:8501/v1/models/fashion_model:predict', data=data, headers=headers)
print(json_response.text)

predictions = json.loads(json_response.text)['predictions']
print(predictions)