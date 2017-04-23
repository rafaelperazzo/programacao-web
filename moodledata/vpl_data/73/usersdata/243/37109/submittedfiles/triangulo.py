# -*- coding: utf-8 -*-
import math
a=int(input('dig a:'))
b=int(input('dig b:'))
c=int(input('dig c:'))

a>=b>=c>0

if a<b+c:
    print('N')
else:
    print('N')
if a<b+c:
    if (a**2)==(b**2)+(c**2):
        print('Re')
    if (a**2)>(b**2)+(c**2):
        print('Ob')
    if (a**2)<(b**2)+(c**2):
        print('Ac')
    if a==b==c:
        print('Eq')
    if b==c!=a:
        print('Is')
    if (a!=b) and (b!=c):
        print('Es')