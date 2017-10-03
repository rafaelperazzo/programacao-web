# -*- coding: utf-8 -*-

P1= float(input('Digite o peso esquerdo:'))
C1= float(input('Digite o comprimento esquerdo:'))
P2= float(input('Digite o peso direito:'))
C2= float(input('Digite o comprimento direito:'))

if (P1*C1==P2*C2):
    print('0')

if (P1*C1>P2*C2):
    print('-1')

if (P1*C1<P2*C2):
    print('1')


