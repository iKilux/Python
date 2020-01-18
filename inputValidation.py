
while True:
    print('Veuillez entrer votre age')
    age=input()
    if age.isdecimal():
        break
    else:
        print('Entrer un age valide')

while True:
    print('Entrer un mot de passe comprenant des chiffres et des lettres')
    password=input()

    if password.isalnum():
        break
    else:
        print('Votre mot de passe doit contenir des lettres et des chiffres')
print('votre age est '+age+'\nvotre mot est :\t'+'*'*len(password))

