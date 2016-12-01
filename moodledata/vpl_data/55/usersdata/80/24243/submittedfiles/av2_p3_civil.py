# -*- coding: utf-8 -*-
from __future__ import division
import numpy as np


def peso(X,y,z):
    a=0
    b=0
    for i in range(0,X.shape[0],1):
        if(i!=z):
            a=a+X[y,i]
    for n in range(0,X.shape[0],1):
        if(n!=y):
            b=b+X[n,z]
    k=a+t
    return k

n=input('Tamanho da Matriz:')
x=input('Indice da Linha:')
y=input('Indice da Coluna:')
X=np.zeros((n,n))
for i in range(0,n,1):
    for j in range(0,n,1):
        X[i,j]=input('Valor:')
print ('O peso é:%d' %peso(X,x,y))        
    
