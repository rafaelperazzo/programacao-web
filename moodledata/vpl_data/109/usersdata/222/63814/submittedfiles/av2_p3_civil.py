# -*- coding: utf-8 -*-
import numpy as np
n=int(input('n:'))
matriz=np.zeros((n,n))
x=int(input('x:'))
y=int(input('y:'))
soma1=0
soma2=0
for i in range(0,matriz.shape[0],1):
    for j in range(0,matriz.shape[1],1):
        matriz[i,j]=int(input('indice:'))
for i in range(0,matriz.shape[0],1):
    for j in range(0,matriz.shape[1],1):
        if i==x:
            soma1=soma1+matriz[i,j]
        if i==y:
            soma2=soma2+matriz[i,j]
s=(soma1+soma2-2*matriz[i,j])
print(s)
