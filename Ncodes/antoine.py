import math

def afficheSuiteTcheque(number:int):
    if number % 2 == 0:
        print(number // 2, end=' ')
        return number //2
    else:
        print(3*number +1, end=' ')
        return 3*number +1
number = 3
nombreDeTerme = 0
compteur=0
listMax = []
while number != 1:
    if number % 2 == 0:
        compteur += 1
    listMax += [number]
    number = afficheSuiteTcheque(number)
    nombreDeTerme += 1
    maximumNumber = max(listMax)
print()
print(f"Le nombre de terme est {nombreDeTerme}")
print()
print(f"Le plus grand nombre rencontré est {maximumNumber}")
print()
print(f"Le poucentage de nombre paire est {(100*compteur)//nombreDeTerme}%")
