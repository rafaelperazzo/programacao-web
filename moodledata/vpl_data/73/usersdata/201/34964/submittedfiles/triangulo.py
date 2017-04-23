# -*- coding: utf-8 -*-
import math
a=float(input('digite um valor'))
b=float(input('digite um valor'))
c=float(input('digite um valor'))
if a<b+c:
    print('S')
    if (a**2)==(b**2)+(c**2):
        print('Re')
    elif (a**2)>(b**2)+(c**2):
        print('Ob')
    elif (a**2)<(b**2)+(c**2):
        print('Ac')
        
else:
    print('N')

