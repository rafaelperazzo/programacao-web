# -*- coding: utf-8 -*-
from __future__ import division

#entrada
P1 = input('digite o valor do peso da criança do lado esquerdo:)
P2 = input('digite o valor do peso da criança do lado direito:)
C1 =  input('digite o valor do comprimento da gangorra do lado esquerdo:)
C2 = input('digite o valor do comprimento da gangorra do lado direito:)

#processamento e saida
if P1*C1==P2*C2:
    print('0')
elif P1*C1>P2*C2:
    print('-1')
elif P1*C1<P2*C2:
    print('1')
