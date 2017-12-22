# -*- coding: utf-8 -*-
import numpy as np

n=int(input("Digite o número de linhas: "))
m=int(input("Digite o número de colunas: "))
matriz=np.empty([m,n])

for i in range(0,n,1):
    for j in range(0,m,1):
        matriz[i][j]=float(input("Digite o valor do elemento da M(%d,%d): "%(i+1,j+1)))
        

