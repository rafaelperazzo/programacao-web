# -*- coding: utf-8 -*-
v=int(input('Volume inicial: '))
t=int(input('Numero de trocas: '))
soma=0
for i in range(1,t+1,1):
    x=float(input('Digite o novo valor: '))
    if soma+x+v<100:
        soma=soma+x
    else:
        soma=100
t=soma+v
print(t)