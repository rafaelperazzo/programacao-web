# -*- coding: utf-8 -*-
m=int(input('Digite a quantidade de listas: '))
n=int(input('Digite a quantidade de elementos das listas: '))
for i in range(0,m,1):
    L=[]
    for i in range(0,n):
        L.append(int(input('Digite os elementos das listas: ')))
print(L)
    