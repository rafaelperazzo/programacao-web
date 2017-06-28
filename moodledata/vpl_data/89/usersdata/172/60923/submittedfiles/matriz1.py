# -*- coding: utf-8 -*-
import numpy as np 
def menorlinha(a):
    for i in range(0,a.shape[0],1):
        for j in range(0,a.shape[1],1):
            if a[i,j]==1:
                return(i)
def menorcoluna(a):
    for j in range(0,a.shape[1],1):
        for i in range(0,a.shape[0],1):
            if a[i,j]==1:
                return(j)
def maiorlinha(a):
    for i in range(0,a.shape[0]-1,-1,-1):
        for j in range(0,a.shape[1]-1,-1,-1):
            if a[i,j]==1:
                return(i)            
def maiorcoluna(a):
    for j in range(0,a.shape[1]-1,-1,-1):
        for i in range(0,a.shape[0]-1,-1,-1):
            if a[i,j]==1:
                return(j)  
linhas=int(input( 'Digite as linhas: '))
colunas=int(input(' Digite as colunas: '))
a=np.zeros((linhas,colunas))
for i in range(0,a.shape[0],1):
    for j in range(0,a.shape[1],1):
        a[i,j]=int(input('valor:'))
x= menorlinha(a)
y= maiorlinha(a)
w= menorcoluna(a)
z= maiorcoluna(a)
print(a[x:y+1, w:z+1])
