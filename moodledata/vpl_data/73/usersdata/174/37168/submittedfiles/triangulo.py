# -*- coding: utf-8 -*-
import math
a = float(input('Comprimento A:'))
b = float(input('Comprimento B:'))
c = float(input('Comprimento C:'))

if a>=b>=c>0 and a<(b+c):
    print('S')
    if (a**2)==(b**2)+(c**2):
        print ('Re')
    elif (a**2)>(b**2)+(c**2):
        print ('Ob')
    elif (a**2)<(b**2)+(c**2):
        print ('Ac')
    elif a==b and b==c:
        print ('Eq')
    elif (b == c)!=a:
        print('Is')
    elif a!=b!=c:
        print ('Es')
else:
    print ('N')
    