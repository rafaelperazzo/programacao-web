# -*- coding: utf-8 -*-
from __future__ import division
#entrada
P1=input('digite valor de P1:')
C1=input('digite valor de C1:')
P2=input('digite valor de P2:')
C2=input('digite valor de C2:')
#processamento
P1*C1==P2*C2

if P1*C1==P2*C2:
    print ('0')
    
if P1*C1<P2*C2:
    print('-1')
    
if P1*C1>P2*C2:
    print('1')