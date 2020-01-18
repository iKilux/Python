def afficherM():
    lettre = input ()
    lettre = lettre.upper()
    
    if lettre == 'M':
        print('###       ###')
        print('####     ####')
        print('### #   # ###')
        print('###  # #  ###')
        print('###   #   ###')
        print('###       ###')
        print('###       ###')
        
    elif lettre == 'C':
        print(' ############')
        print('###')
        print('###')
        print('###')
        print('###')
        print('###')
        print(' ############')
        
    elif lettre == 'O':
        print(' ########### ')
        print('###       ###')
        print('###       ###')
        print('###       ###')
        print('###       ###')
        print('###       ###')
        print(' ########### ')

    elif lettre == 'N':
        print('####      ###')
        print('#####     ###')
        print('###  #    ###')
        print('###   #   ###')
        print('###    #  ###')
        print('###     #####')
        print('###      ####')

    elif lettre == 'S':
        print('#############')
        print('###       ###')
        print('###          ')
        print('#############')
        print('          ###')
        print('###       ###')
        print('#############')
           
for i in range(26):
    afficherM()