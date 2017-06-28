# -*- coding: utf-8 -*-
import numpy as np
def somalinha(a,i):
    soma=0
    for j in range(0,a.shape[1],1):
        soma=soma+a[i,j]
    return(soma)        
    
def somacoluna(a,j):
    soma=0
    for i in range(0,a.shape[0],1):
        soma=soma+a[i,j]
    return(soma)


n=int(input('digite a dimensao da matriz:'))
x=float(input('digite a posicao:'))
l=x//1
q=(x%1)*10

a=np.zeros((n,n))
for i in range(0,a.shape[0],1):
    for j in range(0,a.shape[1],1):
        a[i,j]=int(input('digite o peso:'))

resultado=somalinha(a,l)+somacoluna(a,q)-(2*a[l,q])

print('%f' %resultado)

