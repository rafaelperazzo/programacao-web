# -*- coding: utf-8 -*-
v=int(input('Volume inicial: '))
t=int(input('Numero de trocas: '))
soma=0
for i in range(1,t+1,1):
    x=float(input('Digite o novo valor: '))
    soma=soma+x
total=soma+v
print(total)