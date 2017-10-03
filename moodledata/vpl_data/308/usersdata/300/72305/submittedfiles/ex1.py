# -*- coding: utf-8 -*-
from __future__ import division
a = float(input('Digite a: '))
b = float(input('Digite b: '))
c = float(input('Digite c: '))
#COMECE A PARTIR DAQUI!
D = b**2 - 4 * a * c
s1 = (- b + D**0,5)
s2 = (- b - D**0,5)
x1 = s1/2*a
x2 = s2/2*a
if D >= 0:
    print(x1)
    print(x2)
else:
    print("SRR")