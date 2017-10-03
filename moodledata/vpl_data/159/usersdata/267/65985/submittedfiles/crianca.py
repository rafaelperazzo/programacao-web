# -*- coding: utf-8 -*-
P1 = float(input('Peso da criança que ficará do lado esquerdo: '))
C1 = float(input('Comprimento da gangorra do lado esquerdo: '))
P2 = float(input('Peso da criança que ficará do lado direito: '))
C2 = float(input('Comprimento da gangorra do lado direito: '))
#PROCESSAMENTO
print()
if P1*C1==P2*C2:
    print('0')
if P1*C1>P2*C2:
    print('-1')
if P1*C1<P2*C2:
    print('1')
