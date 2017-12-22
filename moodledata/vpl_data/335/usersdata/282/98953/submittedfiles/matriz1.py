# -*- coding: utf-8 -*-
matriz=[]
m = int(input('Digite a quantidade de linhas (m): '))
n = int(input('Digite a quantidade de colunas (n): '))
for i in range(0,m,1):
    linha=[]
    for j in range(0,n,1):
        linha.append(int(input('Digite o termo: ')))
    matriz.append(linha)
for i in range (0,m,1):
    for j in range (0,n,1):
        if matriz[i][j]==1:
            print(str(i)+str(j))
print(matriz)



