# -*- coding: utf-8 -*-
matriz = []
m = int(input("Digite o número de linhas da matriz: "))
n = int(input("Digite o número de colunas da matriz: "))
for i in range (0,m,1):
    linha = []
    for j in range (0,n,1):
        linha.append(int(input("Digite o valor do %dº elemento %dª da lista : "%(j+1))))
    matriz.append(linha)
print(matriz)

        

