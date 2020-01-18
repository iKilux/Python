#This is a guess number game
import random
nombreG=random.randint(0,100)
print('I am thinking about a number between 0  and 100')
#on recueille le nombre choisi par l'user
for tryy in range(1,7):
    nombre=int(input())
    if nombre<nombreG:
        print('This number is too low')
    elif nombre>nombreG:
        print('This number is too big')
    else:
        break
if nombre==nombreG:
    print('Bravo ! You guessed the number in '+str(tryy)+' guesses')
else:
    print('You loose ! The Number was '+str(nombreG))
    
