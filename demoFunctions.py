
import numpy as np
from libraryFunctions import cipher_it, from_cipher, enigma_it, from_enigma

# A demo program to show off all of the actions you can take in the oneHotLibrary
# By the way, the reason why the function lists ave the 0th index as '' is beacuse there is no option for that slot, and starting at 0 in options in confusing





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

    print('The input for this function is: ')
    currentCipher = listItems[0]
    print(listItems[1])
    print('')
    print('Result: ')

    if currentCipher == 'cipher_it':
        result = cipher_it(listItems[1], listItems[2])
        
    elif currentCipher == 'from_cipher':
        result = from_cipher(listItems[1], listItems[2])
        
    elif currentCipher == 'enigma_it':
        result = enigma_it(listItems[1], listItems[2], listItems[3])

    elif currentCipher == 'from_enigma':
        result = from_enigma(listItems[1], listItems[2], listItems[3])

    print(result)

# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- #

def prints_functions_premade(numb):

    # The decryption ones show the uncripted text on the comment next to it
    functions = ['',                                                   
                 ['cipher_it', 'This is a test string, to show off the cipher_it encryption', np.array([])], 
                 ['from_cipher', '', np.array([])],                                                 # This is a test string, to show off the from_cipher decryption
                 ['enigma_it', 'This is a test string, to show off the enigma_it encryption', np.array([]), np.array([])], 
                 ['from_enigma', '', np.array([]), np.array([])]]                                   # This is a test string, to show off the from_enigma decryption
    prints_functions(functions[numb])