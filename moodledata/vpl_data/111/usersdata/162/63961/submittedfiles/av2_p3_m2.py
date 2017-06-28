# -*- coding: utf-8 -*-
import numpy as np
def somaLinha(A,i):
    soma=0
    for j in range(0,A.shape[1],1):
        soma=soma+A[i,j]
    return soma
def somaColuna(A,j):
    soma2=0
    for i in range(0,A.shape[0],1):
        soma2=soma2+A[i,j]
    return soma2
def termo(A):
    if somaLinha(A,0)==somaLinha(A,1) or somaLinha(A,0)==somaLinha(A,2):
        somaBase=somaLinha(A,0)
    else:
        somaBase=somaLinha(A,1)
    for i in range(0,A.shape[0],1):
        if somaLinha(A,i)!=somaBase:
            errox=i
    for j in range(0,A.shape[1],1):
        if somaColuna(A,j)!=somaBase:
            erroy=j
            
    erro=A[errox,erroy]
    return erro
    
def diferen(A):
    if somaLinha(A,0)==somaLinha(A,1) or somaLinha(A,0)==somaLinha(A,2):
        somaBase=somaLinha(A,0)
    else:
        somaBase=somaLinha(A,1)
    for i in range(0,A.shape[0],1):
        if somaLinha(A,i)!=somaBase:
            somaErro=somaLinha(A,i)
    valor=somaErro-somaBase
    return valor

n=int(input('n:'))
A=np.zeros((n,n))
for i in range(0,A.shape[0],1):
    for j in range(0,A.shape[1],1):
        A[i,j]=int(input('Digite o número:'))
print(int(termo(A)-diferen(A)))
print(int(termo(A)))
        

        