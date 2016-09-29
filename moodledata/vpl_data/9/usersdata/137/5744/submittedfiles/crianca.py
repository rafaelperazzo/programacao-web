# -*- coding: utf-8 -*-
from __future__ import division

P1=input('digite o peso da criança 1:')
C1=input('digite o comprimento 1:')
P2=input('digite o peso da criança 2:')
C2=input('digite o comprimento 2:')
if P1*C1==P2*C2:
    print('0')
elif (P1*C1)>(P2*C2):
    print('-1')
else:
    print('+1')