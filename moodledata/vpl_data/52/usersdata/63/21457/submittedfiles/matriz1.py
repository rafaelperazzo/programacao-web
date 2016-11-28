# -*- coding: utf-8 -*-
from __future__ import division

def colunamenor (lista):
    for j in range(0,lista.shape[1],1):
        for i in range(0,lista.shape[0],1):
            if a[i,j]==1:
                return j
                
                
def colunamaior(lista):
    for j in range(0,lista.shape[1],1):
        for i in range(0,lista.shape[0],1):
            if a[i,j]==1:
                cd=j
    return cd
    
def linhamenor (lista):
    for i in range(0,lista.shape[0],1):
        for j in range(0,lista.shape[1],1):
            if a[i,j]==1:
                return i
                
def linhamaior (lista):
    for i in range(0,lista.shape[0],1):
        for j in range(0,lista.shape[1],1):
            if a[i,j]==1:
                lb=i
    return lb
    
linhas=input('digite as linhas:')
colunas=input('digite as colunas:')
a=np.zeros((linhas,colunas))
for i in range(0,a.shape[0],1):
    for j in range(0,a.shape[1],1):
        a[i,j]=input('digite um elemento:')
        
print (a[linhamenor(a):linhamaior(a)+1,colunamenor(a):colunamaior (a)+1])