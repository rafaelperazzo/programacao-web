# -*- coding: utf-8 -*-
P1 = float(input("Digite o peso (Kg) da criança à esquerda: "))
C1 = float(input("Digite o comprimento do lado esquerdo: "))
P2 = float(input("Digite o peso (Kg) da criança à direita: "))
C2 = float(input("Digite o comprimento do lado direito: "))
((P1*C1)=(P2*C2))
if P1*C1==P2*C2:
    print('0')
if  P1*C1>P2*C2:
    print('-1')
if  P1*C1<P2*C2:
    print('1')
