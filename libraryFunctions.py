
# The actual working functions
import unidecode
import numpy as np
import matplotlib.pyplot as plt

# ----------------------------- #

def to_one_hot(texto):

    texto = texto.lower()
    texto = unidecode.unidecode(texto)

    caracteres_utilizados = []
    
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

def to_string(mensagem_codificada):
    
    string = ""
    
    for i in mensagem_codificada:
        j = 0
        while j < 27:
            if i[j] == 1:
                caractere = j + 96
                if j == 0:
                    caractere = 32
                letra = chr(caractere)
                string += letra
            j = j+1
    return string

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

cipher = to_one_hot('XNYZURGSJICWMFQKODHTBLPAVE ')
print(cipher_it("aabbcc  eeeeee", cipher))
print(from_cipher(cipher_it("aabbcc  eeeeee", cipher), cipher))