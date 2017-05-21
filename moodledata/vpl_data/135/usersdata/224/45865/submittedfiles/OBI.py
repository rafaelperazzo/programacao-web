# -*- coding: utf-8 -*-
N=int(input('Digite o numero de competidores: '))
P=int(input('Digite o numero mínimo de ponto para as duas fases: '))
soma=0
i=1
for i in range(1,N+1,1):
    x=int(input('Nota1: '))
    y=int(input('Nota2: '))
    if x+y>=P:
        soma=soma+1
print(soma)