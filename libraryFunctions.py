
# The actual working functions
import unidecode
import numpy as np
import matplotlib.pyplot as plt

# ----------------------------- #

def to_one_hot(texto):

    texto = texto.lower()
    texto = unidecode.unidecode(texto)

    caracteres_utilizados = []
    #tamanho 27x1
    #ir preenchendo com valores ascii
    #diminuir 97 do valor de cada letra
    #normalizar 
    
    
    for letra in texto:
        #converte para código ascii e transforma em 0 a 27
        letra = ord(letra) - 96
        if letra == -64:
        #para espaços
            letra = 0
        if letra >= 0 and letra <= 27:
            saida = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
            saida[letra] = 1
            caracteres_utilizados.append(saida)
    
    array_saida = np.array(caracteres_utilizados)

    return array_saida

# ----------------------------- #

def to_string():
    pass

# ----------------------------- #

def cipher_it(text, cipher):
    
    arrayText = to_one_hot(text)                          # Into array
    encodedArray = arrayText @ cipher                     # Into cipher
    codedText = to_string(encodedArray)                   # Out of array
    return codedText

# ----------------------------- #

def from_cipher(codedText, cipher):

    encodedArray = to_one_hot(codedText)                # Into array
    arrayText = encodedArray @ np.linalg.inv(cipher)    # Undo cipher
    text = to_string(arrayText)                         # Out of array
    return text

# ----------------------------- #

def enigma_it():
    pass

# ----------------------------- #

def from_enigma():
    pass


# print(cipher_it("O dia está ensolarado"))