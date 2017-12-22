# -*- coding: utf-8 -*-
n=[]
sem_repetir=[]
p=int(input('digite a quantidade de pedidos: '))
for i in range(0,p):
    n.append(int(input('digite o tamanho: ')))
    
for i in n:
    if i not in sem_repetir:
        sem_repetir.append(i)




