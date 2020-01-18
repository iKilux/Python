#typing sequence loop
print('Donner le nombre de chats à enregistrer')
number=int(input())
catGate=[]
for i in range(number):
    print('Donner le nom du chat '+str(i+1)+' element')
    catGate=catGate+[input()]
print(catGate)
