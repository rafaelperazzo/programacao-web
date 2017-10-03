# -*- coding: utf-8 -*-
from __future__ import division
a = input('Digite a: ')
b = input('Digite b: ')
c = input('Digite c: ')
#COMECE A PARTIR DAQUI!
Delta = (b**2) - (4*a*c)
x1 = ((-b) + (Delta)**0.5) / (2*a)
print('%.2f' %x1)