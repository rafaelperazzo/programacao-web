# -*- coding: utf-8 -*-
from __future__ import division
a = float(input('Digite a: '))
b = float(input('Digite b: '))
c = float(input('Digite c: '))
#COMECE A PARTIR DAQUI!
DeltaH = (b**2)-(4*a*c)
if DeltaH >=0:
    x1 = (-b+DeltaH)/(2*a)
    x2 = (-b+DeltaH)/(2*a)
print ('x1= %.2f' % x1)
print ('x2= %.2f' % x2)
if DeltaH <0 : 
    x1 = (-b+DeltaH)/(2*a)
    x2 = (-b+DeltaH)/(2*a)
print ('SRR')