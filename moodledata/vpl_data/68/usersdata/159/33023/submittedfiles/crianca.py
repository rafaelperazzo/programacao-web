# -*- coding: utf-8 -*-
P1=float(input('Peso da criança da esquerda:'))
C1=float(input('Comprimento do lado esquerda da gangorra:'))
P2=float(input('Peso da criança da direita:'))
C2=float(input('Comprimento do lado direito da gangorra:'))

if (P1*C1)==(P2*C2):
    print('0')
elif (P1*C1)>(P2*C2):
    print('-1')
else:
    print('1')