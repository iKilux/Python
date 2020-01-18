#! /usr/bin/python3
import pyperclip
text=pyperclip.paste()
lines= text.split('\n')
for i in range(len(lines)):
	lines[i]=' * '+lines[i]
text= ('\n').join(lines)
pyperclip.copy(text)

#Le code que j'ai ecrit: mais ce n'est pas optimal
'''for name in text.split('\n'):
	name='* '+name+'\n'
	while '*' not in text:
		text=''
		break
	text+=name'''

#la liste qu' il fallait copier 
'''Lists of animals
Lists of aquarium life
Lists of biologists by author abbreviation
Lists of cultivars'''