# -*- coding: utf-8 -*-
N=int(input('Digite o número de competidores:'))
P=int(input('Digite o número mínimo de pontos:'))
soma=0
i=1
for i in range(1,N+1,1):
    x=int(input('Nota 1:'))
    y=int(input('Nota 2:'))
    if x+y>=P:
        soma=soma+1
print(soma)        