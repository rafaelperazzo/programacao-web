 -*- coding: utf-8 -*-
V=int(input('digite o volume inicial: '))
T=int(input('digite a quantidade de trocas: '))
for in range (0,T,1):
    A_i=int(input('digite as trocas de volume: '))
    VT=V+A_i
    if VT>100:
        VT=100
    elif VT<0:
        VT=0
    else:
        VT=VT
print(VT)