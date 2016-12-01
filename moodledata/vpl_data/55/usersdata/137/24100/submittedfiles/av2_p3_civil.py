# -*- coding: utf-8 -*-
from __future__ import division
import numpy as np

def somaLinhas(a,j):
    s=0
    for i in range (0,a.shape[0],1):
        soma=0
        for j in range (0,a.shape[1],1):
            soma=soma+a[i,j]
        s.append(soma)
    return s

def somaColunas(a,i):
    s=0
    for j in range (0,a.shape[1],1):
        soma=0
        for j in range (0,a.shape[1],1):
        soma=soma+a[i,i]
        s.append(soma)
    return s


n=input('dimensao da matriz:')
i=input ('indice i:')
j=input ('indice j:')
a=np.zeros ((n,n))
b=somaLinhas(a,pj)
c=somaColunas(a,pi)
peso=b+c-(2*(a[pi,pj]))


for i in range (0,a.shape[0],1):
    for j in range (0,a.shape[1],1):
        a[i,j]= input('a:')
print(d)

