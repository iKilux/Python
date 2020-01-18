#strong password
import re 
name = input('Enter your name ')
password = input('Enter your password ')

lowerRegex = re.compile(r'[a-z]')
upperRegex = re.compile(r'[A-Z]')
digitRegex = re.compile(r'[0-9]')


def strongPassword(element):
    if len(element) >= 8 and lowerRegex.search(element) != None and upperRegex.search(element) != None and digitRegex.search(element) != None:
        print('This is a strong password ')
    else:
        print('this is weak')
strongPassword(password)
