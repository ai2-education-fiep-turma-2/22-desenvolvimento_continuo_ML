import requests
import json
import pandas as pd

url = "http://127.0.0.1:5001/"

action = "predict-mpg"

postData = json.loads('{"cylinders":"8","displacement":"307","horsepower":"130","weight":"3504","acceleration":"12","year":"70","originL":"0"}')

r = requests.post(url = (url + action), json = postData)

print(r.json())
