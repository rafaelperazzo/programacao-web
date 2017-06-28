# -*- coding: utf-8 -*-
import numpy as np
n=int(input('digite n: '))
a=np.zeros(n,n)
indice_x=int(input('digite a linha: '))
indice_y=int(input('digite a coluna: '))
for i in range(0,a.shape[0],1):
    for j in range(0,a.shape[1],1):
        a[i,j]=int(input('digite valor: '))
