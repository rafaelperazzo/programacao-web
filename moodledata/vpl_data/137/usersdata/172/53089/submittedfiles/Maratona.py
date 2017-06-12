# -*- coding: utf-8 -*-
n=int(input('número de postos: '))
x=int(input('número médio: '))
cont=0
anterior=0
for i in range(0,n,1):
    d=int(input('distância: '))
    r=d-anterior
    if (r)<=x:
        cont=cont+1
        anterior=d
if cont==n:
    print('S')
else:
    print('N')
    
    
    