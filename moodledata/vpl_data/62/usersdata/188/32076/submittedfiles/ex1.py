# -*- coding: utf-8 -*-
from __future__ import division
a = input('Digite a: ')
b = input('Digite b: ')
c = input('Digite c: ')
#COMECE A PARTIR DAQUI!
DELTA=|b*b+(-4)*a*c|
X1=(-b+(DELTA**(1/2)))/2*a
X2=(-b-(DELTA**(1/2)))/2*a
if DELTA>=0:
    print('Valor de X1 %.4f'%X1)
    print('Valor de X2 %.4f'%X2)
else:
    print('SRR')