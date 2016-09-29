# -*- coding: utf-8 -*-
from __future__ import division
a = input('Digite a: ')
b = input('Digite b: ')
c = input('Digite c: ')
#COMECE A PARTIR DAQUI!
z = float  ((b**2)-(4*a*c))
x=(-b)+(z**0.5)/(2*a)
y=(-b)-(z**0.5)/(2*a)
if z >= 0:
 print x, y, "As raizes sao:"
else:
 print("SRR")



