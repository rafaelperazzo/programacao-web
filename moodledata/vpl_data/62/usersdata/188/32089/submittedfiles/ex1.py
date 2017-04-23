# -*- coding: utf-8 -*-
from __future__ import division
a = float(input('Digite a: '))
b = float(input('Digite b: '))
c = float(input('Digite c: '))
#COMECE A PARTIR DAQUI!
DELTA=(b**2)-(4*a*c)
X1=(-b+(DELTA**(1/2)))/2*a
X2=(-b-(DELTA**(1/2)))/2*a
if DELTA>=0:
    print('Valor de X1 %.4f'%X1)
    print('Valor de X2 %.4f'%X2)
else:
    print('SRR')