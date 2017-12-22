# -*- coding: utf-8 -*-
import numpy as np
matriz=[]
n=int(input('digite a ordem da matriz: '))
while not n>=3:
    n=int(input('digite a ordem da matriz: '))
for i in range (0,n):
    linhas=[]
    for j in range (0,n):
        linhas.append(int(input('qual o valor da linha coluna?:' )))
    matriz.append(linhas)
ntrans=np.empty([n,n])
print(matriz)
for j in range (0,n):
    for i in range (0,n):
        ntrans[j][i]=matriz[i][j]
print(ntrans)

somatotal = 0
for i in range (0,n):
    for j in range (0,n-1):
        if sum(matriz[i]) + sum(ntrans[j]) - 2*(matriz[i][j]) < sum(matriz[i]) + sum(ntrans[j+1]) - 2*(matriz[i][j+1]):
            somatotal = sum(matriz[i]) + sum(ntrans[j]) - 2*(matriz[i][j])
        else:
            somatotal = sum(matriz[i]) + sum(ntrans[j+1]) - 2*(matriz[i][j+1])

print(somatotal)
        


