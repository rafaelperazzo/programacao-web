# -*- coding: utf-8 -*-
P1=float(input('Digite P1:'))
C1=float(input('Digite C1:'))
P2=float(input('Digite P2:'))
C2=float(input('Digite C2:'))
if P1*C1==P2*C2:
    print('0')
elif P1*C1>P2*C2:
    print('-1')
else:
    print('1')
