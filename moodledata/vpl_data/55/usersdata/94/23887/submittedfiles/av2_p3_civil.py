# -*- coding: utf-8 -*-
from __future__ import division
import numpy as np

def soma_linha(a,b):
    soma=0
    for j in range(0,a.shape[1],1):
        soma=soma+a[b,j]
    return soma
    
def soma_coluna(a,d):
    soma=0
    for i in range(0,a.shape[0],1):
        soma=soma+a[i,d]
    return soma
    
def soma(a,b,d):
    soma=0
    soma=(soma_linha(a,b)+soma_coluna(a,d))-(2*a[b,d])
    return soma
    
n=input('diga a dimensao da matriz:')
x=input('digite o numero da linha q o elemento vai estar:')
y=input('digite o numero da coluna q o elemento vai estar:')

a=np.zeros((n,n)) 

for i in range (0,a.shape[0],1):
    for j in range(0,a.shape[1],1):
        a[i,j]= input('digite o elemento:')

st=soma(a,x,y)
print ('%d' %st)