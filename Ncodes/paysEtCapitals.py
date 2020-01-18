#on va  faire un jeu de pays et de capital
print('###########################################################')
print('##                                                       ##')
print('##      BIENVENU DANS LE JEU DE PAYS ET DE CAPITAL       ##')
print('##                                                       ##')
print('###########################################################')
print('Choisir un niveau')
print('#A:Les pays en afrique \n#B:Les pays en europe \n#C:Les pays en asie \n#D:Les pays en amerique')

#dictionnaire des pays

paysAfrique = {'du senegal': 'dakar', 'du mali': 'bamako', 'du ghana': 'accra',
        'de la mauritanie': 'nouakchott', 'du malawi': 'lilongwe', 'de l\'ile maurice': 'port louis',
        'de la zambie': 'lusaka', 'du somalie': 'mogadishu', 'du zimbabwe': 'harare',
        'du djibouti': 'djibouti', 'du maroc': 'rabat','de l\'egypte': 'le caire',
        'de la tunisie': 'tunis', 'de l\'algerie': 'alger', 'de la libye': 'tripoli'}

paysEurope = {'de la france': 'paris', 'de l\'italie': 'rome', 'de l\'espagne': 'madrid', 'portugal': 'lisbonne',
              'de la belgique': 'bruxelles', 'de l\'angleterre': 'londres'}

paysAsie = {'de la chine': 'pekin', 'du japon': 'tokyo', 'de taiwan': 'taipei'}

paysAmerique = {'des usa':'washington', 'du canada': 'toronto', 'de cuba':'la havane', 'mexique': 'mexico'}

#forcer l'utilisateur a choisir une lettre entre A B C ou D
while True:
    choix = input ()
    choix = choix.lower()
    if choix !='a' and choix != 'b' and choix != 'c' and choix != 'd':
        continue
    else:
        break
if choix == 'a':
    print(30*'#'+' LES PAYS D\'AFRIQUE '+'#'*30)
    points = 0
    for name in paysAfrique.keys(): 
        print('Quelle est la capitale '+name,)
        reponse = input ()
        reponse = reponse.lower()
        if reponse == paysAfrique[name]:
            points = points + 1
        else:
            points = points
    print('vous avez une note de '+str(points)+'/'+str(len(paysAfrique.keys())))
elif choix == 'b':
    print(30*'#'+' LES PAYS D\'EUROPE '+'#'*30)
    points = 0
    for name in paysEurope.keys():
        print('Quelle est la capitale '+name)
        reponse = input ()
        reponse = reponse.lower()
        if reponse == paysEurope[name]:
            points = points + 1
        else:
            points = points
    print('vous avez une note de '+str(points)+'/'+str(len(paysEurope.keys())))
elif choix == 'c':
    print(30*'#'+' LES PAYS D\'ASIE '+'#'*30)
    points = 0
    for name in paysAsie.keys():
        print('Quelle est la capitale '+name)
        reponse = input ()
        reponse = reponse.lower()
        if reponse == paysAsie[name]:
            points = points + 1
        else:
            points = points
    print('vous avez une note de '+str(points)+'/'+str(len(paysAsie.keys())))
else:
    print(30*'#'+' LES PAYS D\'AMERIQUE '+'#'*30)
    points = 0
    for name in paysAmerique.keys():
        print('Quelle est la capitale '+name)
        reponse = input ()
        reponse = reponse.lower()
        if reponse == paysAmerique[name]:
            points = points + 1
        else:
            points = points
    print('vous avez une note de '+str(points)+'/'+str(len(paysAmerique.keys())))
