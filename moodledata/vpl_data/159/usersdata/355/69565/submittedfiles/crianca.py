# -*- coding: utf-8 -*-
P1=float(input('Peso da criança a esquerda: '))
C1=float(input('Comprimento da gangorra no lado esquerdo: '))
P2=float(input('Peso da criança a direita: '))
C2=float(input('Comprimento da gangorra no lado direito: '))

if (P1*C1==P2*C2):
    print('0')
if (P1*C1>P2*C2):
    print('-1')
else:
    print('1')

