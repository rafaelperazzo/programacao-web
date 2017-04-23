# -*- coding: utf-8 -*-
import math
a=int(input('Digite lado 1: '))
b=int(input('Digite lado 2: '))
c=int(input('Digite lado 3: '))
if a<b+c:
    print('S')
    if(a**2)==(b**2+c**2):
        print('Re')
    if (a**2)>(b**2+c**2):
        print('Ob')
    if (a**2)<(b**2+c**2):
        print('Ac')
    if a==b and b==c:
        print('Eq')
    if b==c and c!=a:
        print('Is')
    if a!=b and b!=c:
        print('Es')
else:
    print('N')
