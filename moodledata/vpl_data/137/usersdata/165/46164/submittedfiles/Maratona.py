# -*- coding: utf-8 -*-
N=int(input('digite o numero de postos de agua:'))
M=int(input('digite o valor intermediario:'))
a=0
cont=0
for i in range(1,N+1,1):
    p=int(input('digite a posicao do posto de agua:'))
    if (p-a)<=M:
       cont=cont+1 
    else:
        cont=cont
    a=p

if cont==i+1:
    print('S')
else:
    print('N')