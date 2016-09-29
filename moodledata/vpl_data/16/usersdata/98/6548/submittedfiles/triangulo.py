# -*- coding: utf-8 -*-
from __future__ import division
import math
a=input('Digite o valor de a: ')
b=input('Digite o valor de b: ')
c=input('Digite o valor de c: ')

if a>=b+c or b>=a+c or c>=a+b:
    print('N')
else: 
    print('S')
    
if (a**2)==(b**2)+(c**2):
    print('Re')
if (a**2)>(b**2)+(c**2):
    print('Ob')
if (a**2)<(b**2)+(c**2):
    print('Ac')
    
if a==b==c:
    print('Eq')
if a==b=!c or a==c=!b or b==c=!a:
    print('Is')
if a=!b=!c:
    print('Es')
    