# -*- coding: utf-8 -*-
matriz = []
m = int(input("Digite o numero de linhas da matriz :"))
n = int(input("Digite o numero de colunas da matriz :"))
for i in range(0,m,1):
    linha = []
    for j in range(0,n,1):
        linha.append(int(input("Digite o valor do %dº elemento da %dª lista : " %((j+1),(i+1)))))
    matriz.append(linha)
print(matriz)
