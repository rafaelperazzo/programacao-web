# -*- coding: utf-8 -*-
from __future__ import division
import numpy as np

def somaLinhas(a,pj):
    soma=0
    for i in range (0,a.shape[0],1):
        soma[i]=soma+a[i,pj]
    return soma

def somaColunas(a,pi):
    soma=0
    for j in range (0,a.shape[1],1):
        soma[j]=soma+a[pi,i]
    return soma

def peso(a):
    b=somaLinhas(a,pj)
    c=somaColunas(a,pi)
    peso=b+c-2*(a[pi,pj])
    return peso
    
n=input('dimensao da matriz:')
pi=input ('indice i:')
pj=input ('indice j:')
a=np.zeros ((n,n))
b=somaLinhas(a,pj)
c=somaColunas(a,pi)
d=peso(a)

for i in range (0,a.shape[0],1):
    for j in range (0,a.shape[1],1):
        a[i,j]= input('a:')
print(d)

