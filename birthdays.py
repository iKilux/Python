#! usr/bin/python3
birthday={'Khadim':'December 09'}
while True:
    print()
    print('Enter a name ! or press K to stop')
    name=input()
    if name=='k':
        break
    if name in birthday:
        print(birthday[name]+' is the birthday of '+name)
    else:
        print('We do not have any information about '+name)
        print('When is the birthday of '+name)
        bday=input()
        birthday[name]=bday
        print('Birthday database updated.')
        
