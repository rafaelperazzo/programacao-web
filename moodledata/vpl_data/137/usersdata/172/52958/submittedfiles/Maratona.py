# -*- coding: utf-8 -*-
n=int(input('número de postos: '))
x=int(input('número médio: '))
soma=0
cont=0
anterior=0
for i in range(2,n+1,1):
    d=int(input('distância: '))
    if anterior<x:
        cont=cont+1
        anterior=anterior+d
if cont==0:
    print('s')
else:
    print('n')
    
    
    