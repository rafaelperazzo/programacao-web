# -*- coding: utf-8 -*-
from __future__ import division
a = input('Digite a: ')
b = input('Digite b: ')
c = input('Digite c: ')
#COMECE A PARTIR DAQUI!
Delta= b**2-4*a*c
raizDelta= Delta**0.5
X1= (-b+raizDelta)/(2*a)
X2= (-b-raizDelta)/(2*a)

if Delta >= 0:
    print('X1= %.2f' % X1)
    print('X2= %.2f' % X2)
if raizDelta < 0:
    print('SRR')