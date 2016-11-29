# -*- coding: utf-8 -*-
from __future__ import division
import numpy as np
#Funções
def menorcoluna(x):
    for j in range(0,x.shape[1],1):
        for i in range(0,x.shape[0],1):
            if x[i,j]==1:
                return j
                
def maiorcoluna(x):
    for j in range(0,x.shape[1],1):
        for i in range(0,x.shape[0]):
            if x[i,j]==1:
                maiorcoluna=j
    return maiorcoluna
        
def menorlinha(x):
    for i in range(0,x.shape[0],1):
        for j in range(0,x.shape[1],1):
            if x[i,j]==1:
                return i
                
def maiorlinha(x):
    for i in range(0,x.shape[0],1):
        for j in range(0,x.shape[1],1):
            if x[i,j]==1:
                maiorlinha=i
    return maiorlinha

#P.Principal
linhas=input('Digite a quantidade de linhas de a:')
colunas=input('Digite a quantidade de colunas de a:')

a=np.zeros( (linhas,colunas) )

for i in range(0,a.shape[0],1):
    for j in range(0,a.shape[1],1):
        a[i,j]=input('Digite um elemento para a matriz a:')
        
print (a[menorlinha(a):maiorlinha(a)+1,menorcoluna(a):maiorcoluna(a)+1])


