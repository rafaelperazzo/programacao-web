# -*- coding: utf-8 -*-
from __future__ import division

def somaLinha(a,l):
    somal=0
    for i in range(0,a.shape[1],1):
        somal=somal+a[l,i]
    return soma
    
def somaColuna(a,c):
    somac=0
    for j in range(0,a.shape[0],1):
        somac=somac+a[j,c]
    return soma
    
def peso(a,l,c):
    calculo=somaColuna(a,c)+somaLinha(a,l)-(2*a[l,c])
    return calculo
    
n=input('digite a dimensao da matriz:')
x=input('digite a posicao de x:')
y=input('digite a posicao de y:')
matriz=np.zeros((n,n))

for i in range(0,a.shape[0],1):
    for j in range0,a.shape[1],1):
        m[i,j]=input('digite o elemento:')
print ('%.1d'%(somaColuna(a,x,y)))
    