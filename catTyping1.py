cats=[]
while True:
    print('Type a name of the cat '+str(len(cats)+1)+' or nothing to stop')
    name=input()
    if name=='':
        break
    cats=cats+[name]
if len(cats)==0:
    print('Vous navez rien inserer')
else:
    print('Your cats are:')
    for name in cats:
        print(name, end=', ')
