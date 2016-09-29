# -*- coding: utf-8 -*-
from __future__ import division

P1 = input('Digite P1:')
C1 = input('Digite C1:')
P2 = input('Digite P2:')
C2 = input('Digite C2:')

if P1*C1 > P2*C2:
    print('-1')
elif P1*C1 < P2*C2:
    print('1')
else:
    print('0')
