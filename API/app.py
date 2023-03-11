from oneHotCipher.libraryFunctions import *
from flask import Flask, jsonify, request
import ast
from flask_restful import Api
import json

app = Flask(__name__)
api = Api(app)


@app.route('/convert/to_one_hot/', methods=['POST'])
def convert_to_one_hot():
    texto = request.get_json('amostra')
    
    texto = texto.values()
    for i in texto:
        a = str(i)
    
    saida = to_one_hot(a)

    saida = json.dumps({'saida': saida.tolist()})
    return jsonify(saida, 200)

@app.route('/convert/to_string', methods=['POST'])
def convert_to_string():
    texto = request.get_json('amostra')
 
    texto = [i for i in texto.values()] #como lista
    texto = ast.literal_eval(texto[0])
  
    saida = to_string(texto)
    return jsonify(saida, 200)

@app.route('/convert/cipher_it', methods=['POST'])
def convert_cipher_it():
    entrada = request.get_json('amostra')
    
    texto = list(entrada.values())[0]
    cifra = list(entrada.values())[1]

    a = str(texto)
    
    b = to_one_hot(cifra)
    
    saida = cipher_it(a, b)

    saida = json.dumps({'saida': saida})
    return jsonify(saida, 200)

@app.route('/convert/from_cipher', methods=['POST'])
def convert_from_cipher():
    entrada = request.get_json('amostra')
    
    texto = list(entrada.values())[0]
    cifra = list(entrada.values())[1]

    a = str(texto)
    
    b = to_one_hot(cifra)
    print(b)

    saida = from_cipher(a, b)

    saida = json.dumps({'saida': saida})
    return jsonify(saida, 200)

@app.route('/convert/enigma_it', methods=['POST'])
def convert_enigma_it():
    entrada = request.get_json('amostra')
    
    texto = list(entrada.values())[0]
    cifra = list(entrada.values())[1]
    aux_cifra = list(entrada.values())[2]

    a = str(texto)
    
    b = to_one_hot(cifra)
    c = to_one_hot(aux_cifra)

    saida = enigma_it(a, b, c)

    saida = json.dumps({'saida': saida})
    return jsonify(saida, 200)

@app.route('/convert/from_enigma', methods=['POST'])
def convert_from_enigma():
    entrada = request.get_json('amostra')
    
    texto = list(entrada.values())[0]
    cifra = list(entrada.values())[1]
    aux_cifra = list(entrada.values())[2]

    a = str(texto)
    
    b = to_one_hot(cifra)
    c = to_one_hot(aux_cifra)

    saida = from_enigma(a, b, c)

    saida = json.dumps({'saida': saida})
    return jsonify(saida, 200)

if __name__ == "__main__":
	app.run()