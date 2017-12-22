# -*- coding: utf-8 -*-
linhas=int(input('Digite o numero de linhas: '))
colunas=int(input('Digite o numero de colunas: '))

matriz=[]
for i in range(0,linhas,1):
    linhas=[]
    for j in range(0,colunas,1):
        linhas.append(int(input('Digite os elementos da matriz: ')))
    matriz.append(linhas)

print(matriz)    


            

