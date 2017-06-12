# -*- coding: utf-8 -*-
N=int(input('digite o numero de postos:'))
M=int(input('digite a distancia maxima media:'))
distancia=42195
prox=0
for i in range (0,N,1):
    n=int(input('distancia dos postos:'))
    if (distancia/N)<=M:
        ante=distancia/N
        prox=prox+ante
if (N*M)>=distancia:
    print('S')
else:
    print('N')