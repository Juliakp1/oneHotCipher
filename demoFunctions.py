
# A demo program to show off all of the actions you can take in the oneHotLibrary

def returns_function_chosen(number):
    functions = ['', 'to_one_hot', 'to_string', 'cipher_it', 'from_cipher', 'enigma_it', 'from_enigma']
    return functions[number]
    
def print_avaliable_functions():
    for i in range(1,7):
        name = returns_function_chosen(i)
        print(str(i) + ' - ' + str(name))
    print('')

def print_function_desc(numb):
    functions = ['', 
                 'to_one_hot -> ciphers messages like a matriz to one-hot encoding', 
                 'to_string -> converts one-hot encoded messages to legible strings', 
                 'cipher_it -> ', 
                 'from_cipher -> ', 
                 'enigma_it -> ', 
                 'from_enigma -> ']
    return functions[numb]