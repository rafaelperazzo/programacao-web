# -*- coding: utf-8 -*-
import numpy as np
np.empty
matrix=[]
m=int(input("Digite o número de linhas da lista: "))
n=int(input("Digite o número de colunas da lista: "))

for i in range(0,m,1):
    for j in range(0,n,1):
        matrix[i][j]=int(input("Digite o valor do elemento (%d,%d): "%(i,j)))
print(matrix)
        
        