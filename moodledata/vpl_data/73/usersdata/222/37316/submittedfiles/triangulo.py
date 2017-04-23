# -*- coding: utf-8 -*-
import math
a=float(input('digite a:'))
b=float(input('digite b:'))
c=float(input('digite c:'))
a>=b>=c
if a<(b+c):
    print('S')
    if (a**2)==(b**2)+(c**2):
        print('Re')
    elif (a**2)>(b**2)+(c**2):
        print('Ob')
    elif (a**2)<(b**2)+(c**2):
        print('Ac')
    elif a==b and b==c:
        print('Eq')
    elif b==c and c!=a:
        print('Is')
    elif a!=b and a!=c:
        print('Es')
else:
    print('N')
        



