# -*- coding: utf-8 -*-
import numpy as np

i=int(input('digite o numero de linhas da matriz: '))
j=int(input('digite o numero de colunas da matriz: '))
m=np.empty([i,j])

for i in range(0,i,1):
    for j in range(0,j,1):
        m[i] [j]=int(input('digite o numero: '))
print(m)     

