# -*- coding: utf-8 -*-
from __future__ import division

def menorcoluna(a):
    for j in range (0,shape[1],1):
        for i in range (0, shape[0],1):
            if a[i,j]==1:
                return j
    
def menorcoluna(a):
    for j in range (0,shape[1],1):
        for i in range (0, shape[0],1):
            if a[i,j]==1:
                cd=j
    return cd
    
def menorlinha(a):
    for i in range (0,shape[0],1):
        for j in range (0, shape[1],1):
            if a[i,j]==1:
                return i
    
def menorlinha(a):
    for i in range (0,shape[0],1):
        for j in range (0, shape[1],1):
            if a[i,j]==1:
                lb=j
    return lb
    
n=input('Digite o número de linhas:')
m=input('Digite o número de colunas:')

a=np.zeros ( (linhas , colunas) )
for i in range (0,shape[0],1):
    for j in range (0,shape[1],1):
        a[i,j]=input('Digite um elemento:')
print (a[lc:lb+1,ce:cd+1])
    
