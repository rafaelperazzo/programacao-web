# -*- coding: utf-8 -*-
from __future__ import division

p1 = input('Digite P1: ')
c1 = input('Digite C1: ')
p2 = input('Digite P2: ')
c2 = input('Digite C2: ')

if (p1*c1==p2*c2):
    print('0')
elif (p1*c1>p2*c2):
    print('-1')
else:
    print('1')
