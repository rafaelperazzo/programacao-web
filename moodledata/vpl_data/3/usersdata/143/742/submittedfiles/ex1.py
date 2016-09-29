# -*- coding: utf-8 -*-
from __future__ import division
a = input('Valor de a')
b = input('Valor de b')
c = input('Valor de c')

delta = (b)**2-4*a*c
x1 = (-b+delta**0.5)/2*a
x2 = (-b-delta**0.5)/2*a

if (delta<0):
    print ('A equação não pussui raízes reais')
else:
    print('%f.2'%x1)
    print('%f.2'%x2)
    
    


