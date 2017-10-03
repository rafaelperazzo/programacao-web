# -*- coding: utf-8 -*-
P1 = float(input('digite o valor de P1: '))
C1 = float(input('digite o valor de C1: '))
P2 = float(input('digite o valor de P2: '))
C2 = float(input('digite o valor de C2: '))
if P1*C1 == P2*C2:
    print('0')
elif P1*C1 > P2*C2:
    print('-1')
elif P1*C2 < P2*C2:
    print('1')

