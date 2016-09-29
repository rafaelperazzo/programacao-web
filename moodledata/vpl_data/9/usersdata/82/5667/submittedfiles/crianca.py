# -*- coding: utf-8 -*-
from __future__ import division

#ENTRADA
P1 = input ('Digite o valor de P1:')
C1 = input ('Digite o valor de C1:')
P2 = input ('Digite o valor de P2:')
C2 = input ('Digite o valor de C2:')

#PROCESSAMNETO E SAIDA

if P1*C1==P2*C2:
    print '('0')'
else:
    if P1*C1>=P2*C2:
        print '('-1')'
    else:
        if P1*C1<=P2*C2:
            print '('1')'
            
    