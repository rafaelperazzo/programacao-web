# -*- coding: utf-8 -*-
N=int(input('digite o numero de postos:'))
M=int(input('digite a distancia maxima media:'))
distancia=42195
prox=0
ante=0
cont=0
for i in range (0,N,1):
    n=int(input('distancia dos postos:'))
    if (distancia/N)<=M:
        media=distancia/N
        prox=ante+media
        if prox-ante<=M:
            cont=cont+1
    ante=prox
if media<=M and prox<=(N*M) and cont==N-1:
    print('S')
else:
    print('N')