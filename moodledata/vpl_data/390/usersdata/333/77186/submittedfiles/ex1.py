# -*- coding: utf-8 -*-
from __future__ import division
a = input('Digite a: ')
b = input('Digite b: ')
c = input('Digite c: ')
#COMECE A PARTIR DAQUI!
x1 = (((-b) + (Delta)**0.5) / (2*a))
x2 = (((-b) - (Delta)**0.5) / (2*a))
Delta = ((b**2) - (4*a*c))
if Delta >= 0 :
    print('x1 = %.2f and x2 = %.2f' %x1 %x2)
else:
    print('SRR')
