# -*- coding: utf-8 -*-
N=int(input('digite o numero de postos:'))
M=int(input('digite a distancia maxima media:'))
distancia=42195
for i in range (1,N,1):
    n=int(input('distancia dos postos:))
    if n<=M and (N*M)>=distancia:
        print('S')
    else:
        print('N')