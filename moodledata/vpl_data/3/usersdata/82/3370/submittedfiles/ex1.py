# -*- coding: utf-8 -*-
from __future__ import division
a = input('Digite a: ')
b = input('Digite b: ')
c = input('Digite c: ')

x1= (-b)+((b**2)-4*a*c)**0.5
x2= (-b)-((b**2)-4*a*c)**0.5
   
if ((b**2)-4*a*c)>=0:
    print ('x1 = %d:' %x1)
    print ('x2 = %d:' %x2)
else:
    print ('SRR')
    
