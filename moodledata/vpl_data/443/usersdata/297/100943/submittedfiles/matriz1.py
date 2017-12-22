# -*- coding: utf-8 -*-
m=int(input('digite o número de linhas que sua matriz terá: '))
n=int(input('digite o número de linhas que sua matriz terá: '))
matriz=[]
for i in range(0,m,1):
    linhas=[]
    for j in range(0,n,1):
        linhas.append(int(input('digite o elemento da linha e da coluna: ')))
    matriz.append(linhas)
def espelhado(m,n):
    r=0
    s=0
    for i in range(0,m,1):
        for j in range(0,n,1):
            matriz[i][j]=matriz[m-r][n-s]
            r=r+1
            s=s+1
    return espelhado
print(espelhado(matriz))