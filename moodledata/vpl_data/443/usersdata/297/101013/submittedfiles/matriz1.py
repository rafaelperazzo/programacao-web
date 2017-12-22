# -*- coding: utf-8 -*-
m=int(input('digite o número de linhas que sua matriz terá: '))
n=int(input('digite o número de linhas que sua matriz terá: '))
matriz=[]
for i in range(0,m,1):
    linhas=[]
    for j in range(0,n,1):
        linhas.append(int(input('digite o elemento da linha e da coluna: ')))
    matriz.append(linhas)
inversa=[]
for i in range(m-1,0,-1):
    invlin=[]
    for j in range(n-1,0,-1):
        invlin.append(matriz[i][j])
    inversa.append(invlin)
print(inversa)
    