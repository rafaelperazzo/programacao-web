# -*- coding: utf-8 -*-
from __future__ import division
import math
a=input('digite o valor de a:')
b=input('digite o valor de b:')
c=input('digite o valor de c:') 
if (a<(b+c)):
    print('S')
    if (a**2)==(b**2)+(c**2):
        print('Re')
    if (a**2)>(b**2)+(c**2):
        print('Ob')
    if (a**2)<(b**2)+(c**2):
        print('Ac')
    if (a==b) and (a==c) and (b==c):
        print('Eq')
    if (b==c) and (c!=a):
        print('Is')
    if (a!=b!=c):
        print('Es')
else:
    print('N')