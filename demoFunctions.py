
import numpy as np
import random
from libraryFunctions import to_one_hot, cipher_it, from_cipher, enigma_it, from_enigma

# A demo program to show off all of the actions you can take in the oneHotLibrary
# By the way, the reason why the function lists ave the 0th index as '' is beacuse there is no option for that slot, and starting at 0 in options in confusing



def generates_random_alphabet():
    # the space is a letter, and its letter 0
    alphabet = ' abcdefghijklmnopqrstuvwxyz'
    newAlpha = ''.join(random.sample(alphabet, len(alphabet)))
    return newAlpha

# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- #

def returns_function_chosen(number):
    functions = ['', 'cipher_it', 'from_cipher', 'enigma_it', 'from_enigma']
    return functions[number]

# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- #
    
def print_avaliable_functions():
    for i in range(1,5):
        name = returns_function_chosen(i)
        print(str(i) + ' - ' + str(name))

# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- #

def print_function_desc(numb):
    functions = ['', 
                 'cipher_it -> encrypts messages to cipher encoding', 
                 'from_cipher -> converts/decrypts simple cipher encoded messages to legible strings', 
                 'enigma_it -> encrypts messages to enigma encoding', 
                 'from_enigma -> converts/decrypts enigma encoded messages to legible strings']
    print(functions[numb])

# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- #

# Converts the input into a 'shows inputs' and 'run specified function'
def prints_functions(listItems):

    # If its a cipher -> only one matrix encryption
    if len(listItems) == 3:

        text = listItems[1]
        currentCipher = listItems[0]
        cipherMatrix = to_one_hot(listItems[2])

        print('The input for this function is: ')
        print(text)
        print('')
        print('The cipher is: ')
        print(listItems[2])
        print('')
        print('Result: ')
        
        if currentCipher == 'cipher_it':
            result = cipher_it(text, cipherMatrix)
        elif currentCipher == 'from_cipher':
            result = from_cipher(text, cipherMatrix)
    
    # If its an enigma -> two matrix encryption
    else:

        text = listItems[1]
        currentCipher = listItems[0]
        cipherMatrix = to_one_hot(listItems[2])
        cipherMatrix2 = to_one_hot(listItems[3])

        print('The input for this function is: ')
        print(text)
        print('')
        print('The ciphers are: ')
        print(listItems[2])
        print(listItems[3])
        print('')
        print('Result: ')

        if currentCipher == 'enigma_it':
            result = enigma_it(text, cipherMatrix, cipherMatrix2)
        elif currentCipher == 'from_enigma':
            result = from_enigma(text, cipherMatrix, cipherMatrix2)

    print(result)

# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- #

def prints_functions_premade(numb):

    cipher = generates_random_alphabet()
    cipher2 = generates_random_alphabet()

    functions = ['',                                                   
                 ['cipher_it', 'This is a test string to show off the cipher it encryption', cipher], 
                 ['from_cipher', 'This is a test string to show off the from cipher decryption', cipher],                                                 
                 ['enigma_it', 'This is a test string to show off the enigma it encryption', cipher, cipher2], 
                 ['from_enigma', 'This is a test string to show off the from enigma decryption', cipher, cipher2]]

    # So i can type read-able strings into the function above, and cypher it in real time
    if functions[numb][0] == 'from_cipher':
        text = cipher_it(functions[numb][1], to_one_hot(functions[numb][2]))
        functions[numb][1] = text
    elif functions[numb][0] == 'from_enigma':
        text = enigma_it(functions[numb][1], to_one_hot(functions[numb][2]), to_one_hot(functions[numb][3]))
        functions[numb][1] = text

    prints_functions(functions[numb])