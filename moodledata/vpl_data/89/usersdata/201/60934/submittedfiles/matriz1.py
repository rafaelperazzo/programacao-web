# -*- coding: utf-8 -*-
import numpy as np
def menorLinha(a):
    for i in range(0,a.shape[0],1):
        for l in range(0,a.shape[1],1):
            if a[i+1]==1:
                return(i)
                
def menorColuna(a):
    for l in range(0,a.shape[1],1):
        for i in range(0,a.shape[0],1):
            if a[i,l]==1:
                return(l)
                
def maiorLinha(a):
    for i in range(a.shape[0]-1,-1,-1):
        for l in range(0,a.shape[1],1):
            if a[i,l]==1:
                return(i)
                
def maiorColuna(a):
    for l in range(a.shape[1]-1,-1,-1):
        for i in range(0,a.shape[0],1):
            if a[i,l]==1:
                return(l)
                
linhas=int(input('Digite o número de linhas:'))
colunas=int(input('Digite o número de colunas:'))
a=np.zeros((linhas,colunas))
for i in range(0,a.shape[0],1):
    for l in range(0,a.shape[1],1):
        a[i,l]=int(input('Valor:'))
        
        
x=menorLinha(a)
y=maiorLinha(a)
w=menorColuna(a)
z=maiorColuna(a)
print(a[x:y+1,w:z+1])
