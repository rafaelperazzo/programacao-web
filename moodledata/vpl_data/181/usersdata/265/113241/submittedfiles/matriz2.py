# -*- coding: utf-8 -*-
import numpy as np
 
n=int(input('digite n: '))
a=np.zeros((n,n))
cont=0
 
for i in range(0,a.shape[0],1):
    for j in range(0,a.shape[1],1):
        a[i,j]=int(input('digite o termo: '))

def soma_linha(a,l):
    soma=0
    for j in range(0,a.shape[1],1):
        soma=soma+a[l,j]
    return(soma)
    
def soma_coluna(a,c):
    soma=0
    for i in range(0,a.shape[0],1):
        soma=soma+a[i,c]
    return(soma)

def soma_diagonal(a):
    soma=0
    
    
