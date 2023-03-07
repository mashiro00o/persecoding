symbol = input()

if symbol == '<':
    i = '<+&>'
elif symbol == '+':
    i = '+&><'
elif symbol == '&':
    i = '&><+'
else:
    i = '><+&'

print(i * 2)
