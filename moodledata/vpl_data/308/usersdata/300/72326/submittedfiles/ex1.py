# -*- coding: utf-8 -*-
from __future__ import division
a = float(input('Digite a: '))
b = float(input('Digite b: '))
c = float(input('Digite c: '))
#COMECE A PARTIR DAQUI!
D = b**2 - 4 * a * c
r1 = - b + D**0,5
r2 = - b - D**0,5
x1 = r1/(2*a)
x2 = r2/(2*a)
if D >= 0:
    print(x1)
    print(x2)
else:
    print("SRR")