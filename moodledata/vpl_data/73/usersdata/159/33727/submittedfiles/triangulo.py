# -*- coding: utf-8 -*-
import math
n1=int(input('Digite o primeiro número:'))
n2=int(input('Digite o segundo número:'))
n3=int(input('Digite o terceiro número:'))

if n1>=n2 and n1>=n3:
    a=n1
    if n2>=n3:
        b=n2 and c=n3
    else:
        b=n3 and c=n2
elif n2>=n1 and n2>=n3:
    a=n2
    if n1>=n3:
        b=n1 and c=n3
    else:
        b=n3 and c=n1
elif n3>=n2 and n3>=n1:
    a=n3
    if n2>=n1:
        b=n2 and c=n1
    else:
        b=n1 and c=n2

if a<b+c:
    print('S')
    if (a*a)==(b*b)+(c*c):
        print('Re')
    elif (a*a)>(b*b)+(c*c):
        print('Ob')
    elif (a*a)<(b*b)+(c*c):
        print('Ac')
    elif a==b and a==c:
        print('Eq')
    elif b==c and b!=a:
        print('Is')
    elif a!=b and a!=c and b!=c:
        print('Es')
else:
    print('N')