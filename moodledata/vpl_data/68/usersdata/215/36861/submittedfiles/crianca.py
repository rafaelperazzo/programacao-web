# -*- coding: utf-8 -*-
P1=float(input('Peso esquerda:'))
C1=float(input('comprimento  esquerda:'))
P2=float(input('Peso direita:'))
C2=float(input('comprimento direita:'))
if P1*C1==P2*C2:
    print('0')
elif P1*C1>P2*C2:
    print('-1')
else :
    print('1')