# -*- coding: utf-8 -*-
from __future__ import division

P1=input('Digite o peso da criança do lado esquerdo:')
C1=input('Digite o comprimento do lado esquerdo da gangorra:')
P2=input('Digite o peso da criança do lado direito:')
C2=input('Digite o comprimento do lado direito da gangorra:')

if (P1*C1)==(P2*C2):
    print('0')
if (P1*C1)>(P2*C2):
    print('-1')
if (P1*C1)<(P2*C2):
    print('1')

