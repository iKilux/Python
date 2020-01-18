#! usr/bin/python3

import pyperclip
'''
copie = pyperclip.paste()
lcopie = copie.split('\n')
mot =''
for name in lcopie:
    name = '* '+name
    mot += name + '\n'
print(mot)
#pyperclip.copy(mot)
'''
text = pyperclip.paste()
lesLignes = text.split('\n')

for i in range(len(lesLignes)):
    lesLignes[i] = '* ' + lesLignes[i]
text = '\n'.join(lesLignes)
pyperclip.copy(text)
