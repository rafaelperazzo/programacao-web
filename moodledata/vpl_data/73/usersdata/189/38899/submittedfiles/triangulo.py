# -*- coding: utf-8 -*-
import math
a=int(input('digite o a:'))
b=int(input('digite o b:'))
c=int(input('digite o c:'))
if a<b+c:
    print('s')
    if (a**2)==(b**2)+(c**2):
        print('Re')
    elif (a**2)>(b**2)+(c**2):
        print('Ob')
    elif (a**2)<(b**2)+(c**2):
        print('Ac')
    if a==b==c:
        print('Eq')
    elif a==b!=c:
        print('Is')
    elif a!=b!=c:
        print('Ec')
else:
    print('n')

