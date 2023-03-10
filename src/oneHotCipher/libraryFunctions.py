
# The actual working functions
import unidecode, random
import numpy as np
import matplotlib.pyplot as plt

# ----------------------------- #

def to_one_hot(text):
    """
    Takes a piece of text and converts it into a matrix

    Arguments
    ---------------
    text (string) : phrase to be encoded
    """

    texto = text.lower()
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

def to_string(codedText):
    """
    Takes a coded matrix and converts it into read-able text

    Arguments
    ---------------
    codedText (list) : a list of lists representing the coded matrix
    """

    string = ""
    for i in codedText:
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
    """
    Takes the text and ciphers it based on the second argument

    Arguments
    ---------------
    text (string) : phrase to be encoded
    cipher (list) : a list of lists representing a cipher matrix
    """
    
    arrayText = to_one_hot(text)                          # Into array
    encodedArray = arrayText @ cipher                     # Into cipher
    codedText = to_string(encodedArray)                   # Out of array
    return codedText

# ----------------------------- #

def from_cipher(codedText, cipher):
    """
    Takes the coded text and uses the cipher to undo the encryption

    Arguments
    ---------------
    text (string) : phrase to be decoded
    cipher (list) : a list of lists representing a cipher matrix
    """

    encodedArray = to_one_hot(codedText)                # Into array
    arrayText = encodedArray @ np.linalg.inv(cipher)    # Undo cipher
    text = to_string(arrayText)                         # Out of array
    return text

# ----------------------------- #

def enigma_it(text, cipher, auxCipher):
    """
    Takes the text and ciphers it, and at every letter uses an auxiliary
    cipher to protect it further

    Arguments
    ---------------
    text (string) : phrase to be encoded
    cipher (list) : a list of lists representing a cipher matrix
    auxCipher (list) : a list of lists representing a cipher matrix
    """

    arrayText = to_one_hot(text)
    prevCipher = cipher
    finalList = []

    for character in arrayText:
        newChar = character @ prevCipher
        finalList.append(newChar)
        prevCipher = prevCipher @ auxCipher
    
    finalArray = np.array(finalList)
    codedText = to_string(finalArray)
    return codedText

# ----------------------------- #

def from_enigma(codedText, cipher, auxCipher):
    """
    Takes the text and un-ciphers it, reverting the base cipher alongside the 
    auxiliary cipher 

    Arguments
    ---------------
    text (string) : phrase to be decoded
    cipher (list) : a list of lists representing a cipher matrix
    auxCipher (list) : a list of lists representing a cipher matrix
    """

    arrayText = to_one_hot(codedText)
    prevCipher = np.linalg.inv(cipher)              # Starts with the inverted cipher
    invAuxCipher = np.linalg.inv(auxCipher)
    finalList = []

    for character in arrayText:
        newChar = character @ prevCipher
        finalList.append(newChar)
        prevCipher = invAuxCipher @ prevCipher       # Every letter multiplies the INVERSE of the auxCipher, so it reverses the cryptography
    
    finalArray = np.array(finalList)
    decodedText = to_string(finalArray)
    return decodedText

# ----------------------------- #