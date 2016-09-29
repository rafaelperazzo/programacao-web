# -*- coding: utf-8 -*-
from __future__ import division
import math
a=input('digite o valor de a:')
b=input('digite o valor de b:')
c=input('digite o valor de c:')

#processamento
if a**2==b**2+c**2:
    print('re')
    
if a**2>b**2+c**2:
    print('ob')

if a**2<b**2+c**2:
    print('ac')

if a==b==c:
    print('eq')
    
if a==b!=c:
    print('is')

if a!=b!=c:
    print('es')
    
if a<b+c:
    print('s')
    
else:
    print('n')
    


