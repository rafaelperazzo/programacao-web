# -*- coding: utf-8 -*-
import numpy as np
n= int(input('Digite a quantidade de linhas e colunas da matriz: '))
matriz= np.empty([n,n])
for i n range (0,n,1):
    for j in range (0,n,1):
        matriz[i][j]= float(input('Digite o elemento da linha%.d e coluna%.d: ' %(i,j)))
soma=0
somac= 0
somaDP=0
somaDS= 0
for i in rangge (0,n,1):
    for i in range(0,n,1):
        soma[+=matriz[i+j]
    somaL*=-1
for j in rangge (0,n,1):
    for i in range(0,n,1):
        soma[+=matriz[i+j]
    somaL*=-1
