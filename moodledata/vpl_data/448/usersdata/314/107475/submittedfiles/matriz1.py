# -*- coding: utf-8 -*-
linhas=int(input('Digite o numero de linhas: '))
colunas=int(input('Digite o numero de colunas: '))

matriz=[]
for i in range(linhas):
    linhas=[]
    for j in range(colunas):
        matriz.append(int(input('Digite os elementos da matriz: ')))
    linhas.append(matriz)

print(matriz)    
            

