# -*- coding: utf-8 -*-
m=int(input("Digite a quantidade de colunas: "))
n=int(input("Digite a quantidade de linhas: "))
matriz=[]
for i in range (0,m,1):
    linha=[]
    for j in range (0,n,1):
        linha.append(int(input("Digite o %d numero da linha: "%(i+1))))
    matriz.append(linha)

print (matriz)



