spam = ['Kaba', 'Mahamadou', 'Amadou', 'Moussa']
table = [1, 2, 3, 5]
def comma(element):
    mot =''
    for i in range (len(element)):
        if i != len(element)-1:
            mot += str(element[i]) + ', '
        else:
            mot += ' and ' + str(element[i])
    print(mot)
comma(spam)
comma(table)
