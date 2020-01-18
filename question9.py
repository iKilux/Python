#import random
#spam=random.randint(1,3)
spam=0
for i in range(1,5,1):
    if spam==1:
        print('Hello!')
    if spam==2:
        print('Howdy!')
    if spam>2:
        print('Greetings')
    spam=spam+1
