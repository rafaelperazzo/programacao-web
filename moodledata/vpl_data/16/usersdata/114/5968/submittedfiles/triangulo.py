# -*- coding: utf-8 -*-
from __future__ import division
import math

a=int(input('valor positivo para a: '))
b=int(input('valor positivo (menor ou igual que a) para b : '))
c=int(input('valor positivo (menor ou igual que b) para c : '))

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