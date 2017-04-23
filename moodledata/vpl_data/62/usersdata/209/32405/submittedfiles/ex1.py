# -*- coding: utf-8 -*-
from __future__ import division
a = float(input('Digite a: '))
b = float(input('Digite b: '))
c = float(input('Digite c: '))
#COMECE A PARTIR DAQUI!
D=(b**2)-(4*a*c)
if D>=0:
    X1=((-b)+(DELTA**(1/2)))/2*a
    print('X1 é %.2f'%X1)
    X2=((-b)-(DELTA**(1/2)))/2*a
    print('X2 é %.2f'%X2)
else:
    print('SRR')

