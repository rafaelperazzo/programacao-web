# -*- coding: utf-8 -*-
from __future__ import division
import math

c=int(inpu('valor positivo para c: ')
b=int(inpu('valor para b maior ou igual ao de c: ')
a=int(inpu('valor para a maior ou igual ao de b: ')

if a>(b+c):
    print('N')
if a<(b+c):
    print('S')
    if (a**2)==(b**2)+(c**2):
        print('Re')
    if (a**2)>(b**2)+(c**2):   
        print('Ob')
    if (a**2)<(b**2)+(c**2):
        print('Ac')