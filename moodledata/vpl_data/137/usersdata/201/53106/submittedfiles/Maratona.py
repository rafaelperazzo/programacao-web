# -*- coding: utf-8 -*-
N=int(input('Número de postos de água::'))
M=int(input('Distância intermediaria máxima:'))
cont=0
v=0
for i in range(0,N,1):
    n=int(input('Distância entre os postos:'))
    if (n-v)<=M:
        cont=cont+1