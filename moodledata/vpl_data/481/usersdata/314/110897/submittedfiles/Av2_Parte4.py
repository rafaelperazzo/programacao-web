# -*- coding: utf-8 -*-
tamanho=int(input('Digite o tamanho da matriz: '))

matriz=[]

for i in range(tamanho):
    linhas=[]
    for j in range(tamanho):
        linhas.append(int(input('Digite os elementos das linhas: ')))
    matriz.append(linhas)    

print(matriz)    
