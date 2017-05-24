a=float(input('digite a:'))
b=float(input('digite b:'))
c=float(input('digite c:'))
if a==b==c:
    print('iguais')
elif a==b or b==c or a==c:
    print('2 iguais')
else:
    print('diferentes')