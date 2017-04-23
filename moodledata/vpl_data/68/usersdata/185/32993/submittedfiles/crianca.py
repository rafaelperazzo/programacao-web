# -*- coding: utf-8 -*-
P1=float(input('digite peso 1:'))
P2=float(input('digite peso 2:'))
C1=float(input('digite comprimento 1:'))
C2=float(input('digite comprimento 2:'))
E1=(P1*C1)
E2=(P2*C2)
if E1==E2:
    print('0')
if E1>E2:
    print('-1')
if E1<E2:
    print ('1')

