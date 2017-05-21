# -*- coding: utf-8 -*-
N=int(input('digite o numero de postos de agua:'))
M=int(input('digite o valor intermediario:'))
a=0
cont=1
for i in range(1,n+1,1):
    n=int(input('digite a posicao do posto de agua:'))
    if (n-a)<=M:
       cont=cont+1 
       a=n

if cont==n:
    print('S')
else:
    print('N')