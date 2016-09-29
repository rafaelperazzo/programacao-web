# -*- coding: utf-8 -*-
from __future__ import division
a = input('Digite a: ')
b = input('Digite b: ')
c = input('Digite c: ')

delta= (b**2) - (4*a*c)
if delta>0:
    
x1=( -b + math.sqrt(delta))/(2*a)
x2=( -b - math.sqrt(delta))/(2*a)
print ('valor de x1=',x1)
print ('valor de x2=',x2)

if delta <0:
    print('SSR')

    