# -*- coding: utf-8 -*-
import numpy as np
a=int(input("Digite o número de linhas: "))
b=int(input("Digite o número de colunas: "))
m=np.zeros((a,b))
for i in range (0,m.shape[0],1):
    for j in range (0,m.shape[1],1):
        m[i,j]=float(input("Digit um termo: "))
e=0
c=0
for i in range (0,m.shape[0],1):
    for j in range (0,m.shape[1],1):
        if a[i,j] != 0:
            e=e+i
            c=c+j
        break
f=0
d=0
for i in range (0,m.shape[0],1):
    for j in range (0,m.shape[1],1):
        if a[i,j] != 0:
            f=f+i
            d=d+1
print(m[e:f;c:d])