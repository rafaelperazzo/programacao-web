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
    
def soma_colnas(x):
    soma=[]
    for j in range(0,x.shape[0],1):
        soma.append(sum(x[:,i]))
        
    return soma
    
#CodigoPrincipal
linhas=input('Digite o numero de linhas:')
colunas=input('Digite o numero de colunas:')


    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
