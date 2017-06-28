# -*- coding: utf-8 -*-
def linhas(a):
    soma=0
    for i in range(0,a.shape[0],1):
        for j in range(0,a.shape[1],1):
            soma=soma+a[i]
    return(soma)

def colunas(a):
    soma=0
    for j in range(0,a.shape[1],1):
        for i in range(0,a.shape[1],1):
            soma=soma+a[j]
    return(soma)
    
def diagonalPrincipal(a):
    soma=0
    for i in range(0,a.shape[0],1):
        for j in range(0,a.shape[1],1):
            if i==j:
                soma=soma+a[i]
    return(soma)
    
import numpy as np

n=int(input('digite n:'))
a=np.zeros((n,n))
for i in range(0,a.shape[0],1):
    for j in range(0,a.shape[1],1):
        a[i,j]=float(input('digite o valor:'))
x=linhas(a)
y=colunas(a)
z=diagonalPrincipal(a)
if x==y==z:
    print('S')
else:
    print('N')
            


