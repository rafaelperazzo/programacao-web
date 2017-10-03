# -*- coding: utf-8 -*-
P1= float(input('Digite o peso 1: '))
C1= float(input('Digite o comprimento 1: '))
P2= float(input('Digite o peso 2: '))
C2= float(input('Digite o comprimento 2: '))
if P1*C1=P2*C2:
    print('0')
else:
    if P1*C1>P2*C2:
        print('-1')
    else:
        if P1*C1<P2*C2:
            print('1')