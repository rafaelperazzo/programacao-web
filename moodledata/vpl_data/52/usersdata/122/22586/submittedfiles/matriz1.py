# -*- coding: utf-8 -*-
from __future__ import division
import numpy as np

#A matriz deve se chamar "a".

def menorcoluna (a):
    for j in range (0,a.shape[1],1):
        for i in range (0,a.shaape[0],1):
            if a[i,j]==1:
                return j
                
def maiorcoluna (a):
    for j in range (0,a.shape[1],1):
        for i in range (0,a.shape[0],1):
            if a[i,j]==1:
                cd=j
    return cd
    
def menorlinha (a):
    for i in range (0,a.shape[0],1):
        for j in range (0,a.shaape[1],1):
            if a[i,j]==1:
                lc=i
                return i
                
def maiorlinha (a):
    for i in range (0,a.shape[0],1):
        for j in range (0,a.shape[1],1):
            if a[i,j]==1:
                lb=i
    return lb
    
#ENTRADA
linhas=input('Digite a quantidade de linhas da matriz: ')
colunas=input('Digite a quantidade de colunas da matriz: ')
a=np.zeros( (linhas,colunas) )
for i in range (0,a.shape[0],1):
    for j in range (0,a.shape[1],1):
        a[i,j]=input ('Digite um valor para a matriz:')
        
print (a[menorlinha(a):maiorlinha(a)+1,menorcoluna(a):maiorcoluna(a)+1])
