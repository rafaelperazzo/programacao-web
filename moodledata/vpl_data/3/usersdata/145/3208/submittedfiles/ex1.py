# -*- coding: utf-8 -*-
from __future__ import division
a = input('Digite a:')
b = input('Digite b:')
c = input('Digite c:')

d=(b**2)-(4*a*c)
if d>=0:
    x1=-b+(d**0.5)/2*a
    x2=-b-(d**0.5)/2*a
print ('x1=%.2f'%x1)
print ('x2=%.2f'%x2)

if d<0:   
    print('SRR')

    