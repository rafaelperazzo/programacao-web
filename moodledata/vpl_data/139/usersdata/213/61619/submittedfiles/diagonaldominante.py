# -*- coding: utf-8 -*-
def diagonalDominante(matriz):
    contador=0
    for i in range (0,matriz.shape[0],1):
        somaDaLinha=0
        for j in range (0,matriz.shape[1],1):
            if i==j:
                elementoDP=matriz[i,j]
            while i!=j:
                somaDaLinha=somaDalinha+matriz[i,j]
            if elementoDP>=somaDaLinha:
                contador=contador+1
    return(contador)

import numpy as np
n=int(input('Informe a quantidade de linhas e colunas da matriz: '))
matriz=np.zeros((n,n))
for i in range (0,matriz.shape[0],1):
    for j in range(0,matriz.shape[1],1):
        matriz[i,j]=float(input('Informe os termos da matriz: '))
resultador= diagonalDominante(matriz)
if resultado==n:
    print('SIM')
else:
    print('NAO')



