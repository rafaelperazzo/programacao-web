# -*- coding: utf-8 -*-
import math
a=int(input('digite a:'))
b=int(input('digite b:'))
c=int(input('digite c:'))
if a<b+c:
    print('S')
    if (a**2)==(b**2)+(c**2):
        print('RE')
    if (a**2)>(b**2)+(c**2):
        print('OB')
    if (a**2)<(b**2)+(c**2):
        print('AC')
else:
    print('N')