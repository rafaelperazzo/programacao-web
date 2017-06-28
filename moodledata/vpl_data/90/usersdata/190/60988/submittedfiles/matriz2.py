# -*- coding: utf-8 -*-
def linhas(a):
    somaL=0
    for i in range(0,a.shape[0],1):
        soma=0
        for j in range(0,a.shape[1],1):
            soma=soma+a[i,j]
        somaL.append(soma)
    for k in range(0,len(somaL),1):
        if somaL[0]!=somaL[i]:
            return(False)
        else:
            return(somaL[0])

def colunas(a):
    somaC=0
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
            


