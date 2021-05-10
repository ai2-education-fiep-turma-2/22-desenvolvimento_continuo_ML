# IMPORT FLASK
import json
from flask import Flask, request, jsonify
app = Flask(__name__)

# BANCO DE DADOS "FAKE". SO PRA ARMAZENAR DADOS
listOfUsers = ["Primeiro Nome", "Segundo Nome", "Terceiro Nome"]
idades = [10,12,13]

@app.route('/', methods=["GET"])
def index():
    return json.dumps("Hello, World!")

@app.route('/get-users', methods=["GET"])
def getUsers():
    return jsonify(nome = listOfUsers[1], idade = idades[1] )

@app.route('/post-user', methods=["POST"])
def insertUser():
    getData = request.json
    nomeUser = getData['nome']
    idade = getData['idade']
    listOfUsers.append(nomeUser)
    idades.append(int(idade))
    print(listOfUsers)
    print(idades)
    return json.dumps("OK")
