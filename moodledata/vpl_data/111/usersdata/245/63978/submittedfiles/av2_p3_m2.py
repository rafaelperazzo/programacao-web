# -*- coding: utf-8 -*-
import numpy as np
n=int(input('Digite o tamanho da Matriz:'))
a=np.zeros((n,n))
if n>=3:
    for i in range(0,a.shape[0],1):
        for j in range(0,a.shape[1],1):
            a[i,j]=int(input('Digite um valor:'))
soma=0
for i in range(0,a.shape[0],1):
    soma1=soma+a[i,0]
    