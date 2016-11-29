# -*- coding: utf-8 -*-
from __future__ import division

import numpy as np

def somaDiagonalPrincipal(a):
    soma=0
    for i in range(0,a.shape[0],1):
        soma=soma+a[i,i]
        
    return soma
    
def somaDiagonalSecundaria(a):
    soma=0
    for i in range(0,a.shape[0],1):
        soma=soma+a[i,a.shape[0]-i-1]
        
    return soma
    
def somaLinhas(a):
    s=[]
    for i in range(0,a.shape[0],1):
        soma=0
        for j in range(0,a.shape[1],1):
            soma=soma+a[i,j]
        s.append(soma)
        
    return s
    
def somaColunas(a):
    r=[]
    for j in range(0,a.shape[1],1):
        soma=0
        for i in range(0,a.shape[0],1):
            soma=soma+a[i,j]
            r.append(soma)
            
    return r
    
def quadradoMagico(a):
    sdP=somaDiagonalPrincipal(a)
    sdS=somaDiagonalSecundaria
    
    somaL=somaLinhas(a)
    somaC=somaColunas(a)
    
    contador=0
    for i in range(0,len(somaL),1):
        if sdP==sdS==somaL[i]==somaC[i]:
            contador=contador+1
            
            
    if contador==len(somaL):
        return True
    else:
        return False
        
#programa principal

n=input('digite o numero de linhas da matriz:')
#n=input('digite o numero de colunas da matriz:')

matriz=np.zeros((n,n))
for i in range(0,matriz.shape[0],1):
    for j in range(0,matriz.shape[1],1):
        matriz[i,j]=input('digite um elemento da matriz:')
    
if quadradoMagico(matriz):
    print('S')
else:
    print('N')