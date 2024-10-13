first = (input('число 1: '))
second = (input('число 2: '))
third = (input('число 3: '))
if first == second == third:
    print (3)
elif first == second or second == third or first == third:
    print(2)
else:
    print(0)