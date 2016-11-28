# -*- coding: utf-8 -*-
from __future__ import division
#FUNÇÕES:
import numpy as np

def MatrizRecorte(a):
    
    c1=0
    for j in range(0,a.shape[0],1):
        if 1 in a[:,j]:
            c1=j
            break
    
    c2=0
    for j in range(0,a.shape[1],1):
        if 1 in a[:,j]:
            c2=j
    
    l1=0
    for i in range(0,a.shape[0],1):
        if 1 in a[i,:]:
            l1=i
            break
    
    l2=0
    for i in range(0,a.shape[0],1):
        if 1 in a[i,:]:
            l2=i
    
    linhas=(l2-l1)+1
    colunas=(c2-c1)+1
    
    r=np.zeros((linhas,colunas))
    
    for i in range(0,r.shape[0],1):
        for j in range(0,r.shape[1],1):
            r[i,j]=a[i+l1,j+c1]
    
    return r
    
    #programa principal
    
    linhas=input('Digite o numero de linhas:')
    colunas=input('Digite o numero de colunas:')
    
    a=np.zeros((linhas,colunas))
    
    for i in range(0,a.shape[0],1):
        for j in range(0,a.shape[1],1):
            a[i,j]=input('Digite um valor:')
    
    print MatrizRecorte(a)