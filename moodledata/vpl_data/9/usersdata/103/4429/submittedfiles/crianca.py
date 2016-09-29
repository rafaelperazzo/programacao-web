# -*- coding: utf-8 -*-
from __future__ import division
p1=input('Insira P1:')
c1=input('Insira C1:')
p2=input('Insira P2:')
c2=input('Insira C2:')
if p1*c1==p2*c2:
    print('0')
if p1*c1>p2*c2:
    print('-1')
if p1*c1<p2*c2:
    print('1')
