# -*- coding: utf-8 -*-
def menorlinha(a):
    for i in range(0,a.shape[0],1):
        for j in range(0,a.shape[1],1):
            if a[i,j]==1:
                return (i)
def menorcoluna(a):
    for j in range(0,a.shape[1],1):
        for i in range(0,a.shape[0],1):
            if a[i,j]==1:
                return (j)
def maiorlinha(a):
    for i in range(a.shape[0]-1,-1,-1):
        for j in range(0,a.shape[1],1):
            if a[i,j]==1:
                return (i)
def maiorcoluna(a):
    for j in range(a.shape[1]-1,-1,-1):
        for i in range(0,a.shape[0],1):
            if a[i,j]==1:
                return (j)
n=int(input('digite o numero de linhas:'))
m=int(input('digite o numero de colunas:'))
import numpy as np
a=np.zeros((n,m))
for i in range(0,a.shape[0],1):
    for j in range(0,a.shape[1],1):
        a[i,j]=int(input('digite os valores:'))
lme=menorlinha(a)
cme=menorcoluna(a)
lma=maiorlinha(a)
cma=maiorcoluna(a)
print(a[lme:cme,lma:cma+1])
