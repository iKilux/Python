def spam(div):
    try:
        return 100/div
    except ZeroDivisionError:
        print('Error: Impossible de diviser par 0')
        
print(spam(2))
print(spam(1))
print(spam(0))
print(spam(100))
    
