# -*- coding: utf-8 -*-
from __future__ import division
a = input('Digite a: ')
b = input('Digite b: ')
c = input('Digite c: ')
#COMECE A PARTIR DAQUI!
D=(b**2)-(4*a*c)
if D>=0:
    x1=((-b)+(D**(1/2)))/2*a
    x2=((-b)-(D**(1/2)))/2*a
    print('%f'%x1)
    print('%f'%x2)
else:
    print('SRR')
