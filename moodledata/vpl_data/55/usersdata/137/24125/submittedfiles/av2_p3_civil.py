# -*- coding: utf-8 -*-
from __future__ import division
import numpy as np

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

n=input('dimensao da matriz:')
pi=input ('indice i:')
pj=input ('indice j:')
a=np.zeros ((n,n))
b=somaLinhas(a,pi,pj)
c=somaColunas(a,pi,pj)
peso=b+c-(2*(a[pi,pj]))

for i in range (0,a.shape[0],1):
    for j in range (0,a.shape[1],1):
        a[i,j]= input('a:')
print(peso)

