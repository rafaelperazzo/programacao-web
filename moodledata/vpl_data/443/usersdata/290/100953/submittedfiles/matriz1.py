# -*- coding: utf-8 -*-
m=int(input("Digite a quantidade de linhas da matriz: "))
n=int(input("Digite a quantiade de colunas da matriz: "))
matriz=[]
for i in range(0,m,1):
    linha=[]
    for i in range(0,n,1):
        linha.append(int(input("Digite o valor para a matriz: ")))
    matriz.append(linha)
for linha in matriz:
    linha.reversa()
matriz.reversa()
print(matriz)

