# -*- coding: utf-8 -*-
v=int(input('digite um valor:'))
N=int(input('digite o numero de postos:'))
M=int(input('digite a distancia maxima media:'))
cont=0
x=0
for i in range (1,N,1):
    n=int(input('distancia dos postos:'))
    x=n-v
    if x<=M:
        cont=cont+1
    v=n
if cont==N:
    print('S')
else:
    print('N')