# -*- coding: utf-8 -*-
from __future__ import division
a=float(input('Digite a:'))
b=float(input('Digite b:'))
c=float(input('Digite c:'))
delta=((b)**2-(4*a*c))
if delta>=0:
    X1=(-b+delta**0.5)/2*a
    print('X1:%.f'%X1)
    X2=(-b-delta**0.5)/2*a
    print('X2:%.f'%X2)
else:
    print('não existem raízes')