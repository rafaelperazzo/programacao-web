# -*- coding: utf-8 -*-
from __future__ import division

import numpy as np

def diagsec(a):
    x=a.shape[1]-1
    soma=0
    for i in range(0,a.shape[0],1):
        for j in range(0,a.shape[1],1):
            if j==x:
                soma=soma+a[i,j]
                x=x-1
    return soma
    
def diagprim(a):
    soma=0
    for i in range(0,a.shape[0],1):
        for j in range(0,a.shape[1],1):
            if i==j:
                soma=soma+a[i,j]
    return soma
    
def somalinha(a):
    s=[]
    for i in range(0,a.shape[0],1):
        soma=0
        for j in range(0,a.shape[1],1):
            soma=soma+a[i,j]
        s.append(soma)
    return s
    
def somacoluna(a):
    s=[]
    for j in range(0,a.shape[1],1):
        soma=0
        for i in range(0,a.shape[0],1):
            soma=soma+a[i,j]
        s.append(soma)
    return s    

def resultado(a):
    x=diagsec(a)
    y=diagprim(a)
    z=somalinha(a)
    w=somacoluna(a)
    
    cont=0
    for i in range(0,len(z),1):
        if x==y==z[i]==w[i]:
            cont = cont+1
            
    if cont==len(z):
        return True
    else:
        return False
        
linhas=input('número de linhas: ')
colunas=input('número de colunas: ')
a=np.zeros((linhas,colunas))
for i in range(0,a.shape[0],1):
    for j in range(0,a.shape[1],1):
        a=input('elementos: ')

if resultado(a):
    print 'S'
else:
    print 'N'
    
    

            












