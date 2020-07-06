# IMPORT FLASK
from flask import Flask, request, jsonify
app = Flask(__name__)

# BANCO DE DADOS "FAKE". SO PRA ARMAZENAR DADOS
listOfUsers = ["Primeiro Nome", "Segundo Nome", "Terceiro Nome"]

@app.route('/', methods=["GET"])
def index():
    return jsonify("Hello, World!")

@app.route('/get-users', methods=["GET"])
def getUsers():
    return jsonify(listOfUsers)

@app.route('/post-user', methods=["POST"])
def insertUser():
    getData = request.json
    nomeUser = getData['nome']
    sobrenomeUser = getData['sobrenome']
    listOfUsers.append(nomeUser + " " + sobrenomeUser)
    return getUsers()