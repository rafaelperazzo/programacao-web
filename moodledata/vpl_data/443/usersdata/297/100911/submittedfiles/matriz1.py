# -*- coding: utf-8 -*-
m=int(input('digite o número de linhas que sua matriz terá: '))
n=int(input('digite o número de linhas que sua matriz terá: '))
matriz=[]
for i in range(0,m,1):
    linhas=[]
    for j in range(0,n,1):
        linhas.append(int(input('digite o elemento da linha e da coluna: ')))
    matriz.append(linhas)
print(matriz)