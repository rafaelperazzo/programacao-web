# -*- coding: utf-8 -*-
import numpy as np

def menorLinha(a):
    for i in range(0,a.shape[0],1):
        for j in range(0,a.shape[1],1):
            if a[i,j]==1:
                return(i)

def menorColuna(a):
    for i in range(0,a.shape[1],1):
        for j in range(0,a.shape[0],1):
            if a[i,j]==1:
                return(j)

def maiorLinha(a):
    for i in range(a.shape[0]-1,-1,-1):
        for j in range(a.shape[1]-1,-1,-1):
            if a[i,j]==1:
                return(i)                

def maiorColuna(a):
    for i in range(a.shape[1]-1,-1,-1):
        for j in range(a.shape[0]-1,-1,-1):
            if a[i,j]==1:
                return(i)

linhas=int(input('Quantidade de linhas da matriz: '))
colunas=int(input('Quantidade de colunas da matriz: '))
a=np.zeros((linhas,colunas))

for i in range(0,a.shape[0],1):
    for j in range(0,shape[1],1):
        a[i,j]=int(input('Digite o valor do termo: '))
        
x=menorLinha(a)
y=maiorLinha(a)
w=menorColuna(a)
z=maiorColuna(a)
        
print(a[x:y+1,w:z+1])