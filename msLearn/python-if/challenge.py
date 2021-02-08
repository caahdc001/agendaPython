print('Tell me your name: ')
name = input()
print(name + ' would you like to continue? press y or yes for continue or n or no to exiting...')
option = input()

if option == 'y' or option == 'yes':
    print('Continuing ...')
    print('Complete!')
elif option == 'n' or option == 'no':
    print('Exiting')
else:
    print('Option invalid! Please try again and respond with yes or no.')