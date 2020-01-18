#! /usr/bin/python3
n = int(input('Veuiller saisir le nombre à decomposer:  '))
listePremiers = [1]
i = 2
oldNumber = n
while n > 1:
    if n % i == 0:
        listePremiers += [i]
        n = n / i
    else:
        i = i + 1

'''
nombre=1
for i in range(len(listePremiers)):
    nombre *=listePremiers[i]
if oldNumber == nombre:
    print('Decomposition correcte !! ')
else:
    print('Revoyer le programme')
'''
print(str(oldNumber)+ ' : ', end='')
for number in listePremiers:
    print(str(number), end =' ')
print()
