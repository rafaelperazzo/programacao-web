# -*- coding: utf-8 -*-
from __future__ import division
a = input('Digite a: ')
b = input('Digite b: ')
c = input('Digite c: ')
#COMECE A PARTIR DAQUI!
d = ((b**2)-4*a*c)
x1 = ((b+(d**0.5))/2*a)
x2 = ((b-(d**0.5))/2*a)
if float(d) >= 0:
    print('%.2f\n%.2f'%(x1,x2))
else:
    print('SRR')