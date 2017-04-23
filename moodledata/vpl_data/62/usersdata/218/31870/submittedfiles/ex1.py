# -*- coding: utf-8 -*-
from __future__ import division
a =float(input('Digite a:'))
b =float(input('Digite b:'))
c =float(input('Digite c:'))
Delta=(b*b)*(-4)*a*c
if Delta>0:
    x1=((-b)+(Delta**(1/2)))/(2*a)
    X2=((-b)-(Delta**(1/2)))/(2*a)
    print('X1%.2f'%X1)
    print('X2%.2f'%X2)
else:
    print('SRR')
    