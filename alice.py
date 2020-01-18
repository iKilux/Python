#! /usr/bin/python3
#flow control statement
print('Enter your name')
myName=input()
print('Enter your age')
age=input()
age=int(age)
if myName==('Alice'):
    print('Hi, Alice')
elif age < 12:
    print('You are not Her')
else:
    print('You aint Alice nor a Kid')
    
