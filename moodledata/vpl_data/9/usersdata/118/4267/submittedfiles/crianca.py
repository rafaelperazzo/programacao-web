# -*- coding: utf-8 -*-
from __future__ import division

#1
P1 = input('Digite o valor do peso 1:')
C1 = input('Digite o valor do comprimento 1:')
P2 = input('Digite o valor do peso 2:')
C2 = input('Digite o valor do comprimento 2:')


#2
if P1*C1 == P2*C2 :
    print('0')
if P1*C1 > P2*C2 :
    print('-1')
if P1*C1 < P2*C2 :
    print('1')