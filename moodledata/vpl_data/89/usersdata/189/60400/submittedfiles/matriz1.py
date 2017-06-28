# -*- coding: utf-8 -*-
def menorlinha(a):
    for i in range(0,a.shape[0],1):
        for j in range(0,a.shape[1],1):
            if a[i,j]==1:
                return(i)

def menorcoluna(a):
    for i in range(0,a.shape[1],1):
        for j in range(0,a.shape[0],1):
            if a[i,j]==1:
                return(j)

def maiorlinha(a):
    for i in range(0,a.shape[0]-1,-1,-1):
        for j in range(0,a.shape[1],1):
            if a[i,j]==1:
                return(i)
                
def maiorcoluna(a):
    for i in range(0,a.shape[1]-1,-1,-1):
        for j in range(0,a.shape[0],1):
            if a[i,j]==1:
                return(j)

linhas=int(input('linhas:'))
colunas=int(input('colunas:'))  
import numpy as np
a=np.zeros((linhas,colunas))
for i in range(0,a.shape[0],1):
        for j in range(0,a.shape[1],1):
            a[i,j]==int(input('valor:')

a1=menorlinha(a)
b=maiorlinha(a)
c=menorcoluna(a)
d=maiorcoluna(a)
print(a[a1:b+1,c:d+1])
