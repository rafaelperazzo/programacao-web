# -*- coding: utf-8 -*-
from __future__ import division 
import numpy as np

def menorColuna(a):
    for j in range (0,a.shape[1],1):
        for i in range (0,a.shape[0],1):
            if a[i,j]==1:
                return j
                
def maiorColuna(a):
    for j in range (0,a.shape[1],1):
        for i in range (0,a.shape[0],1):
            if a[i,j]==1:
                cd=j
    return cd
                
def menorLinha(a):
    for i in range (0,a.shape[0],1):
        for j in range (0,a.shape[1],1):
            if a[i,j]==1:
                return i
                
def maiorLinha(a):
    for i in range (0,a.shape[0],1):
        for j in range (0,a.shape[1],1):
            if a[i,j]==1:
                lb=i
    return lb
    
def corteRetangular(a):
    
    ce=menorColuna(a)
    cd=maiorColuna(a)
    
    lc=menorLinha(a)
    lb=maiorLinha(a)

    return a[lc:lb+1,ce:cd+1] #<------------ O ERRO ESTAVA AQUI
    
    
linhas=input('Digite o número de linhas da matriz:')
colunas=input('Digite o número de colunas da matriz:')

a=np.zeros((linhas,colunas))

for i in range (0,a.shape[0],1):
    for j in range (0,a.shape[1],1):
        a[i,j]=input('Digite um elemento da matriz:')
        
print corteRetangular(a) #<-------------- o erro estava aqui

