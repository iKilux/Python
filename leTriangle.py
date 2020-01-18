#triangle isocele
print('Enter an integer')
hauteur=int(input())
star=1
space=hauteur -1
for i in range (hauteur):
    print(space*' '+star*'*')
    star+=2
    space-=1
