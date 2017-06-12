# -*- coding: utf-8 -*-
v=int(input('digite um valor:'))
N=int(input('digite o numero de postos:'))
M=int(input('digite a distancia maxima media:'))
prox=0
ante=0
cont=0
for i in range (0,N,1):
    n=int(input('distancia dos postos:'))
    x=n-v
    if x<=M:
        cont=cont+1
if cont==N:
    print('S')
else:
    print('N')