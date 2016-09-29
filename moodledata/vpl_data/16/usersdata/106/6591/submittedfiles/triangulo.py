# -*- coding: utf-8 -*-
from __future__ import division
import math
# entrada
a = input ('Digite o valor da maior medida:')
b = input ('Digite o valor da medida intermediária:')
c = input ('Digite p valor da menor medida:')

if a>=(b+c):
    print ('N')
else:
    print ('S')
    if a**2 == (b**2) + (c**2):
        print ('RE')
    if a**2 > (b**2) + (c**2):
        print ('OB')
    if a**2 < (b**2) + (c**2):
        print ('AC')
    if a==b and b==c:
        print ('EQ')
    if b==c and c!=a:
        print ('IS')
    if b!=c and b!=a and c!=a:
        print ('ES')