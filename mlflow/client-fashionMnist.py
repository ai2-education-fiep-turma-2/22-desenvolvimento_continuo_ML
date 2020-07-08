import requests
import numpy as np
import pandas as pd

import requests
import json
import numpy as np
from PIL import Image
import cv2

img_array = cv2.imread('blusa1.jpeg', cv2.IMREAD_GRAYSCALE)
img_pil = Image.fromarray(img_array)
img_28x281 = np.array(img_pil.resize((28, 28), Image.ANTIALIAS))

img_28x28 = img_28x281.reshape(1, 28, 28, 1)

columns2 = np.zeros((1, 28, 28,1))



df=pd.DataFrame(img_28x28.tolist(),columns=columns2.tolist())

#rotina para chamada ao Microserviço

host = 'headtop.ncc.unesp.br'
port = '8891'

url = f'http://{host}:{port}/invocations'

headers = {
    'Content-Type': 'application/json',
}

# converter pandas para json
http_data = df.to_json(orient='split')

#requisicao ao modelo servido pelo mlflow
r = requests.post(url=url, headers=headers, data=http_data)

print(f'Classe: {r.text}')