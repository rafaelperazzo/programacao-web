# -*- coding: utf-8 -*-
matriz=[]
m = int(input('Digite o numero de linhas da matriz: '))
n = int(input('Digite o numero de colunas da matriz: '))
for i in range (0,m,1):
    linha=[]
    for j in range (0,n,1):
        linha.append(int(input('Digite um %d termo para a matriz: ' %(i+1))))
    matriz.append(linha)
print(matriz)

for linha in matriz:
    linha.reverse()
matriz.reverse()
print(matriz)
