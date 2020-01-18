#! usr/bin/python3 
import re

upperRegex= re.compile(r'[A-Z]')
lowerRegex= re.compile(r'[a-z]')
digitRegex= re.compile(r'\d')

print('Enter a password')
mdp= input()

def upperLowerDigit(mdp):
	majuscule = upperRegex.search(mdp)
	miniscule = lowerRegex.search(mdp)
	digit     = digitRegex.search(mdp)
	
	if len(mdp) < 7: 
		print('invalid password !')
	else:
		if  majuscule!= None and miniscule!= None and digit!= None:
			print('Strong password !')
		else:
			print('Weak password !')

upperLowerDigit(mdp)