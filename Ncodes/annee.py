print('Donner votre nom')
name = input()
print('Monsieur '+name+ ' donnez votre année de naissance')
annee = int(input())

if (2019-annee)< 18:
    print('Desolé '+name+' vous n\'etes pas autorisé à acceder au fichier')
else:
    print('Access granted ! Welcome mister '+name.upper())
