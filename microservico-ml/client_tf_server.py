import requests
import json
import numpy as np
from pickle import load

Xpred=np.zeros(7)


Xpred[0]=8
Xpred[1]=307
Xpred[2]=130
Xpred[3]=3504
Xpred[4]=12
Xpred[5]=70
Xpred[6]=0

'''
Xpred[0]=1
Xpred[1]=1
Xpred[2]=1
Xpred[3]=2
Xpred[4]=2
Xpred[5]=2
Xpred[6]=2
'''

Xpred = Xpred.reshape(1,7)

scaler = load(open('scaler.pkl', 'rb'))
Xpred = scaler.transform(Xpred)

data = json.dumps({"signature_name": "serving_default", "instances": Xpred.tolist()})

headers = {"content-type": "application/json"}
json_response = requests.post('http://localhost:5001/v1/models/auto_model:predict', data=data, headers=headers)
print(json_response.text)

predictions = json.loads(json_response.text)['predictions']
print(predictions)
