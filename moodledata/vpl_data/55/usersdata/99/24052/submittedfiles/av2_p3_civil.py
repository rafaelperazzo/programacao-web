# -*- coding: utf-8 -*-
from __future__ import division
import numpy as np

#Funções
def soma_linha(matriz,linha):
    somal=0
    for j in range(0,matriz.shape[1],1):
        somal=somal+matriz[linha,j]
        
    return somal
    
def soma_coluna(matriz,coluna):
    somac=0
    for i in range(0,matriz.shape[0],1):
        somac=somac+matriz[i,coluna]
        
    return somac
    
def peso(matriz,linha,coluna):
    soma=soma_coluna(matriz,coluna)+soma_linha(matriz,linha)-(2*matriz[linha,coluna])
    
    return soma

#CódigoPrincipal
n=int(input('Digite a dimensão da matriz:'))
x=input('Digite a posição x:')
y=input('Digite a posição y:')

a=np.zeros( (n,n) )
for i in range(0,a.shape[0],1):
    for j in range(0,a.shape[1],1):
        a[i,j]=input('Digite um valor para a matriz a:')
        

print int(peso(a,x,y))















