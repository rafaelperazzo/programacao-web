# -*- coding: utf-8 -*-
from __future__ import division
a = float(input('Digite a: '))
b = float(input('Digite b: '))
c = float(input('Digite c: '))
#COMECE A PARTIR DAQUI!
d=(b**2)-(4*a*c)
if d>=0:
    x1=(-b+(d**1/2))/2*a
    print('x1 é %.f'%x1)
    x2=(-b-(d**1/2))/2*a
    print('x2 é %.f'%x2)
if d<0:
    print('srr')