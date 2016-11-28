# -*- coding: utf-8 -*-
from __future__ import division
import numpy as np

def soma_diagonal_principal(a):
    soma=0
    for i in range(0,a.shape[0],1):
        soma=soma+a[i,i]
    return soma
    
def soma_diagonal_secundaria(a):
    soma=0
    for i in range(0,a.shape[0],1):
        soma=soma+a[i,a.shape[0]-i-1]
    return soma
    
def soma_linha(a):
    w=[]
    for i in range (0,a.shape[0],1):
        soma=0
        for j in range(0,a.shape[1],1):
            soma=soma+a[i,j]
        w.append(soma)
        
    return w
    
def soma_coluna(a):
    w=[]
    for j in range(0,a.shape[1],1):
        soma=0
        for i in range(0,a.shape[0],1):
            soma=soma+a[i,j]
        w.append(soma)
    return w
    
def magico(a):
    
    sdp=soma_diagonal_principal(a)
    sds=soma_diagonal_secundaria(a)
    sl=soma_linha(a)
    sc=soma_coluna(a)
    
    cont=0
    for i in range(0,len(sl),1):
        if sdp==sds==sl[i]==sc[i]:
            cont=cont+1
    if cont==len(sl):
        return True
        
    else:
        return False
        
n=input('digite a  dimensão da matriz:')
a=np.zeros((n,n))

for i in range (0,a.shape[0],1):
    for j in range(0,a.shape[1],1):
        a[i,j]=input('digite um elemento:')

if magico(a):
    print ('S')
else:
    print ('N')
    
    
        
