# -*- coding: utf-8 -*-
import numpy as np
n=int(input('digite o valor de m: '))
while n<3:
n=int(input('digite o valor de m: '))
matriz=[]
for i in range(0,n):
    linhas=[]
    for j in range(0,n):
        linhas.append(int(input('digite os valores (%d,%d): ' %(i+1,j+1))))
    matriz.append(linhas)
print(matriz)
#fazendo matriz transposta
matriztrans=np.empty([n,n]):
for j in range(0,n):
    for i in range(0,n):
        matriztrans[j][i]=matriz[i][j]
print(matriztrans)

for i in range(1,n-1):
    if sum(matriz[0])==sum(matriz[i]):
        continue
    elif sum(matriz[i]) == sum(matriz[i+1]):
        continue
    else:
#o indice da linha onde o elemneto errado esta
        print(matriz.index(matriz[i]))
        
for j in range(1,n-1):
    if sum(matriztrans[0]) == sum(matriztrans[j]):
        continue
    elif sum(matriztrans[j]) == sum(matriztrans[j+1]):
        continue
    else:
        print(matriztrans.index(matriztrans[j]))
print(matriz[matriz.index(matriz[i])][matriztrans.index(matriztrans[j])])
    


