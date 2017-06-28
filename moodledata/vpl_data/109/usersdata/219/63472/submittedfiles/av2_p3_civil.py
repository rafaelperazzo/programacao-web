# -*- coding: utf-8 -*-
import numpy as np
def sl(a,i):
    soma=0
    for j in range(0,a.shape[1],1):
        soma=soma+a[i,j]
    return(soma)
    
def sc(a,j):
    soma=0
    for i in range(0,a.shape[0],1):
        soma=soma+a[i,j]
    return(soma)
    
    
n=int(input('Digite a dimensão da matriz:'))
e=int(input('Digite a posição da linha:'))
r=int(input('Digite a posição da coluna:'))

a=np.zeros((n,n))
for i in range(0,a.shape[0],1):
    for j in range(0,a.shape[1],1):
        a[i,j]=int(input('Digite o peso:'))
        
resultado=sl(a,e)+sc(a,r)-(2*a[e,r])

print(resultado)


