# -*- coding: utf-8 -*-
from __future__ import division
a = float(input('Digite a: '))
b = float(input('Digite b: '))
c = float(input('Digite c: '))
#COMECE A PARTIR DAQUI!
D = b**2 - 4 * a * c

x1 = (-b + D**0,5)/(2*a)
x2 = (-b - D**0,5)/(2*a)
if D >= 0:
    print('%.2f' % x1)
    print('%.2f' % x2)
else:
    print("SRR")