# -*- coding: utf-8 -*-
from __future__ import division
a = input('digite a: ')
b = input('digite b: ')
c = input('digite c: ')
d= (b*b)-(4*a*c)
if d>=0:
    x1= ((-b)+(d**0.5))/2*a
    x2= ((-b)-(d**0.5))/2*a
    print (x1)
    print (x2)
else 
    print('sem raizes reais')