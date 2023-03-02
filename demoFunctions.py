
import numpy as np
from libraryFunctions import to_one_hot, to_string, cipher_it, from_cipher, enigma_it, from_enigma

# A demo program to show off all of the actions you can take in the oneHotLibrary
# By the way, the reason why the function lists ave the 0th index as '' is beacuse there is no option for that slot, and starting at 0 in options in confusing





def returns_function_chosen(number):
    functions = ['', 'to_one_hot', 'to_string', 'cipher_it', 'from_cipher', 'enigma_it', 'from_enigma']
    return functions[number]

# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- #
    
def print_avaliable_functions():
    for i in range(1,7):
        name = returns_function_chosen(i)
        print(str(i) + ' - ' + str(name))

# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- #

def print_function_desc(numb):
    functions = ['', 
                 'to_one_hot -> encrypts messages to one-hot encoding (turning it into a matrix)', 
                 'to_string -> converts/decrypts one-hot encoded messages to legible strings', 
                 'cipher_it -> encrypts messages to cipher encoding', 
                 'from_cipher -> converts/decrypts simple cipher encoded messages to legible strings', 
                 'enigma_it -> encrypts messages to enigma encoding', 
                 'from_enigma -> converts/decrypts enigma encoded messages to legible strings']
    print(functions[numb])

# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- #

# Converts the input into a 'shows inputs' and 'run specified function'
def prints_functions(listItems):

    print('The inputs for this function are: ')
    currentCipher = listItems[0]

    if currentCipher == 'to_one_hot':
        print(listItems[1])
        print('')
        print('Result: ')
        result = to_one_hot(listItems[1])
        print(result)

    elif currentCipher == 'to_string':
        print(listItems[1])
        print('')
        print('Result: ')
        result = to_string(listItems[1])
        print(result)

    elif currentCipher == 'cipher_it':
        print(listItems[1])
        print(listItems[2])
        print('')
        print('Result: ')
        result = cipher_it(listItems[1], listItems[2])
        print(result)
        
    elif currentCipher == 'from_cipher':
        print(listItems[1])
        print(listItems[2])
        print('')
        print('Result: ')
        result = from_cipher(listItems[1], listItems[2])
        print(result)
        
    elif currentCipher == 'enigma_it':
        print(listItems[1])
        print(listItems[2])
        print(listItems[3])
        print('')
        print('Result: ')
        result = enigma_it(listItems[1], listItems[2], listItems[3])
        print(result)

    elif currentCipher == 'from_enigma':
        print(listItems[1])
        print(listItems[2])
        print(listItems[3])
        print('')
        print('Result: ')
        result = from_enigma(listItems[1], listItems[2], listItems[3])
        print(result)

# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- #

def prints_functions_premade(numb):

    # The decryption ones show the uncripted text on the comment next to it
    functions = ['', 
                 ['to_one_hot', 'This is a test string, to show off the to_one_hot encryption'], 
                 ['to_string', np.array([])],                                                       # This is a test string, to show off the to_string decryption
                 ['cipher_it', 'This is a test string, to show off the cipher_it encryption', np.array([])], 
                 ['from_cipher', '', np.array([])],                                                 # This is a test string, to show off the from_cipher decryption
                 ['enigma_it', 'This is a test string, to show off the enigma_it encryption', np.array([]), np.array([])], 
                 ['from_enigma', '', np.array([]), np.array([])]]                                   # This is a test string, to show off the from_enigma decryption
    prints_functions(functions[numb])