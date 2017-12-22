# -*- coding: utf-8 -*-
import math as np
matriz=[]
m = int(input('digite o número de m: '))
n = int(input('digite o numero de n: '))
for i in range(0,m):
    linha=[]
    for j in range(0,n):
        linha.append(int(input('digite o termo: ')))
    matriz.append(linha)
print(matriz)
b=[]
for i in range(0,matriz.shape[0],1):
    soma=0
    for j in range(0,matriz.shape[1],1):
        soma = soma + matriz[i][j]
    b.append(soma)
print(b)    
