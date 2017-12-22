# -*- coding: utf-8 -*-
n=int(input("Digite o número de linhas: "))
m=int(input("Digite o número de colunas: "))
matriz=[]
for i in range(0,n,1):
    linha=[]
    for i in range(0,m,1):
        linha.append(int(input("Digite o valor para a linha: ")))
    matriz.append(linha)
for i in range(0,n,1):
    for j in range(0,m,1):
        if matriz[i][j]==1:
            print(i)
            print(j)

