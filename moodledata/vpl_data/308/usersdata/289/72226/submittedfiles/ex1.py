# -*- coding: utf-8 -*-
from __future__ import division
a = input('Digite a: ')
b = input('Digite b: ')
c = input('Digite c: ')
#COMECE A PARTIR DAQUI!
Delta= ((b**2)-4*a*c)
if Delta >= 0:
    raizDelta= Delta**0.5
    x1= (-b+raizDelta)/(2*a)
    print(x1)
    x2= (-b-raizDelta)/(2*a)
    print(x2)
else:
    print('SRR')