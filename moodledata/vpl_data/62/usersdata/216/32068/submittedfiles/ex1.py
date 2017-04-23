# -*- coding: utf-8 -*-
from __future__ import division
a = float(input('Digite a: '))
b = float(input('Digite b: '))
c = float(input('Digite c: '))
#COMECE A PARTIR DAQUI!

delta= (b**2)-(4*a*c)
x1= (-b+(delta)**0.5)/(2*a)
x2= (-b-(delta)**0.5)/(2*a)

if delta>=0:
    print('%.2f'%x1)
    print('%.2f'%x2)
else:
    print('SRR')
    
    