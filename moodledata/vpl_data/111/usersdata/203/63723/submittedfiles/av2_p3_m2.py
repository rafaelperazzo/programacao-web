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
def laura(a):
    if soma_linha(a,0)==soma_linha(a,1) or soma_linha(a,0)==soma_linha(a,2)
        soma_base=soma_linha(a,0)
    else:
        soma_base=soma_linha(a,1)
    for i in range(0,a.shape[0],1):
        if soma_linha(a,i)!=soma_base:
            indice_errado_x=i
    for j in range(0,a.shape[1],1):
        if soma_coluna(a,j)!=soma_base:
            indice_errado_j=j
    errado=a[i,j]
    return errado
n=int(input('digite n: '))
a=np.zeros((n,n))
for i in range(0,a.shape[0],1):
    for j in range(0,a.shape[1],1):
        a[i,j]=int(input('digite valor: '))
b=laura(a)
print(b)
    
    