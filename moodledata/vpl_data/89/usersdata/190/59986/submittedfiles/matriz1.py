# -*- coding: utf-8 -*-
def menorLinha(a):
    for i in range(0,a.shape[0],1):
        for j in range(0,a.shape[1],1):
            if a[i,j]==1:
                return (i)
                
def menorColuna(a):
    for j in range(0,a.shape[1],1):
        for i in range(0,a.shape[0],1):
            if a[i,j]==1:
                return (j)
def maiorLinha(a):
    for i in range(a.shape[0]-1,-1,-1):
        for j in range(0,a.shape[1],1):
            if a[i,j]==1:
                return(i)

def maiorColuna(a):
    for j in range(a.shape[1]-1,-1,-1):
        for i in range(0,a.shape[1],1):
            if a[i,j]==1:
                return(j)

            
            
    
import numpy as np
n=int(input('digite o numero de linhas:'))
m=int(input('digite o numero de colunas:'))
a=np.zeros((n,m))

for i in range(0,a.shape[0],1):
    for j in range(0,a.shape[1],1):
        a[i,j]=int(input('digite o valor:'))
        
x=menorLinha(a)
y=maiorLinha(a)
w=menorColuna(a)
z=maiorColuna(a)

print(a[x y+1,w z+1])
