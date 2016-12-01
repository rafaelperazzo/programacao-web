# -*- coding: utf-8 -*-
from __future__ import division

import numpy as np

def somaDaLinha(a,l):
    somal=0
    for j in range(0,a.shape[1],1):
        somal=somal+a[l,j]
        
    return somal
    
def somaDaColuna(a,c):
    somac=0
    for i in range(0,a.shape[0],1):        
        somac=somac+a[i,c]
    
    return somac
    
def peso(a,l,c):
    
    pesot=somaDaLinha(a,l)+somaDaColuna(a,c)-(2*a[l,c])
    
    return pesot

#codigo principal
n=input('digite a dimensao da matriz:')

x=input('digite o indice da linha:')
y=input('digite o indice da coluna:')

matriz=np.zeros((n,n))

for i in range(0,matriz.shape[0],1):
    for j in range(0,matriz.shape[1],1):
        matriz[i,j]=input('digite um elemento da matriz:')
        
print peso(matriz,x,y)
        
