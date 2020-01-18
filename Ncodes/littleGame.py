import random
for i in range(random.randint(4, 10)):
    a = random.randint(1, 10)
    b = random.randint(1, 10)
    if a < b :
        print(a*'#')
        print(b*'#')
        vratio = a/b
    else:
        print(b*'#')
        print(a*'#')
        vratio = b/a
    print()
    print('Donner le num')
    rationum = int(input())
    print('Donner le denum')
    ratiodenum = int(input())
    ratio = rationum / ratiodenum
    if ratio == vratio:
        print('Good Job')
    else:
        print('Désolé !')

