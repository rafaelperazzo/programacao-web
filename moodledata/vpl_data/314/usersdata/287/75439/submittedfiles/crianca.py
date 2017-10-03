# -*- coding: utf-8 -*-
P1=float(input('Digite o peso da criança 1: '))
C1=float(input('Digite o comprimento da gangorra onde a criança 1 esta: '))
P2=float(input('Digite o peso da vriança 2: '))
C2=float(input('Digite o comprimento da gangorra onde a criança 2 esta: '))
if (P1*C1)==(P2*C2):
    print('0')
if (P1*C1)>(P2*C2):
    print('-1')
if (P1*C1)<(P2*C2):
    print('1')
    

