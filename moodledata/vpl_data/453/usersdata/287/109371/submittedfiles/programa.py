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

somatotal = sum(matriz[0]) + sum(ntrans[0]) - 2*(matriz[0][0])
for i in range (0,n):
    for j in range (0,n):
        if somatotal > sum(matriz[i]) + sum(ntrans[j]) - 2*(matriz[i][j]):
            somatotal = somatotal
        else:
            somatotal = sum(matriz[i]) + sum(ntrans[j]) - 2*(matriz[i][j])

print(somatotal)
        


