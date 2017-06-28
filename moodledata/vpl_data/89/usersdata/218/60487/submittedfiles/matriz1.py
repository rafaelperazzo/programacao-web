# -*- coding: utf-8 -*-
def menorlinha (a):
    for i in range (0,a.shape[0],1):
        for j in range (0,a.shape[1],1):
            if a[i,j]==1:
                return (i)
def maoirlinha (a):
    for i in range (a.shape[0]-1,-1,-1):
        for j in range (0,a.shape[1],1):
            if a[i,j]==1:
                return (i)
def menorcoluna (matriz):
    for j in range (0,a.shape[1],1):
        for i in range (0,a.shape[0],1):
            if matriz[i,j]==1:
                return (j)
def maoircoluna (a):
    for j in range (a.shape[1]-1,-1,-1):
        for i in range (0,a.shape[0],1):
            if a[i,j]==1:
                return (j)                
n=int(input('digite a quantidade de linhas:'))
m=int(input('digite a quantidade de colunas:'))
import numpy as np
a=np.zeros( (n,m) )
for i in range (0,a.shape[0],1):
    for j in range (0,a.shape[1],1):
        a[i,j]=float(input('digite o elemento da matriz:'))
print(a[menorlinha(a):(maiorlinha(a)+1),menorcoluna(a):(maiorcoluna(a)+1)])        