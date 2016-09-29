# -*- coding: utf-8 -*-
from __future__ import division
P1=input('informe o valor do peso P1:')
C1=input('informe o valor do peso C1:')
P2=input('informe o valor do comprimento P2:')
C2=input('informe o valor do comprimento C2:')
if ((P1*C1)>(P2*C2)):
    print('1')
if ((P1*C1)==(P2*C2)):
    print('0')
if ((P1*C1)<(P2*C2)):
    print('-1')
