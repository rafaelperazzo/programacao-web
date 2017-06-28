# -*- coding: utf-8 -*-
import numpy as np
linhas=int(input('Informe o número de linhas:'))
colunas=int(input('Informe o número de colunas:'))
a=np.zeros((linhas,colunas))

for i in range(0,a.shape[0],1):
    for j in range(0,a.shape[1],1):
        a[i,j]=int(input('Informe um valor:'))
        
def linha1(a):
    for i in range(0,a.shape[0],1):
        for j in range(0,a.shape[1],1):
            if a[i,j]==1:
                return (i)

def linha2(a):
     for i in range(a.shape[0]-1,-1,-1):
        for j in range(0,a.shape[1],1):
            if a[i,j]==1:
                return (i)
def coluna1(a):
    for j in range(0,a.shape[1],1):
        for i in range(0,a.shape[0],1):
            if a[i,j]==1:
                return (i)

def coluna2(a):
    for j in range(a.shape[1]-1,-1,-1):
        for i in range(0,a.shape[0],1):
            if a[i,j]==1:
                return (i)
x=linha1
y=linha2
z=coluna1
w=coluna2
print(a[x:y+1, z:w+1])                
            
            

