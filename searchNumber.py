#! /usr/bin/python3
#fonction de verification de numero de telephone
def verifnumber(text):
	if len(text) != 12:
		return False
	for i in range(0, 2):
		if not text[i].isdecimal():
			return False
	if text[2] !='-':
		return False
	for i in range(3,6):
		if not text[i].isdecimal():
			return False
	if text[6] !='-':
		return False
	for i in range(7,9):
		if not text[i].isdecimal():
			return False
	if text[9] !='-':
		return False

	for i in range(10, 12):
		if not text[i].isdecimal():
			return False
	return True
#code permettant de retrouver un numero dans un text 
print('Veuillez saisir du texte. les numeros s\'écrivent sous le format XX-XXX-XX-XX')
message=input()
for i in range(len(message)):
	chunk=message[i:i+12]
	if verifnumber(chunk):
		print('number found '+chunk)
print('Done !')
