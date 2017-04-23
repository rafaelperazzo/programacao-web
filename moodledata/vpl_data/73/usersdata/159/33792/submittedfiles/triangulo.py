# -*- coding: utf-8 -*-
import math
a=int(input('Digite o primeiro número:'))
b=int(input('Digite o segundo número:'))
c=int(input('Digite o terceiro número:'))

if a<b+c:
    print('S')
    if (a*a)==(b*b)+(c*c):
        print('Re')
    elif (a*a)>(b*b)+(c*c):
        print('Ob')
    elif (a*a)<(b*b)+(c*c):
        print('Ac')
    if a==b and a==c:
        print('Eq')
    elif b==c and b!=a:
        print('Is')
    elif a!=b and a!=c and b!=c:
        print('Es')
else:
    print('N')