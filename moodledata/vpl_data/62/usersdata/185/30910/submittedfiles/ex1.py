# -*- coding: utf-8 -*-
from __future__ import division
a =int(input('Digite a: '))
b =int(input('Digite b: '))
c =int(input('Digite c: '))
DeltaH=(b*b)-(4*a*c)
x1=(-b+(DeltaH)**0.5)/2*a
x2=(-b-(DeltaH)**0.5)/2*a
if DeltaH>=0:
    print(x1)
    print(x2)
else:
    print('SRR')
