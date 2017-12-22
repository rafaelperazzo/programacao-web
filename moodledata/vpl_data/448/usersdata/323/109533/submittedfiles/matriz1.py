# -*- coding: utf-8 -*-
import copy
import numpy as np

m=int(input('Digite a quantidade de linhas da matriz: '))
n=int(input('Digite a quantidade de colunas da matriz: '))

a=np.zeros((m,n))

for i in range(0,m,1):
    for j in range(0,n,1):
        a[i,j]= float(input('Digite os elementos: '))

def rotacionar(matriz, grau):
    nova_matriz=copy.deepcopy(matriz)
    for i in range(len(matriz)):
        if grau==180:
            nova_matriz[len(matriz)-(i+1)]
            [len(matriz)-(j+1)]=matriz[i][j]
    return nova_matriz



