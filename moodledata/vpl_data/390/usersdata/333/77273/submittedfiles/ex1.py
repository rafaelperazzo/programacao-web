# -*- coding: utf-8 -*-
from __future__ import division
a = input('Digite a: ')
b = input('Digite b: ')
c = input('Digite c: ')
#COMECE A PARTIR DAQUI!
x = (b**2) - (4*a*c)
if x < 0 :
    print('SRR')
x1 = ((-b) + x**(0.5)/(2*a))
x2 = ((-b) - x**(0.5)/(2*a))
else:
    x=math.sqrt(x)
    x1 = (-b+x)/(2*a)
    x2 = (-b-x)/(2*a)
    print("\n\nx' %s \nx' ' = % x1, x2)
    

   