# -*- coding: utf-8 -*-
import numpy as np
def matriz(a):
    for i in range(0,a.shape[0],1):
        for j in range(0,a.shape[1],1):
            a[i,j]=int(input('digite um elemento:'))
    return(a)
linhas=int(input('digite o numero de linhas:'))
colunas=int(input('digite o numero de colunas:'))
a=np.zeros((linhas,colunas))
print(matriz(a))