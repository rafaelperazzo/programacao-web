# -*- coding: utf-8 -*-
from __future__ import division
a = float(input( 'digite a: '))
b = float(input( 'digite b: '))
c = float(input( 'digite c: '))
#COMECE A PARTIR DAQUI! calcular equaçao de segundo grau ax^2 + bx + c 
delta = ((b**2) -(4*a*c)) 
print('%.2f' %delta) 
if delta >= 0:
    x1 = ((-b + (delta**(0.5)))/(2*a))
    x2 = ((-b - (delta**(0.5)))/(2*a))
    print('%.2f' %x1)
    print('%.2f' %x2) 
else:
    print('SRR') 
    