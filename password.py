#! usr/bin/python3

import sys

if len(sys.argv) < 3:
    print('You must enter 2 arguments')
    sys.exit()

account = sys.argv[1]
valeur = int(sys.argv[2])
print(account*valeur)
