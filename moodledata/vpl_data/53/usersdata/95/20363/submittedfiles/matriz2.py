# -*- coding: utf-8 -*-
from __future__ import division
import numpy as np
def soma_linhas(a):
    x=[]
    for i in range(0,m.shape[0],1):
        soma=0
        for j in range(0,m.shape[1],1):
            soma=soma+a[i,j]
        x.append(soma)
    return x

def soma_colunas(a):
    x=[]
    for j in range(0,m.shape[1],1):
        soma=0
        for i in range(0,m.shape[0],1):
            soma=soma+a[i,j]
        x.append(soma)
    return x

def diagonal_p(a):
    soma=0
    for i in range(0,a.shape[0],1):
        soma+=a[i,i]
    return soma

def diagonal_s(a):
    soma=0
    for i in range(0,a.shape[0],1):
        soma+=a[i,a.shape[0]-1-i]
    return soma
    
def magico(a):
    d1=diagonal_p(a)
    d2=diagonal_s(a)
    l=soma_linhas(a)
    c=soma_colunas(a)
    cont=0
    for i in range(0,len(l),1):
        if d1==d2==l[i]==c[i]:
            cont=cont+1
    if cont==len(l):
        return True
    else:
        return False
    
n=input('Digite a dimensao da matriz:')
m=np.zeros((n,n))

for i in range(0,m.shape[0],1):
    for j in range(0,m.shape[1],1):
        m[i,j]=input('Digite um elemento:')

if magico(m):
    print('S')
else:
    print ('N')
    
