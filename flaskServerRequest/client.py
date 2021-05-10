import requests
import json
import pandas as pd

url = "http://127.0.0.1:5000/"

#chamando /
r = requests.get(url = url)
print(r.json())

#recuperando um usuario especifico
action = "get-users"
r = requests.get(url = (url + action))

getData = r.json()
nomeUser = getData['nome']
idade = getData['idade']

print(nomeUser, idade )

#incluindo novo usuario
action = "post-user"
postData =  json.loads('{"nome":"user1", "idade":"11"}')
r = requests.post(url = (url + action), json = postData)
