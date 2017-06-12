# -*- coding: utf-8 -*-
n=int(input('numero de postos de agua:'))
m=int(input('numero da distancia intermediária maxíma de um atleta:')
soma=0
a=0
for i in range(1,n+1,1):
    p=int(input('digite a posição:'))
    if (p-a)<=m:
        soma=soma+1
    a=p
if soma==n:
    print('S')
else:
    print('N')