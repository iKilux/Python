
inventory={'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
def displayInventory(dico):
    print('Your inventory: ')
    count=0
    for name in dico.keys():
        print(str(dico[name])+' '+name)
        count+=dico[name]
    print('Number of items : '+str(count))

def addInventory(invent, addItems):
    
    for name in addItems:
        try:
            invent[name]+=1
            invent.setdefault(name, invent[name])
        except KeyError:
            invent[name]=1      
    #print(invent)
addInventory(inventory, dragonLoot)
displayInventory(inventory)
