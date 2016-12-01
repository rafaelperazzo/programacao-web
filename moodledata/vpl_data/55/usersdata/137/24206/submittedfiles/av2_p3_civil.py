# -*- coding: utf-8 -*-
from __future__ import division
import numpy as np
'''
def somaLinhas(a,l,c):                 #essa era outra ideia! 
    soma=0
    for j in range (0,a.shape[1],1):  
            soma=soma+a[l,j]
    return soma

def somaColunas(a,l,c):
    soma=0
    for i in range (0,a.shape[0],1):
        soma=soma+a[i,c]
    return soma
'''
def pesoM(m,l,c):
    soma1=0
    j=m.shape[1]-1
    while (j>=0):
        soma1=soma1+m[l,j]
        j=j+1
    soma2=0
    i=m.shape[0]-1
    while (i>=0):
        soma2=soma2+m[i,c]
        i=i+1
    soma=soma1+soma2-(2*(m[l,c]))
    return soma

n=input('dimensao da matriz:')
l=input ('indice i:')
c=input ('indice j:')
a=np.zeros((n,n))

for i in range (0,n,1):
    for j in range (0,n,1):
        a[i,j]= input('a:')
f=pesoM(a,l,c)
print(f)

