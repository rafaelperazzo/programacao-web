# -*- coding: utf-8 -*-
from __future__ import division
import numpy as np

def soma_linha(a,l):
    somal=0
    for j in range(0,a.shape[0],1):
        somal=somal+a[l,j]
    return somal
    
def soma_coluna(a,c):
    somac=0
    for i in range(0,a.shape[0],1):
        somac=somac+a[i,c]
    return somac
    
def peso_posicao(a,l,c):
    calculo=soma_coluna(a,c)+soma_linha(a,l)-(2*a[l,c])
    return calculo
    
n=input('digite a dimensao da matriz:')
x=input('digite a posicao do x:')
y=input('digite a posicao do y:')
m=np.zeros((n,n))

for i in range(0,m.shape[0],1):
    for j in range(0,m.shape[1],1):
        m[i,j]=input('digite o elemento:')
print peso_posicao(m,x,y)