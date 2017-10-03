# -*- coding: utf-8 -*-
from __future__ import division
a = input('Digite a: ')
b = input('Digite b: ')
c = input('Digite c: ')
#COMECE A PARTIR DAQUI!
delta = float(b**2 - 4*a*c)
if delta<0:
    print('SRR')
else:
    x1=float(-b/(2*a) + (delta**(0.5))/(2*a))
    x2=float(-b/(2*a) - (delta**(0.5))/(2*a))
    print('%.2f' % x1)
    print('%.2f' % x2)