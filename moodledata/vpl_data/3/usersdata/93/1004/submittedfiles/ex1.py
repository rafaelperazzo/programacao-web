# -*- coding: utf-8 -*-
from __future__ import division
a = input('Digite a: ')
b = input('Digite b: ')
c = input('Digite c: ')
#COMECE A PARTIR DAQUI!
delta=(b**2 - 4*a*c)
if delta>=0:
    raizDelta=(delta)**(1/2)
    x1=(-b+raizDelta)/2
    x2=(-b-raizDelta)/2
    print('x1=% \n x2=%' %(x1, x2))
if delta<0:
    print('SSR')
