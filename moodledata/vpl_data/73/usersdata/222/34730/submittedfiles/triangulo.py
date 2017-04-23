# -*- coding: utf-8 -*-
import math
a=float(input('digite a:'))
b=float(input('digite b:'))
c=float(input('digite c:'))
a>=b>=c>0
a<b+c
if (a**2)==(b**2)+(c**2):
    print('Re')
elif (a**2)>(b**2)+(c**2):
    print('Ob')
elif (a**2)<(b**2)+(c**2):
    print('Ac')
if a==b==c:
    print('Eq')
elif b==c!=a:
    print('Is')
elif a!=b!=c:
    print('Es')
