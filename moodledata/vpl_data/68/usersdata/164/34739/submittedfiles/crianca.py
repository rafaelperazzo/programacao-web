# -*- coding: utf-8 -*-
P1=float(input('Digite o peso da criança do lado esquerdo: '))
C1=float(input('Digite o comprimento da gangorra do lado esquerdo: '))
P2=float(input('Digite o peso da criança do lado direito: '))
C2=float(input('Digite o comprimento da gangorra do lado direito: '))
l1=P1*C1
l2=P2*C2
if (l1>l2):
    print('-1')
elif (l2>l1):
    print('1')
else:
    print('0')
