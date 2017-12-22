# -*- coding: utf-8 -*-
m=int(input('Digite a quantidade de listas desejada: '))
lista=[]
for i in range(0,m,1):
    n=int(input('Digite a quantidade de elementos de cada lista: '))
    for i in range(0,n,1):
        lista.append(int(input('Digite os elementos de cada lista: ')))

