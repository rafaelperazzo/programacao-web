# -*- coding: utf-8 -*-
def menorlinha(a):
    for i in range(0,a.shape[0],1):
        for l in range(0,a.shape[1],1):
            if a[i,l]==1:
                return(i)
def menorcoluna(a):
    for l in range(0,a.shape[1],1):
        for i in range(0,a.shape[0],1):
            if a[i,l]==1:
                return(l)
def maiorlinha(a):
    for i in range(0,a.shape[0]-1,-1,-1):
        for l in range(0,a.shape[1],1):
            if a[i,l]==1:
                return(i)
def maiorcoluna(a):
    for l in range(0,a.shape[1]-1,-1,-1):
        for i in range(0,a.shape[0],1):
            if a[i,l]==1:
                return(l)
linhas=int(input('linhas:'))
colunas=int(input('colunas:'))  
import numpy as np
a=np.zeros((linhas,colunas))
for i in range(0,a.shape[0],1):
        for l in range(0,a.shape[1],1):
            a[i,l]==int(input('valor:')
x=menorlinha (a)
y=maiorlinha (a)
w=menorcoluna (a)
z=maiorcoluna (a)
print(a[x:y+1,w:z+1])
