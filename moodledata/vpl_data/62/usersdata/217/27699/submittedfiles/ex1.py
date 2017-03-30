# -*- coding: utf-8 -*-
from __future__ import division
a = input('Digite a: ')
b = input('Digite b: ')
c = input('Digite c: ')
#COMECE A PARTIR DAQUI!
d=((b**2)-4*a*c)
if d >= 0:
    x1=(-b+(d**1/2))/2*a
    x2=(-b-(d**1/2))/2*a
if d < 0:
        print('SSR')
print('%9.2f %10.2f'%(d,x1,x2))
    