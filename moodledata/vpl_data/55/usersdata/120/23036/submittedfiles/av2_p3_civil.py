# -*- coding: utf-8 -*-
from __future__ import division
import numpy as np

#definir somalinha
def somalinha(a,linha):
    soma=0
    for j in range(0,a.shape[1],1):
        soma=soma+a[linha,j]
    return soma
    
#definir somacoluna
def somacoluna(a,coluna):
    soma=0
    for i in range(0,a.shape[0],1):
        soma=soma+a[i,coluna]
    return soma
    
# definir peso
def somatotal(a,linha,coluna):
    somatotal=somalinha(a,linha)+somacoluna(a,coluna)-(2*a[linha,coluna])
    return somatotal  


n=input('digite n:')
x=input('digite x:')
y=input('digite y:')
a=np.zeros((n,n))
for i in range(0,a.shape[0],1):
    for j in range(0,a.shape[1],1):
        a[i,j]=input('Digite os elementos da matriz: ')
peso=somatotal(a,x,y)
print ('%d'%peso)

    
    
