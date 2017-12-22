# -*- coding: utf-8 -*-
m=int(input('Digite a quantidade de linhas da matriz: '))
n=int(input('Digite a quantidade de colunas da matriz: '))
matriz=[]
for i in range(0,m,1):
    linha=[]
    linha.append(int(input('Digite o %d elemento da linha: ' %(i+1))))
    for j in range(0,n,1):
        linha.append(int(input('Digite o %d elemento da coluna: ' %(j+1))))
    matriz.append(linha)
print(matriz)    
