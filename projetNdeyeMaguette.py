#! usr/bin/python3

import sys
baseDeDonnees={'cahier':7, 'stylo':3, 'papier':10}
   
print('Entrer le nom du produit')
nomProduit=input()

def verifProduit(nomProduit):
    if nomProduit in baseDeDonnees.keys():
        print('Combien avez-vous vendu de '+nomProduit+'s ?')
        quantiteProduit=int(input())
        baseDeDonnees[nomProduit]=baseDeDonnees[nomProduit]-quantiteProduit
    else:
        print('On a pas de '+nomProduit+' dans notre base de donnees.')
        print('Appuyer sur une touche pour inserer comme nouveau produit ?')
        print('Appuyer espace pour quitter')
        decision=input()
        if decision==' ':
            sys.exit()
        else:
            print('entrer la quantite a assigne a '+nomProduit)
            nouvelQuantite=int(input())
            baseDeDonnees[nomProduit]=nouvelQuantite
    print(baseDeDonnees)

verifProduit(nomProduit)



