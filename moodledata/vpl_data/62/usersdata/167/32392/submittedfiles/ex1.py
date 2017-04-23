# -*- coding: utf-8 -*-
from __future__ import division
a = float(int('Digite a: '))
b = float(int('Digite b: '))
c = float(int('Digite c: '))
#COMECE A PARTIR DAQUI!
d=(b**2)-(4*a*c)
if d>=0:
    x1=(-b+(d**1/2))/2*a
    print('x1 é %'%x1)
    x2=(-b-(d**1/2))/2*a
    print('x2 é %'%x2)
    else d<0:
        print('SRR')
