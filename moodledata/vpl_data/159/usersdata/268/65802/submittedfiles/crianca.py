# -*- coding: utf-8 -*-
P1=float(input(' criança 1: '))
C1=float(input(' metragem 1: '))
P2=float(input(' criança 2: '))
C2=float(input(' metragem 2: '))

if (P1*C1>P2*C2):
    print('-1')
elif (P1*C1<P2*C2):
    print('1')
else:
    print('0')