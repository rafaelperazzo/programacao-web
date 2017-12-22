# -*- coding: utf-8 -*-
n=int(input('Digite o numero de linhas e o de colunas da matriz: '))
matriz=[]
for j in range(0,n,1):
    colunas=[]
    for i in range(0,n,1):
        colunas.append(float(input('digite o elemento da linhas %d, coluna%d : ' %((j+1),(i+1))))
    matriz.append(colunas)
print(matriz)

