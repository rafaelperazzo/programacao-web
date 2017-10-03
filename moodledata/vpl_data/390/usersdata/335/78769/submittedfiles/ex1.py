# -*- coding: utf-8 -*-
from __future__ import division
#COMECE A PARTIR DAQUI!
a = float(input('digite um valor para a '))
b = float(input('digite um valor para b '))
c = float(input('digite valor para c '))
delta = (b**2)-4*a*c
print(delta)
if delta>=0:
    x1 = (-b+delta**0.5)/2*a
    x2 = (-b-delta**0.5)/2*a
else:
    print('ssr')