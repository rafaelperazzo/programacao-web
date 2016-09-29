# -*- coding: utf-8 -*-
from __future__ import division
import math
a=input('Digite o valor de a: ')
b=input('Digite o valor de b: ')
c=input('Digite o valor de c: ')
d=input('Digite o valor de d: ')

contador=0

if (a>b):
    print('S')

contador=(contador+1)

elif (b>a and b>c):
    print('S')

contador=(contador+1)

elif (c>b and c>d):
    print('S')

contador=(contador+1)

elif (d>c):
    print('S')
 
contador=(contador+1)   

elif (contador>1):
    print('N')
