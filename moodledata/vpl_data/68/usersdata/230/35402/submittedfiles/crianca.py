# -*- coding: utf-8 -*-
P1=float(input('Digite peso da criança(lado esquerdo): '))
P2=float(input('Digite peso da criança(lado direito): '))
C1=float(input('Digite comprimento da gangorra(lado esquerdo): '))
C2=float(input('Digite comprimento da gangorra(lado direito): '))
if (P1*C1)==(P2*C2):
    print('0')
elif (P1*C1)>(P2*C2):
    print('-1')
else:
    print('1')

