# -*- coding: utf-8 -*-
from __future__ import division

P1=input('Digite o peso da criança do lado esquerdo:')
P2=input('Digite o peso da criança do lado direito:')
C1=input('Digite o comprimento da gangorra do lado esquerdo:')
C2=input('Digite o comprimento da gangorra do lado direito:')

if (P1*C1==P2*C2):
    print('0')
    
elif (P1*C1>P2*C2):
    print('-1')
    
else:
    print('1')