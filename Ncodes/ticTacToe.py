
theBoard = {'topL': ' ', 'topM': ' ', 'topR': ' ',
            'midL': ' ', 'midM': ' ', 'midR': ' ',
            'lowL': ' ', 'lowM': ' ', 'lowR': ' '}

#fonctionn d'affichage du tableau
def printBoard(board):
    print(board['topL'] + '|' + board['topM'] + '|' + board['topR'])
    print('-+-+-')
    print(board['midL'] + '|' + board['midM'] + '|' + board['midR'])
    print('-+-+-')
    print(board['lowL'] + '|' + board['lowM'] + '|' + board['lowR'])

#fonction qui permet de voir si 3 cases ont la meme valeur
def verification_case(board):
    if   (board['topL'] != ' ') and (board['topL'] == board['topM'] == board['topR']):
        return True
    elif (board['midL'] != ' ') and (board['midL'] == board['midM'] == board['midR']):
        return True
    elif (board['lowL'] != ' ') and (board['lowL'] == board['lowM'] == board['lowR']):
        return True
    elif (board['topL'] != ' ') and (board['topL'] == board['midM'] == board['lowR']):
        return True
    elif (board['lowL'] != ' ') and (board['lowL'] == board['midM'] == board['topR']):
        return True
    elif (board['topL'] != ' ') and (board['topL'] == board['midL'] == board['lowL']):
        return True
    elif (board['topM'] != ' ') and (board['topM'] == board['midM'] == board['lowM']):
        return True
    elif (board['topR'] != ' ') and (board['topR'] == board['midR'] == board['lowR']):
        return True
    else:
        return False

turn ='X'
move = 'random'
for i in range(9):
    printBoard(theBoard)
    print()
    print('Turn for ' + turn + '. Move on which space ?' + '(' + str(i+1) + ')')
    move = input()
    while theBoard[move] != ' ':
        print(f"La position {move} est occupée !")
        move = input()
    print()
    if theBoard[move] == ' ':
        theBoard[move] = turn
    if turn == 'X':
        turn = 'O'
    else:
        turn = 'X'
    if i > 3 and verification_case(theBoard):
        if turn == 'X':
            turn = 'O'
            print(turn + ' a gagné')
            break
        else:
            turn = 'X'
            print(turn + ' a gagné')
            break
    else:
        continue


printBoard(theBoard)



#les regles du tictactoe
'''si trois cases alignées horizontalemen, verticalement ou obliquement ont la meme
valeur alors le joueur qui y a inserer ses valeurs a gagner'''

'''chaque case est utilisée une seule fois a chaque partie'''
