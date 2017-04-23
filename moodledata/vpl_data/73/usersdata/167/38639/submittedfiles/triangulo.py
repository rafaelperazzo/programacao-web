# -*- coding: utf-8 -*-
import math
a=int(input('digite a:'))
b=int(input('digite b:'))
c=int(input('digite c:'))
if a<b+c:
    if (a**2)==(b**2)+(c**2):
        print('ret')
    if (a**2)>(b**2)+(c**2):
        print('obt')
    if (a**2)<(b**2)+(c**2):
        print('acu')
else:
    print('N')