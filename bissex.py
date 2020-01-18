#! usr/bin/python3
print('inserer une année')
annee = int(input())

if annee%400 == 0 or (annee%4 == 0 and annee%100 !=0):
    print(str(annee)+ ' est une année bissextile')
else:
    print(str(annee)+ ' n\'est pas bissextile')
