# -*- coding: utf-8 -*-
import numpy as np
n=int(input('Digite o tamanho da Matriz:'))
a=np.zeros((n,n))
if n>=3:
    for i in range(0,a.shape[0],1):
        for j in range(0,a.shape[1],1):
            a[i,j]=int(input('Digite um valor:'))
soma1=0
soma2=0
for i in range(0,a.shape[0],1):
    soma1=soma1+a[i,0]
for j in range(0,a.shape[1],1):
    soma2=soma2+a[i,0]
m=0
if soma1==soma2:
    m=soma1
print(m)