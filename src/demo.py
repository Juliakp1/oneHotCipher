
# A demo program to show off all of the actions you can take in the oneHotLibrary
# PLEASE make the terminal bigger before starting, else you might lose some info

from demoFunctions import returns_function_chosen, print_avaliable_functions, print_function_desc, generates_random_alphabet, prints_functions_premade, prints_functions

print('')
print(' $$$$$$\                      $$\   $$\            $$\            $$$$$$\  $$\           $$\                           ')
print('$$  __$$\                     $$ |  $$ |           $$ |          $$  __$$\ \__|          $$ |    ')
print('$$ /  $$ |$$$$$$$\   $$$$$$\  $$ |  $$ | $$$$$$\ $$$$$$\         $$ /  \__|$$\  $$$$$$\  $$$$$$$\   $$$$$$\   $$$$$$\ ')
print('$$ |  $$ |$$  __$$\ $$  __$$\ $$$$$$$$ |$$  __$$\|_$$  _|        $$ |      $$ |$$  __$$\ $$  __$$\ $$  __$$\ $$  __$$\ ')
print('$$ |  $$ |$$ |  $$ |$$$$$$$$ |$$  __$$ |$$ /  $$ | $$ |          $$ |      $$ |$$ /  $$ |$$ |  $$ |$$$$$$$$ |$$ |  \__|')
print('$$ |  $$ |$$ |  $$ |$$   ____|$$ |  $$ |$$ |  $$ | $$ |$$\       $$ |  $$\ $$ |$$ |  $$ |$$ |  $$ |$$   ____|$$ |')
print(' $$$$$$  |$$ |  $$ |\$$$$$$$\ $$ |  $$ |\$$$$$$  | \$$$$  |      \$$$$$$  |$$ |$$$$$$$  |$$ |  $$ |\$$$$$$$\ $$ |')
print(' \______/ \__|  \__| \_______|\__|  \__| \______/   \____/        \______/ \__|$$  ____/ \__|  \__| \_______|\__|')
print('                                                                               $$ | ')
print('                                                                               \__|    ')

exitRun = False
while not exitRun:

    print('')
    print('--------------------------------------')
    print('')
    print('Welcome to the demo program!')
    print('You can choose to see a pre-made algorythm or try it out for yourself! ')
    print('1 - See the pre-made demo')
    print('2 - Enter my own data')
    print('')

    demoSelect = input()

    while (demoSelect not in ['1','2']):
        print('Not an option! Please try again')
        demoSelect = input()

    demoSelect = int(demoSelect)

    # -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- #

    if demoSelect == 1:
        print('')
        print('Great! Youve selected the pre-made demo, here are your options:')
        print_avaliable_functions()
        print('')
        optionSelect = input()

        while (optionSelect not in ['1','2','3','4']):
            print('Not an option! Please try again')
            optionSelect = input()

        print('')
        print('You have selected option ' + optionSelect + ', so here is what it does: ')

        optionSelect = int(optionSelect)
        print_function_desc(optionSelect)
        print('')
        print('--------------------------------------')
        print('')
        prints_functions_premade(optionSelect)

        
    # -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- #

    elif demoSelect == 2:
        print('')
        print('Great! Youve selected the diy demo, here are your options:')
        print_avaliable_functions()
        print('')
        
        optionSelect = input()
        while (optionSelect not in ['1','2','3','4']):
            print('Not an option! Please try again')
            optionSelect = input()

        print('')
        print('You have selected option ' + optionSelect + ', so here is what it does: ')

        optionSelect = int(optionSelect)
        print_function_desc(optionSelect)
        print('')
        print('--------------------------------------')
        print('')

        print('')
        print('Input text: ')
        text = input()
        print('')
        print('Cipher: ')
        cipher = input()
        
        # it just checks the lengh, but that should show how it works to someone trying it out
        while (len(cipher) != 27):
            print('This cipher isnt valid! Please use all the alphabet letters AND a space')
            print('Example: ')
            print(generates_random_alphabet())
            print('')
            cipher = input()

        function = returns_function_chosen(optionSelect)
        listItems = [function, text, cipher]

        if optionSelect in [3, 4]:
            print('')
            print('Auxiliary cipher: ')
            cipher2 = input()
            while (len(cipher2) != 27):
                print('This cipher isnt valid! Please use all the alphabet letters AND a space')
                print('Example: ')
                print(generates_random_alphabet())
                cipher2 = input()
            listItems.append(cipher2)    

        print('')
        print('--------------------------------------')
        print('')

        prints_functions(listItems)

    # -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- #

    print('')
    print('Do you want to keep using the program? (y/n) ')
    text = input()
    while (text not in ['y','n']):
        print('Please use (y) for yes and (n) for no')
        text = input()
    if text == 'n':
        exitRun = True

# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- #

print('')
print('--------------------------------------')
print('')
print('Thank you for trying out the demo! See you soon :D')
print('')



    