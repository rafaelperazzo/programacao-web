# -*- coding: utf-8 -*-
P1=float(input('Digite o peso da primeira pessoa:'))
C1=float(input('Digite o comprimento do lado esquerdo:'))
P2=float(input('Digite o peso da segunda pessoa:'))
C2=float(input('Digite o comprimento do lado direito:'))
if (P1*C1)==(P2*C2):
    print('0')
if (P1*C1)>(P2*C2):
    print('-1')
if (P2*C2)>(P1*C1):
    print('1')
    

