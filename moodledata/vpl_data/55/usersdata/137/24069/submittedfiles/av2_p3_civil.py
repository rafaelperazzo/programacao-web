# -*- coding: utf-8 -*-
from __future__ import division
import numpy as np

def somaLinhas(a):
    s=0
    for i in range (0,a.shape[0],1):
        soma=0
        s[i]=soma+a[i,pj]
    return s

def somaColunas(a):
    s=0
    for j in range (0,a.shape[1],1):
        soma=0
        s[j]=soma+a[pi,i]
    return s

def peso(a):
    peso=b+c-(2*(a[pi,pj]))
    return peso
    
n=input('dimensao da matriz:')
pi=input ('indice i:')
pj=input ('indice j:')
a=np.zeros ((n,n))
b=somaLinhas(a,pj)
    c=somaColunas(a,pi)
d = peso(a,b,c)

for i in range (0,a.shape[0],1):
    for j in range (0,a.shape[1],1):
        a[i,j]= input('a:')
print(d)

