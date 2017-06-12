# -*- coding: utf-8 -*-
N=int(input('digite o numero de postos:'))
M=int(input('digite a distancia maxima media:'))
prox=0
ante=0
cont=0
v=M
for i in range (0,N,1):
    n=int(input('distancia dos postos:'))
    prox=ante+M
    ante=prox
    if (prox-ante)<=M:
        cont=cont+1
if cont==N:
    print('S')
else:
    print('N')