# -*- coding: utf-8 -*-
from __future__ import division

a = input ('Digite a: ')
b = input ('Digite b: ')
c = input ('Digite c: ')

delta = ((b**2)-(4*a*c))

if (delta=>0):
    x1 = (-b+(delta**0.5))/(2*a)
    x2 = (-b-(delta**0.5))/(2*a)
    
    print ('%.2f' %x1)
    print ('%.2f' %x2)

else:
    print ('SRR')