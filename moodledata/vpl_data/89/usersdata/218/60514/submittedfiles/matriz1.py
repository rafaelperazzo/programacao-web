# -*- coding: utf-8 -*-
def recorte (a):
    for i in range (0,a.shape[0],1):
        for j in range (0,a.shape[1],1):
            if a[i,j]==1:
                x=i
    for i in range (a.shape[0]-1,-1,-1):
        for j in range (0,a.shape[1],1):
            if a[i,j]==1:
                y=i
    for j in range (0,a.shape[1],1):
        for i in range (0,a.shape[0],1):
            if matriz[i,j]==1:
                z=j
    for j in range (a.shape[1]-1,-1,-1):
        for i in range (0,a.shape[0],1):
            if a[i,j]==1:
                w=j
    return (x,y,z,w)            
n=int(input('digite a quantidade de linhas:'))
m=int(input('digite a quantidade de colunas:'))
import numpy as np
a=np.zeros( (n,m) )
for i in range (0,a.shape[0],1):
    for j in range (0,a.shape[1],1):
        a[i,j]=float(input('digite o elemento da matriz:'))
print(recorte(a))