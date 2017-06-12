# -*- coding: utf-8 -*-
n=int(input('Digite o número de posto:'))
m=int(input('Digite a distancia intermediaria maxima do atleta:'))
a=m
cont=0
for i in range(1,n+1,1):
    d=int(input('Digite o posição dos postos:'))
    a=d-m
    if a<m:
        cont=cont+1
if cont!=n:
    print('N')
else:
    print('S')
    