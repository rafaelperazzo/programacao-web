# -*- coding: utf-8 -*-
N=int(input('digite o numero de competidores:'))
p=int(input('digite o numero mínimo de pontos para uma das duas fases:'))
soma=o
i=1
for i in range (1,N+1,1):
    x=int(input('Nota1:'))
    y=int(input('Nota2:'))
    if x+y>=p:
        soma=soma+1
print(soma)
    