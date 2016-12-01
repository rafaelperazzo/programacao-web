# -*- coding: utf-8 -*-
from __future__ import division

import numpy as np

def somaDaLinha(a,l):
    somaLinha=0
    for j in range(0,a.shape[1],1):
            somaLinha=somaLinha+a[l,j]

    return somaLinha
    
def somaDaColuna(a,c):
    somacoluna=0
    for i in range(0,a.shape[0],1):
            somaColuna=somaColuna+a[i,c]

    return somaColuna
    
def peso(a,l,c):
    pesototal=somaDaLinha(a,l)+somaDaColuna(a,c)-(2*a[l,c])

    return pesototal

#codigo principal
n=input('digite a dimensao da matriz:')

x=input('digite o indice da linha:')
y=input('digite o indice da coluna:')

a=np.zeros((n,n))

for i in range(0,a.shape[0],1):
    for j in range(0,a.shape[1],1):
        a[i,j]=input('digite um elemento da matriz a:')
        
print('%.1d'% (peso(a,x,y)))
        
        
