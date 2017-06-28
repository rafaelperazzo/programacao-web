# -*- coding: utf-8 -*-
import numpy as np
def menor linha(a):
    for i in range(0,a.shape[0],1):
        for j in range(0,a.shape[1],1):
            if a[i,j]==1:
                return(i)
def menor coluna (a):
    for j in range(0,a.shape[1],1):
        for i in range(0,a.shape[0],1):
            if a[i,j]==1:
                return(j)
def maior linha (a):
    for i in range(a.shape[0]-1,-1,-1):
        for j in range(a.shape[1]-1,-1,-1):
            if a[i,j]==1:
                return(i)
def maior coluna (a):
    for j in range(a.shape[1]-1,-1,-1):
        for  in range(a.shape[0]-1,-1,-1):
            if a[i,j]==1:
                return(i)
linhas=int(input('digite as linhas:'))
colunas=int(input('digite as colunas:'))
a=np.zeros((linhas,colunas))
for i in range (0,a.shape[0],1):
    for j in range (0,a.shape[1],1):
        a[i,j]=int(input('digite o valor:'))
x= menor linha(a)
y= maior linha(a)
w=menor coluna (a)
z= maior coluna (a)
print(a[x:y+1, w:z+1])