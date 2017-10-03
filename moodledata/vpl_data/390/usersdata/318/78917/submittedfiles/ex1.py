# -*- coding: utf-8 -*-
from __future__ import division
a = float(input('Digite a: '))
b = float(input('Digite b: '))
c = float(input('Digite c: '))
#COMECE A PARTIR DAQUI!

delta = (b**2)-4*a*c
x1 = (-b+delta)/(2*a)
x2 = (-b-delta)/(2*a)

if delta==0:
    print'x1:'(x1)
if delta>0:
    print'x1:'(x1)
    print'x2:'(x2)
if delta<0:
    print('SRR')

print(delta)
print(x1)
print(x2)
