# -*- coding: utf-8 -*-
import numpy as np
n=int(input('numero de linhas: '))
m=int(input('numero de colunas: '))
a=np.zeros((n,m))
for i in range(0,a.shape[0],1):
    for j in range(0,a.shape[1],1):
        a[i,j]=float(input('elemento: '))
def menorlinha(a):
    for i in range(0,a.shape[0],1):
        for j in range(0,a.shape[1],1):
            if a[i,j]==1:
                return i
def menorcoluna(a):
    for j in range(0,a.shape[1],1):
        for i in range(0,a.shape[0],1):
            if a[i,j]==1:
                return j
def maiorlinha(a):
    for i in range(a.shape[0]-1,-1,-1):
        for j in range(a.shape[1]-1,-1,-1):
            if a[i,j]==1:
                return i
def maiorcoluna(a):
    for j in range(a,shape[1]-1,-1,-1):
        for i in range(a.shape[0]-1,-1,-1):
            if a[i,j]==1:
                return j
x=menorlinha(a)
y=maiorlinha(a)
w=menorcoluna(a)
z=maiorcoluna(a)
corte=a[x:y+1,w:z+1]
print(corte)