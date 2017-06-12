# -*- coding: utf-8 -*-
N=int(input('digite o numero de pessoas:'))
p=int(input('digite o numero mínimo de pontos para uma das duas etapas:'))
soma=o
i=1
for i in range (2,N+1,1):
    x=int(input('nota1:'))
    y=int(input('nota2:'))
    if x+y>=p:
        soma=soma+1
print(soma)
    