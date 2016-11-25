# -*- coding: utf-8 -*-
from __future__ import division

def soma(a,b):
    linhas=a.shape[0]
    colunas=a.shape[1]
    c=np.zeros((linhas,colunas))
    for i in range (0,c.shape[0],1):
        for j in range (0,c.shape[1],1):
            c[i,j]=a[i,j]+b[i,j]
    return c

linhas=input('digite o numero de linhas:')
colunas=input('digite o numero de colunas:')
a=np.zeros ((linhas,colunas))
b=np.zeros ((linhas,colunas))
for i in range (0,a.shape[0],1):
    for j in range (0,a.shape[1],1):
        a[i,j]=input('digite um valor para a matriz a:')
        
for i in range (0,b.shape[0],1):
    for i in range (0,b.shape[1],1):
        b[i,j]=input('digite um valor para a matriz b:')
        
print soma(a,b)

