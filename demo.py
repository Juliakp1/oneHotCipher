
# A demo program to show off all of the actions you can take in the oneHotLibrary

from demoFunctions import print_avaliable_functions, print_function_desc

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

if demoSelect == 1:
    print('')
    print('Great! Youve selected the pre-made demo, here are your options:')
    print_avaliable_functions()
    optionSelect = input()

    while (optionSelect not in ['1','2','3','4','5','6']):
        print('Not an option! Please try again')
        optionSelect = input()

    print('')
    print('You have selected option ' + optionSelect + ', so here is what it does: ')
    print('')
    print_function_desc()
    print('')

elif demoSelect == 2:
    print('')
    print('Great! Youve selected the diy demo, here are your options:')
    print_avaliable_functions()
    optionSelect = input()

    while (optionSelect not in ['1','2','3','4','5','6']):
        print('Not an option! Please try again')
        optionSelect = input()

    print('')
    print('Oh ummm, this part isnt fully fleshed out yet, unfortunatly :(')
    print('Please do try again in a later update though!')
    print('')

print('Thank you for trying out the demo! See you soon :D')
print('')



    