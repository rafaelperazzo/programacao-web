# -*- coding: utf-8 -*-
from __future__ import division
a=float(input('Digite a: '))
b=float(input('Digite b: '))
c=float(input('Digite c: '))
Delta=(b**2)-4*a*c
if Delta<0:
    print('SRR')
else:
    x1=(-b+(Delta**0.5))/2*a
    x2=(-b-(Delta**0.5))/2*a
    print('%.2f' %x1)
    print('%.2f' %x2)


