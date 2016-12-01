# -*- coding: utf-8 -*-
from __future__ import division

import numpy as np

def somaDaLinha(a):
    somaLinha=0
    somaFinalDaLinha=0
    for j in range(0,a.shape[1],1):
        somaLinha=somaLinha+a[x,j]
    x=x-1
    somaFinalDaLinha=somaLinha-a[x,y]
    
    return somaFinalDaLinha
    
def somaDaColuna(a):
    somaColuna=0
    somaFinalDaColuna=0
    for i in range(0,a.shape[0],1):        
        somaColuna=somaColuna+a[i,y]
    y=y-1
    somaFinalDaColuna=somaColuna-a[x,y]
    
    return somaFinalDaColuna
    
def peso(a):
    
    pesototal=somaDaLinha(a)+somaDaColuna(a)
    
    return pesototal
    return pesot

#codigo principal
n=input('digite a dimensao da matriz:')

x=input('digite o indice da linha:')
y=input('digite o indice da coluna:')

a=np.zeros((n,n))

for i in range(0,a.shape[0],1):
    for j in range(0,a.shape[1],1):
        a[i,j]=input('digite um elemento da matriz a:')
        
print('%.1d'% peso(a))
        
