# -*- coding: utf-8 -*-
P1=float(input('Digite peso da criança do lado esquerdo: '))
P2=float(input('Digite peso da criança do lado direito: '))
C1=float(input('Digite o comprimento da gangorra do lado esquerdo: '))
C2=float(input('Digite o comprimento da gangorra do lado direito: '))
if P1*C1==P2*C2:
    print('0')
elif (P1*C1)>(P2*C2):
    print('-1')
elif (P1*C1)<(P2*C2):
    print('1')

