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
    if (a**2)>(b**2)+(c**2):
        print('Ob')
    if (a**2)<(b**2)+(c**2):
        print('Ac')
    if a==b and b==c:
        print('Eq')
    if b==c and c!=a:
        print('Is')
    if a!=b and a!=c:
        print('Es')
else:
    print('N')
        



