# -*- coding: utf-8 -*-
P1=float(input('digite o valor do peso 1:'))
P2=float(input('digite o valor do peso 2:'))
C1=float(input('digite o valor do comprimento 1:'))
C2=float(input('digite o valor do comprimento 2:'))
if P1*C1==P2*C2:
    print('0')
elif P1*C1>P2*C2:
    print(-1)
else:
    print(1)