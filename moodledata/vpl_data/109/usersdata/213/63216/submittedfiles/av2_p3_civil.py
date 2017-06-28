# -*- coding: utf-8 -*-
def pesoDaPosicao(matriz,matriz[linha,coluna]):
    for i in range(0,matriz.shape[0],1):
        for j in range(0,matriz.shape[1],1):
            
import numpy as np
n=int(input('Informe a quantidade de linhas e colunas da matriz: '))
matriz=np.zeros((n,n))



for i in range(0,matriz.shape[0],1):
    for j in range(0,matriz.shape[1],1):
        matriz[i,j]=int(input('Informe os elementos da matriz: '))


