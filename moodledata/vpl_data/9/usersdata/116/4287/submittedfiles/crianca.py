# -*- coding: utf-8 -*-
from __future__ import division

P1 = input ('insira P1:')
C1 = input ('insira C1:') 
P2 = input ('insira P2:')
C2 = input ('insira C2:')

if P1*C1==P2*C2 :
    print ('0')
else: 
    if P1*C1>P2*C2:
        print ('-1')
    if P1*C1<P2*C2:
        print ('1')