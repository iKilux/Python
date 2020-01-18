theBoard={'A': ' ', 'B': ' ', 'C': ' ',
	'D': ' ', 'E': ' ','F': ' ',
	'G': ' ', 'H': ' ', 'I': ' '}
theBoard1={'A': 'A', 'B': 'B', 'C': 'C',
	'D': 'D', 'E': 'E','F': 'F',
	'G': 'G', 'H': 'H', 'I': 'I'}

'''
A:top-L
B:top-M
C:top-R
D:mid-L
E:mid-M
F:mid-R
G:low-L
H:low-M
I:low-R
'''
def printBoard(board):
    print(theBoard['A']+'|'+theBoard['B']+'|'+theBoard['C'])
    print('-+-+-')
    print(theBoard['D']+'|'+theBoard['E']+'|'+theBoard['F'])
    print('-+-+-')
    print(theBoard['G']+'|'+theBoard['H']+'|'+theBoard['I'])

turn='X'
for i in range(9):
    printBoard(theBoard)
    print('Turn for '+ turn +'. Move on which space? ')
    move=input()
    theBoard[move]= turn
    if turn == 'X':
        turn='O'
    else:
        turn='X'
printBoard(theBoard)

