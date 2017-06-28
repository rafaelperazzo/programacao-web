# -*- coding: utf-8 -*-
import numpy as np
def transporta(a,b):
    for i in range(0,b.shape[0],1):
        for j in range(0,b.shape[1],1):
            b[i,j]==a[j,i]
            b[i,j]=int(input('elemento:'))
n=int(input('digite o numero de linhas:'))
m=int(input('digite o numero de colunas:'))
b=b.zeros((n,m))
print(transposta)