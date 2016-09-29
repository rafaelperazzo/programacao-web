# -*- coding: utf-8 -*-
from __future__ import division
import math
#1
a = int(input('Digite o valor de da medida a :'))
b = int(input('Digite o valor de da medida b :'))
c = int(input('Digite o valor de da medida c :'))

#2

if a<b+c:
    print('S')
else: 
    print('N')
if a**2==((b**2)+(c**2)):
    print('Re')
if a**2 > ((b**2)+(c**2)):
    print('Ob')
if a**2 < ((b**2)+(c**2)):
    print('Ac')
if a==b==c:
    print('Eq')
if b==c!=a:
    print('Is')
if a!=b!=c:
    print('Es')
