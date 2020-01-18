#palindrome
mot = input()
mot = mot.lower()
def palindrome(mot):
    word = ''
    for i in range(len(mot)): 
        word +=mot[len(mot)-i-1]

    if mot == word:
        print(mot + ' est un palindrome')
    else:
        print('Pas de palindrome')

palindrome(mot)

#passingReference
spam =[1, 2, 4]
def all(spam):
    spam.append('OKK')
all(spam)
print(spam)
