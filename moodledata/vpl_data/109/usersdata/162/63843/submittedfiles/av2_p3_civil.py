# -*- coding: utf-8 -*-
import numpy as np
def somaLinha(a,i):
    soma=0
    for j in range(0,a.shape[1],1):
        soma=soma+a[i,j]
    return soma
def somaColuna(a,j):
    soma1=0
    for i in range(0,a.shape[0],1):
        soma1=soma1+a[i,j]
    return soma1    

n=int(input('Digite n:'))
x=int(input('Digite x:'))
y=int(input('Digite y:'))

a=np.zeros((n,n))
for i in range(0,a.shape[0],1):
    for j in range(0,a.shape[1],1):
        a[i,j]=int(input('Digite o peso:'))
result=somaLinha(a,x)+somaColuna(a,y)-(2*a[x,y])
print(result)
