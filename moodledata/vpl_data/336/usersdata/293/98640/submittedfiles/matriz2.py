# -*- coding: utf-8 -*-
import numpy as np
n=int(input("Digite o número de linhas da matriz: "))

matriz= np.empty([n,n])

for i in range(0,n,1):
    for j in range(0,n,1):
        matriz[i][j]= int(input("Digite o elemento da %dª linhas e da %dª coluna, respectivamente: "%(i+1,j+1)))

