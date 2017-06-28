# -*- coding: utf-8 -*-
import numpy as np
def somaLinha(a,i):
    soma=0
    for j in range(0,a.shape[1],1):
        soma=soma+a[i,j]
    return soma
def somaColuna(a,j):
    soma2=0
    for i in range(0,a.shape[0],1):
        soma2=soma2+a[i,j]
    return soma2
def termo(a):
    if somaLinha(a,0)==somaLinha(a,1) or somaLinha(a,0)==somaLinha(a,2):
        somaBase=somaLinha(a,0)
    else:
        somaBase=somaLinha(a,1)
    for i in range(0,a.shape[0],1):
        if somaLinha(a.i)!=somaBase:
            errox=i
    for j in range(0,a.shape[1],1):
        if somaColuna(a,j)!=somaBase:
            erroy=j
            
erro=a[errox,erroy]
    return erro
    
def diferen(a):
    if somaLinha(a,0)==somaLinha(a,1) or somaLinha(a,0)==somaLinha(a,2):
        somaBase=somaLinha(a,0)
    else:
        somaBase=somaLinha(a,1)
    for i in range(0,a.shape[0],1):
        if somaLinha(a,i)!=somaBase:
            somaErro=somaLinha(a,i)
    valor=somaErro-somaBase
    return valor

n=int(input('n:'))
a=np.zeros((n,n))
for i in range(0,a.shape[0],1):
    for j in range(0,a.shape[1],1):
        a[i,j]=int(input('Digite o número:'))
print(int(termo(a)-diferen(a)))
print(int(termo(a)))
        

        