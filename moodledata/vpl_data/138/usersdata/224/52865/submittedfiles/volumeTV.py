# -*- coding: utf-8 -*-
v=int(input('Volume inicial: '))
t=int(input('Numero de trocas: '))
soma=0
for i in range(1,t+1,1):
    x=int(input('Digite o novo valor: '))
    soma=v+x
    if soma>=100:
        a=100
    if soma<=0:
        a=0
    else:
        a=a
    v=soma
print(soma)