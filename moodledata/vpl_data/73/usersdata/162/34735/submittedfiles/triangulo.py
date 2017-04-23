a=int(input('Digite a:'))
b=int(input('Digite b:'))
c=int(input('Digite c:'))
if (a>=b>=c) and (a<b+c):
    print('S')
    if (a**2)==(b**2)+(c**2):
        print('Re')
    elif (a**2)>(b**2)+(c**2):
        print('Ob')
    else:
        print('Ac')
    if (a==b==c):
        print('Eq')
    elif (b==b!=a):
        print('Is')
    elif (a!=b!=c):
        print('Es')
else:
    print('N')
 
