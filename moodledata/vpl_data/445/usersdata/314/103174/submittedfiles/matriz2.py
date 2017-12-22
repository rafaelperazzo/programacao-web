# -*- coding: utf-8 -*-
tamanho=int(input('Digite o tamanho da matriz: '))

matriz=[]

for i in range(tamanho):
    mi=[]
    for j in range(tamanho):
        mi.append(int(input('Digite os elementos: ')))
matriz.append(mi)

print(matriz)

