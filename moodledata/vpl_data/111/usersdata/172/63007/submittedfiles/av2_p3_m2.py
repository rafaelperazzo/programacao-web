# -*- coding: utf-8 -*-
import numpy as np
def somalinhas(a):
    soma=0
    for i in range(0,a.shape[0],1):
        for l in range(0,a.shape[1],1):
            soma=soma+a[i,l]
        return(soma)    
def somacolunas(a):
    soma=0
    for l in range(0,a.shape[1],1):
        for l in range(0,a.shape[0],1):
            soma=soma+a[i,l]            
        return(soma)
n=int(input('linhas e colunas:'))
a=np.zeros((n,n))
for i in range(0,a.shape[0],1):
    for l in range(0,a.shape[1],1):
        a[i,l]=float(input('valor:'))
print(a)