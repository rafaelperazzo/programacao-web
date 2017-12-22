# -*- coding: utf-8 -*-
import numpy as np
n=int(input('digite o valor de m: '))
matriz=[]
for i in range(0,n):
    linhas=[]
    for j in range(0,n):
        linhas.append(int(input('digite os valores (%d,%d): ' %(i+1,j+1))))
    matriz.append(linhas)
print(matriz)
matriztrans=np.empty([n,n]):
for j in range(0,n):
    for i in range(0,n):
        matriztrans[j][i]=matriz[i][j]
print(matriztrans)
    


