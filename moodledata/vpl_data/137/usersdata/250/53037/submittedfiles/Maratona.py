# -*- coding: utf-8 -*-
N=int(input('digite o numero de postos:'))
M=int(input('digite a distancia maxima media:'))
distancia=42195
prox=0
ante=0
for i in range (0,N,1):
    n=int(input('distancia dos postos:'))
    if (distancia/N)<=M:
        media=distancia/N
        prox=ante+media
    ante=prox
if media<=M and prox<=(N*M) and prox-ante<=M :
    print('S')
else:
    print('N')