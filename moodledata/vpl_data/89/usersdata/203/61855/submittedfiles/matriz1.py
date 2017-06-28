# -*- coding: utf-8 -*-
import numpy as np
n=int(input('numero de linhas: '))
m=int(input('numero de colunas: '))
a=np.zeros((n,m))
for i in range(0,a.shape[0],1):
    for j in range(0,a.shape[1],1):
        a[i,j]=float(input('elemento: '))
print(a)

