while True:
    chiffres = input('N\'inserer que des chiffres:  ')
    if chiffres.isdecimal():
        break
    else:
        print('je vous ai bien demandé de n\'inserer que des chiffres')

while True:
    lettres = input('N\'inserer que des lettres:  ')
    if lettres.isalpha():
        break
    else:
        print('Inserer que des lettres svp')

while True:
    chiffresEtLettres = input('Inserer des chiffres et des lettres:  ')
    if chiffresEtLettres.isalnum():
        break
    else:
        print('eviter les espaces et les caracteres speciaux '
