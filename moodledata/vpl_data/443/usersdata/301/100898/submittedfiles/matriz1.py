# -*- coding: utf-8 -*-
matriz=[]
m=int(input("digite o vaor de linhas: "))
n= int(input('digite o valor de colunas: '))
for i in range(0,m,1):
    linha=[]
    for j in range(0,n,1):
        linha.append(int(input('digite os elementos%d: '%(j+1))))
    matriz.append(linha)


