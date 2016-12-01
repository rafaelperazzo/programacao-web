# -*- coding: utf-8 -*-
from __future__ import division
import numpy as np
def menorcoluna (a):
    for j in range (0,a.shape[1],1):
        for i in range (0,a.shape[0],1):
            if a[i,j]==1:
                ce=j
                break
    return ce
def maiorcoluna (a):
    for j in range (0,a.shape[1],1):
        for i in range (0,a.shape[0],1):
            if a[i,j]==1:
                cd=j
    return cd
    
def maiorlinha (a):
    for i in range (0,a.shape[0],1):
        for j in range (0,a.shape[1],1):
            if a[i,j]==1:
                lb=i
                break
    return lb
    
def menorlinha (a):
    for i in range (0,a.shape[0],1):
        for j in range (0,a.shape[1],1):
            if a[i,j]==1:
                lc=i
    return lc
    
    

linhas=input("Digite a quantidade de linhas:")
colunas=input("Digite a quantidade de colunas:")
a=np.zeros((linhas,colunas))
for i in range (0,a.shape[0],1):
    for j in range (0,a.shape[1],1):
        a[i,j]=input("Digite um elemento:")

lc=menorlinha(a)
lb=maiorlinha(a)
ce=menorcoluna(a)
cd=maiorcoluna(a)
b=np(lc:lb+1,ce:cd+1)
print b
    
