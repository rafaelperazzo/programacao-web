# -*- coding: utf-8 -*-
from __future__ import division
import math

a=input('o valor de a: ')
b=input('o valor de b: ')
c=input('o valor de c: ')

if a<b+c:
    print('S')
    if (a**2)==(b**2)+(c**2):
        print('RE')
    if (a**2)>(b**2)+(c**2):
        print('Ob')
    if (a**2)<(b**2)+(c**2):
        print('Ac')
    if (a)==(b)==(c):
        print('Eq')
    if (b)==(c)!=(a):
        print('Is')
    if (a)!=(b)!=(c):
        print('Es')
        
else:
    print('N')
