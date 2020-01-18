names = { 'Mahamadou': 'Kaba', 'Moussa': 'Wague', 'Ahmadou': 'Ba', 'Ferdinand': 'Oyono'}
def afficheNames(name, lgauche, ldroite):
    print('Les noms qui figurent sur la liste'.center(lgauche + ldroite, '-')
    for prenom, nom in name.items():
          print(prenom.ljust(lgauche) + nom.rjust(ldroite))
afficheNames(names, 10, 10)
afficheNames(names, 30, 40)
afficheNames(names, 40, 20)
