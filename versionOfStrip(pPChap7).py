#! usr/bin/python3
'''
import re

wspaceRegex= re.compile(r'^\s+', re.DOTALL)
wspaciRegex= re.compile(r'(\s+)\s$', re.DOTALL)
print('Je parle de la mame oui mame ame la mame de mame')
texte= ' Je parle de la mame oui mame ame la mame de mame '
print()
print('Enter the substituded word')
mot= input()
print('Enter the substitude word')
remp= input()
motRegex = re.compile(mot)

def versOfStrip(texte, mot):
	if mot=='':
		sentence = wspaceRegex.sub('', texte)
		sentence = wspaciRegex.sub('', texte)
		print(sentence)
	else:
		print(motRegex.sub(remp, texte))


versOfStrip(texte,'')
versOfStrip(texte, mot)'''
#code ci dessous plus optimal
import re
phrase = input('Entrer votre texte ')
mot = input('entrer le mot à enlever ')
print(len(phrase))
theRegex = re.compile(r''+mot)
spaceBiginningRegex = re.compile(r'^\s+')
spaceEndingRegex    = re.compile(r'(\s+)\s$')
def regexStrip(sentence, word):
    if word == '':
        sentence0 = spaceBiginningRegex.sub(r''+word, sentence)
        sentence2 = spaceEndingRegex.sub(r''+word, sentence0)
        print(sentence2)
        print(len(sentence2))
    else:
        if word in sentence:
            sentence1 = theRegex.sub(r'', sentence)
            print(sentence1)
        else:
            print(f"le mot \"{word}\" ne se trouve pas dans \"{sentence}\"")
regexStrip(phrase, mot)
