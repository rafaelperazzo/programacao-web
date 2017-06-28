# -*- coding: utf-8 -*-
import numpy as np
def soma_linha(a,i):
    soma=0
    for j in range(0,a.shape[1],1):
        soma=soma+a[i,j]
    return soma
def soma_coluna(a,j):
    soma=0
    for i in range(0,a.shape[0],1):
        soma=soma+a[i,j]
    return soma
for i in range(0,a.shape[0],1):
    for j in range(0,a.shape[1],1):
        a=soma_linha(a,i)


