# -*- coding: utf-8 -*-
N=int(input('digite o numero de competidores:'))
P=int(input('digite o numero mínimo de ponto para as duas fases:'))
soma=o
i=1
for i in range (1,N+1,1):
    x=int(input('Nota1:'))
    y=int(input('Nota2:'))
    if x+y>=P:
        soma=soma+1
print('soma')
    