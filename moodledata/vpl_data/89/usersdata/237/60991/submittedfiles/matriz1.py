# -*- coding: utf-8 -*-
import numpy as np
a=int(input("Digite o número de linhas: "))
b=int(input("Digite o número de colunas: "))
m=np.zeros((a,b))
print(m)
for i in range (0,m.shape[0],1):
    for j in range (0,m.shape[1],1):
        m[i,j]=float(input("Digit um termo: "))
print(m)