#! usr/bin/python3
import re
phrase = input('Entrer votre texte ')
mot = input('entrer le mot à enlever ')
print(len(phrase))
theRegex = re.compile(r''+mot)
spaceBeginingRegex = re.compile(r'^\s+')
spaceEndingRegex    = re.compile(r'(\s+)\s$')
def regexStrip(sentence, word):
    if word == '':
        sentence0 = spaceBeginingRegex.sub(r''+word, sentence)
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
