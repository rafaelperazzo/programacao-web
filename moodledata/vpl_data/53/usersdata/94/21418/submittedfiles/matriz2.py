# -*- coding: utf-8 -*-
from __future__ import division
import numpy as np

def soma_diagonal_principal(a):
    soma=0
    for i in range(0,a.shape[0],1):
        soma=soma+a[i,i]
    return soma
    
def soma_diagonal_secundaria(b):
    soma=0
    for i in range(0,b.shape[0],1):
        soma=soma+b[i,b.shape[0]-i-1]:
    return soma
    
def soma_linha(c):
    c=[]
    for i in range (0,c.shape[0],1):
        soma=0
        for j in range (0,c.shape[1],1):
            soma=soma+a[i,j]
        a.append(soma)
        
    return c
    
def soma_coluna(d):
    d=[]
    for j in range(0,d.shape[1],1):
        soma=0
        for i in range(0,d.shape[0],1):
            soma=soma+a[i,j]
        a.append(soma)
    return d
    
def magico(a):
    
    sdp=soma_diagonal_principal(a)
    sds=soma_diagonal_secundaria(b)
    sl=soma_linha(c)
    sc=soma_coluna(d)
    
    cont=0
    for i in range(0,len(sl),1):
        if sdp==sds==sl[i]==sc[i]:
            cont=cont+1
    if cont==len(sl):
        return True
        
    else:
        return False
        
linhas=input('digite a quantidade de linhas')
colunas=input('digite a quantidade de colunas')

a=np.zeros((linhas,colunas))

for i in range (0,a.shape[0],1):
    for j in range(0,a.shape[1],1):
        a[i,j]=input('digite um elemento:')

if magico(a):
    print ('S')
else:
    print ('N')
    
    
        
