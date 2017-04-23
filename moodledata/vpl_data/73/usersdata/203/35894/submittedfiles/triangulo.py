# -*- coding: utf-8 -*-
import math
a=int(input('digite a: '))
b=int(input('digite b: '))
c=int(input('digite c: '))
if a<(b+c):
    print('S')
    if (a**2)==b**2+c**2:
        print('Re')
    if (a**2)>b**2+c**2:
        print('Ob')
    if (a**2)<b**2+c**2:
        print('Ac')
    if a==b and b==c:
        print('Eq')
    if a==b and b!=c:
        print('Is')
    if a!=b and b!=c:
        print('Es')
else:
    print('N')
