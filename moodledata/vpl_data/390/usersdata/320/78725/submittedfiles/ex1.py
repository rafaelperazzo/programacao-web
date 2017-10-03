# -*- coding: utf-8 -*-
from __future__ import division
a = input('Digite a: ')
b = input('Digite b: ')
c = input('Digite c: ')
#COMECE A PARTIR DAQUI!
delta = (b**2) - (4*a*c)
if delta >= 0:
    X1 = (-b + delta**(1/2))/(2*a)
    X2 = (-b - delta**(1/2))/(2*a)
    print ('%.2f' %X1)
    print ('%.2f' %X2)
else:
    print ('Sem raizes reais')