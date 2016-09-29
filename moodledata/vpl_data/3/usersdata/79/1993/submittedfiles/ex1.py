# -*- coding: utf-8 -*-
from __future__ import division
a = input('Digite a: ')
b = input('Digite b: ')
c = input('Digite c: ')
#COMECE A PARTIR DAQUI!
delta = float(b**2) - (4*a*c)

if delta >= 0:
    x1 = ((-b) - (delta**0.5))/(2*a)
    x2 = ((-b) - (delta**0.5))/(2*a)
    
    print('Valor de x1: ') +str(x1)
    print('Valor de x2: ') +str(x2)
    
else: 
    print('SRR')