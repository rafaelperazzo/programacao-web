# -*- coding: utf-8 -*-
P1=float(input('digite peso da criança do lado esquerdo:'))
C1=float(input('digite o comprimento da gangorra do lado esquerdo:'))
P2=float(input('digite o peso da criança do lado direito:'))
C2=float(input('digite o comprimento da gangorra do lado direito:'))
if P1*C1==P2*C2:
    print('0')
if P1*C1>P2*C2:
    print('-1')
if P1*C1<P2*C2:
    print('1')

