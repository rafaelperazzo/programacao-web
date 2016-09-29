# -*- coding: utf-8 -*-
from __future__ import division
P1 = input('Digite o peso da criança da esquerda: ')
P2 = input('Digite o peso da criança da direita: ')
C1 = input('Digite o comprimento do lado esquerdo: ')
C2 = input('Digite o comprimento do lado direito: ')
if P1*C1 == P2*C2:
    print('0')
elif P1*C1 > P2*C2:
    print('-1')
else:
    print('1')