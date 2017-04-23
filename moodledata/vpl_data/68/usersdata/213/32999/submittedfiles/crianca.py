# -*- coding: utf-8 -*-
P1=float(input('Informe P1: '))
C1=float(input('Informe C1: '))
P2=float(input('Informe P2: '))
C2=float(input('Informe C2: '))

if P1>((P2*C2)/C1) and C1>((P2*C2)/P1):
    print('-1')
elif P2>((P1*C1)/C2) and C2>((P1*C1)/P2):
    print('1')
else:
    print('0')
