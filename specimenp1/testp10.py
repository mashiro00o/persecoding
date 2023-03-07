i = input()
icecream = i.count('I')
milk = i.count('M')
icecubes = i.count('C')
whippedcream = i.count('W')

if icecream < 2:
    print('I')
elif milk < 1:
    print('M')
elif icecubes < 3:
    print('C')
elif whippedcream < 1:
    print('W')
