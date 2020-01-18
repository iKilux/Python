for i in range (11):
    for j in range (11):
	print('combien font'+str((i+1))+'*'+str(j+1)+'?')
	reponse = input()
	if reponse == (i+1)*(j+1):
            print('OK')
        else:
            print('false')
