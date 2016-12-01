# -*- coding: utf-8 -*-
from __future__ import division

import numpy as np

def somaLinha(a):
    s=[]
    for i in range(0,a.shape[0],1):
        somalinha=0
        for j in range(0,a.shape[1],1):
            somalinha=somalinha+a[i,j]
        s.append(somalinha)
    
    return s
    
def somaColuna(a):
    r=[]
    for j in range(0,a.shape[1],1):
        somacoluna=0
        for i in range(0,a.shape[0],1):
            somacoluna=somacoluna+a[i,j]
        r.append(somacoluna)
    
    return r
    
def peso(x,y):
    
    pesom=somaLinha(a)+somaColuna(a)-matriz[i,j]

    return peso

n=input('digite a dimensao da matriz:')

x=input('digite o indice das linhas:')
y=input('digite o indice das colunas:')

matriz=np.zeros((n,n))

for i in range(0,matriz.shape[0],1):
    for j in range(0,matriz.shape[1],1):
        matriz[i,j]=input('digite um elemento da matriz:')
        
print(peso)
        
