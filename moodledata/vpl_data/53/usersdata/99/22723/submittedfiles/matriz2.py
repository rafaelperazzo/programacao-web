# -*- coding: utf-8 -*-
from __future__ import division
import numpy as np

def soma_diagonalP(x):
    soma=0
    for i in range(0,x.shape[0],1): 
        soma=soma+x[i,j]
        
    return soma
    
def soma_diagonalS(x):
    soma=0
    i=0
    j=x.shape[0]-1
    while i<x.shape[0]:
        soma=soma+x[i,j]
        i=i+1
        j=j-1
        
    return soma
    
def soma_linhas(x):
    soma=[]
    for i in range(0,x.shape[0],1):
        soma.append(sum(x[i,:]))
        
    return soma
    
def soma_colunas(x):
    soma=[]
    for j in range(0,x.shape[0],1):
        soma.append(sum(x[:,i]))
        
    return soma
    
def quadrado_magico(x):
    sd1=soma_diagonalP(x)
    sd2=soma_diagonalS(x)
    somaL=soma_linhas(x)
    somaC=soma_colunas(x)
    
    cont=0
    for i in range(0,len(somaL),1):
        if sd1==sd2==somaL[i]==somaC[i]:
            cont=cont+1
            
    if cont==len(somaL):
        return True
    else:
        return False
    
#CodigoPrincipal
n=input('Digite o valor de n:')
a=np.zeros( (n,n) )

for i in range(0,a.shape[0],1):
    for j in range(0,a.shape[1],1):
        a[i,j]=input('Digite um valor para a matriz:')


if quadrado_magico(a):
    print('S')
else:
    print('N')


    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
