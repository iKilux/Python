while True:
    print('Type your name ')
    name=input()
    if name!='Joe':
        continue
    print('Welcome Joe! What is the password ? (Is it a fish)')
    password=input()
    if password=='swordfish':
        break
print('Acces granted')
