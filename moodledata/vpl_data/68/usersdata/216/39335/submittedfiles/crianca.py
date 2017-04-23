# -*- coding: utf-8 -*-
P1=float(input('Digite o peso:'))
C1=float(input('Digite o comprimento:'))
P2=float(input('Digite o peso:'))
C2=float(input('Digite o comprimento:'))

if (P1*C1)==(P2*C2):
    print('0')
elif (P1*C1)>(P2*C2):
    print('-1')
else:
    print('1')


