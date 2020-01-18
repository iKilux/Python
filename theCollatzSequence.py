#the collatz sequence code



#creation de la fonction collatz()

def collatz(number):
    if number%2==0:
        print(number//2)
        return number//2
    else:#verificaton if odd
        print(3*number+1)
        return 3*number+1

#saisie du nombre 
try:
    print('Type an integer ')
    number=int(input())
    while collatz(number)!=1:
        number=collatz(number)
except ValueError:
    print('You must enter an integer ! ')
