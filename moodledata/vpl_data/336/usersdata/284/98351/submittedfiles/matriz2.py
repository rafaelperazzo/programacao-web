# -*- coding: utf-8 -*-
import numpy as np

i=int(input('digite o numero de linhas da matriz: '))
j=int(input('digite o numero de colunas da matriz: '))
matriz=np.empty([i,j])

for i in range(0,i,1):
    for j in range(0,j,1):
        matriz [i][j]=float(input('digite o numero: '))
        print(matriz)        

