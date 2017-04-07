# -*- coding: utf-8 -*-
from __future__ import division
a = input('Digite a: ')
b = input('Digite b: ')
c = input('Digite c: ')
#COMECE A PARTIR DAQUI!
DELTA=(b**2)-(4*a*c)
X1=(-b+(DELTA)**1/2)/2*a
X2=(-b-(DELTA)**1/2)/2*a
if DELTA>=0:
    PRINT('X1=%.2f'%X1)
    PRINT('X2=%.2f'%X2)
else:
    print('SRR')