# -*- coding: utf-8 -*-
from __future__ import division
a = input('Digite a: ')
b = input('Digite b: ')
c = input('Digite c: ')
#COMECE A PARTIR DAQUI!
delta=(b**2 - 4*a*c)**(1/2)
x1=(-b+delta)/2
x2=(-b-delta)/2
if delta>0:
    print('x1=% \n x2=%' %(x1, x2))
if delta<0:
    print('SSR')
