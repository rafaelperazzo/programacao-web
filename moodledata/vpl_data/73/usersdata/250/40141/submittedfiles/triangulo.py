# -*- coding: utf-8 -*-
import math
a=int(input('digite o comprimento a:'))
b=int(input('digite o comprimento b:'))
c=int(input('digite o comprimento c:'))
if a<b+c:
    print('S')
    if a**2==(b**2)+(c**2):
        print('Re')
    elif a**2>(b**2)+(c**2):
        print('Ob')
    elif a**2<(b**2)+(c**2):
        print('Ac')
    if a==b and a==c and b==c:
        print('Eq')
    elif b==c and b!=a and a!=c:
        print('Is')
    elif a!=b and a!=c and b!=c:
        print('Es')
else:
    print('N')