# -*- coding: utf-8 -*-
import numpy as np
m=int(input('Digite o numero de linhas: '))
n=int(input('Digite o numero de colunas: '))
a=np.empty([m,n])
for i in range (m-1,-1,-1):
    for j in range (n-1,-1,-1):
        a[i][j]=int(input('Digite o numero: ')
print (a)

