# -*- coding: utf-8 -*-
from __future__ import division
import numpy as np
'''
def somaLinhas(a,pi,pj):
    soma=0
    for j in range (0,a.shape[1],1):
            soma=soma+a[pi,j]
    return soma

def somaColunas(a,pi,pj):
    soma=0
    for i in range (0,a.shape[0],1):
        soma=soma+a[i,pj]
    return soma
'''
def pesoM(a,m,l,c):
    soma1=0
    i=l
    j=m.shape[1]-1
    while i==l and j>=0:
        soma1=soma1+m[l,j]
        j=j+1
    soma2=0
    i=m.shape[0]-1
    j=c
    while i>=0 and j==c:
        soma2=soma2+m[i,c]
        i=i+1
    soma=soma1+soma2-(2*m[l,c])
    return soma

m=input('dimensao da matriz:')
l=input ('indice i:')
c=input ('indice j:')
a=np.zeros ((m,m))
f=pesoM(a,m,l,c)

for i in range (0,a.shape[0],1):
    for j in range (0,a.shape[1],1):
        a[i,j]= input('a:')
print(f)

