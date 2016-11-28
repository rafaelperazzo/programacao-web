# -*- coding: utf-8 -*-
from __future__ import division
import numpy as np
def magico(x):
    b=[]
    for i in range(0,x.shape[0],1):
        b.append(x[0,i])
    soma=sum(b)
    cont=0
    for i in range(1,x.shape[0],1):
        somax=0
        for j in range(0,x.shape[0],1):
            somax=somax+x[i,j]
        if somax!=soma:
                cont=cont+1
    for i in range(0,x.shape[0],1):
        somay=0
        for j in range(0,x.shape[0],1):
            somay=somay+x[j,i]
        if somay!=soma:
                cont=cont+1
    somadp=0
    for i in range(0,x.shape[0],1):
        somadp=somadp+x[i,i]
    if somadp!=soma:
        cont=cont+1
    somads=0
    for i in range(0, x.shape[0],1):
        somads=somads+x[i,(x.shape[0]-1)-i]
        if somads!=soma:
            cont=cont+1
    if cont==0:
        return True
    else:
        return False
    
linhas=input('l:')

a= np.zeros((linhas,linhas))
for i in range(0,a.shape[0],1):
    for j in range(0,a.shape[0],1):
        a[i,j]=input('a:')
        
if magico(a):
    print('S')
else:
    print ('N')
    
