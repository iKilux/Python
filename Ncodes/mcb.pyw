#! /usr/bin/python3
#projet 2 chapitre 8 : automateTheBoringStuffsWithPython
import shelve, sys, pyperclip

mcbShelf = shelve.open('mcb')
if len(sys.argv) == 3:
    if sys.argv[1].lower() == 'save':
        mcbShelf[sys.argv[2]] = pyperclip.paste()
    elif sys.argv[1].lower() == 'delete':
        del mcbShelf[sys.argv[2]]
elif len(sys.argv) == 2:
    if sys.argv[1].lower() == 'list':
        pyperclip.copy(str(list(mcbShelf.keys())))
        print(str(list(mcbShelf.keys())))
    elif sys.argv[1].lower() == 'deleteall':
        while True:
            if len(list(mcbShelf.keys())) != 0:
                for i in range(len(list(mcbShelf.keys()))):
                    for name in list(mcbShelf.keys()):
                        del mcbShelf[name]
            else:
                break
    elif sys.argv[1] in mcbShelf:
        pyperclip.copy(mcbShelf[sys.argv[1]])
else:
    print('There is less or too much argument')
mcbShelf.close()
