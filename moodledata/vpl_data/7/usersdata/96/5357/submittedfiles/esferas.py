# -*- coding: utf-8 -*-
from __future__ import division

A = input('Digite o valor do peso da esfera A:')
B = input('Digite o valor do peso da esfera B:')
C = input('Digite o valor do peso da esfera C:')
D = input('Digite o valor do peso da esfera D:')

if A == B + C + D and D == B + C and B == C:
    print('S')
else:
    print('N')