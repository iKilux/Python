import random
print('##'*82)
#print(65*'#'+'  PROGRAMME POUR ALIMATOU DIAGNE  '+'#'*65)
print('PROGRAMME POUR ALIMATOU DIAGNE'.center(164, '#'))
print('##'*82)

def multiplication():
    compteur = 0
    for i in range (10):
        numb = random.randint(1, 11)
        numb2= random.randint(1,11)
        vreponse = numb*numb2
        print('combien font '+str(numb)+' * '+str(numb2)+' ?')
        reponse = int(input())
        if reponse == vreponse :
            compteur = compteur + 1
        else:
            compteur = compteur
            
    #print(140*'*'+'Vous avez une note de '+str(compteur)+'/'+str(i+1))
    print('Vous avez une note de '.rjust(140, '*') + str(compteur)+'/'+str(i+1))

def soustraction ():
    points = 0
    for i in range (10):
        number = random.randint(0,10)
        number2= random.randint(1,11)
        if number > number2:
            print('le resultat de '+str(number)+'-'+str(number2)+' est de:')
            result = int(input())
            if result == number - number2:
                #print('ok')
                points = points + 1
            else:
                #print('false')
                points = points
        else:
            print('le resultat de '+str(number2)+'-'+str(number)+' est de:')
            result = int(input())
            if result == number2 - number:
                #print('ok')
                points = points + 1
            else:
                #print('false')
                points = points
    #print(140*'*'+'Vous avez une note de '+str(points)+'/'+str(i+1))
    print('Vous avez une note de '.rjust(140, '*')+str(points)+'/'+str(i+1))
    

def addition ():
    point = 0
    for i in range(10):
        a = random.randint(0, 11)
        b = random.randint(0, 11)
        print('le resultat de '+str(a)+'+'+str(b)+' est de:')
        resultat = int(input())
        if resultat == (a + b):
            point = point + 1
        else:
            point = point
    #print(140*'*'+'Vous avez une note de '+str(point)+'/'+str(i+1))
    print('Vous avez une note de '.rjust(140, '*')+str(point)+'/'+str(i+1))
def operations():
    multiplication()
    soustraction()
    addition()
operations()

