from oneHotCipher.libraryFunctions import *
from flask import Flask, jsonify, request
import json

app = Flask(__name__)


#roda perfeitamente
@app.route('/convert/to_one_hot/', methods=['POST'])
def convert_to_one_hot():
    texto = request.get_json('amostra')
    
    texto = texto.values()
    for i in texto:
         a = str(i)
    
    saida = to_one_hot(a)

    saida = json.dumps({'nums': saida.tolist()})
    return jsonify(saida)





#daqui pra baixo ainda não
@app.route('/convert/to_string', methods=['POST'])
def convert_to_string():
    texto = request.get_json('amostra')
    texto = texto.values()

    for i in texto:
         a = str(i)

    saida = to_string(a)
    saida = json.dumps({'nums': saida.tolist()})
    return jsonify(saida)

@app.route('/convert/cipher_it', methods=['POST'])
def convert_cipher_it():
    texto = request.json
    saida = cipher_it(texto)
    return jsonify (saida)

@app.route('/convert/from_cipher', methods=['POST'])
def convert_from_cipher():
    texto = request.json
    saida = from_cipher(texto)
    return jsonify(saida)

@app.route('/convert/enigma_it', methods=['POST'])
def convert_enigma_it():
    texto = request.json
    saida = enigma_it(texto)
    return jsonify(saida)

@app.route('/convert/from_enigma', methods=['POST'])
def convert_from_enigma():
    texto = request.json


    saida = from_enigma(texto)
    return jsonify(saida)

if __name__ == "__main__":
	app.run()