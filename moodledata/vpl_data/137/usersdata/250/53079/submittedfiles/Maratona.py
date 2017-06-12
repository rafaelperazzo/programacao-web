# -*- coding: utf-8 -*-
N=int(input('digite o numero de postos:'))
M=int(input('digite a distancia maxima media:'))
cont=0
v=0
for i in range (0,N,1):
    n=int(input('distancia dos postos:'))
    if (n-v)<=M:
        cont=cont+1
    v=n
if cont==N:
    print('S')
else:
    print('N')