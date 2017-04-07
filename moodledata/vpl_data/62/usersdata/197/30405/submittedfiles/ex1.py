# -*- coding: utf-8 -*-
from __future__ import division
a = float(input('Digite a: '))
b = float(input('Digite b: '))
c = float(input('Digite c: '))
#COMECE A PARTIR DAQUI!
DELTA=(b*b)+(-4*a*c)
X1=(-b+(DELTA)**(1/2))/2*a
X2=(-b-(DELTA)**(1/2))/2*a
if DELTA>=0:
    PRINT('X1=%.2f'%X1)
    PRINT('X2=%.2f'%X2)
else:
    print('SRR')