# -*- coding: utf-8 -*-
from __future__ import division

def somalinha(a,b):
    i=0
    for j in range(0,a.shape[1],1):
        i=i+a[b,j]
    return i
        
def somacoluna(a,c):
    i=0
    for i in range(0,a.shape[0],1):
        i=i+a[i,c]
    return i

def somatotal(a,b,c):
    soma=somalinha(a,b)+somacoluna(a,c)
    return soma

n=input('digite o valor de n:')
x=input('digite o valor de x:')
y=input('digite o valor de y:')
a=np.zeros((n,n))
for i in range (0,a.shape[0],1):
    for j in range(0,a.shape[1],1):
        a[i,j]=input('digite os elementos:')

print('%d'%(somatotal(a,x,y)))
    
