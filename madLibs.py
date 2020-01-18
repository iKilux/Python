#! usr/bin/python3

import re, os 

#les regex permettant de  cibler les mots a changer 

adjectiveRegex = re.compile(r'ADJECTIVE')
nounRegex = re.compile(r'NOUN')
verbRegex = re.compile(r'VERB')


#print(content) 							#affichage du contenu du fichier

print('enter an adjective')
adjective = input() 							#va remplacer ADJECTIVE dans file.txt

print('Enter a noun')
noun = input() 								#va remplacer NOUN dans file.txt

print('Enter a verb')
verb = input() 								#va remplacer VERB dans file.txt

print('Enter a noun ')
noun1 = input() 							#va remplacer NOUN dans file.txt

fileName = open('file.txt', 'r') 					#ouverture du fichier en mode lecture
content = fileName.read() 						#lecture du contenu du fichier 
fileName.close()							#fermeture du fichier

fileName = open('file.txt', 'w') 					#ouverture du fichier en mode ecriture
fileName.write(adjectiveRegex.sub(adjective, content))			#remplacement de ADJECTIVE
fileName.close()

fileName = open('file.txt', 'r')
contentA = fileName.read()
fileName.close()

fileName = open('file.txt', 'w')
fileName.write(verbRegex.sub(verb, contentA))
fileName.close()

fileName = open('file.txt', 'r')
contentB = fileName.read()
fileName.close()

fileName = open('file.txt', 'w')
fileName.write(nounRegex.sub(noun, contentB, 1))
fileName.close()

fileName = open('file.txt', 'r')
contentC = fileName.read()
fileName.close()

fileName = open('file.txt', 'w')
fileName.write(nounRegex.sub(noun1, contentC, 1))
fileName.close()

fileName = open('file.txt', 'r')
contentD = fileName.read()
fileName.close()

print(contentD)
