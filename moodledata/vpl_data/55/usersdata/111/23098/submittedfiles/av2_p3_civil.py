# -*- coding: utf-8 -*-
from __future__ import division
import numpy as np

def somalinha(a,x):
    soma=0
    for i in range(0,a.shape[0],1):
        for j in range(0,a.shape[1],1):
            if x==i:
                soma=soma+a[i,j]
    return soma
    
def somacoluna(a,y):
    soma=0
    for j in range(0,a.shape[1],1):
        for i in range(0,a.shape[0],1):
            if y==j:
                soma=soma+a[i,j]
    return soma
    
n=input('Digite a dimensão da matriz: ')
a=np.zeros((n,n))

x=input('Digite o valor da posição x: ')
y=input('Digite o valor da posição y: ')

for i in range(0,n,1):
    for j in range(0,n,1):
        a[i,j]=input('Digite os elementos da matriz: ')
        
x=x-1
y=y-1

c=2*abs(a[x,y])


x=somalinha(a,x)
y=somacoluna(a,y)
resultado=(x+y-c)
print resultado
        






