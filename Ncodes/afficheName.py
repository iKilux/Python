names = {'Mahamadou':'Kaba', 'Moussa': 'Wague', 'Ahmadou': 'Ba', 'Ferdinand': 'Oyono'}

def afficheNoms(dico, vgauche, vdroite):
    print('Les noms'.center(vgauche + vdroite, '*'))
    for prenom, nom in dico.items():
        print(prenom.ljust(vgauche, '_') + nom.rjust(vdroite))
        
#afficheNoms(names, 10,15)
#afficheNoms(names, 50,5)
#afficheNoms(names, 70,30)

def carre(entier):
	print(f"Le carré de {entier} est " + str((entier*entier)))