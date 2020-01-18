picnicItems = {'sandwiches': 4, 'apples': 12, 'cups': 4, 'cookies': 8000}
def afficherItems(items, rwid, lwid):
    print('Affichage'.center(rwid+lwid, '+'))
    for nameItem, qItem in items.items():
        print(nameItem.ljust(lwid, '.')+ str(qItem).rjust(rwid))
#afficherItems(picnicItems, 30, 10)
afficherItems(picnicItems, 5, 20)
