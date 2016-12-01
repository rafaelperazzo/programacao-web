# -*- coding: utf-8 -*-
from __future__ import division
import numpy as np

def soma_linha(a,l):
    soma=0
    for j in range(0,a.shape[1],1):
        soma=soma+a[l,j]
    return soma
    

def soma_coluna(a,c):
    soma=0
    for i in range(0,a.shape[0],1):
        soma=soma+a[i,c]
    return soma
    

def soma_total(a,l,c):
    soma=soma_linha(a,l)+soma_coluna(a,c)-(2*a[l,c])
    return soma
    
    
n=input('digite o valor de n:')
x=input('digite o valor de x:')
y=input('digite o valor de y:')
a=np.zeros((n,n))
for i in range(0,a.shape[0],1):
    for j in range(0,a.shape[1],1):
        a[i,j]=input('digite um elemento:')
        
print soma_total(a,x,y)
        

